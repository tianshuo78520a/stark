from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column
from sqlalchemy import Integer,String, Text, Date, DateTime
from sqlalchemy import create_engine
from flask import g
from chun import db


class New(db.Model):
    __tablename__ = 'new'

    id = Column(Integer, primary_key=True)
    title = Column(String(255), nullable=False)  # 文章标题
    info = Column(String(12222222), nullable=False)  # 文章内容
    picture = Column(String(255), nullable=False)  # 图片地址
    href = Column(String(255), nullable=False)  # 文章路径
    of = Column(String(64), nullable=False)  # 文章来源




