from configparser import ConfigParser


def get_data(file, category, key):
    config = ConfigParser()
    config.read(file)
    return config.get(category, key)