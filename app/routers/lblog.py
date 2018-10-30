#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import views.lblog as blog_view
from aiohttp import web


def setup_routes(app):

    app.router.add_get("/comment", blog_view.get, name="get_comments")
    app.router.add_patch(
        "/comment/" + r"{id:[a-zA-Z0-9\-]{36}}", blog_view.patch, name="update_comment_hidestatus")