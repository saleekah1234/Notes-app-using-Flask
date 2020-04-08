from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class NoteForm(FlaskForm):
    text = TextAreaField('Note', validators=[DataRequired()])
    submit = SubmitField('Submit')