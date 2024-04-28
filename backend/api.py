from flask import make_response, jsonify, redirect, url_for, request
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
from . import crawler

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

def _ensure(fm, to):
    if fm > 100:
        fm = 100
    if fm < 1:
        fm = 1
    if to > 100:
        to = 100
    if to < 1:
        to = 1
    if to < fm:
        to = fm
    return fm,to
        
def register_api(bp):
    @bp.route("/<category>")
    def dispatch(category):
        if category not in mapp:
            response = make_response(jsonify({'error': f'{category}不存在！'}))
        else:
            data = crawler.crawl(mapp[category])
            tp = request.args.get("type", "json")
            allow_tps = ["json", "pie"]
            if tp not in allow_tps:
                tp = "json"
            if tp == "json":
                response = make_response(jsonify(data))
                response.headers['Content-Type'] = "application/json"
            elif tp == "pie":
                sub = request.args.get("sub", "view")
                table = ["view", "danmaku", "favorite", "coin", "share"]
                if sub not in table:
                    sub = "view"
                from_ = int(request.args.get("from", 1))
                to = int(request.args.get("to", 100))
                from_, to = _ensure(from_,to)
                plt.pie(np.array(data[sub][from_-1:to]))
                buffer = BytesIO()
                plt.savefig(buffer,format="png")
                buffer.seek(0)
                response = make_response(buffer)
                response.headers["Content-Type"] = "image/png"
        response.headers['Access-Control-Allow-Origin'] = "*"
        return response
    crawler.init()
