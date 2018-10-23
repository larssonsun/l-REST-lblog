#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlalchemy as sa
from aiomysql.sa import create_engine


async def init_db(app):
    confdb = app['config']['database']
    engine = await create_engine(user=confdb['DB_USER'], db=confdb['DB_NAME'],
                                 host=confdb['DB_HOST'], port=confdb['DB_PORT'], password=confdb['DB_PASS'])

    async def close_db(app):
        app['db_pool'].close()
        await app['db_pool'].wait_closed()

    app.on_cleanup.append(close_db)
    app['db_pool'] = engine
    return engine