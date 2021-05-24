from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FileField, SubmitField, DateField, SelectField, BooleanField, FileField, \
    DateTimeField, TextAreaField, RadioField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_wtf.file import FileField, FileAllowed, FileRequired

class CreateCourse(FlaskForm):
    account = StringField("account", validators=[DataRequired("Please enter your account.")])

# class CreateCourse_AddCILOs(FlaskForm):
#     addCILOs = SubmitField('addCILOs')
#
# class CreateCourse_DELETECILOs(FlaskForm):
#     delCILOs = SubmitField('delCILOs')


class CreateCourse_SubmitForm(FlaskForm):
    courseName = StringField("courseName", validators=[DataRequired("Please enter course name.")])
    code = StringField("code", validators=[DataRequired("Please enter course code.")])
    academicYear = DateTimeField("academicYear", validators=[DataRequired("Please enter academic year.")])
    # programme = StringField("programme", validators=[DataRequired("Please enter programme.")])
    programmes = SelectField("programmes", validators=[DataRequired("Please select programme.")])
    type = SelectField("type", validators=[DataRequired("Please select course type.")])
    CILO1 = TextAreaField("cilo1")
    CILO2 = TextAreaField("cilo2")
    CILO3 = TextAreaField("cilo3")
    # pre_cilos = MultiCheckboxField('wyhdakeai')

class Search_CILO(FlaskForm):
    keyword =  StringField("keyword", validators=[DataRequired("Please enter search Key Word.")])
    searchType = SelectField("searchType", validators=[DataRequired("Please select course type.")])

class Search_course(FlaskForm):
    keyword = StringField("keyword", validators=[DataRequired("Please enter search Key Word.")])
    searchBy = SelectField("searchBy", validators=[DataRequired("Please select course type.")])
    courseType = SelectField("courseType", validators=[DataRequired("Please select course type.")])

