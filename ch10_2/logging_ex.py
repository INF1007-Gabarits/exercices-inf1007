import logging
import os
import time


def setup_logging(logs_dir, con_level, file_level=logging.DEBUG):
	# Créer le gestionnaire qui écrit dans la console.
	con_handler = logging.StreamHandler()
	con_handler.setLevel(con_level)

	# Créer le dossier de journaux s'il n'existe pas.
	if not os.path.exists(logs_dir):
		os.mkdir(logs_dir)
	# Construire le chemin du fichier selon la date et l'heure actuelle.
	filename = os.path.join(
		logs_dir,
		time.strftime("%Y%m%d_%H%M%S.log", time.localtime())
	)
	# Créer le gestionnaire qui écrit dans le fichier avec le nom ci-dessus.
	file_handler = logging.FileHandler(filename)
	file_handler.setLevel(file_level)

	# Configurer le format de chaque entrée dans le journal. On veut la date et l'heure du message, son niveau et le message lui-même.
	log_fmt = logging.Formatter(
		fmt="[%(asctime)s][%(levelname)-8s] %(message)s",
		datefmt="%Y-%m-%d %H:%M:%S"
	)
	con_handler.setFormatter(log_fmt)
	file_handler.setFormatter(log_fmt)

	# Ajouter nos deux handler au journaliseur par défaut.
	logging.getLogger().addHandler(con_handler)
	logging.getLogger().addHandler(file_handler)
	logging.getLogger().setLevel(logging.DEBUG)


def main():
	# Les messages de niveau Warning et plus sérieux sont affichés dans la console, tous les messages sont écrits dans le fichier.
	setup_logging("logs", logging.WARNING, logging.DEBUG)

	# Pas un message de journal, donc pas traité par le module de journalisation. Ça va être dans la console, mais sans le préambule, et ne sera pas écrit dans le fichier.
	print("Hello, world!")
	# Présent dans le fichier, pas dans la console.
	logging.debug("Hey!")
	logging.info("Look!")
	# Présent dans le fichier et la console
	logging.warning("Listen!")
	logging.error("HelloOo!")
	# Attendre une seconde.
	time.sleep(1.1)
	# Le timestamp du message va montrer la seconde de différence.
	logging.critical("Watch out!")
	print("Bye!")

if __name__ == "__main__":
	main()
