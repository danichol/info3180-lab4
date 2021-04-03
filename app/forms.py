from flask_wtf import FlaskForm
from wtforms import StringField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms.validators import DataRequired

class PhotoForm(FlaskForm):
    photo=FileFIeld('Photo',validators=[
        FileRequired(),
        FileAllowed([["jpg","png"],"Images only!!"])
    ])
