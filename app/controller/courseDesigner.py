from sqlalchemy.sql.expression import null
from wtforms import RadioField
from wtforms.validators import DataRequired
from flask import Blueprint,render_template, request, jsonify, flash
from flask import render_template, url_for,redirect
from app.models.CILOs import CILO, CILO_preCILO
from app.models.file import File
from app.models.gradeReport import GradeRepport
from flask_bootstrap import Bootstrap
from app.models.base import db
from sqlalchemy import or_,and_,all_,any_
from app.forms import  CreateCourse_SubmitForm, Search_CILO, Search_course
from app.models.course import Course, Course_preCourse
import os
from app.models.programme import Programme

designerBP = Blueprint('designer',__name__)


@designerBP.route('/home',methods=['GET','POST'])
def main():
    return render_template('designer/home.html',title='designer main',header='designer main')


@designerBP.route('/createCourse',methods=['GET','POST'])
def createCourse():
    courses = Course.query.all()
    programmes = Programme.query.all()
    cilos = CILO.query.all()

    cilos_sum = len(cilos)

    #
    # addCILOs = CreateCourse_AddCILOs()
    # delCILOS = CreateCourse_DELETECILOs()
    form = CreateCourse_SubmitForm()
    #
    # test = request.form.getlist('type')


    # select_programme_id = request.form.get('programmes')
    select_precourse_id = request.form.get('courses')
    pre_cilos_for_cilo1 = request.form.getlist('pre_cilos')
    add_precilo1_status = request.form.get('add_precilo1_status')
    for i in pre_cilos_for_cilo1:
        cilo = CILO.query.filter_by(cilo_id=i).first()


    # flash("courseName:"+str(form.courseName.data)+ " code: " + str(form.code.data) + " academic year: " + str(form.academicYear.data) + " Programme: " + str(form.programme.data) + " Type: "+ str(form.type.data))
    # flash("CILO1: " + str(form.CILO1.data) + " CILO2: " + str(form.CILO2.data) + " CILO3: " + str(form.CILO3.data))

    # if CILOsNum < 2 or CILOsNum > 3:
    #     return render_template('404.html')
    #
    # #CILO 操作
    # if addCILOs.addCILOs.data:
    #     if CILOsNum + 1 > 3:
    #         flash("Sorry, the max CILOs number is 3")
    #     else:
    #         CILOsNum = CILOsNum + 1
    #         return redirect(CILOsNum)
    # if delCILOS.delCILOs.data:
    #     if CILOsNum == 2:
    #         flash("Sorry, the min CILOs number is 2")
    #     else:
    #         CILOsNum = CILOsNum - 1
    #         return redirect(CILOsNum)


    if form.courseName.data:
        # print('start submission')
        # print("courseName:"+str(form.courseName.data)+ " code: " + str(form.code.data) + " academic year: null" + " Programme: " + str(form.programme.data) + " Type: "+ str(form.type.data) +"CILO1: " + str(form.CILO1.data) + " CILO2: " + str(form.CILO2.data) + " CILO3: " + str(form.CILO3.data))

        # submit开使
        cilo_start_id = Course.createCourse(form.courseName.data, form.code.data, form.type.data, 1231, form.programmes.data)

        numOfcurCILOcreated = CILO.createCILOs(str(form.CILO1.data), str(form.CILO2.data), str(form.CILO3.data),Course.getLastCourseId())

        print(add_precilo1_status)
        if add_precilo1_status == "2":

            course_preCourseObeject = Course_preCourse(Course.getLastCourseId(), select_precourse_id)

            db.session.add(course_preCourseObeject)
            for i in pre_cilos_for_cilo1:
                pre_cilo_id = CILO.query.filter_by(cilo_id=i).first().cilo_id
                db.session.add(CILO_preCILO(cilo_start_id, pre_cilo_id))
            db.session.commit()

        # Course_curCILO.createCurCILOforCourse(numOfcurCILOcreated)
        return render_template('designer/createCourse.html', title='create course', header='create course', courses=courses, programmes=programmes, cilos_sum=cilos_sum)

    return render_template('designer/createCourse.html', title='create course', header='create course', courses=courses, programmes=programmes, cilos_sum=cilos_sum)


@designerBP.route('/department',methods=['GET','POST'])
def department():
    if request.method == 'GET':
        return render_template('designer/department.html',title='department',header='department')



@designerBP.route('/openCILO', methods=['GET', 'POST'])
def openCILO():
    if request.method == 'POST':
        f = request.files['file']
        if(f.filename==""):
            return jsonify(code = 1001, message = "Empty path")
        dst = os.path.join(os.path.dirname(__file__), f.name)
        if '.csv' == os.path.splitext(f.filename)[1]:
            dst = os.path.join(os.path.dirname(__file__), f.name)
            f.save(dst)
            with open(dst, 'r') as file:
                cont = file.read()
            os.remove(dst)
            file = File(dst,cont)
            return  jsonify( code = 0, message = 'successfully')
        else:
            return jsonify(code = 1002, message = 'File not in .csv format')
        return jsonify(code=0, message="invalid file")

    return render_template('designer/importCILO.html')



@designerBP.route('/openAssess', methods=['GET', 'POST'])
def openAssess():
    if request.method == 'POST':
        f = request.files['file']
        if(f.filename==""):
            return jsonify(code = 1001, message = "Empty path")


        dst = os.path.join(os.path.dirname(__file__), f.name)
        if '.csv' == os.path.splitext(f.filename)[1]:
            dst = os.path.join(os.path.dirname(__file__), f.name)
            f.save(dst)
            with open(dst, 'r') as file:
                cont = file.read()
            os.remove(dst)
            file = File(dst,cont)
            return  jsonify( code = 0, message = 'successfully')
        else:
            return jsonify(code = 1002, message = 'File not in .csv format')
        return jsonify(code=0, message="invalid file")
    return render_template('designer/importAssessment.html')



@designerBP.route('/editCILO',methods=['GET','POST'])
def editCILO():
    if request.method == 'POST':
        return render_template('designer/editCILO.html', title='editCILO', header='editCILO')
    return render_template('designer/editCILO.html', title='editCILO', header='editCILO')



@designerBP.route('/editAssess',methods=['GET','POST'])
def editAssess():
    if request.method == 'POST':
        return render_template('designer/editAssessment.html', title='edit assessment', header='edit assessment')
    return render_template('designer/editAssessment.html', title='edit assessment', header='edit assessment')



@designerBP.route('/searchCourse',methods=['GET','POST'])
def searchCourse():
    search_Form = Search_course()
    keyword = search_Form.keyword.data
    searchBy = search_Form.searchBy.data
    courseType = search_Form.courseType.data
    if  not keyword:
        flash("Please input keyword")
    else:
        flash("Keyword: "+ keyword + " SearchBy: "+ searchBy+" 类型：" +courseType)
        result = []
        if courseType == 'current': 
            if searchBy == 'Code': #checked
                result.append(Course.searchcurCoursebyCode(keyword))  
            elif searchBy == 'name':
                for i in Course.searchcurCoursebyName(keyword):
                    result.append(i)
        elif courseType == 'pre':
            if searchBy =='Code':
                for i in Course_preCourse.searchPreCoursesByCode(keyword):
                    result.append(i)
            elif searchBy == 'name':
                for i in Course_preCourse.searchPreCoursesByName(keyword):
                    result.append(i)
        elif courseType == 'after':
            if searchBy =='Code':
                for i in Course_preCourse.searchAftCoursesByCode(keyword):
                    result.append(i)
            elif searchBy == 'name':
                for i in Course_preCourse.searchAftCoursesByName(keyword):
                    result.append(i)
        print(result)
        if result != [None]:
            for i in result:  
                flash("Search "+courseType +" course by content result: keyword: "+ keyword + " CourseName: "+ str(i.courseName) + "CourseID"+ str(i.course_id) )        
        else:
            flash("there is no searched result")
        
    return render_template('designer/searchCourse.html', title='search course', header='search course')



@designerBP.route('/searchCILO',methods=['GET','POST'])
def searchCILO():
    search_Form = Search_CILO()
    keyword = search_Form.keyword.data
    searchBy = search_Form.searchType.data
    result = []
    if  not all([keyword]):
        flash("Please input keyword")
    else:
        flash("Keyword: "+ keyword + " SearchBy: "+ searchBy)
        if searchBy == 'id':
            result = CILO.searchCILObyID(keyword)
        else:
            result = []
            for i in CILO.searchCILObyContent(str(keyword)):
                result.append(i)
        if result != [None]: 
            for i in result: 
                flash("Search CILO by content result: CILOID: "+ keyword + " CILONumber: "+ str(i.ciloNumber) + "CILOContent"+ i.ciloContent )        
        else:
            flash("there is no searched result")
    return render_template('designer/searchCILO.html', title='search CILO', header='search CILO')



@designerBP.route('/courseMain',methods=['GET','POST'])
def CourseMain():
    return render_template('designer/courseMain.html',title='Student Course Main Page',header='Student Course Main Page')



@designerBP.route('/visualization',methods=['GET','POST'])
def visualization():
    return render_template('designer/visualization.html',title='visualization',header='visualization')



@designerBP.route('/analysis',methods=['GET','POST'])
def analysis():
    return render_template('designer/analysis.html',title='analysis page',header='analysis page')
# from flask import Blueprint,render_template, request
# from app.models.base import db
# from app.models.courseDesigner import CourseDesigner

# courseDesignerBP = Blueprint('courseDesigner',__name__)

# @courseDesignerBP.route('', methods=['GET'])
# def get_lecturer():
#     with db.auto_commit():
#         courseDesigner = CourseDesigner('tzm',2,'CST','tzmdcm')
#         # 数据库的insert操作
#         db.session.add(courseDesigner)
#         db.session.commit()
#     return 'hello student'