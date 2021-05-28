from flask import Blueprint,render_template, request
from app.models.base import db
from sqlalchemy import or_, and_, all_, any_
from app.models.student import Student
from app.models.course import Course
from app.models.assessment import Assessment, Assessment_CILO
from app.models.gradeReport import GradeRepport
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
    print("111")
    # assessment1 = Assessment('quiz', 1)
    # assessment2 = Assessment('project', 1)
    # db.session.add(assessment1)
    # db.session.add(assessment2)
    # db.session.commit()
    # assessment_cilo1 = Assessment_CILO(1, 1, 30)
    # assessment_cilo2 = Assessment_CILO(1, 2, 30)
    # assessment_cilo3 = Assessment_CILO(2, 1, 40)
    # db.session.add(assessment_cilo1)
    # db.session.add(assessment_cilo2)
    # db.session.add(assessment_cilo3)
    # db.session.commit()

    cilos = Course.query.first().cilo
    assessment_cilo1 = []
    assessment_cilo2 = []
    assessment_cilo3 = []
    for i in cilos:
        if i.ciloNumber == 1:
            assessment_cilo1 = Assessment_CILO.query.filter_by(cilo_id=i.cilo_id).all()
        if i.ciloNumber == 2:
            assessment_cilo2 = Assessment_CILO.query.filter_by(cilo_id=i.cilo_id).all()
        if i.ciloNumber == 3:
            assessment_cilo3 = Assessment_CILO.query.filter_by(cilo_id=i.cilo_id).all()
    cilo1percentage = 0
    cilo2percentage = 0
    cilo3percentage = 0
    for i in assessment_cilo1:
        cilo1percentage += i.percentage
    for i in assessment_cilo2:
        cilo2percentage += i.percentage
    for i in assessment_cilo3:
        cilo3percentage += i.percentage
    print('cilo1: ' + str(cilo1percentage))
    print('cilo2: ' + str(cilo2percentage))
    print('cilo3: ' + str(cilo3percentage))

    cilo1grade = 0
    cilo2grade = 0
    cilo3grade = 0
    student = Student.query.first()  # return obeject
    for i in assessment_cilo1:
        print(GradeRepport.query.filter(
            and_(GradeRepport.stu_id == student.stu_id, GradeRepport.assessment_id == i.assessment_id)).first())
        cilo1grade += GradeRepport.query.filter(
            and_(GradeRepport.stu_id == student.stu_id,
                 GradeRepport.assessment_id == i.assessment_id)).first().grade * (1 / Assessment_CILO.query.filter(
            Assessment_CILO.assessment_id == i.assessment_id).count())
    for i in assessment_cilo2:
        print(GradeRepport.query.filter(
            and_(GradeRepport.stu_id == student.stu_id, GradeRepport.assessment_id == i.assessment_id)).first())
        cilo2grade += GradeRepport.query.filter(
            and_(GradeRepport.stu_id == student.stu_id,
                 GradeRepport.assessment_id == i.assessment_id)).first().grade * (1 / Assessment_CILO.query.filter(
            Assessment_CILO.assessment_id == i.assessment_id).count())
    for i in assessment_cilo3:
        print(GradeRepport.query.filter(
            and_(GradeRepport.stu_id == student.stu_id, GradeRepport.assessment_id == i.assessment_id)).first())

        cilo3grade += GradeRepport.query.filter(
            and_(GradeRepport.stu_id == student.stu_id,
                 GradeRepport.assessment_id == i.assessment_id)).first().grade * (1 / Assessment_CILO.query.filter(
            Assessment_CILO.assessment_id == i.assessment_id).count())
    cilo1 = round((cilo1grade / cilo1percentage * 100), 2)
    cilo2 = round((cilo2grade / cilo2percentage * 100), 2)
    cilo_list = ["CILO1", "CILO2", "CILO3"]
    if (cilo3percentage == 0):
        cilo3 = 0
        cilo_list = ["CILO1", "CILO2"]
        result_list = [cilo1, cilo2]
    else:
        cilo3 = round((cilo3grade / cilo3percentage * 100), 2)
        result_list = [cilo1, cilo2, cilo3]
    return render_template('student/performance.html', title='performance', header='performance',
                           result_list=result_list, cilo_list=cilo_list)

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


