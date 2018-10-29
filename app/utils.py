#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import decimal
import hashlib
from json import JSONEncoder, dumps


class DecimalEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return float(o)
        super(DecimalEncoder, self).default(o)


def myjsondumps(content):
    # ensure_ascii=False， 即不转换为ascii编码（中文会以unicode的方式显示：\u8bd5）
    return dumps(content, cls=DecimalEncoder, ensure_ascii=False)


def hash_sha256(ctt, key):
    sha256 = hashlib.sha256(key.encode('utf-8'))
    sha256.update(ctt.encode('utf-8'))
    return sha256.hexdigest()
