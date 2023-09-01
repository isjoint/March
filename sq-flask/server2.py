"""
@date: 2023/8/31
@author: March
@desc: test

"""
# 启动文件，程序入口

# 排查问题的两个大方向：
# 1.新增文件有没有运行
# 2.有没有绑定到核心对象app上

from app import create_app
# from config import settings
my_app = create_app()
my_app.run(host=my_app.config['HOST'],
           port=my_app.config['PORT'],
           debug=my_app.config['DEBUG'])
# my_app.run(host=settings.HOST,
#            port=settings.PORT,
#            debug=settings.DEBUG)








