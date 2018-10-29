#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pathlib
import pytoml as toml
from aiohttp_swagger import setup_swagger

pathlib.Path(__file__).parent.parent #__file__ 是用来获得模块所在的路径的，这可能得到的是一个相对路径
PACKAGE_NAME = 'app'


def load_config(path):
    with open(path) as f:
        conf = toml.load(f)
    return conf

    
async def swagger(app):
    setup_swagger(
        app=app, swagger_url='/api/doc', swagger_info=app['swagger_dict']
    )
