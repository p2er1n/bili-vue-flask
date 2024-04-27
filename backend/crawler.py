import time
import requests
from . import database as db

# 各个排行榜的每个视频（原排名从高到底）的弹幕数/播放量，
# 弹播比从高到底每个视频的原排名

# 全站：https://api.bilibili.com/x/web-interface/ranking/v2
param = {
    '全站':'',
    '国创相关':'?rid=168',
    '动画':'?rid=1',
    '音乐':'?rid=3',
    '舞蹈':'?rid=129',
    '游戏':'?rid=4',
    '知识':'?rid=36',
    '科技':'?rid=188',
    '运动':'?rid=234',
    '汽车':'?rid=223',
    '生活':'?rid=160',
    '美食':'?rid=211',
    '动物圈':'?rid=217',
    '鬼畜':'?rid=119',
    '时尚':'?rid=155',
    '娱乐':'?rid=5',
    '影视':'?rid=181',
    '原创':'?rid=0&type=origin',
    '新人':'?rid=0&type=rookie',
}

headers = {
    'Host': 'api.bilibili.com',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:125.0) Gecko/20100101 Firefox/125.0',
    'Accept': '*/*',
    'Accept-Language': 'zh,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.bilibili.com/v/popular/rank/tech',
    'Origin': 'https://www.bilibili.com',
    'DNT': '1',
    'Sec-GPC': '1',
    'Connection': 'keep-alive',
    'Cookie': '',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'TE': 'trailers',
}
url = 'https://api.bilibili.com/x/web-interface/ranking/v2'

def _get_title(response_json):
   return [o['title'] for o in response_json['data']['list']]

def _get_view(response_json):
   return [o['stat']['view'] for o in response_json['data']['list']]    

def _get_danmaku(response_json):
   return [o['stat']['danmaku'] for o in response_json['data']['list']]    

def _get_favorite(response_json):
   return [o['stat']['favorite'] for o in response_json['data']['list']]    

def _get_coin(response_json):
   return [o['stat']['coin'] for o in response_json['data']['list']]    

def _get_share(response_json):
   return [o['stat']['share'] for o in response_json['data']['list']]    

def _get_reply(response_json):
   return [o['stat']['reply'] for o in response_json['data']['list']]    

def _get_author(response_json):
   return [{ 'name': o['owner']['name'], 'face': o['owner']['face'] } for o in response_json['data']['list']]    

def _update_cookie():
    response = requests.get('https://www.bilibili.com', headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:125.0) Gecko/20100101 Firefox/125.0'})
    if response.status_code != 200:
        raise Exception(f"status_code error: {response.status_code}, {response.url}")
    headers['Cookie'] = response.headers['Set-Cookie']

def _crawl(url, headers):
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"status_code error: {response.status_code}, {response.url}")
    response_json = response.json()
    return {
        'title': _get_title(response_json),
        'view': _get_view(response_json),
        'danmaku': _get_danmaku(response_json),
        'favorite': _get_favorite(response_json),
        'coin': _get_coin(response_json),
        'share': _get_share(response_json),
        'author': _get_author(response_json)
    }

def crawl(category):
    if category == None:
        category = "全站"
    if category not in param:
        raise Exception(f"{category} is not a valid category name!")

    res = db.get(category)
    if res != None:

       print(f"{category} is in db")
       
       data = {'title': [], 'view': [], 'danmaku': [], 'favorite': [], 'coin': [], 'share': [], 'author': []}
       for i,r in enumerate(res):
          data['title'].append(r[0])
          data['view'].append(r[1])
          data['danmaku'].append(r[2])
          data['favorite'].append(r[3])
          data['coin'].append(r[4])
          data['share'].append(r[5])
          data['author'].append({'name': r[6], 'face': r[7]})
       return data
    _update_cookie()
    res = _crawl(url + param[category], headers)
    for rk in range(len(res['title'])):
       db.store((res['title'][rk], res['view'][rk], res['danmaku'][rk], res['favorite'][rk], res['coin'][rk], res['share'][rk], res['author'][rk]['name'],res['author'][rk]['face'], category, rk, int(time.time())), category)
    print(f"cached {category}")
    return res

def init():
   print("initing...")
   l =  ['全站', '国创相关', '动画', '音乐', '舞蹈', '游戏', '知识', '科技', '运动', '汽车', '生活', '美食', '动物圈', '鬼畜', '时尚', '娱乐', '影视', '原创', '新人']
   for c in l:
      print(f"fetching {c}")
      crawl(c)
init()
      
if __name__ == "__main__":
    # test
    print(crawl("全站"))







