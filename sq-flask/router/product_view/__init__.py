"""
@date: 2023/9/1
@author: March
@desc: test

"""
from flask import Blueprint

product_bp = Blueprint("product_bp", __name__, url_prefix="/v1/")
# 导入在下面
from . import product


