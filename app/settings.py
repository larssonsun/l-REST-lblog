#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pathlib
import pytoml as toml

pathlib.Path('__file__').parent.parent
PACKAGE_NAME = 'app'


def load_config(path):
    with open(path) as f:
        conf = toml.load(f)
    return conf