#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import views.lblog as blog_view


def setup_routes(app):
    app.router.add_get("/v1/comment", blog_view.get)
    app.router.add_patch(
        "/v1/comment/" + r"{id:[a-zA-Z0-9\-]{36}}", blog_view.patch)
