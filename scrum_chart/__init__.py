import datetime
from flask import Flask, request, session, g, render_template, redirect, url_for
from operator import itemgetter, attrgetter

app = Flask(__name__)
app.config.from_object('config')

from scrum_chart.database import db, Scrum, ScrumSprint, Project

@app.route('/')
def index():
    scrum_id = request.args.get('scrum_id')
    scrumList = None
    if scrum_id != None:
        source = getdataFromDb(scrum_id)
        scrumList = ScrumSprint.query.filter_by(scrum_id = scrum_id).all()
    else:
        source = getdataFromQuery(request)

    return render_template('index.html',
        source = source,
        scrums = Scrum.query.all(),
        projects = Project.query.all(),
        scrumList = scrumList
    )

@app.route('/sprint/add', methods=['POST'])
def addSprint():
    scrum_id = request.form.get("scrum_id")

    if scrum_id == None:
        return redirect(url_for('index'))
    scrum = Scrum.query.filter_by(id = scrum_id).first()
    if scrum == None:
        return redirect(url_for('index'))
    if request.form['left_sprint'] == '' or request.form['day'] == '':
        return redirect(url_for('index', scrum_id = scrum.id))

    scrumSprint = ScrumSprint(scrum_id = scrum_id, day = request.form['day'], left_sprint = request.form['left_sprint'])
    db.session.add(scrumSprint)
    db.session.commit()

    return redirect(url_for('index', scrum_id = scrum.id))

@app.route('/sprint/update', methods=['POST'])
def updateSprint():
    scrum_id = request.form.get("scrum_id")
    if scrum_id == None:
        return redirect(url_for('index'))

    scrum = Scrum.query.filter_by(id = scrum_id).first()
    if scrum == None:
        return redirect(url_for('index'))

    sprint_id = request.form.get("sprint_id")
    if sprint_id == None:
        return redirect(url_for('index', scrum_id = scrum.id))

    if request.form['left_sprint'] == '':
        return redirect(url_for('index', scrum_id = scrum.id))

    scrumSprint = ScrumSprint.query.filter_by(id = sprint_id).first()
    scrumSprint.left_sprint = request.form['left_sprint']
    db.session.commit()

    return 'true'

def getdataFromQuery(request):
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

    return source

def getdataFromDb(scrum_id):
    scrum = Scrum.query.filter_by(id = scrum_id).first()
    start_date = datetime.datetime.strptime(scrum.start_date, '%Y-%m-%d')
    end_date = datetime.datetime.strptime(scrum.end_date, '%Y-%m-%d')
    days = calc_days(start_date, end_date)
    stand_line = get_stand_line_value(start_date, end_date, scrum.total_sprint, days)
    scrum_sprints = ScrumSprint.query.filter_by(scrum_id = scrum.id).all()
    scrum_sprints = sorted(scrum_sprints, key = attrgetter('day'))
    actual_values = []
    actual_values.append(scrum.total_sprint)

    for item in scrum_sprints:
        actual_values.append(item.left_sprint)

    return {
            'dates': stand_line[1],
            'stand_values':stand_line[0],
            'actual_values': actual_values
        }

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
    stand_value.append(total)
    dates = [0]
    while tag <= end_date:
        if tag.weekday() not in [6, 5]:
            total = round(total - step, 2)
        if total < 0:
            total = 0
        stand_value.append(total)
        dates.append(tag.strftime('%m-%d %A'))
        tag += datetime.timedelta(days=1)

    # stand_value.append(total)

    return [stand_value, dates]

