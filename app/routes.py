import requests, csv, os
from app import app, db
from app import selenium
from app.datascraper import cleanData
from app.forms import DataForm, SessionForm, CSVForm, CronjobForm
from app.models import Record
from flask import render_template, flash, redirect, url_for, session, jsonify
from bs4 import BeautifulSoup
from datetime import datetime

@app.route('/')
def index():
    dataForm = DataForm()
    sessionForm = SessionForm()
    csvForm = CSVForm()
    cronjobForm = CronjobForm()
    data = session.get('data')
    context = {'data': data, 'dataForm': dataForm, 'sessionForm': sessionForm, 'csvForm': csvForm,
               'cronjobForm': cronjobForm}
    return render_template('index.html', **context)


@app.route('/getData', methods=['POST'])
def getData():
    dataForm = DataForm()
    if dataForm.validate_on_submit():
        page = requests.get('https://www.nbastuffer.com/2019-2020-nba-player-stats/')
        data = BeautifulSoup(page.content, 'html.parser')
        html = [i for i in list(data.children)][3]
        tr_list = html.find_all('tr')[1:]
        session['data'] = cleanData(tr_list, dataForm.search.data)
        flash("Retrieved Data Successfully", "success")
        return redirect(url_for('index', data=session.get('data')))


@app.route('/clearSession', methods=['POST'])
def clearSession():
    session.clear()
    flash("Session has been cleared", "info")
    return redirect(url_for('index'))


@app.route('/tocsv', methods=['POST'])
def toCSV():
    row_list = ["NAME", "TEAM", "POS", "AGE", "GP", "MPG", "FTA", "FT%", "2PA", "2P%", "3PA", "3P%", "PPG", "RPG",
                "APG", "SPG", "BPG", "TOPG"]
    csv_list = [row_list]
    for list_ in session.get('data'):
        csv_list.append(list_)

        record = None
        for index, value in enumerate(list_):
            record = Record(
                name=list_[0],
                team=list_[1],
                pos=list_[2],
                age=list_[3],
                gp=list_[4],
                mpg=list_[5],
                fta=list_[6],
                ftp=list_[7],
                twpa=list_[8],
                twpp=float(list_[9]), 
                thpa=list_[10],
                thpp=float(list_[11]),
                ppg=float(list_[12]),
                rpg=float(list_[13]),
                apg=float(list_[14]),
                spg=float(list_[15]),
                bpg=float(list_[16]),
                topg=float(list_[17])
            )
        db.session.add(record)
        db.session.commit()
    with open(os.path.join(os.path.dirname(__file__), f'{datetime.utcnow().strftime("%m%d%Y%H%M%S")}.csv'), 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(csv_list)
    session.clear()
    flash("Saved to database", "info")
    flash("Information saved to CSV file", "success")
    return redirect(url_for('index'))


@app.route('/setCronjob', methods=['POST'])
def setCronjob():
    selenium.execute()
    flash("Cronjob Updated", "success")
    return redirect(url_for('index'))

@app.route('/records/<int:id>', methods=['GET'])
def get_record(id):
    return jsonify(Record.query.get(id).to_dict())

@app.route('/records', methods=['GET'])
def get_records():
    data = [i.to_dict() for i in Record.query.all()]
    return jsonify(data)

