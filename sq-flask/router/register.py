"""
@date: 2023/8/31
@author: March
@desc: test

"""
from flask import Blueprint, request
from libs.response import generate_response

register_bp = Blueprint("register", __name__, url_prefix="/v1/")

# 保存用户信息
# userdict = {}
@register_bp.route("/register")
def register():
    username = request.json.get("username")
    passwd = request.json.get("passwd")
    re_passwd = request.json.get("re_passwd")
    if username and passwd and re_passwd:
        if passwd != re_passwd:
            return generate_response(message="密码不一致！", code=10001)
        if username in userdict:
            return generate_response(message="用户已存在！", code=10001)
        else:
            userdict['username'] = username
            userdict['passwd'] = passwd
            print(f"userdict is {userdict}")
            return generate_response(message="注册成功！")
    return generate_response(message="参数不完整！", code=10001)
