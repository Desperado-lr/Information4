import logging

from redis import StrictRedis


class Config(object):
    """项目的配置"""
    DEBUG = True

    SECRET_KEY = "cFkIZAsQm7CV3tTTYaNO3nVSS2p1Q/rrCFNlBlmptbFvcQn58o/bMgqOhELkdNU5"

    #  为mysql 添加配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:123456@127.0.0.1:3306/information5"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 在请求结束时候，如果指定此配置为True 那么 SQLAchemy 会自动执行一次 db.session.commit()操作
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # redis 的配置
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    # Session 保存配置
    SESSION_TYPE = "redis"
    # 是否开始session签名
    SESSION_USE_SIGNER = True
    # 定义Session 保存的 redis
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    # 设置需要过期
    SESSION_PERMANENT = False
    # 设置过期时间
    PERMANENT_SESSION_LIFETIME = 86400 * 2

    # 设置日志等级
    LOG_LEVEL = logging.DEBUG


class DevelopmentConfig(Config):
    """开发环境下的配置"""
    DEBUG = True


class PorductionConfig(Config):
    """生产环境下的配置"""
    DEBUG = False
    # 生产环境下的数据库配置
    LOG_LEVEL = logging.WARNING
    # SQLALCHEMY_DATABASE_URI = "mysql://root:123456@127.0.0.1:3306/information4"


class TestingConfig(Config):
    """单元测试环境下的配置"""
    DEBUG = True
    TESTING = True


config = {
    "development": DevelopmentConfig,
    "production": PorductionConfig,
    "testing": TestingConfig
}
