# flask_hook
flask请求钩子

### 1.flask请求钩子类型
 1) before_first_request在处理第一个请求之前运行注册的函数
 2) before_request 在每次请求前运行注册的函数
 3) after_request 在每次请求之后运行未出错的注册函数
 4) teardown_request 在每次请求之后运行注册函数，无视异常

### 2.flask全局变量g
 在flask中使用全局变量g来完成数据在各个钩子和处理函数之间的传递

### 3.请求钩子参数
 对于after_request和teardown_request，他们默认接受一个参数，一个response对象，由视图函数产生，这两个函数可以直接返回该resp，也可以做一些处理
 例如取出resp中的数据，进行计算，再用make_response方法重新创建一个resp对象

### 4.代码逻辑
 1) 在before_request中初始化数据库连接
 2) 运行hello_world视图函数
 3) 运行after_request
 4) 在teardown_request中释放数据库连接
