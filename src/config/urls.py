import sys

from src.config.definitions import CRAWL_MAX_PRICE_ITEM, CRAWL_MIN_PRICE_ITEM, CSGO
#csgo & dota2    730 & 570
BUFF_ROOT = 'https://buff.163.com/'
STEAM_ROOT = 'https://steamcommunity.com/'
BUFF_GOODS = BUFF_ROOT + 'api/market/goods?'
BUFF_HISTORY_PRICE = BUFF_ROOT + 'api/market/goods/price_history?'
BUFF_HISTORY_PRICE_CNY = BUFF_ROOT + 'api/market/goods/price_history/buff?'


def goods_root_url():
    if CSGO==1:
        return BUFF_ROOT + 'market/?game=csgo#tab=selling&page_num=1'
    else: 
        return BUFF_ROOT + 'market/?game=dota2#tab=selling&page_num=1'

def category_root_url(category):
    if CSGO==1:
        return BUFF_GOODS + 'game=csgo&page_num=1&category=%s' % category
    else:
        return BUFF_GOODS + 'game=dota2&page_num=1&category=%s' % category
    


def category_page_url(page_num, category):
    if CSGO==1:
        return BUFF_GOODS + 'game=csgo&page_num={}&category={}'.format(page_num, category)
    else: 
        return BUFF_GOODS + 'game=dota2&page_num={}&category={}'.format(page_num, category)

def steam_price_history_url(item):
    """7 days history prices"""
    name = item.steam_url.rsplit('/', 1)[-1]
    if CSGO==1:
        return STEAM_ROOT + 'market/pricehistory/?appid=730&market_hash_name={}'.format(name)
    else: 
        return STEAM_ROOT + 'market/pricehistory/?appid=570&market_hash_name={}'.format(name)
    

def buff_price_history_url(item_id):
    if CSGO==1:
        return BUFF_HISTORY_PRICE_CNY + 'game=csgo&goods_id={}&currency=CNY&days=7'.format(item_id)
    else: 
        return BUFF_HISTORY_PRICE_CNY + 'game=dota2&goods_id={}&currency=CNY&days=7'.format(item_id)
    


def goods_section_root_url(category):
    """
    buff HAS BUG: only request with page number beyond actual upper bound,
    can you get the true page number with this price section.

    So sys.maxsize here is used as page number in order to get all page number and item count.
    """
    if CSGO==1:
        base = BUFF_GOODS + 'game=csgo&page_num={}&sort_by=price.asc&min_price={}&max_price={}' \
        .format(sys.maxsize, CRAWL_MIN_PRICE_ITEM, CRAWL_MAX_PRICE_ITEM)
    else: 
        base = BUFF_GOODS + 'game=dota2&page_num={}&sort_by=price.asc&min_price={}&max_price={}' \
        .format(sys.maxsize, CRAWL_MIN_PRICE_ITEM, CRAWL_MAX_PRICE_ITEM)
    if category is not None:
        base += '&category={}'.format(category)

    return base


def goods_section_page_url(category, page_num, page_size=20):
    # buff support page_size parameter, but the max value can only be 80
    if CSGO==1:
        base = BUFF_GOODS + 'game=csgo&page_num={}&sort_by=price.desc&min_price={}&max_price={}&page_size={}' \
        .format(page_num, CRAWL_MIN_PRICE_ITEM, CRAWL_MAX_PRICE_ITEM, page_size)
    else: 
        base = BUFF_GOODS + 'game=dota2&page_num={}&sort_by=price.desc&min_price={}&max_price={}&page_size={}' \
        .format(page_num, CRAWL_MIN_PRICE_ITEM, CRAWL_MAX_PRICE_ITEM, page_size)
        
    if category is not None:
        base += '&category={}'.format(category)

    return base
