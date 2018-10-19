import logging

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from info import create_app, db

# manage.py 是程序启动的入口，之关心启动的相关参数以及内容
# 不关心具体该如何创建app或者相关业务逻辑

# 通过指定的配置名字创建对应配置的app
# create_app 就类似于 工厂方法
app = create_app('development')

manager = Manager(app)
# 将app与db关联
Migrate(app, db)
# 将迁移命令添加到manager中
manager.add_command('db', MigrateCommand)





if __name__ == '__main__':
    manager.run()
