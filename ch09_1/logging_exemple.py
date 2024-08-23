import logging


def logging_exemple():
    logging.basicConfig(level=logging.DEBUG, filename="./log.txt")

    logging.debug("debug logging test")
    logging.info("info logging test")
    logging.warning("warning logging test")
    logging.error("error logging test")
    logging.critical("critical logging test")


if __name__ == "__main__":
    logging_exemple()

    x =5
    x+=1
    print(x)