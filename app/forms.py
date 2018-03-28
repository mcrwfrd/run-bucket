from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField, DateField, DecimalField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Optional
from werkzeug import check_password_hash, generate_password_hash
from app.models import User


class UsernamePasswordForm(Form):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')


class UsernameEmailPasswordForm(Form):
    username = StringField('Username', validators=[DataRequired()]) #check uniq
    email = StringField('Email', validators=[DataRequired(), Email()]) #same
    password = PasswordField('Password',
                              validators=[DataRequired(),
                              EqualTo('checkPassword', message='Passwords must match')])
    checkPassword = PasswordField('Repeat Password',
                                  validators=[DataRequired()])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        existing_user = User.query.filter_by(username=self.username.data).first()
        if existing_user is not None:
            raise ValidationError('That usename is already taken! Please choose a different one.')


class RunDistanceDateForm(Form):
    runName = StringField('Run Name', validators=[DataRequired()])
    runDistance = DecimalField('Distance', places=2)
    #runUnits = RadioField('Units', ['km', 'mi'])
    runComments = TextAreaField('Comments', validators=[Optional()])
    runDate = DateField('Run Date',
                        format='%Y-%m-%d',
                        validators=[DataRequired()])
    submit = SubmitField('Log Run')
