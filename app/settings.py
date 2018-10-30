#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pathlib
import re

import pytoml as toml
from aiohttp import web
from aiohttp_apispec import setup_aiohttp_apispec, validation_middleware
from aiohttp_swagger import setup_swagger

from utils import hash_sha256

pathlib.Path(__file__).parent.parent  # __file__ 是用来获得模块所在的路径的，这可能得到的是一个相对路径
PACKAGE_NAME = 'app'


def load_config(path):
    with open(path) as f:
        conf = toml.load(f)
    return conf


def setup_apispec(app):
    setup_aiohttp_apispec(
        app=app,
        title="L-blog REST API Documentation",
        version="v1",
        info={"description": "some markdown description"},
        securityDefinitions={
            "user": {"type": "apiKey", "name": "Authorization", "in": "header"}
        },
        url="/api/docs/json")

    app.middlewares.extend([
        my_middleware,
        validation_middleware
    ])

    if app['config']['web']['WEB_SWAGGER_ENABLE']:
        app.on_startup.append(swagger)


@web.middleware
async def my_middleware(request, handler):
    try:
        if re.match("/api/docs/swagger\w*", request.path):
            return await handler(request)

        # authorate apikey
        apikey = request.headers.get("Authorization")
        if not apikey:
            raise web.HTTPUnauthorized

        cfg_web = request.app['config']['web']
        if not apikey or hash_sha256(cfg_web["WEB_CLIENT_TOKEN"], cfg_web["WEB_CLIENT_TOKEN_HASHKEY"]) != apikey:
            raise web.HTTPNotAcceptable

        return await handler(request)
    except web.HTTPException as ex:
        return web.json_response(status=ex.status)


async def swagger(app):
    # def setAddonParms(route):
    #     if route.method not in ("GET", "POST", "PUT", "DELETE", "PATCH"):
    #         return None
    #     path = app["swagger_dict"]["paths"].get(route.resource.canonical)
    #     if not path:
    #         return None
    #     method = path.get(str.lower(route.method))
    #     if not method:
    #         return None
    #     parms = method.get("parameters")
    #     parms.extend([{'in': 'header', 'name': 'Accept-version',
    #                    'required': True, 'type': 'string'}])

    # [setAddonParms(route) for route in app.router.routes()]

    setup_swagger(
        app=app, swagger_url='/api/docs/swagger', swagger_info=app['swagger_dict']
    )
