from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, DateField, DecimalField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, Optional
from werkzeug import check_password_hash, generate_password_hash

class UsernamePasswordForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

#    def __init__(self, *args, **kwargs):
#        Form.__init__(self, *args, **kwargs)
#        self.user = None
#
#    def validate(self):
#        rv = Form.validate(self)
#        if not rv:
#            return False
#
#        user = query_db('''select * from user where username = ?''',
#                        [self.username.data],
#                        one=True)
#        if user is None:
#            self.username.errors.append('Unknown username')
#            return False
#
#        if not check_password_hash(user['pw_hash'], self.password.data):
#            self.password.errors.append('Invalid password')
#
#        self.user = user
#        return True






class UsernameEmailPasswordForm(Form):
    username = StringField('Username', validators=[DataRequired()]) #check uniq
    email = StringField('Email', validators=[DataRequired(), Email()]) #same
    password = PasswordField('Password',
                              validators=[DataRequired(),
                              EqualTo('checkPassword', message='Passwords must match')])
    checkPassword = PasswordField('Repeat Password',
                                  validators=[DataRequired()])
    submit = SubmitField('Sign Up')

class RunDistanceDateForm(Form):
    runName = StringField('Run Name', validators=[DataRequired()])
    runDistance = DecimalField('Distance', places=2)
    #runUnits = RadioField('Units', ['km', 'mi'])
    runComments = TextAreaField('Comments', validators=[Optional()])
    runDate = DateField('Run Date',
                        format='%Y-%m-%d',
                        validators=[DataRequired()])
    submit = SubmitField('Log Run')
