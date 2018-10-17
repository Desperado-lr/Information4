from redis import StrictRedis


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
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    # 设置需要过期
    SESSION_PERMANENT = False
    # 设置过期时间
    PERMANENT_SESSION_LIFETIME = 86400 * 2


class DevelopmentConfig(Config):
    """开发环境下的配置"""
    DEBUG = True


class PorductionConfig(Config):
    """生产环境下的配置"""
    DEBUG = False
    # 生产环境下的数据库配置
    SQLALCHEMY_DATABASE_URI = "mysql://root:123456@127.0.0.1:3306/information4"


class TestingConfig(Config):
    """单元测试环境下的配置"""
    DEBUG = True
    TESTING = True


config = {
    "development": DevelopmentConfig,
    "production": PorductionConfig,
    "testing": TestingConfig
}
