#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from aiohttp import web
from aiohttp_apispec import docs, marshal_with, use_kwargs
from marshmallow import Schema, fields

from models.lblog import get_comments
from utils import myjsondumps


class PatchComment_HideStatus_Schema(Schema):
    hide_status = fields.Int(description="comments hide_status")


class ResponseSchema(Schema):
    msg = fields.Str()
    data = fields.Dict()


@docs(
    tags=["comment"],
    summary="get all comments",
    description="get all content from all comments.",
)
@use_kwargs(PatchComment_HideStatus_Schema(strict=True))
@marshal_with(ResponseSchema(), 200)
async def get(request):
    comments = await get_comments(request.app["db_pool"])
    return web.json_response(
        {"msg": "done", "data": comments}, dumps=myjsondumps)


@docs(
    tags=["comment"],
    summary="update the comment's status",
    description="get one comment by id, then update the status by status.",
)
@use_kwargs(PatchComment_HideStatus_Schema(strict=True))
@marshal_with(ResponseSchema(), 200)
async def patch(request):
    payloadDict = request["data"]
    return web.json_response(
        {"msg": "done", "data": payloadDict}, dumps=myjsondumps)
