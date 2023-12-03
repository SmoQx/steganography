import numpy as np
import os
import pathlib


def file_encoder(file_name: pathlib.Path, password: str = "tekst"):
    if password == "tekst":
        with open(file_name) as file_to_encode:
            file = file_to_encode.read()
            print(file.split())
        np_loaded = np.loadtxt(file_name)
        return np_loaded


if __name__ == '__main__':
    file_encoder(pathlib.Path("./downloads/dane13.txt"))
