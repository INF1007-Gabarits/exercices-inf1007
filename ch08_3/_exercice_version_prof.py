#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import struct
import math
from collections import namedtuple


SAMPLING_FREQ = 44100 # Hertz, taux d'échantillonnage standard des CD
SAMPLE_BITS = 16
SAMPLE_WIDTH = SAMPLE_BITS // 8
MAX_SAMPLE_VALUE = 2**(SAMPLE_BITS-1) - 1

# Les formats d'encodage (struct) pour les sous-entêtes.
RIFF_HEADER_STRUCT = "4sI 4s"
FORMAT_HEADER_STRUCT = "4sI HHIIHH"
DATA_HEADER_STRUCT = "4sI"
# Le format d'encodage pour les entêtes.
WAVE_FILE_HEADERS_STRUCT = "<" + RIFF_HEADER_STRUCT + FORMAT_HEADER_STRUCT + DATA_HEADER_STRUCT


# Contient tous les champs des entêtes d'un fichier WAVE.
WaveFileHeaders = namedtuple("WaveFileHeaders", """
	riff_id,
	file_size,
	wave,
	fmt_id,
	fmt_size,
	wav_type,
	num_channels,
	sampling_freq,
	bytes_per_second,
	bytes_per_sample,
	sample_bits,
	data_id,
	data_size
""")


def merge_channels(channels):
	# À partir de plusieurs listes d'échantillons (réels), les combiner de façon à ce que la liste retournée aie la forme :
	# [c[0][0], c[1][0], c[2][0], c[0][1], c[1][1], c[2][1], ...] où c est l'agument channels
	return [sample for samples in zip(*channels) for sample in samples]

def separate_channels(samples, num_channels):
	# Faire l'inverse de la fonction merge_channels
	# Si on a en entrée [11, 21, 12, 22, 13, 23]
	# Sur deux channels on obtiendrait :
	# [
	#   [11, 12, 13]
	#   [21, 22, 23]
	# ]
	return [samples[i::num_channels] for i in range(num_channels)]

def sine_gen(freq, amplitude, duration_seconds):
	# Générer une onde sinusoïdale à partir de la fréquence et de l'amplitude donnée, sur le temps demandé et considérant le taux d'échantillonnage. On veut bien une fonction génératrice, pas retourner une liste.
	# Les échantillons sont des nombres réels entre -1 et 1.
	for i in range(int(SAMPLING_FREQ * duration_seconds)):
		# Formule de la valeur y d'une onde sinusoïdale à l'angle x en fonction de sa fréquence F et de son amplitude A :
		# y = A * sin(F * x), où x est en radian.
		# Si on veut le x qui correspond au moment t, on peut dire que 2π représente une seconde, donc x = t * 2π.
		# Or t est en secondes, donc t = i / nb_échantillons_par_secondes, où i est le numéro d'échantillon.
		yield amplitude * math.sin(freq * (i / SAMPLING_FREQ * 2*math.pi))

def create_headers(num_samples):
	headers_size = struct.calcsize(WAVE_FILE_HEADERS_STRUCT)
	data_size = num_samples * SAMPLE_WIDTH
	riff_file_size = struct.calcsize(WAVE_FILE_HEADERS_STRUCT) - 8 + data_size

	return WaveFileHeaders(
		riff_id=          b"RIFF",
		file_size=        riff_file_size,
		wave=             b"WAVE",
		fmt_id=           b"fmt ",
		fmt_size=         struct.calcsize(FORMAT_HEADER_STRUCT) - 8,
		wav_type=         1,
		num_channels=     2,
		sampling_freq=    SAMPLING_FREQ,
		bytes_per_second= SAMPLING_FREQ * SAMPLE_WIDTH,
		bytes_per_sample= SAMPLE_WIDTH,
		sample_bits=      SAMPLE_BITS,
		data_id=          b"data",
		data_size=        data_size
	)

def convert_to_bytes(samples):
	# Convertir les échantillons en tableau de bytes en les convertissant en entiers signés de 16 bits.
	# Les échantillons en entrée sont entre -1 et 1, nous voulons les mettre entre -MAX_SAMPLE_VALUE et MAX_SAMPLE_VALUE.
	packer = struct.Struct(f"{len(samples)}h")
	return packer.pack(*(int(sample * MAX_SAMPLE_VALUE) for sample in samples))

def write_wave_file(filename, samples):
	# Créer les entêtes à encoder à l'aide de create_headers, les encoder en octets avec le format d'encodage donné dans la constante WAVE_FILE_HEADERS_STRUCT.
	headers = create_headers(len(samples))
	headers_bytes = struct.pack(WAVE_FILE_HEADERS_STRUCT, *headers)
	# Convertir les échantillons en octets avec la fonction convert_to_bytes.
	data_bytes = convert_to_bytes(samples)
	# Ouvrir le fichier donné en écriture binaire et écrire les octets d'entêtes suivis les octets de données.
	with open(filename, "wb") as out_file:
		out_file.write(headers_bytes)
		out_file.write(data_bytes)

def convert_to_samples(sample_bytes):
	# Faire l'opération inverse de convert_to_bytes, en convertissant des échantillons entiers signés de 16 bits en échantillons réels.
	unpacker = struct.Struct(f"{len(sample_bytes) // SAMPLE_WIDTH}h")
	int_samples = unpacker.unpack(sample_bytes)
	return [int_sample / MAX_SAMPLE_VALUE for int_sample in int_samples]

def read_wave_file(filename):
	# Lire les octets des entêtes.
	headers_size = struct.calcsize(WAVE_FILE_HEADERS_STRUCT)
	# Ouvrir le fichier en mode lecture binaire.
	with open(filename, "rb") as in_file:
		headers_bytes = in_file.read(headers_size)
		# Décoder les entêtes en octets avec le format d'encodage donné dans la constante WAVE_FILE_HEADERS_STRUCT.
		headers = WaveFileHeaders(*struct.unpack_from(WAVE_FILE_HEADERS_STRUCT, headers_bytes))
		# Lire les octets de données à partir de la fin des entête. Le nombre d'octets à lire est donné par data_size des entêtes.
		data_bytes = in_file.read(headers.data_size)
	# Décoder les octets de données en échantillons réel avec la fonction convert_to_samples en se positionnant au début des données (après les octets).
	samples = convert_to_samples(data_bytes)
	# Retourner les entêtes décodés (sous la forme d'un WaveFileHeaders) et la liste d'échantillons réel en deux valeurs.
	return headers, samples


def main():
	if not os.path.exists("output"):
		os.mkdir("output")

	# Si on veut juste tester l'encodage des échantillons, on peut appeler convert_to_bytes avec quelques échantillons, écrire les octets directement dans un fichier binaire sans entête et les importer comme «Raw data» dans Audacity.
	with open("output/test.bin", "wb") as out_file:
		data = convert_to_bytes([0.8, -0.8, 0.5, -0.5, 0.2, -0.2])
		out_file.write(data)

	# Exemple simple avec quelques échantillons pour tester le fonctionnement de l'écriture.
	write_wave_file("output/test.wav", [0.8, -0.8, 0.5, -0.5, 0.2, -0.2])

	# On génére un la3 (220 Hz), un do#4, un mi4 et un la4 (intonnation juste).
	sine_a3 = sine_gen(220, 0.5, 5.0)
	sine_cs4 = sine_gen(220 * (5/4), 0.4, 5.0)
	sine_e4 = sine_gen(220 * (3/2), 0.35, 5.0)
	sine_a4 = sine_gen(220 * 2, 0.3, 5.0)

	# On met les samples dans des channels séparés (la et do# à gauche, mi et la à droite)
	merged = merge_channels([
		(sum(elems) for elems in zip(sine_a3, sine_cs4)),
		(sum(elems) for elems in zip(sine_e4, sine_a4))
	])
	write_wave_file("output/major_chord.wav", merged)

	_, samples = read_wave_file("data/kinship_maj.wav")
	# On réduit le volume (on pourrait faire n'importe quoi avec les samples à ce stade)
	samples = [s * 0.2 for s in samples]
	write_wave_file("output/kinship_mod.wav", samples)

if __name__ == "__main__":
	main()
