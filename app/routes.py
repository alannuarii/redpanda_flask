from cgi import test
from app import app
from app import db
from flask import render_template, request, redirect, url_for
from datetime import datetime, timedelta
from app.models.feeder import Feeder
import pandas as pd
import numpy as np



# Initialization
conn = app.config['SQLALCHEMY_DATABASE_URI']


@app.route('/')
def index():
    
    return render_template('pages/home.html', title='Home | RedPanda', active_home='active')


# FEEDER 
@app.route('/data-feeder', methods=['GET','POST'])
def data_feeder():
    if request.method == 'POST':
        feeder = request.files['feeder']
        data_excel = pd.read_excel(feeder)
        data_excel.to_sql(name='feeder', con=conn, if_exists='append', index=False)

    feeder_sql = pd.read_sql('feeder', con=conn).iloc[0:24,2:]
    feeder_sql['pltd_tahuna'] = feeder_sql.iloc[0:24,1:6].sum(axis=1)
    feeder_sql['pltd_petta'] = feeder_sql.iloc[0:24,7:10].sum(axis=1)
    feeder_sql['pltd_tamako'] = feeder_sql.iloc[0:24,11:13].sum(axis=1)
    feeder_sql['pltd_lesabe'] = feeder_sql.iloc[0:24,14:16].sum(axis=1)
    feeder_sql['total'] = feeder_sql.iloc[0:24,1:16].sum(axis=1)
    
    return render_template('pages/feeder/data-feeder.html', title='Data Feeder | RedPanda', active_feeder='active', columns=feeder_sql.columns.values, rows=list(feeder_sql.values.tolist()), zip=zip)


@app.route('/forecast-feeder', methods=['GET','POST'])
def forecast_feeder():
    today = datetime.now()
    day7 = today + timedelta(days=-7)
    day14 = today + timedelta(days=-14)
    day21 = today + timedelta(days=-21)
    day28 = today + timedelta(days=-28)

    data1 = pd.read_sql_query("SELECT * FROM feeder WHERE tanggal='{}'".format(day7.strftime('%Y-%m-%d')), con=conn).iloc[0:24,2:19]
    data2 = pd.read_sql_query("SELECT * FROM feeder WHERE tanggal='{}'".format(day14.strftime('%Y-%m-%d')), con=conn).iloc[0:24,2:19]
    data3 = pd.read_sql_query("SELECT * FROM feeder WHERE tanggal='{}'".format(day21.strftime('%Y-%m-%d')), con=conn).iloc[0:24,2:19]
    data4 = pd.read_sql_query("SELECT * FROM feeder WHERE tanggal='{}'".format(day28.strftime('%Y-%m-%d')), con=conn).iloc[0:24,2:19]

    list_data = [data1,data2,data3,data4]
    data_concat = pd.concat(list_data,keys=range(len(list_data))).groupby(level=1)
    forecast = data_concat.max()
    forecast['pltd_tahuna'] = forecast.iloc[0:24,1:6].sum(axis=1)
    forecast['pltd_petta'] = forecast.iloc[0:24,7:10].sum(axis=1)
    forecast['pltd_tamako'] = forecast.iloc[0:24,11:13].sum(axis=1)
    forecast['pltd_lesabe'] = forecast.iloc[0:24,14:16].sum(axis=1)
    forecast['total'] = forecast.iloc[0:24,1:16].sum(axis=1)
    
    return render_template('pages/feeder/forecast-feeder.html', title='Forecast Feeder | RedPanda', active_feeder='active', columns=forecast.columns.values, rows=list(forecast.values.tolist()), zip=zip, today=today.strftime('%d %B %Y'))