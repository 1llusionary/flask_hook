import yaml
import os

def get_config():
    # 获取当前文件路径 F:\PythonPro\flask_test
    file_path = os.path.dirname(__file__)

    # 获取配置文件的路径 F:\PythonPro\flask_test\config.yaml
    yaml_path = os.path.join(file_path, 'config.yaml')
    f = open(yaml_path, 'r')
    cont = f.read()
    data = yaml.load(cont)
    #print(data)
    f.close()
    return data