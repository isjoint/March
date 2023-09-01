"""
@date: 2023/8/31
@author: March
@desc: test

"""
# 管理视图
from flask import Blueprint

view01_bp = Blueprint("view01", __name__, url_prefix="/v1/")

@view01_bp.route("/index")
def index():
    return "this is index"
