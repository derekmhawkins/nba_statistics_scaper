from app import app
import requests, csv, os
from flask import render_template, flash, redirect, url_for, session
from bs4 import BeautifulSoup
from app.datascraper import cleanData
from app.forms import DataForm, SessionForm, CSVForm, CronjobForm
from app import selenium
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
    for i in session.get('data'):
        csv_list.append(i)
    with open(os.path.join(os.path.dirname(__file__), f'{datetime.utcnow().strftime("%m%d%Y%H%M%S")}.csv'), 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(csv_list)
    session.clear()
    flash("Information saved to CSV file", "success")
    return redirect(url_for('index'))


@app.route('/setCronjob', methods=['POST'])
def setCronjob():
    selenium.execute()
    flash("Cronjob Dpdated", "success")
    return redirect(url_for('index'))
