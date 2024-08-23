#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import wave
import struct
import math
import collections

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt


SAMPLING_FREQ = 44_100 # Hertz, taux d'échantillonnage standard des CD
SAMPLE_BITS = 16 # Échantillons de 16 bit
SAMPLE_WIDTH = SAMPLE_BITS // 16
MAX_INT_SAMPLE_VALUE = 2**(SAMPLE_BITS-1) - 1



# Un tuple contenant les signaux d'un accord parfait majeur.
MajorChord = collections.namedtuple("MajorChord", """
	root,
	third,
	fifth,
	octave,
	chord
""")


def merge_channels(channels):
	# Équivalent de :  [sample for samples in zip(*channels) for sample in samples]
	return np.fromiter((sample for samples in zip(*channels) for sample in samples), float)

def separate_channels(samples, num_channels):
	# Équivalent de :  [samples[i::num_channels] for i in range(num_channels)]
	return np.fromiter((samples[i::num_channels] for i in range(num_channels)), float)

def generate_sample_time_points(duration):
	# Générer un tableau de points temporels également espacés en seconde. On a SAMPLING_FREQ points par seconde.
	pass

def sine(freq, amplitude, duration):
	# Générer une onde sinusoïdale à partir de la fréquence et de l'amplitude donnée, sur le temps demandé et considérant le taux d'échantillonnage.
	# Formule de la valeur y d'une onde sinusoïdale à l'angle x en fonction de sa fréquence F et de son amplitude A :
	# y = A * sin(F * x), où x est en radian.
	# Si on veut le x qui correspond au moment t, on peut dire que 2π représente une seconde, donc x = t * 2π
	# On utilise la fonction précédente pour générer les t
	pass

def square(freq, amplitude, duration):
	# Générer une onde carrée d'une fréquence et amplitude donnée.
	pass

def sawtooth(freq, amplitude, duration):
	# Générer une onde en dents de scie (sawtooth) à partir de l'amplitude et fréquence donnée.
	pass

def sine_with_overtones(root_freq, amplitude, overtones, duration):
	# Générer une onde sinusoïdale avec ses harmoniques. Le paramètre overtones est un dictionnaire où la clé est le multiple de la fondamentale et la valeur est l'amplitude relative de l'harmonique.
	pass

def normalize(samples, norm_target):
	# Normalisez un signal à l'amplitude donnée.
	pass

def build_major_chord(root_freq, wave_fn, duration):
	# Un accord majeur (racine, tierce, quinte, octave) en intonation juste.
	third_freq, fifth_freq, octave_freq = root_freq * 5/4, root_freq * 3/2, root_freq * 2
	root =   wave_fn(root_freq, 1, duration)
	third =  wave_fn(third_freq, 0.9, duration)
	fifth =  wave_fn(fifth_freq, 0.8, duration)
	octave = wave_fn(octave_freq, 0.7, duration)
	# Étant donné qu'on additionne les signaux, on normalize pour que ça soit à un bon niveau.
	chord =  normalize(root + third + fifth + octave, 1)
	return MajorChord(root, third, fifth, octave, chord)

def convert_to_bytes(samples):
	# Convertir les échantillons en tableau de bytes en les convertissant en entiers 16 bits.
	# Les échantillons en entrée sont entre -1 et 1, nous voulons les mettre entre -MAX_SAMPLE_VALUE et MAX_SAMPLE_VALUE
	# Juste pour être certain de ne pas avoir de problème, on doit clamper les valeurs d'entrée entre -1 et 1.
	pass

def convert_to_samples(bytes):
	# Faire l'opération inverse de convert_to_bytes, en convertissant des échantillons entier 16 bits en échantillons réels
	pass

def apply_fft(sig, sampling_rate):
	"""
	Applique une tranformée de Fourier discrète rapide (FFT) sur un signal 1D.

	:param sig: Le signal, en numpy.ndarray réel.

	:param sampling_rate: Le taux d'échantillonnage, en Hz, du signal.

	:returns: L'axe de magnitude normalisée (entre 0 et 1) de la FFT (partie réelle seulement) et l'axe fréquentiel associé.
	"""
	
	# TODO: Créer l'axe fréquentiel approprié.
	#       On veut un tableau ainsi :
	#         - Valeurs réelles espacées uniformément
	#         - Taille = moitié de la longueur du signal
	#         - Première valeur = 0, dernière valeur = taux d'échantillonnage / 2 (fréquence de Nyquist du signal)

	# TODO: Créer l'axe de magnitude en appliquant une FFT.
	#       On veut un axe ainsi :
	#         - Même taille que l'axe de fréquence, donc on prend juste la première moitié des valeurs retournées par `scipy.fft.fft`, c'est-à-dire la partie réelle de la FFT.
	#         - En valeurs absolues (les valeurs négatives sont des résultats déphasés)
	#         - On normalise en divisant par la moitié du nombre d'échantillons (taille du signal)

	# On retourne les deux axes, avec l'axe de magnitude en premier.
	pass


def main():
	try:
		# On met les fichiers de sortie dans leur propre dossier.
		os.mkdir("output")
	except:
		pass

	# On génère des ondes qui nous intéresse.
	duration = 10.0
	root_freq = 220 # La3
	# Des accords majeurs (racine, tierce, quinte, octave) en intonation juste.
	sine_chord = build_major_chord(root_freq, sine, duration)
	square_chord = build_major_chord(root_freq, square, duration)
	saw_chord = build_major_chord(root_freq, sawtooth, duration)
	# Un La3 avec quelques harmoniques.
	overtone_values = {i: 0.5**(i-1) for i in range(2, 10)}
	note_with_overtones = sine_with_overtones(root_freq, 1, overtone_values, duration)

	# On affiche une onde d'exemple.
	xs = generate_sample_time_points(duration)
	ys = square(1.0, 0.5, duration) + sawtooth(10.0, 0.1, duration)
	plt.figure(figsize=(12, 6))
	plt.plot(xs, ys)
	plt.grid(color="wheat")
	plt.xlim([0, 2])
	plt.ylim([-1.1, 1.1])
	plt.xlabel("t (s)")
	plt.ylabel("y")
	plt.show()

	# On affiche une FFT d'exemple.
	mag, freq = apply_fft(sine_chord.chord, SAMPLING_FREQ)
	xs, ys = freq, mag
	plt.figure(figsize=(12, 6))
	plt.plot(xs, ys)
	plt.grid(color="wheat")
	plt.xscale("log")
	plt.xlim([10, SAMPLING_FREQ / 2])
	plt.ylim([0, 1])
	plt.xlabel("F (Hz)")
	plt.ylabel("Magnitude")
	plt.show()

	# Exemple d'un la et mi (quinte juste), un dans le channel gauche et l'autre dans le channel droit
	with wave.open("output/perfect_fifth_panned.wav", "wb") as writer:
		# On fait la config du writer (2 channels, échantillons de deux octets, fréquence d'échantillonnage).
		writer.setnchannels(2)
		writer.setsampwidth(SAMPLE_WIDTH)
		writer.setframerate(SAMPLING_FREQ)
		# On met les samples dans des channels séparés (la à gauche, mi à droite), et on écrit dans le fichier
		merged = merge_channels([saw_chord.root, saw_chord.fifth])
		writer.writeframes(convert_to_bytes(merged))

	with wave.open("output/major_chord.wav", "wb") as writer:
		# On fait la config du writer (1 channel, échantillons de deux octets, fréquence d'échantillonnage).
		writer.setnchannels(1)
		writer.setsampwidth(SAMPLE_WIDTH)
		writer.setframerate(SAMPLING_FREQ)
		# On écrit un accord majeur dans le fichier.
		writer.writeframes(convert_to_bytes(sine_chord.chord))

	with wave.open("output/overtones.wav", "wb") as writer:
		# On fait la config du writer (1 channel, échantillons de deux octets, fréquence d'échantillonnage).
		writer.setnchannels(1)
		writer.setsampwidth(SAMPLE_WIDTH)
		writer.setframerate(SAMPLING_FREQ)
		# On écrit une note avec harmoniques dans le fichier.
		writer.writeframes(convert_to_bytes(note_with_overtones))

if __name__ == "__main__":
	main()
