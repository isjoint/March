"""
@date: 2023/9/1
@author: March
@desc: test

"""
# 商品信息查询
from . import product_bp
from flask import current_app, request
from libs.response import generate_response

@product_bp.route("/product/get")
def get_product():
    # 通过url携带参数传递id
    id = request.args.get("id")
    if id is None:
        sql_str = "select * from product_kind_table p,product_info pi where p.id = pi.product_id"
    else:
        sql_str = f"select * from product_kind_table p,product_info pi where p.id = pi.product_id and product_id = {id}"
    cur = current_app.mysql_db.cursor()
    cur.execute(sql_str)
    data = cur.fetchall()
    if data:
        print(data)
        return generate_response(data=data, message="success!")
    else:
        return generate_response(message="get data empty", code=10002)






