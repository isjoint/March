"""
@date: 2023/8/31
@author: March
@desc: test

"""
from flask import Flask
import os
from libs.conn_mysql import conn_mysql
# 核心对象的设置和创建
def create_app():
    my_app = Flask(__name__)
    # 连接数据库
    my_app.mysql_db = conn_mysql()

    my_app.config.from_object('config.settings')

    # 从环境变量里读取
    if 'FLASK_CONF' in os.environ:
        my_app.config.from_envvar('FLASK_CONF')

    import router  # 运行到位
    router.init_app(my_app)  # 将蓝图和app绑定

    return my_app





