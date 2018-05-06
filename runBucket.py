from app import app, db
from app.models import User, Run

@app.shell_context_processor
def make_shell_contract():
    return {'db': db, 'User': User, 'Run': Run}
