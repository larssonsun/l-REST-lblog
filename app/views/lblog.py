#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from aiohttp import web
from aiohttp_apispec import docs, marshal_with, use_kwargs
from marshmallow import Schema, fields

from models.lblog import get_comments

import decimal
from json import JSONEncoder, dumps


class DecimalEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        super(DecimalEncoder, self).default(o)


def myjsondumps(content):
    # ensure_ascii=False， 即不转换为ascii编码（中文会以unicode的方式显示：\u8bd5）
    return dumps(content, cls=DecimalEncoder, ensure_ascii=False)


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
