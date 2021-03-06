import os
import json
import pandas as pd
from collections import namedtuple
import requests
import yaml


# ------------------------------------ MISC ---------------------------------- #
def connected_to_internet(url="http://www.google.com", timeout=5):
    """
       Check that there is an internet connection

       :param url: url to use for testing (Default value = 'http://www.google.com')
       :param timeout: timeout to wait for [in seconds] (Default value = 5)
    """

    try:
        _ = requests.get(url, timeout=timeout)
        return True
    except requests.ConnectionError:
        print("No internet connection available.")
    return False


# --------------------------------- FOLDERS ---------------------------------- #
def listdir(fld):
    """
    List the files into a folder with the complete file path instead of the relative files path luke os.listdir.

    :param fld: string, folder path

    """
    if not os.path.isdir(fld):
        raise FileNotFoundError("Could not find directory: {}".format(fld))

    return [os.path.join(fld, f) for f in os.listdir(fld)]


def get_subdirs(folderpath):
    """
    returns the subfolders in a given folder
    """
    return [f.path for f in os.scandir(folderpath) if f.is_dir()]


def get_last_dir_in_path(folderpath):
    if not os.path.isdir(folderpath):
        raise FileNotFoundError("Invalid path: {}".format(folderpath))
    return os.path.basename(os.path.normpath(folderpath))


def check_create_folder(folderpath, raise_error=False):
    # Check if a folder exists, otherwise creates it
    if not os.path.isdir(folderpath):
        if raise_error:
            raise FileNotFoundError("Could not find directory: {}".format(folderpath))
        else:
            os.mkdir(folderpath)


def check_folder_empty(folderpath, raise_error=False):
    if not len(os.listdir(folderpath)):
        return True
    else:
        if not raise_error:
            return False
        else:
            raise FileExistsError("The folder {} is not empty".format(folderpath))


# ----------------------------------- FILES ---------------------------------- #
def check_file_exists(filepath, raise_error=False):
    # Check if a file with the given path exists already
    if os.path.isfile(filepath):
        return True
    elif raise_error:
        raise FileExistsError("File {} doesn't exist".format(filepath))
    else:
        return False


def get_file_name(filepath):
    # Returns just the name, no complete path or extension
    return os.path.splitext(os.path.basename(filepath))[0]
