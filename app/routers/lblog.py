#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from views.lblog import Comment
from aiohttp_apispec import setup_aiohttp_apispec


def setup_routes(app):
    app.router.add_view("/v1/Comment", Comment)
    setup_aiohttp_apispec(app=app, title="My Documentation",
                          version="v1", url="/api/docs/api-docs")
