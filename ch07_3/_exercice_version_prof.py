#!/usr/bin/env python
# -*- coding: utf-8 -*-

import mido


NOTES_PER_OCTAVE = 12


def build_note_dictionaries(note_names, add_octave_no=True):
	C0_MIDI_NO = 12 # Plus basse note sur les pianos est La 0, mais on va commencer à générer les noms sur Do 0

	midi_to_name = {}
	name_to_midi = {}
	# Pour chaque octave de 0 à 8 (inclus). On va générer tout l'octave 8, même si la dernière note du piano est Do 8
	for octave in range(8+1):
		# Pour chaque note de l'octave
		for note in range(NOTES_PER_OCTAVE):
			# Calculer le numéro MIDI de la note et ajouter aux deux dictionnaires
			midi_no = C0_MIDI_NO + octave * NOTES_PER_OCTAVE + note
			# Ajouter le numéro de l'octave au nom de la note si add_octave_no est vrai
			full_note_name = note_names[note] + (str(octave) if add_octave_no else "")
			midi_to_name[midi_no] = full_note_name
			# Garder les numéros de notes dans name_to_midi entre 0 et 11 si add_octave_no est faux
			name_to_midi[full_note_name] = midi_no if add_octave_no else midi_no % NOTES_PER_OCTAVE
	return midi_to_name, name_to_midi

def build_print_note_name_callback(midi_to_name):
	# Fonction locale
	# Soit message MIDI midi_msg, midi_msg.type donne le type, midi_msg.note donne la note
	
	# Dans mon callback :
	def callback(midi_msg):
		# Si j'ai un note_on et une vélocité > 0, alors j'affiche le nom de la note associée au numéro (grâce au dict midi_to_name)
		if midi_msg.type == "note_on" and midi_msg.velocity > 0:
			print(midi_to_name[midi_msg.note])
	return callback

def build_print_chord_name_callback(chord_names_and_notes, name_to_midi):
	# Construire le dictionnaire d'assocations entre état des notes et accord joué.
	chords = {}

	# Par exemple, [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0] -> "Do majeur"
	for name, notes in chord_names_and_notes.items():
		chord_notes = [False] * 12
		for note in notes:
			chord_notes[name_to_midi[note] % NOTES_PER_OCTAVE] = True
		chords[tuple(chord_notes)] = name

	# Créez et retourner le callback
	def callback(midi_msg):
		global note_states
		# Si une note est appuyée
		if midi_msg.type == "note_on" and midi_msg.velocity > 0:
			# Je met son élément correspondant dans l'état du clavier à True
			note_states[midi_msg.note % NOTES_PER_OCTAVE] = True
			note_states_tuple = tuple(note_states)
			# Si accord connu
			if note_states_tuple in chords:
				# Affiche nom de l'accord
				print(chords[note_states_tuple])
		# Sinon si une note est relâchée
		elif midi_msg.type == "note_off" or (midi_msg.type == "note_on" and midi_msg.velocity == 0):
			# Idem mais à False
			note_states[midi_msg.note % NOTES_PER_OCTAVE] = False
	return callback

note_states = [False] * 12


def main():
	PORT_MIDI = "UM-ONE 0"

	english_names = ["C", "Db", "D", "Eb", "E", "F", "F#", "G", "Ab", "A", "Bb", "B"]
	solfeggio_names = ["Do", "Réb", "Ré", "Mib", "Mi", "Fa", "Fa#", "Sol", "Lab", "La", "Sib", "Si"]

	midi_to_name_eng_8va, name_to_midi_eng_8va = build_note_dictionaries(english_names, True)
	midi_to_name_fr, name_to_midi_fr = build_note_dictionaries(solfeggio_names, False)
	print(midi_to_name_eng_8va[64])
	print(name_to_midi_eng_8va["C0"])
	print(midi_to_name_fr[61])
	print(midi_to_name_fr[73])
	print(name_to_midi_fr["Fa#"])

	input("Appuyez sur ENTER pour passer à l'étape suivante...")
	print("- - " * 30)

	midi_to_name, name_to_midi = build_note_dictionaries(solfeggio_names, True)
	print_note_name = build_print_note_name_callback(midi_to_name)
	keyboard = mido.open_input(PORT_MIDI, callback=print_note_name)

	input("Affichage des noms de notes (Appuyez sur ENTER pour passer à l'étape suivante)..." "\n")
	keyboard.close()

	print("- - " * 30)

	chord_names = {
		"Do majeur" : ("Do", "Mi", "Sol"),
		"Fa majeur" : ("Fa", "La", "Do"),
		"Sol majeur" : ("Sol", "Si", "Ré"),
		"La mineur" : ("La", "Do", "Mi")
	}
	
	midi_to_name, name_to_midi = build_note_dictionaries(solfeggio_names, False)
	print_chord_name = build_print_chord_name_callback(chord_names, name_to_midi)
	keyboard = mido.open_input(PORT_MIDI, callback=print_chord_name)
	
	input("Affichage des noms d'accords (Appuyez sur ENTER pour passer à l'étape suivante)..." "\n")
	keyboard.close()

if __name__ == "__main__":
	main()
