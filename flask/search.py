from flask import Flask, render_template, request
import os
import csv
import json
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/s')
def search():
    result = []
    keyword = request.args.get('wd')

    # check keyword
    keywords = ['开发',
            '系统',
            '教育',
            '政策',
            '国务院',
            '政府',
            '服务',
            '程序',
            '开源',
            '数据库',
            '资讯',
            '中国',
            '美国',
            '试题',
            '考试',
            '数学',
            '地理',
            '语文',
            '教材',
            '历史',
            '人物',
            '中华',
            '展览',
            '美术',
            '音乐'
            ]
    if keyword not in keywords:
        result.append(['xxx', 'keyword:({}) not supported!!! white list:{}'.format(keyword, keywords)])
        return render_template('search.html', titles=result)

    # debug
    # result = [['http://www.baidu.com', 'baidu'], ['http://www.sohu.com', 'sohu']]

    csv_rows = load_csv_file('../mySpider/data-reverse.csv')
    reverse_map = {}
    for row in csv_rows:
        reverse_map[row[0]] = row[1]
    freq_dict = reverse_map[keyword]
    print(freq_dict)
    pair_list = sorted(freq_dict.items(), key = lambda kv:(kv[1], kv[0]), reverse=True)
    print(freq_dict)
    if len(pair_list) > 5:
        pair_list = pair_list[0:5]
    for pair in pair_list:
        url = pair[0]
        name = pair[0]
        result.append([url, name])

    return render_template('search.html', titles=result)


def load_csv_file(filename):
    rows = []
    with open(filename) as csvfile:
        csv_reader = csv.reader(csvfile)
        next(csv_reader)
        for row in csv_reader:
            index = 1
            row[index] = row[index].replace("'", '"')
            row[index] = json.loads(row[index])
            rows.append(row)
    return rows


if __name__ == '__main__':
    app.run(debug=True, port=8000)