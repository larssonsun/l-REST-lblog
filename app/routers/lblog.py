#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from views.lblog import Comment
from aiohttp_apispec import setup_aiohttp_apispec


def setup_routes(app):
    app.router.add_get("/v1/Comment", Comment.get)
    app.router.add_patch(
        "/v1/Comment/" + r"{id:[a-zA-Z0-9\-]{36}}", Comment.patch)
    setup_aiohttp_apispec(app=app, title="L-blog REST API Documentation",
                          version="v1", url="/api/docs/api-docs")
