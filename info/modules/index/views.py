from flask import render_template, current_app, session

from info import constants
from info.models import User, News
from . import index_blu


@index_blu.route('/')
def index():
    """
    显示首页
    1.如果用户已经登录，将当前用户的数据传到模板中，供模板显示
    :return:
    """
    # 显示用户是否登录的逻辑
    # 取到用户id
    # user_id = session.get("user_id", None)
    # user = None
    # if user_id:
    #     # 尝试查询用户的模型
    #     try:
    #         user = User.query.get(user_id)
    #     except Exception as e:
    #         current_app.logger.error(e)

    user_id = session.get("user_id", None)
    user = None
    if user_id:
        try:
            user = User.query.get(user_id)
        except Exception as e:
            current_app.logger.error(e)

    # 右侧的新闻排行的逻辑
    news_list = []
    try:
        news_list = News.query.order_by(News.clicks.desc()).limit(6)
    except Exception as e:
        current_app.logger.error(e)

    # 定义一个空的字典列表，里面装的就是字典
    news_dict_li = []
    # 遍历对象列表，将对象的字典添加到字典列表中
    for news in news_list:
        news_dict_li.append(news.to_basic_dict())

    # # 查询分类数据，通过模板的形式渲染出来
    # categories = Category.query.all()

    # category_li = []
    # for category in categories:
    #     category_li.append(category.to_dict())

    data = {
        "user": user.to_dict() if user else None,
        "news_dict_li": news_dict_li
        # "category_li": category_li
    }

    return render_template("news/index.html", data=data)


# 在打开网页的时候 浏览器会默认去请求根路径+favicon.ico作网站标签的小图标
@index_blu.route('/favicon.ico')
def favicon():
    return current_app.send_static_file('news/favicon.ico')
