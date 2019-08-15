import datetime
from flask import Flask, request, session, g, render_template

# 加载 app 并添加基础配置
app = Flask(__name__)
app.config.from_object('config')

from scrum_chart.database import Scrum, db

@app.route('/')
def index():
    scrums = Scrum.query.all()
    total = request.args.get('total', 0)
    start = request.args.get('start', '2019-07-01')
    start = datetime.datetime.strptime(start, '%Y-%m-%d')
    end = request.args.get('end', '2019-07-10')
    end = datetime.datetime.strptime(end, '%Y-%m-%d')
    days = calc_days(start, end)
    stand_line = get_stand_line_value(start, end, total, days)

    actual_values = request.args.get('actual', [])

    source = {
        'dates': stand_line[1],
        'stand_values':stand_line[0],
        'actual_values': actual_values
    }
    return render_template('index.html',
        source = source,
        scrums = scrums
    )

@app.route('/chart')
def chart():
    scrum_No = request.args.get('scrum_No')
    scrum = Scrum.query.filter_by(No = scrum_No).first()
    print(scrum.start_date)
    start_date = datetime.datetime.strptime(scrum.start_date, '%Y-%m-%d')
    end_date = datetime.datetime.strptime(scrum.end_date, '%Y-%m-%d')
    days = calc_days(start_date, end_date)
    stand_line = get_stand_line_value(start_date, end_date, scrum.total_sprint, days)

    scrums = Scrum.query.all()
    return render_template('chart.html',
        source = {
            'dates': stand_line[1],
            'stand_values':stand_line[0],
            'actual_values': []
        },
        scrums = scrums
    )

def calc_days(start_date, end_date):
    days = 1
    tag = start_date
    while tag < end_date:
        if tag.weekday() not in [6, 5]:
            days += 1
        tag += datetime.timedelta(days=1)
    return days

def get_stand_line_value(start_date, end_date, total, days):
    tag = start_date
    total = float(total)
    step = round((total / days), 2)
    stand_value = []
    dates = []
    while tag <= end_date:
        if tag.weekday() not in [6, 5]:
            total = round(total - step, 2)
        if total < 0:
            total = 0
        stand_value.append(total)
        dates.append(tag.strftime('%m-%d %A'))
        tag += datetime.timedelta(days=1)

    return [stand_value, dates]

