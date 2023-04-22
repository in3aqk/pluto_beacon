# -*- coding: utf-8 -*-


__author__ = "Paolo Mattiolo IN3AQK"
__copyright__ = "Copyright 2023, IN3AQK"
__license__ = "GPL"
__version__ = "3"
__maintainer__ = "Paolo Mattiolo"


import os
import configparser
from functools import reduce


class Cfg:

    def readIni(self)->bool:
        """Reads the config file and populate the cfg variables

        Returns:
            boolean: Operation result
        """
        current_path = os.path.dirname(os.path.realpath(__file__))
        cfg_file = os.path.join("..",current_path, 'config', 'config.ini')

        if os.path.isfile(cfg_file):
            config = configparser.ConfigParser()
            config.read(cfg_file)
            # serverIp = config.get('DEFAULT','UDP_IP')
            # serverPort = config.getint('DEFAULT','UDP_PORT')

            return True
        else:
            print("Config file not found")
            return False
