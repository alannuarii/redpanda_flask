from cgi import test
import imp
from app import app
from app import db
from flask import render_template, request, redirect, url_for, flash
from datetime import datetime, timedelta
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from app.models.user import User
from app.models.feeder import Feeder
from app.models.har import Har
from app.models.unit import Unit
from app.models.mesin import Mesin

import pandas as pd
import numpy as np



# Initialization
conn = app.config['SQLALCHEMY_DATABASE_URI']

# Pemeliharaan
P1 = [1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1]
P2 = [1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1]
P3 = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]
P4 = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]
P5 = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1]
TO = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
SO = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
MO = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
PdM = [1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1]
CM = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]


@app.route('/login', methods=['GET','POST'])
def login():
    tahun = datetime.now().strftime('%Y')

    if current_user.is_authenticated:
        return redirect(url_for('index'))

    if request.method=='POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()

        if not user:
            flash('Anda memasukkan email yang salah')
            return redirect(url_for('login'))
        if not user.checkPassword(password):
            flash('Anda memasukkan password yang salah')
            return redirect(url_for('login'))

        login_user(user)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)

    return render_template('pages/login.html', title='Login | RedPanda', tahun=tahun)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/')
# @login_required
def index():
    # name = 'Alan Nuari'
    # email = 'email@alan.web.id'
    # password = 'admin'
    # level = 1
    # admin = User(name=name, email=email, level=level)
    # admin.setPassword(password)
    # db.session.add(admin)
    # db.session.commit()
    return render_template('pages/home.html', title='Home | RedPanda', active_home='active')


# FEEDER 
@app.route('/data-feeder', methods=['GET','POST'])
@login_required
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
@login_required
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



# PEMELIHARAAN
@app.route('/rencana-pemeliharaan', methods=['GET','POST'])
@login_required
def rencana_pemeliharaan():
    mesins = Mesin.query.all()
    query = request.args.get('tanggal')
    hars = Har.query.filter_by(tanggal_jumat=query).all()

    if query:
        friday = datetime.strptime(query, '%Y-%m-%d')
        delta_friday = friday + timedelta(days=+6)
        tanggal_friday = friday.strftime('%A')

        if request.method == 'POST':
            result=request.form.to_dict(flat=False)
            for i in range(len(mesins)):
                tanggal_jumat = result['tanggal_jumat'][0]
                jumat = result['jumat'][i]
                sabtu = result['sabtu'][i]
                minggu = result['minggu'][i]
                senin = result['senin'][i]
                selasa = result['selasa'][i]
                rabu = result['rabu'][i]
                kamis = result['kamis'][i]
                mesin_id = result['mesin_id'][i]
                har = Har(tanggal_jumat=tanggal_jumat, jumat=jumat, sabtu=sabtu, minggu=minggu, senin=senin, selasa=selasa, rabu=rabu, kamis=kamis, mesin_id=mesin_id)
                db.session.add(har)
                db.session.commit()

        return render_template('pages/rencana-pemeliharaan.html', title='Rencana Pemeliharaan | RedPanda', active_har='active', mesins=mesins, hars=hars, delta_friday=delta_friday.date(), tanggal_friday=tanggal_friday)

    
        
    return render_template('pages/rencana-pemeliharaan.html', title='Rencana Pemeliharaan | RedPanda', active_har='active', mesins=mesins, hars=hars)