from flask.helpers import url_for
import flask_sqlalchemy
from sqlalchemy.sql.elements import False_
from sqlalchemy.sql.expression import true, distinct
from app.controller import courseDesigner, lecturer
from flask import Blueprint,render_template, request, jsonify, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from app.models.base import db
from app.models.course import Course
from app.models.programme import Programme
from app.models.assessment import Assessment, Assessment_CILO
from app.models.student import Student
from app.models.lecturer import Lecturer
from app.models.courseDesigner import CourseDesigner
from app.models.gradeReport import GradeRepport
from app.models.CILOs import CILO, CILO_preCILO
from app.models.course import Course,Course_preCourse
from app.forms import LoginForm
from sqlalchemy import or_, and_, all_, any_, func
from flask import session

from app.models.user import User

userBP = Blueprint('/',__name__)

@userBP.route('/',methods=['GET','POST'])
def login():
     diction_course = {}
     courses = Programme.query.filter_by(programme_id=2).first().course
     print(courses)
     for i in courses:
          diction_course[i.course_id] = i.courseName


          if i.pre_course != []:
               print('course '+ i.courseName +' precourse is ')
               for item in i.pre_course:
                    diction_course[i.course_id] = i.courseName
                    print(Course.query.filter_by(course_id =item.course_id).first().courseName)
          else:
               print('course '+ i.courseName +' has no precourse')
     print(diction_course)
     # assessment1 = Assessment('quiz', 1)
     # assessment2 = Assessment('project', 1)
     # db.session.add(assessment1)
     # db.session.add(assessment2)
     # db.session.commit()
     # assessment_cilo1 = Assessment_CILO(1, 1, 30, 2)
     # assessment_cilo2 = Assessment_CILO(1, 2, 30, 2)
     # assessment_cilo3 = Assessment_CILO(2, 1, 40, 1)
     # db.session.add(assessment_cilo1)
     # db.session.add(assessment_cilo2)
     # db.session.add(assessment_cilo3)
     # db.session.commit()
     #
     #
     #
     # cilos = Course.query.first().cilo
     # assessment_cilo1 = []
     # assessment_cilo2 = []
     # assessment_cilo3 = []
     # for i in cilos:
     #      if i.ciloNumber == 1:
     #           assessment_cilo1 = Assessment_CILO.query.filter_by(cilo_id = i.cilo_id).all()
     #      if i.ciloNumber == 2:
     #           assessment_cilo2 = Assessment_CILO.query.filter_by(cilo_id = i.cilo_id).all()
     #      if i.ciloNumber == 3:
     #           assessment_cilo3 = Assessment_CILO.query.filter_by(cilo_id = i.cilo_id).all()
     # cilo1percentage = 0
     # cilo2percentage = 0
     # cilo3percentage = 0
     # for i in assessment_cilo1:
     #      cilo1percentage += i.percentage
     # for i in assessment_cilo2:
     #      cilo2percentage += i.percentage
     # for i in assessment_cilo3:
     #      cilo3percentage += i.percentage
     # print('cilo1: '+str(cilo1percentage))
     # print('cilo2: '+str(cilo2percentage))
     # print('cilo3: '+str(cilo3percentage))
     #
     # cilo1grade= 0
     # cilo2grade= 0
     # cilo3grade= 0
     # student = Student.query.first()   #return obeject
     # for i in assessment_cilo1:
     #      print('asdkjhaskdjhadk')
     #      print( GradeRepport.query.filter(and_(GradeRepport.stu_id == student.stu_id, GradeRepport.assessment_id == i.assessment_id)).first())
     #      print('asdkjhaskdjhadk')
     #      cilo1grade += (GradeRepport.query.filter_by(and_(stu_id=student.stu_id, assessment_id = i.asessment_id)).first().grade * 1/(ssessment_CILO.query.filter_by(and_(assessment_id = i.asessment_id)).first().numOfCilo))
     #      print(cilo1grade)
     # for i in assessment_cilo_list:
     #      print(i.cilo)
     #      cilonum = i.cilo.ciloNumber
     #      percentage = i.percentage
     #      if cilonum==1:
     #           cilo1 +=percentage
     #      if cilonum==2:
     #           cilo2 +=percentage
     #      if cilonum==3:
     #           cilo3+=percentage
     # print('cilo1 '+str(cilo1) + ' cilo2 '+str(cilo2) + ' cilo3 ' +str(cilo3))





     # print(User.query.filter_by(user_id=1).first())
     # # not used     print(Course.query.first().programme)
     # print(Course.query.first().programme.programmeName)
     # course = Course.query.first()
     # print(course)
     #
     # print("FUCKKKKKKKKKKKKKKKKKKKKKKKKKKKK")
     #

     # print(Course.query.first())
     # print(course.pre_course)
     # for item in course.pre_course:
     #      print(item.preCourse_id)

     # precourses = Course_preCourse.query.filter_by(course_id=course.course_id).first().pre_course
     # print(precourses)

     # print("FUCKKKKKKKKKKKKKKKKKKKKKKKKKKKK")
     #
     # print(CILO.query.filter_by(course_id=course.course_id).all())
     #

     # # test ATTRIBUT
     # test_student_account = 's123'
     # test_student_password = '123'
     # test_L_account = 'l123'
     # test_L_password = '123'
     # test_C_account = 'c123'
     # test_C_password = '123'
     if request.method == 'POST':
          form = LoginForm()
          account = form.account.data
          password = form.password.data
          temp = "account" + str(account) + "password" + str(password)
          # #账号密码不完整
          if not all([account, password]): 
               flash('Check the account and password')
          else:
               logState = False
               print('this is designer')
               if account[0] == 's':
                    session['userType'] = 'student'
                    print('this is student')
                    logState = User.checkPasssword(account, password)
               elif account[0] == 'l':
                    session['userType'] = 'lecturer'
                    print('this is lecturer')
                    logState = User.checkPasssword(account, password)
               elif account[0] == 'c':
                    session['userType'] = 'designer'
                    print('this is designer')
                    logState = User.checkPasssword(account, password)
               else:
                    flash("Please check your account")
               # 使用SQL查询account和password
               # 如果找不到返回Flase
               #input: account, password
               #output: logState bool
               print(logState)
               if logState == True:
                    url = str(session.get('userType'))+"/home"
                    return redirect(url)
               else:
                    flash("Please check your password")
               return render_template('login.html',title='Login',header='Sample Case', message = "")
     else:
         return render_template('login.html',title='Login',header='Sample Case', message = "")


