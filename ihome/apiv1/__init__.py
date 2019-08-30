# coding:utf-8

from flask import Blueprint


# 创建蓝图对象
api = Blueprint("apiv1", __name__)


# 导入蓝图的视图
from . import html_index_demo, verify_code, passport, profile, houses, orders, pay
