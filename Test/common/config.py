# -*- coding:utf-8 -*-

import configparser
import os


config_file = "config.ini"


def load_config(filename):
    try:
        config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), filename))
        cfg = configparser.ConfigParser()
        cfg.read(config_path, encoding="utf-8")
    except Exception as e:
        print(e)
    return cfg


config = load_config(config_file)

ip = config['machine']['ip']
url = config['machine']['url']



