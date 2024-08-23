import logging
import os
import time


def setup_logging(logs_dir, con_level, file_level=logging.DEBUG):
	con_handler = logging.StreamHandler()
	con_handler.setLevel(con_level)

	if not os.path.exists(logs_dir):
		os.mkdir(logs_dir)
	filename = "{}/{}.log".format(
		logs_dir,
		time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
	)
	file_handler = logging.FileHandler(filename)
	file_handler.setLevel(file_level)

	log_fmt = logging.Formatter(fmt="[%(asctime)s][%(levelname)-8s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
	con_handler.setFormatter(log_fmt)
	file_handler.setFormatter(log_fmt)

	logging.getLogger().addHandler(con_handler)
	logging.getLogger().addHandler(file_handler)
	logging.getLogger().setLevel(logging.DEBUG)


def main():
	setup_logging("logs", logging.WARNING)

	print("Hello, world!")
	logging.debug("Hey!")
	logging.info("Look!")
	logging.warning("Listen!")
	logging.error("HelloOo!")
	time.sleep(1.1)
	logging.critical("Watch out!")
	print("Bye!")

if __name__ == "__main__":
	main()
