from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import InputRequired

class PitchForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired()])
    category = SelectField('Category', choices=[('Events','Events'),('Job','Job'),('Advertisement','Advertisement')],validators=[InputRequired()])
    post = TextAreaField('Your Pitch', validators=[InputRequired()])
    submit = SubmitField('Pitch')

class CommentForm(FlaskForm):
    comment = TextAreaField('Leave a comment',validators=[InputRequired()])
    submit = SubmitField('Comment')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [InputRequired()])
    submit = SubmitField('Submit')
    
    # login and registration form