#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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
