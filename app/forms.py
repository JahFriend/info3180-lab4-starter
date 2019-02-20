from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from werkzeug.utils import secure_filename

class UploadForm(FlaskForm):
    photo= FileField("Photo", validators=[FileRequired(), FileAllowed(['jpg','jpeg','png'],"Images Only!")])
    