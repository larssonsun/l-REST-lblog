#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pathlib
import pytoml as toml
# import os

BASE_DIR = pathlib.Path(__file__).parent.parent
# os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PACKAGE_NAME = 'app'


def load_config(path):
    with open(path) as f:
        conf = toml.load(f)
    return conf