#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import decimal
from json import JSONEncoder, dumps

from aiohttp import web
from aiohttp_apispec import docs, marshal_with, use_kwargs
from marshmallow import Schema, fields

from models.lblog import get_comments
from utils import myjsondumps


class RequestSchema(Schema):
    id = fields.Int()
    name = fields.Str(description="name")


class ResponseSchema(Schema):
    msg = fields.Str()
    data = fields.Dict()


class Comment(web.View):
    @docs(
        tags=["mytag"],
        summary="View method summary",
        description="View method description",
    )
    @use_kwargs(RequestSchema(strict=True))
    @marshal_with(ResponseSchema(), 200)
    async def get(self):
        comments = await get_comments(self.request.app["db_pool"])
        return web.json_response(
            {"msg": "done", "data": comments}, dumps=myjsondumps)
