# runBucket

Paprplane is a super tiny web application for sending messages to your friends. Users can create accounts and send messages to their friends by indicating the correct username.

Paprplane is a work in progress with many hurdles left to jump before it's production-ready:

1. Change the database: Currently Paprplane uses a sqlite database, which I plan to migrate to PostgreSQL before taking this thing live.
2. Improve aesthetics: Currently working with very minimal CSS so the app looks pretty bare-bones, especially the forms. Will probably integrate Bootstrap CSS.
3. Validation Rules: Improve validation rules for email and other form inputs.
4. Improve the name. There are alreay multiple messaging apps on the web working with some variation on the paper airplane theme.

Paprplane is not live yet. To check it out on Unix or Linux, follow these steps:

1. Clone this repository to a local directory:

```bash
git clone https://github.com/mcrwfrd/runBucket.git
```

2. Navigate to the cloned directory and install RunBucket as a Python package:

```bash
cd paprplane
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
