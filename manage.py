from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from redis import StrictRedis
from  flask_session import Session


class Config(object):
    """项目的配置"""
    DEBUG = True

    SECRET_KEY = "cFkIZAsQm7CV3tTTYaNO3nVSS2p1Q/rrCFNlBlmptbFvcQn58o/bMgqOhELkdNU5"

     #  为mysql 添加配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:123456@127.0.0.1:3306/information4"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # redis 的配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    # Session 保存配置
    SESSION_TYPE = "redis"
    # 是否开始session签名
    SESSION_USE_SIGNER = True
    # 定义Session 保存的 redis
    SESSION_REDIS = StrictRedis(host=REDIS_HOST,port=REDIS_PORT)
    # 设置需要过期
    SESSION_PERMANENT = False
    # 设置过期时间
    PERMANENT_SESSION_LIFETIME =86400 * 2

app = Flask(__name__)

# 加载配置
app.config.from_object(Config)

# 初始化数据库
db = SQLAlchemy(app)
# 初始化redis存储对象
redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
# 开始当前项目 CSRF 保护，只做服务器验证
CSRFProtect(app)
# 设置Session 保存到指定位置
Session(app)

@app.route('/')
def index():
    session["name"] = "Desperado-lr"
    return 'index'


if __name__ == '__main__':

    app.run()