import os
from generate_caption import main

def test_single_image(capfd):
    os.system("caption --image examples/cat_running.jpeg")
    out, err = capfd.readouterr()
    num_lines = len([line for line in out.split("\n") if line != ""])
    assert num_lines == 1


def test_folder(capfd):
    os.system("caption --folder examples")
    out, err = capfd.readouterr()
    num_lines = len([line for line in out.split("\n") if line != ""])
    assert num_lines == 3


def test_folder_ext(capfd):
    os.system("caption --folder examples --ext .png")
    out, err = capfd.readouterr()
    num_lines = len([line for line in out.split("\n") if line != ""])
    assert num_lines == 1


def test_invalid_ext(capfd):
    os.system("caption --folder examples --ext invalid")
    out, err = capfd.readouterr()
    assert f"No images with extension invalid found in examples." in out


def test_invalid_folder(capfd):
    os.system("caption --folder invalid")
    out, err = capfd.readouterr()
    assert f"Invalid value for '--folder'" in err


def test_invalid_image(capfd):
    os.system("caption --image invalid")
    out, err = capfd.readouterr()
    assert f"Invalid value for '--image'" in err
