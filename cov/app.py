from flask import Flask, render_template, jsonify
import utils
from jieba.analyse import extract_tags
import string

app = Flask(__name__)


@app.route('/')
def index():
    data_list = utils.get_confirmed_data()
    return render_template("index.html", data=data_list)


@app.route('/index')
def home():
    # return render_template("index.html")
    return index()


@app.route('/region')
def region():
    region_list = utils.get_region_list()
    return render_template("region.html", regions=region_list)


@app.route('/his')
def his():
    his_list = utils.get_his_list()
    return render_template("his.html", his=his_list)


@app.route('/word')
def word():
    return render_template("word.html")


@app.route('/team')
def team():
    return render_template("team.html")


@app.route('/area')
def area():
    area_list = utils.get_area_data()
    return render_template("area.html", area=area_list)


@app.route('/echarts')
def echarts():
    echarts_list = utils.get_echarts_data()
    city = []
    confirm = []
    for i, j in echarts_list:
        city.append(i)
        confirm.append(int(j))
    return render_template("echarts.html", city=city, confirm=confirm)


if __name__ == '__main__':
    app.run()
