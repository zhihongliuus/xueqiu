# -*- coding: utf-8 -*-

"""
xueqiu.api
~~~~~~~~~~

This module contains some XueQiu API strings.

:copyright: (c) 2019 by 1dot75cm.
:license: MIT, see LICENSE for more details.
"""

import os
import platform

# prefix
host = "xueqiu.com"
prefix = "https://xueqiu.com"
prefix2 = "https://stock.xueqiu.com"
cookie_file = platform.system() == "Linux" and \
    os.path.join(os.getenv('HOME'), ".xueqiu", "cookie") or \
    os.path.join(os.getenv('LOCALAPPDATA') or "", "xueqiu", "cookie")  # linux or windows

# stock
stock_quote = prefix2 + "/v5/stock/quote.json?symbol=%s&extend=detail"  # 基本信息
stock_quotec_v5 = prefix2 + "/v5/stock/realtime/quotec.json?symbol=%s"  # 实时行情
stock_quotec_v4 = prefix + "/v4/stock/quotec.json?code=%s"
stocks_quote_v5 = prefix2 + "/v5/stock/batch/quote.json?symbol=%s"  # 多股信息
stocks_quote_v4 = prefix + "/v4/stock/quote.json?code=%s"
# https://stock.xueqiu.com/v5/stock/chart/minute.json?symbol=.DJI&period=1d  # 分时行情
# https://stock.xueqiu.com/v5/stock/history/trade.json?symbol=TSLA&count=20  # 成交明细
# https://stock.xueqiu.com/v5/stock/realtime/quotec.json?symbol=TSLA         # 实时行情
# https://xueqiu.com/recommend/pofriends.json?type=1&code=TSLA&start=0&count=14 # 关注该股票的球友
# https://xueqiu.com/stock/portfolio/popstocks.json?code=TSLA&start=0&count=8   # 大家还关注
# https://xueqiu.com/stock/industry/stockList.json?code=TSLA&type=1&size=8      # 同行业股票
hot_stocks = prefix2 + "/v5/stock/hot_stock/list.json?type=%s&size=%s"  # 热门股票
# type 全球10 沪深12 港股13 美股11
user_stocks = prefix2 + "/v5/stock/portfolio/stock/list.json?uid=%s&pid=-%s&category=1&size=%s" # 用户关注
# pid 全球1, 沪深5, 港股7, 美股6

# selector
selector = prefix + "/stock/screener/screen.json"
select_areas = prefix + "/stock/screener/areas.json"  # 地区
select_industries = prefix + "/stock/screener/industries.json?category=%s"  # 行业
select_fields = prefix + "/stock/screener/fields.json?category=%s"  # 指标
# https://xueqiu.com/stock/screener/values.json?category=SH&field=follow7d

# user, article
# login https://github.com/Rockyzsu/xueqiu
send_code = prefix + "/account/sms/send_verification_code.json"  # post: areacode=86, telephone
user_login = prefix + "/snowman/login"  # post: username password, telephone code
comments = prefix + "/statuses/comments.json?id=%s&count=%s&page=%s&asc=%s"  # 评论
user_page = prefix + "/statuses/original/show.json?user_id=%s"  # 个人信息
user_friends = prefix + "/friendships/groups/members.json?uid=%s&page=%s&gid=0"  # 关注
user_follows = prefix + "/friendships/followers.json?uid=%s&pageNo=%s"  # 粉丝
user_timeline = prefix + "/v4/statuses/user_timeline.json?user_id=%s&page=%s&count=%s"  # 帖子
user_article = prefix + "/statuses/original/timeline.json?user_id=%s&page=%s&count=%s"  # 专栏
news = prefix + "/v4/statuses/public_timeline_by_category.json?since_id=-1&max_id=%s&category=%s&count=%s"  # 首页新闻
# 头条-1, 直播6, 沪深105, 港股102, 美股101, 基金104, 私募113, 房产111, 汽车114, 保险110

# search
search_stock = prefix + "/stock/search.json?code=%s&size=%s&page=%s"
search_post = prefix + "/statuses/search.json?q=%s&symbol=%s&count=%s&page=%s&sort=%s&source=%s"
# sort=[time最新|reply评论|relevance默认] source=[all|user讨论|news新闻|notice公告|trans交易]
search_user = prefix + "/users/search.json?q=%s&count=%s&page=%s"
search_cube = prefix + "/cube/search.json?q=%s&count=%s&page=%s"

# xpath
x_post_content = "//div[@class='article__bd__detail']//text()"