# coding=utf-8
__author__ = 'oyty'

import os
from flask_script import Manager
from app import create_app

# os.getenv 获取环境变量
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

if __name__ == '__main__':
    manager.run()
