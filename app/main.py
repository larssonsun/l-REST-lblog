#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

from aiohttp import web

from db import init_db, init_redis
from routers.lblog import setup_routes
from settings import PACKAGE_NAME, load_config

log = logging.getLogger(__name__)


async def init_app(config):
    app = web.Application()
    app['config'] = config
    setup_routes(app)
    db_pool = await init_db(app)
    redis_pool = await init_redis(app)
    log.debug(app['config'])
    return app


def main(configpath):
    config = load_config(configpath)
    logging.basicConfig(level=config["log"]["LOG_LEVEL"])
    app = init_app(config)
    web.run_app(app, host=config["web"]["WEB_HOST"],
                port=config["web"]["WEB_PORT"])


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", help="Provide path to config file")
    args = parser.parse_args()

    if args.config:
        main(args.config)
    else:
        parser.print_help()
