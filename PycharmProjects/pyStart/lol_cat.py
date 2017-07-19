import os
import platform

import requests
import shutil

import subprocess


def get_url():
    url = "http://consuming-python-services-api.azurewebsites.net/cats/random"
    response = requests.get(url, stream=True)
    save_cat(response.raw)


def get_cat():
    pass


def save_cat(data):
    path = os.path.dirname(__file__)
    file_name = "cat_pic.jpg"
    # print(path+file_name)
    full_path = os.path.join(path, file_name)
    # print(full_path)
    with open(full_path, 'wb') as fout:
        # fout.write(data)
        shutil.copyfileobj(data, fout)
    open_image(full_path)


def open_image(full_path):
    # if platform.system() == 'windows':
    #full_path='C:/"Program Files (x86)"/"Mozilla Firefox"'+"/firefox.exe"
    subprocess.call(full_path, shell=True)


def main():
    get_url()


main()
