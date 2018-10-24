#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlalchemy
from sqlalchemy.dialects.mysql import (BIGINT, BINARY, BIT, BLOB, BOOLEAN,
                                       CHAR, DATE, DATETIME, DECIMAL, DOUBLE,
                                       ENUM, FLOAT, INTEGER, LONGBLOB,
                                       LONGTEXT, MEDIUMBLOB, MEDIUMINT,
                                       MEDIUMTEXT, NCHAR, NUMERIC, NVARCHAR,
                                       REAL, SET, SMALLINT, TEXT, TIME,
                                       TIMESTAMP, TINYBLOB, TINYINT, TINYTEXT,
                                       VARBINARY, VARCHAR, YEAR)
from sqlalchemy.ext.declarative import declarative_base

sa = sqlalchemy
metadata = sa.MetaData()

comm = sa.Table('comments', metadata,
                sa.Column("id", VARCHAR(50), primary_key=True, nullable=False),
                sa.Column("blog_id", VARCHAR(50), index=True, nullable=False),
                sa.Column("user_id", VARCHAR(50), nullable=False),
                sa.Column("user_name", VARCHAR(50), nullable=False),
                sa.Column("user_image", VARCHAR(500), nullable=False),
                sa.Column("content", MEDIUMTEXT(),  nullable=False),
                sa.Column("created_at", DOUBLE(), nullable=False),
                sa.Column("user_id", VARCHAR(50), nullable=False),
                sa.Column("parent_comment_id", VARCHAR(50), nullable=False),
                sa.Column("to_userName", VARCHAR(50), nullable=False),
                sa.Column("hide_status", SMALLINT(50), nullable=False))


async def get_comments(engine):
    result = None
    async with engine.acquire() as conn:
        result_proxy = await conn.execute(
            comm.select().where(comm.c.id != None)
        )
        row_proxy = await result_proxy.fetchall()
        result = [dict(rp) for rp in row_proxy]
    return result


# class Comm(Base):
#     __tablename__ = "comments"

#     id = sa.Column("id", VARCHAR(50), primary_key=True, nullable=False)
#     blog_id = sa.Column("blog_id", VARCHAR(50), index=True, nullable=False)
#     user_id = sa.Column("user_id", VARCHAR(50), nullable=False)
#     user_name = sa.Column("user_name", VARCHAR(50), nullable=False)
#     user_image = sa.Column("user_image", VARCHAR(500), nullable=False)
#     content = sa.Column("content", MEDIUMTEXT(),  nullable=False)
#     created_at = sa.Column("created_at", DOUBLE(), nullable=False)
#     user_id = sa.Column("user_id", VARCHAR(50), nullable=False)
#     parent_comment_id = sa.Column("parent_comment_id", VARCHAR(50), nullable=False)
#     to_userName = sa.Column("to_userName", VARCHAR(50), nullable=False)
#     hide_status = sa.Column("hide_status", SMALLINT(50), nullable=False)

# class Blog(Base):
#     __tablename__ = "blogs"

#     id = sa.Column("id", VARCHAR(50), primary_key=True, nullable=False)
#     user_id = sa.Column("user_id", VARCHAR(50), nullable=False)
#     user_name = sa.Column("user_name", VARCHAR(50), index=True, nullable=False)
#     # `title_image` varchar(500) NOT NULL,
#     name_en = sa.Column("name_en", VARCHAR(100), unique=True, nullable=False)
#     name = sa.Column("name", VARCHAR(50), unique=True, nullable=False)
#     summary = sa.Column("summary", VARCHAR(200), nullable=False)
#     content = sa.Column("content", MEDIUMTEXT(),  nullable=False)
#     created_at = sa.Column("created_at", DOUBLE(), index=True, nullable=False)
#     updated_at = sa.Column("updated_at", DOUBLE(), nullable=False)
#     updated_at = sa.Column("updated_at", INTEGER(255), nullable=False)
#     index = sa.Column("index", INTEGER(255), nullable=False)
#     browse_count = sa.Column("browse_count", INTEGER(255), nullable=False)
#     source_from = sa.Column("source_from", VARCHAR(255), nullable=False)
#     tags = sa.Column("tags", VARCHAR(255), nullable=False)
#     catelog = sa.Column("catelog", VARCHAR(255), nullable=False)
