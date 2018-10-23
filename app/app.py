#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

from aiohttp import web
from aiohttp_apispec import (docs, marshal_with, setup_aiohttp_apispec,
                             use_kwargs)
from marshmallow import Schema, fields
from model.db import init_db
from settings import PACKAGE_NAME, load_config

log = logging.getLogger(__name__)


class RequestSchema(Schema):
    id = fields.Int()
    name = fields.Str(description="name")


class ResponseSchema(Schema):
    msg = fields.Str()
    data = fields.Dict()


class TheView(web.View):
    @docs(
        tags=["mytag"],
        summary="View method summary",
        description="View method description",
    )
    @use_kwargs(RequestSchema(strict=True))
    @marshal_with(ResponseSchema(), 200)
    def delete(self):
        return web.json_response(
            {"msg": "done", "data": {"name": self.request["data"]["name"]}}
        )


def setup_routes(app):
    app.router.add_view("/v1/view", TheView)


async def init_app(config):
    app = web.Application()
    app['config'] = config

    setup_routes(app)
    setup_aiohttp_apispec(app=app, title="My Documentation", version="v1", url="/api/docs/api-docs"
                          )
    db_pool = await init_db(app)
    # redis_pool = await setup_redis(app)
    log.debug(app['config'])
    return app


def main(configpath):
    config = load_config(configpath)
    logging.basicConfig(level=config["log"]["LOG_LEVEL"])
    app = init_app(config)
    web.run_app(app, host=config["web"]["WEB_HOST"], port=config["web"]["WEB_PORT"])


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", help="Provide path to config file")
    args = parser.parse_args()

    if args.config:
        main(args.config)
    else:
        parser.print_help()
