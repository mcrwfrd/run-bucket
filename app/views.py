import datetime
import os
import sqlite3
import time
from werkzeug import check_password_hash, generate_password_hash
from flask_bootstrap import Bootstrap
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, _app_ctx_stack
from io import BytesIO
from sqlalchemy import func
from app import app, db
from app.forms import UsernamePasswordForm, UsernameEmailPasswordForm, RunDistanceDateForm
from app.models import User, Run


@app.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        user_id = session['user_id']
        g.user = db.session.query(User).filter_by(id=user_id)


@app.route('/')
@app.route('/index')
def welcome():
    return render_template('welcome.html')


@app.route('/dashboard')
def dashboard():
    user_id = session['user_id']

    #runs = query_db('''select * from run
    #                    order by run.pub_date desc limit ?''', [PER_PAGE])
    runs = db.session.query(Run).filter_by(user_id=session['user_id']).order_by(Run.date).all()

    legend = 'Running Distance'
    #label_query = query_db('''select pub_date from run
    #            where run.user_id = ?
    #            group by pub_date''',
    #            [session['user_id']])
    label_query = db.session.query(Run.date).filter_by(user_id=user_id) \
                    .group_by(Run.date).all()
    print(label_query)
    labels = []
    for label in label_query:
        labels.append(label[0])

    # value_query = query_db('''select sum(distance) from run
    #              where run.user_id = ?
    #              group by pub_date''',
    #              [session['user_id']])
    value_query = db.session.query(func.sum(Run.distance)) \
                    .filter_by(user_id=user_id).group_by(Run.date).all()
    values = []
    for value in value_query:
        values.append(value[0])

    return render_template('dashboard.html',
                           runs=runs,
                           values=values,
                           labels=labels,
                           legend=legend)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if g.user:
        return redirect(url_for('dashboard'))
    form = UsernameEmailPasswordForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,
                    email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful. Now you can login!')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if g.user:
        return redirect(url_for('dashboard'))
    form = UsernamePasswordForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        flash('You have successfully logged in!')
        session['user_id'] = user.id
        return redirect(url_for('dashboard'))
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have successfully logged out!')
    return redirect(url_for('welcome'))


@app.route('/newrun', methods=['GET', 'POST'])
def newrun():
    if 'user_id' not in session:
        abort(401)
    form = RunDistanceDateForm()
    if form.validate_on_submit():
        print(form.runDistance.data)
        run = Run(name=form.runName.data,
                  distance=form.runDistance.data,
                  note=form.runComments.data,
                  date=form.runDate.data,
                  user_id=session['user_id'])
        db.session.add(run)
        db.session.commit()
        flash('New run successfully logged!')
        return redirect(url_for('dashboard'))
    return render_template('newrun.html', form=form)
