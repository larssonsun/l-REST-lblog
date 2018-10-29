#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pathlib
from aiohttp import web
import pytoml as toml
from aiohttp_apispec import setup_aiohttp_apispec, validation_middleware
from aiohttp_swagger import setup_swagger
from utils import hash_sha256
import re

pathlib.Path(__file__).parent.parent  # __file__ 是用来获得模块所在的路径的，这可能得到的是一个相对路径
PACKAGE_NAME = 'app'


def load_config(path):
    with open(path) as f:
        conf = toml.load(f)
    return conf


# @web.middleware
# async def my_middleware(request, handler):
#     try:
#         # authorate token
#         if re.match("/api/docs/swagger\w*", request.path):
#             pass
#         elif not request.match_info.get("data"):
#             raise web.HTTPUnauthorized
#         else:
#             cfg_web = request.app["config"]["web"]
#             if hash_sha256(cfg_web["WEB_CLIENT_TOKEN"], cfg_web["WEB_CLIENT_TOKEN_HASHKEY"]) != request.match_info["data"].get("token"):
#                 raise web.HTTPNotAcceptable

#         return await handler(request)
#     except web.HTTPException as ex:
#         return web.json_response(status=ex.status)


def setup_apispec(app):
    setup_aiohttp_apispec(app=app, title="L-blog REST API Documentation",
                          version="v1", url="/api/docs/json")

    app.middlewares.extend([
        validation_middleware
    ])

    if app['config']['web']['WEB_SWAGGER_ENABLE']:
        app.on_startup.append(swagger)


async def swagger(app):
    setup_swagger(
        app=app, swagger_url='/api/docs/swagger', swagger_info=app['swagger_dict']
    )
