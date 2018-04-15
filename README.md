# runBucket

runBucket helps you acheive your long-distance running goals by allowing you to record your runs and visualize your progress.

You can create an account, input the data for each run you complete (such as date, time, and distance), and visualize your achievement each day in a bar chart made with [chart.js](http://www.chartjs.org/).

runBucket is a work in progress. The following things are next on my to-do list:

1. ~~Migrate from sqlite to MySQL~~ :heavy_check_mark:
1. ~~Write unit tests~~ :heavy_check_mark: (ongoing)
2. ~~Write error-catching code~~ :heavy_check_mark: (ongoing)
2. Set up a continuous integration testing environment using Docker
3. ~~Push to live server~~ :heavy_check_mark:

runBucket will eventually be a live application, but for now you'll have enjoy it locally. To check it out on Unix or Linux, follow these steps:

1. Clone this repository to a local directory:
```bash
git clone https://github.com/mcrwfrd/runBucket.git
```
2. Create a virtual environment for this project:

```bash
mkvirtualenv runBucket
```
3. Now that we're safely inside a virtual environment, navigate to the cloned directory, install the requirements and initiate the app in the FLASK_APP environment variable:
```bash
cd /path/to/runBucket
pip install -r requirements.txt
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
