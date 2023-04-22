# -*- coding: utf-8 -*-

__author__ = "Paolo Mattiolo IN3AQK"
__copyright__ = "Copyright 2023, IN3AQK"
__license__ = "GPL"
__version__ = "3"
__maintainer__ = "Paolo Mattiolo"


from libs.cfg import Cfg


cfg = None


class Beacon():

    def __init__(self):
        self.cfg = Cfg()
        self.cfg.readIni()
