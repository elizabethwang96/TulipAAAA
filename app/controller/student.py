from flask import Blueprint,render_template, request
from app.models.base import db
from app.models.student import Student

studentBP = Blueprint('student',__name__)

#@studentBP.route('', methods=['GET'])
# def get_student():
#     with db.auto_commit():
#         student = Student('hejing',20,'UIC','hejing@mail.uic.edu.hk','123456')
#         # 数据库的insert操作
#         db.session.add(student)
#     return 'hello student'
@studentBP.route('/home',methods=['GET','POST'])
def studedntMain():
    return render_template('student/home.html', title='student main', header='student main')

@studentBP.route('/performance',methods=['GET','POST'])
def studentPerformance():
    return render_template('student/performance.html',title='performance',header='performance')

@studentBP.route('/overallCourse',methods=['GET','POST'])
def stuOverallCourse():
    return render_template('student/overallCourse.html',title='stuOverallCourse',header='stuOverallCourse')

@studentBP.route('/visualization',methods=['GET','POST'])
def visualization():
    return render_template('student/visualization.html',title='visualization',header='visualization')

@studentBP.route('/searchCourse',methods=['GET','POST'])
def searchCourse():
    return render_template('student/searchCourse.html',title='search course',header='search course')

@studentBP.route('/courseMain',methods=['GET','POST'])
def studentCourseMain():
    return render_template('student/courseMain.html',title='Student Course Main Page',header='Student Course Main Page')

@studentBP.route('/searchCILO',methods=['GET','POST'])
def searchCILO():
    return render_template('student/SearchCILO.html',title='search CILO',header='search CILO')
# from flask import Blueprint,render_template, request
# from app.models.base import db
# from app.models.student import Student

# studentBP = Blueprint('student',__name__)

# @studentBP.route('', methods=['GET'])
# def get_student():
#     with db.auto_commit():
#         student = Student('wyh', 1 ,'CST','wyhdcm')
#         # 数据库的insert操作
#         db.session.add(student)
#     return 'hello student'


