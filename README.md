# RunBucket

RunBucket is a minimalist run tracker that helps runners achieve their long-distance running goals by allowing them to record their runs and visualize their progress.

Runners can create an account, input the data for each run they complete (such as date, time, and distance), and visualize your achievement each day in an interactive bar chart.

### Tools
RunBucket is written in Python3 using the [Flask microframework](http://flask.pocoo.org/). The interactive bar charts are rendered with [Chart.js](https://www.chartjs.org/). The front end is a simple mix of [Flask-Bootstrap](https://pythonhosted.org/Flask-Bootstrap/), [Flask-Nav](https://pythonhosted.org/flask-nav/getting-started.html) and [Flask-WTF](https://flask-wtf.readthedocs.io/en/stable/). The databases is a straightforward MySQL databases, although some day I'd like to experiment with NoSQL here. Finally, the project is hosted on AWS EC2 using Gunicorn as the WSGI server and Nginx to serve requests to the app.

### Planned Features
- Add more KPIs for runs such as duration and vertical gain
- Sharing progress with other runners and tagging other runners that were with you on your run
- Establishing KPI goals and tracking goal progress
- Support for recording KPIs in Imperial units :us: (currently only logical measurement units are supported)

### Test Locally

RunBucket was hosted live on AWS for a time, but I took it offline. If you'd like to take it out for a spin on your local machine, the following instructions will help:
1. Clone this repository to a local directory:
```bash
git clone git@github.com:mcrwfrd/runBucket.git
```
2. Create a virtual environment for this project:
```bash
virtualenv runBucket
```
3. Now that we're safely inside a virtual environment, navigate to the cloned directory, install the requirements and initiate the app in the FLASK_APP environment variable:
```bash
cd /path/to/runBucket
pip3 install -r requirements.txt
export FLASK_APP=runBucket.py
```
4. Initlize the database migrations directory and execute initial migration and upgrade:
```bash
flask db init
flask db upgrade
```
5. Finally, run the application:
```bash
flask run
```
