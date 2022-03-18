from flask_wtf import FlaskForm
from wtforms import TextAreaField,SubmitField, StringField, SelectField
from wtforms.validators import DataRequired,Email,EqualTo
from ..models import User
from flask_wtf.file import FileField, FileRequired, FileAllowed


# class RegisterUser(FlaskForm):

class CreateProfile(FlaskForm):
    fullname = StringField('Enter your full name',validators = [DataRequired()])
    position = TextAreaField('Job Position ',validators=[DataRequired()])
    job_id = StringField('Job ID',validators = [DataRequired()])
    department = StringField('Departments',validators = [DataRequired()])
    awards = TextAreaField('Awards ',validators=[DataRequired()])
    experience = TextAreaField('Experience ',validators=[DataRequired()])

    submit = SubmitField('Update')


    
    


class LeaveForm(FlaskForm):
    category = SelectField('Categories', choices=[('Annual Leave', 'Annual Leave'), 
    ('Maternity Leave', 'Maternity Leave'), ('Paternity Leave', 'Paternity Leave'), 
    ('Emergency Leave', 'Emergency Leave'), ('Sick Leave', 'Sick Leave'),
    ('Study Leave', 'Study Leave'), ('Special Leave', 'Special Leave')], validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Request Leave')