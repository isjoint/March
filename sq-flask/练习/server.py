
from flask import Flask, request
app = Flask(__name__)

# 路由和视图函数绑定
@app.route("/")
def hello():
    return "hello, world!"
@app.route("/home")
def home():
    return "this is home!"
def user():
    return "this is user"
# 构造动态url -- 通过url路径传递参数
app.add_url_rule("/user", view_func=user, endpoint="user2")\

# @app.route("/login/<username>/<passwd>")
# def login(username, passwd):
#     return f"username is {username},passwd is {passwd}"

# @app.route("/login2")
# def login2():
    # 通过url携带参数传递数据
    # print(request.args)
    # print(request.args.get("username"))
    # print(request.args.get("passwd"))

    # 通过json传递数据
    # username = request.json.get("username")
    # passwd = request.json.get("passwd")
    # if username == username and passwd == passwd:
    #     return "login2 html"
    # return "登录失败！"
    # 通过form表单传递数据
    # print(request.form.get("username"))
    # print(request.form.get("passwd"))
    # return "lgoin2..."

    # url属性，path属性
    # print(request.url)
    # print(request.path)
    # print(request.headers)
    # return "login html"

userdict = {}
@app.route("/regist")
def regist():
    username = request.json.get("username")
    passwd = request.json.get("passwd")
    re_passwd = request.json.get("re_passwd")
    if username and passwd and re_passwd:
        if passwd != re_passwd:
            return "注册密码不一致！"
        if username in userdict:
            return "用户已存在！"
        else:
            userdict[username] = passwd
            print(f"userdict is {userdict}")
            return "register success!"
    return "参数不完整！"

@app.route("/login")
def login():
    username = request.json.get("username")
    passwd = request.json.get("passwd")
    cur_user = userdict.get(username)
    if cur_user and passwd == cur_user:
        return "登录成功！"
    return "登录失败！"

@app.route("/status/<age>", methods=["GET", "POST"])
def status(age):
    if int(age) >= 18:
        return "可以上网！"
    else:
        return "未成年，禁止上网！"

# debug = True 开启debug模式，修改代码，自动加载，在开发模式下使用，发生错误会产生更多信息，方便排错
app.run(host="0.0.0.0", debug=True)


