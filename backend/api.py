from flask import make_response, jsonify
from . import crawler

def register_api(bp):
    @bp.route("/qz")
    def qz():
        data = crawler.crawl("全站")
        response = make_response(jsonify(data))
        response.headers['Content-Type'] = "application/json"
        response.headers['Access-Control-Allow-Origin'] = "*"
        return response
    
    @bp.route("/gcxg")
    def gcxg():
        data = crawler.crawl("国创相关")
        response = make_response(jsonify(data))
        response.headers['Content-Type'] = "application/json"
        response.headers['Access-Control-Allow-Origin'] = "*"
        return response
    
    @bp.route("/dh")
    def dh():
        data = crawler.crawl("动画")
        response = make_response(jsonify(data))
        response.headers['Content-Type'] = "application/json"
        response.headers['Access-Control-Allow-Origin'] = "*"
        return response
    
    @bp.route("/yy")
    def yy():
        data = crawler.crawl("音乐")
        response = make_response(jsonify(data))
        response.headers['Content-Type'] = "application/json"
        response.headers['Access-Control-Allow-Origin'] = "*"
        return response
    
    @bp.route("/wd")
    def wd():
        data = crawler.crawl("舞蹈")
        response = make_response(jsonify(data))
        response.headers['Content-Type'] = "application/json"
        response.headers['Access-Control-Allow-Origin'] = "*"
        return response
    
    @bp.route("/yx")
    def yx():
        data = crawler.crawl("游戏")
        response = make_response(jsonify(data))
        response.headers['Content-Type'] = "application/json"
        response.headers['Access-Control-Allow-Origin'] = "*"
        return response    
    
    @bp.route("/zs")
    def zs():
        data = crawler.crawl("知识")
        response = make_response(jsonify(data))
        response.headers['Content-Type'] = "application/json"
        response.headers['Access-Control-Allow-Origin'] = "*"
        return response
    
    @bp.route("/kj")
    def kj():
        data = crawler.crawl("科技")
        response = make_response(jsonify(data))
        response.headers['Content-Type'] = "application/json"
        response.headers['Access-Control-Allow-Origin'] = "*"
        return response
    
    @bp.route("/yd")
    def yd():
        data = crawler.crawl("运动")
        response = make_response(jsonify(data))
        response.headers['Content-Type'] = "application/json"
        response.headers['Access-Control-Allow-Origin'] = "*"
        return response
    
    @bp.route("/qc")
    def qc():
        data = crawler.crawl("汽车")
        response = make_response(jsonify(data))
        response.headers['Content-Type'] = "application/json"
        response.headers['Access-Control-Allow-Origin'] = "*"
        return response
    
    @bp.route("/sh")
    def sh():
        data = crawler.crawl("生活")
        response = make_response(jsonify(data))
        response.headers['Content-Type'] = "application/json"
        response.headers['Access-Control-Allow-Origin'] = "*"
        return response
    
    @bp.route("/ms")
    def ms():
        data = crawler.crawl("美食")
        response = make_response(jsonify(data))
        response.headers['Content-Type'] = "application/json"
        response.headers['Access-Control-Allow-Origin'] = "*"
        return response
    
    @bp.route("/dwq")
    def dwq():
        data = crawler.crawl("动物圈")
        response = make_response(jsonify(data))
        response.headers['Content-Type'] = "application/json"
        response.headers['Access-Control-Allow-Origin'] = "*"
        return response
    
    @bp.route("/gc")
    def gc():
        data = crawler.crawl("鬼畜")
        response = make_response(jsonify(data))
        response.headers['Content-Type'] = "application/json"
        response.headers['Access-Control-Allow-Origin'] = "*"
        return response
    
    @bp.route("/ss")
    def ss():
        data = crawler.crawl("时尚")
        response = make_response(jsonify(data))
        response.headers['Content-Type'] = "application/json"
        response.headers['Access-Control-Allow-Origin'] = "*"
        return response
    
    @bp.route("/yl")
    def yl():
        data = crawler.crawl("娱乐")
        response = make_response(jsonify(data))
        response.headers['Content-Type'] = "application/json"
        response.headers['Access-Control-Allow-Origin'] = "*"
        return response
    
    @bp.route("/ys")
    def ys():
        data = crawler.crawl("影视")
        response = make_response(jsonify(data))
        response.headers['Content-Type'] = "application/json"
        response.headers['Access-Control-Allow-Origin'] = "*"
        return response
    
    @bp.route("/yc")
    def yc():
        data = crawler.crawl("原创")
        response = make_response(jsonify(data))
        response.headers['Content-Type'] = "application/json"
        response.headers['Access-Control-Allow-Origin'] = "*"
        return response
    
    @bp.route("/xr")
    def xr():
        data = crawler.crawl("新人")
        response = make_response(jsonify(data))
        response.headers['Content-Type'] = "application/json"
        response.headers['Access-Control-Allow-Origin'] = "*"
        return response
