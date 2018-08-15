from flask import request, jsonify, send_from_directory, abort, Flask, Response, make_response, g
from yaml_out import get_config
import pymysql
from test_g import test_g

app = Flask(__name__)
app.debug = True


# @app.after_request
# def after_request(response):
#     print(response)
#     print(response.data)
#     data = bytes.decode(response.data)
#     print(data)
#     print(type(data))
#     resp = make_response(data)
#     resp.headers['Content-Type'] = 'text/json'
#     print('after response')
#     print(resp)
#     return resp

#  请求前中间件
@app.before_request
def before_request():
    print('before is running')
    path = request.path  # 获取请求的URL信息,例如  /usr/service
    conf = get_config()  # 获取yaml中所有配置信息，dict
    url_list = conf['url_list']  # 获取所有需要连接数据库的URL
    if path in url_list:
        dbconfig = conf['dbconfig']
        dbconfig['cursorclass'] = pymysql.cursors.DictCursor  # 以字典格式取出数据

        # 使用flask全局变量g来传递参数
        g.conn = pymysql.connect(**dbconfig)
        g.cursor = g.conn.cursor()
        print(g.conn)
    else:
        pass


#  在每次请求之后运行未出错的注册函数
@app.after_request
def after_quest(resp):
    print('after is runnig')
    data = bytes.decode(resp.data)
    resp = make_response(data)
    resp.headers['Content-Type'] = 'text/json'  # 返回JSON
    return resp


#  在每次请求之后运行注册函数，无视异常
@app.teardown_request
def tear_request(resp):
    print('tear is running')
    if hasattr(g, 'cursor'):  # 如果全局变量g中存在cursor对象
        g.cursor.close()
    if hasattr(g, 'conn'):  # 如果全局变量g中存在conn对象
        g.conn.close()
    return resp


@app.route('/usr/service')
def hello_world():
    print('hello')
    print(g.conn)  # 此处获取到的conn与before_request中的为同一个
    test_g()
    return '{"Status": "Success", "B": "2", "C": "400",  "D": "2016-02-23 13:15:30"' \
           ', "E": "4",   "F": "Windows+IIS","G": "2016-02-23 13:15:30","A": "0",}'


if __name__ == '__main__':
    app.run()
