from app import app, db
from app.models import User, Run

@app.shell_context_processor
def make_shell_contract():
    return {'db': db, 'User': User, 'Run': Run}




#from datetime import datetim
#from datetime import time
# import datetime
# import os
# import sqlite3
# import time
# from werkzeug import check_password_hash, generate_password_hash
# from flask_bootstrap import Bootstrap
#
# from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash, _app_ctx_stack
#
# from io import BytesIO
# from .forms import UsernamePasswordForm, UsernameEmailPasswordForm, RunDistanceDateForm


#
# app = Flask(__name__)
# app.config.from_object(__name__)
# bootstrap = Bootstrap(app)
# PER_PAGE = 30
#
# app.config.update(dict(
#     DATABASE=os.path.join(app.root_path, 'runBucket.db'),
#     SECRET_KEY='development key',
#     USERNAME='admin',
#     PASSWORD='default'
# ))
# app.config.from_envvar('RUNBUCKET_SETTINGS', silent=True)
#
# def get_db():
#     """Opens a new database connection if there is none yet for the
#     current application context.
#     """
#     top = _app_ctx_stack.top
#     if not hasattr(top, 'sqlite_db'):
#         top.sqlite_db = sqlite3.connect(app.config['DATABASE'])
#         top.sqlite_db.row_factory = sqlite3.Row
#     return top.sqlite_db
#
# @app.teardown_appcontext
# def close_db(error):
#     if hasattr(g, 'sqlite_db'):
#         g.sqlite_db.close()
#
# def init_db():
#     db = get_db()
#     with app.open_resource('schema.sql', mode='r') as f:
#         db.cursor().executescript(f.read())
#     db.commit()
#
# @app.cli.command('initdb')
# def initdb_command():
#     """Initializes the database."""
#     init_db()
#     print('Initialized the database.')
#
# def query_db(query, args=(), one=False):
#     """Queries the database and returns a list of dictionaries."""
#     cur = get_db().execute(query, args)
#     rv = cur.fetchall()
#     return (rv[0] if rv else None) if one else rv
#
# def get_user_id(username):
#     """Convenience method to look up the id for a username."""
#     rv = query_db('select user_id from user where username = ?',
#                   [username], one=True)
#     return rv[0] if rv else None
#
# def get_username(user_id):
#     """Convenience method to look up the username for an id."""
#     rv = query_db('select username from user where user_id = ?',
#                   [user_id], one=True)
#     return rv[0] if rv else None
#
# def format_datetime(timestamp):
#     """Format a timestamp for display."""
#     return datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d @ %H:%M')
#
# def flash_errors(form):
#     """Flashes form errors"""
#     for field, errors in form.errors.items():
#         for error in errors:
#             flash(u"Error in the %s field - %s" % (
#                 getattr(form, field).label.text,
#                 error
#             ), 'error')

# Now in views
#@app.before_request
#def before_request():
#    g.user = None
#    if 'user_id' in session:
#        g.user = query_db('select * from user where user_id = ?', [session['user_id']], one=True)

# Now in views
#@app.route('/')
#def welcome():
#    return render_template('welcome.html')

# Now in views
# @app.route('/dashboard')
# def dashboard():
#     runs = query_db('''select * from run
#                         order by run.pub_date desc limit ?''', [PER_PAGE])
#
#     legend = 'Running Data'
#     label_query = query_db('''select pub_date from run
#                 where run.user_id = ?
#                 group by pub_date''',
#                 [session['user_id']])
#     labels = []
#     for label in label_query:
#         labels.append(label[0])
#
#     value_query = query_db('''select sum(distance) from run
#                  where run.user_id = ?
#                  group by pub_date''',
#                  [session['user_id']])
#     values = []
#     for value in value_query:
#         values.append(value[0])
#
#     return render_template('dashboard.html',
#                            runs=runs,
#                            values=values,
#                            labels=labels,
#                            legend=legend)

# Now in views
# @app.route('/newrun', methods=['GET', 'POST'])
# def newrun():
#     if 'user_id' not in session:
#         abort(401)
#     error = None
#     form = RunDistanceDateForm()
#     #if request.method == 'POST':
#     if form.validate_on_submit():
#         db = get_db()
#         db.execute('''insert into run (user_id, user_username, run_name, distance, note, pub_date, time_stamp) values (?, ?, ?, ?, ?, ?, ?)''', [
#             session['user_id'],
#             get_username(session['user_id']),
#             request.form['runName'],
#             request.form['runDistance'],
#             request.form['runComments'],
#             str(request.form['runDate']),
#             int(time.time())])
#         db.commit()
#         flash('New run successfully logged!')
#         return redirect(url_for('dashboard'))
#     else:
#         flash_errors(form)
#         print(form.errors.items())
#
#     return render_template('newrun.html', form=form)

# Now in views
#
# Replaced by register when moved checks to form
#@app.route('/register', methods=['GET', 'POST'])
# def register2():
#     if g.user:
#         return redirect(url_for('dashboard'))
#     error = None
#     if request.method == 'POST':
#         if not request.form['username']:
#             error = 'You must enter a username'
#         elif not request.form['email'] or '@' not in request.form['email']:
#             error = 'You must enter a valid email address'
#         elif not request.form['password']:
#             error = 'You must enter a password'
#         elif request.form['password'] != request.form['password2']:
#             error = 'Passwords do not match'
#         elif get_user_id(request.form['username']) is not None:
#             error = 'Someone already beat you to that sweet username'
#         else:
#             db = get_db()
#             db.execute('''insert into user (username, email, pw_hash) values (?, ?, ?)''', [
#                 request.form['username'],
#                 request.form['email'],
#                 generate_password_hash(request.form['password'])])
#             db.commit()
#             flash('Registration successful. Now you can login!')
#             return redirect(url_for('login'))
#     return render_template('register.html', error=error)

# Now in views
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if g.user:
#         return redirect(url_for('dashboard'))
#     error = None
#     form = UsernameEmailPasswordForm()
#     if form.validate_on_submit():
#         db = get_db()
#         db.execute('''insert into user (username, email, pw_hash) values (?, ?, ?)''', [
#             request.form['username'],
#             request.form['email'],
#             generate_password_hash(request.form['password'])])
#         db.commit()
#         flash('Registration successful. Now you can login!')
#         return redirect(url_for('login'))
#     return render_template('register.html', form=form, error=error)

# Now in views
#@app.route('/logout')
#def logout():
#    session.pop('user_id', None)
#    flash('You have successfully logged out!')
#    return redirect(url_for('welcome'))

# add some filters to jinja
#app.jinja_env.filters['datetimeformat'] = format_datetime
