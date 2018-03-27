# runBucket

runBucket helps you acheive your long-distance running goals by allowing you to record your runs and visualise your progress.

You can create an account, input the data for each run you complete (such as date, time, and distance), and visualise your achievement each day in a bar chart made with [chart.js](http://www.chartjs.org/).

runBucket is a work in progress. The following things are next on my to-do list:

1. Migrate from sqlite to MySQL
1. Write unit tests
2. Write error-catching code
2. Set up a continuous integration testing environment using Docker
3. Push to live server

runBucket will eventually be a live applucation, but for now you'll have enjoy it locally. To check it out on Unix or Linux, follow these steps:

1. Clone this repository to a local directory:

```bash
git clone https://github.com/mcrwfrd/runBucket.git
```

2. Navigate to the cloned directory and install RunBucket as a Python package:

```bash
cd runBucket
export FLASK_APP=runBucket.py
```

3. Initlize the database migrations directory and execute initial migration:

```bash
flask db init
flask db migrate
```

4. Run the application:

```bash
flask run
```
