from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField

class DataForm(FlaskForm):
    search = StringField()
    scrapeSubmit = SubmitField('Scrape Data')

class SessionForm(FlaskForm):
    clear = SubmitField('CLEAR SESSION')

class CSVForm(FlaskForm):
    saveToCSV = SubmitField('Save to CSV file')

class CronjobForm(FlaskForm):
    submit = SubmitField('SET CRONJOB')