from flask import make_response, jsonify
from . import crawler

def register_api(bp):
    @bp.route("/<category>")
    def dispatch(category):
        mapp = {
            'qz': '全站',
            'gcxg': '国创相关',
            'dh': '动画',
            'yy': '音乐',
            'wd': '舞蹈',
            'yx': '游戏',
            'zs': '知识',
            'kj': '科技',
            'yd': '运动',
            'qc': '汽车',
            'sh': '生活',
            'ms': '美食',
            'dwq': '动物圈',
            'gc': '鬼畜',
            'ss': '时尚',
            'yl': '娱乐',
            'ys': '影视',
            'yc': '原创',
            'xr': '新人',
        }
        if category not in mapp:
            response = make_response(jsonify({'error': f'{category}不存在！'}))
        else:
            data = crawler.crawl(mapp[category])
            response = make_response(jsonify(data))
        response.headers['Content-Type'] = "application/json"
        response.headers['Access-Control-Allow-Origin'] = "*"
        return response
    
    crawler.init()
