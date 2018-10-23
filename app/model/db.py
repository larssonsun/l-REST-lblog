#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlalchemy as sa
from aiomysql.sa import create_engine


async def init_db(app, config):
    engine = await create_engine(user=config['DB_USER'], db=config['DB_NAME'],
                                 host=config['DB_HOST'], password=config['DB_PASS'])

    app['db_pool'] = engine.pool
    return pool


# async def create_pool(self):
#     pool = await aiomysql.create_pool(host=self.__host, port=self.__port, user=self.__user, password=self.__pwd,
#                                       db=self.__db, loop=self.__loop, charset=self.__charset, autocommit=self.__autocommit, maxsize=self.__maxsize,
#                                       minsize=self.__minsize)
#     return pool
