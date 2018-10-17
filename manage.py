from flask import session
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from info import create_app, db

# 通过指定的配置名字创建对应配置的app
# create_app 就类似于 工厂方法
app = create_app('development')

manager = Manager(app)
# 将app与db关联
Migrate(app, db)
# 将迁移命令添加到manager中
manager.add_command('db', MigrateCommand)


@app.route('/')
def index():
    session["name"] = "Desperado-lr"
    return 'index'


if __name__ == '__main__':
    manager.run()
