from time import time
import argparse
import numpy as np

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('-p', '--path', dest="data", type=str, default=2,
                    help='le path jusquau donnees')


if __name__ == "__main__":
    args = parser.parse_args()
    print(args.data)

