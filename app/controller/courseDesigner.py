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
from app.forms import CreateCourse_SubmitForm, Search_course
from app.forms.course import Search_CILO
from app.models.course import Course, Course_preCourse
from app.models.assessment import Assessment, Assessment_CILO
import os
from app.models.programme import Programme
from flask import session

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
    form = CreateCourse_SubmitForm()


    select_precourse_id = request.form.get('select_precourse_id')
    pre_cilos_for_cilo1 = request.form.getlist('pre_cilos')
    add_precilo1_status = request.form.get('add_precilo1_status')


    if form.courseName.data:

        # submit开使

        cilo_start_id = Course.createCourse(form.courseName.data, form.code.data, form.type.data, 1231, form.programmes.data)
        numOfcurCILOcreated = CILO.createCILOs(str(form.CILO1.data), str(form.CILO2.data), str(form.CILO3.data),Course.getLastCourseId())

        if add_precilo1_status == "2":   # add precilos for cilo1

            course_preCourseObeject = Course_preCourse(Course.getLastCourseId(), select_precourse_id)

            db.session.add(course_preCourseObeject)
            for i in pre_cilos_for_cilo1:
                db.session.add(CILO_preCILO(cilo_start_id, i))
            db.session.commit()

        session['courseID'] = Course.getLastCourseId()
        return redirect(str(session.get('courseID'))+"/createAssess")

    return render_template('designer/createCourse.html', title='create course', header='create course', courses=courses, programmes=programmes, cilos_sum=cilos_sum)


@designerBP.route('/<int:courseID>/createAssess', methods=['GET', 'POST'])
def createAssess(courseID):
    sum_percent = 0
    method_List = {}
    cilos = Course.query.filter_by(course_id = courseID).first().cilo
    start_cilo_id = cilos[0].cilo_id

    if request.method == 'POST':
        print(start_cilo_id)
        data = request.get_json()

        if 0 < len(data):
            for i in range(len(data)):
                if not data[i]['method'] or not data[i]['cilo'] or not data[i]['percent'] or data[i]['percent'].isdigit() is False:
                    flash("Please input valid information")
                    return render_template('designer/editAssessment.html', title='edit assessment',
                                           header='edit assessment')
                # elif int(data[i]['cilo']) < 1 or int(data[i]['cilo']) > CILO.query.order_by(CILO.course_id.desc()).first().ciloNumber:
                #     # .filter_by(course_id=str(session.get('courseID')))
                #     flash("Please input valid CILO number")
                elif int(data[i]['percent']) <= 0 or int(data[i]['percent']) > 100:
                    flash("Please input valid Percentage")
                elif data[i]['method'] not in method_List:
                    sum_percent += int(data[i]['percent'])
                    method_List.update()
            if sum_percent != 100:
                print("The sum of the percentage should be 100%")
            else:
                for i in range(len(data)):
                    db.session.add(Assessment(data[i]['method'],courseID))

                    # assessment_id = Assessment.query.filter_by(type=data[i]['method']).first().assessment_id
                    # cilo_id = CILO.query.filter(
                    #     and_(course_id=session.get('courseID'), ciloNumber=data[i]['cilo'])).first().cilo_id
                    # db.session.add(Assessment_CILO(str(assessment_id), str(cilo_id), str(data[i]['percent'])))
                db.session.commit()
                print('askdfjhslkadfjhskadjfhsklaf')
                start_assessement_id = Assessment.getLastAssesssmentId() - len(data) +1
                print(start_assessement_id)
                print('askdfjhslkadfjhskadjfhsklaf')
                for i in range(len(data)):
                    print('ready to submit')
                    cilos = data[i]['cilo']
                    percentage  = int(data[i]['percent'])
                    output = cilos.split(",")
                    list = [0 for x in range(0,len(output))]
                    k = 0
                    for i in output:
                        list[k] = int(i)
                        k += 1
                    print(list)
                    for i in list:
                        print("fuck")
                        print(Assessment.getLastAssesssmentId())
                        db.session.add(Assessment_CILO(start_assessement_id, start_cilo_id+i-1, percentage/len(list), 1))
                    start_assessement_id +=1
                db.session.commit()
                print(data)
                print('fuckkkkkkkkkkkkkkkkkkkkkkkkkkkkk')
                url = '/courseMain/'+str(courseID)

                return redirect('/designer/'+str(courseID)+'/courseMain')


        print('fasdflskajfhlkas')
        # return render_template('designer/courseCreateSuccessfully.html')
        url = str(courseID)+'/courseMain'

        return redirect(url)
        # render_template('designer/createAssessment.html', title='create assessment', header='create assessment', courseID= courseID, cilos = cilos)

    return render_template('designer/createAssessment.html', title='create assessment', header='create assessment', courseID= courseID, cilos = cilos)


# @designerBP.route('/<int:courseID>/courseMain',methods=['GET','POST'])
# def CourseMain(courseID):
#     course = Course.query.filter_by(course_id = courseID)
#     if request.method == 'POST':
#         print('douzheliasldhajsdhak')

#         return render_template('designer/courseMain.html',title='Student Course Main Page',header='Student Course Main Page',course = course)
#     print('asdaksjdhkajhmeishenme')
#     return render_template('designer/courseMain.html',title='Student Course Main Page',header='Student Course Main Page',course = course)

@designerBP.route('/courseMain/course_id=<int:course_id>',methods=['GET','POST'])
def CourseMain(course_id):
    courseInfo = Course.query.filter(Course.course_id == course_id).first()
    CILOs = CILO.query.filter(CILO.course_id == course_id).all()
    print(len(CILOs))
    return render_template('designer/courseMain.html',title='Student Course Main Page',header='Student Course Main Page', courseInfo = courseInfo, CILOs = CILOs)

@designerBP.route('/department',methods=['GET','POST'])
def department():
    if request.method == 'GET':
        courses = Programme.query.filter_by(programme_id=2).first().course

        return render_template('designer/department.html',title='department',header='department', courses= courses)



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
    result_list = False
    if request.method == "POST":
        search_Form = Search_course()
        keyword = search_Form.keyword.data
        searchBy = search_Form.searchBy.data
        courseType = search_Form.courseType.data
        if not keyword:
            flash("Please input keyword")
        else:
            result = []
            if courseType == 'current':
                if searchBy == 'Code': #checked
                    result.append(Course.query.filter_by(courseCode=keyword).first())


                elif searchBy == 'name':
                    result = Course.query.filter_by(courseName=keyword).all()

            elif courseType == 'pre':
                if searchBy =='Code':
                    course = Course.query.filter_by(courseCode=keyword).first()
                    course_precourse = Course_preCourse.query.filter_by(course_id=course.course_id).all()
                    for i in course_precourse:
                        result.append(i.pre_course)

                    # precourses = course.pre_course
                    # print(precourses)3
                    # result = precourses
                    # for i in Course_preCourse.searchPreCoursesByCode(keyword):
                    #     result.append(i)
                elif searchBy == 'name':
                    course = Course.query.filter_by(courseName=keyword).first()
                    course_precourse = Course_preCourse.query.filter_by(course_id=course.course_id).all()
                    for i in course_precourse:
                        result.append(i.pre_course)
            elif courseType == 'after':
                if searchBy =='Code':
                    course = Course.query.filter_by(courseCode=keyword).first()
                    course_precourse = Course_preCourse.query.filter_by(preCourse_id=course.course_id).all()
                    for i in course_precourse:
                        result.append(i.father_course)
                    # for i in Course_preCourse.searchAftCoursesByCode(keyword):
                    #     result.append(i)
                elif searchBy == 'name':
                    course = Course.query.filter_by(courseName=keyword).first()
                    course_precourse = Course_preCourse.query.filter_by(preCourse_id=course.course_id).all()
                    for i in course_precourse:
                        result.append(i.father_course)
                    # for i in Course_preCourse.searchAftCoursesByName(keyword):
                    #     result.append(i)
            print(result)
            if result != []:
                result_list = True
                return render_template('designer/searchCourse.html', title='search course', header='search course', result_list = result_list, result = result)
            else:
                flash("there is no searched result")
    return render_template('designer/searchCourse.html', title='search course', header='search course', result_list = result_list, result = null)



@designerBP.route('/searchCILO',methods=['GET','POST'])
def searchCILO():
    search_Form = Search_CILO()
    keyword = search_Form.keyword.data
    searchBy = search_Form.searchType.data
    result = []

    if  not all([keyword]):
        flash("Please input keyword")
    else:
        if searchBy == 'id':
            result.append(CILO.query.filter(CILO.cilo_id == keyword).first())
            return render_template('designer/searchCILO.html', title='search CILO', header='search CILO', result = result)
        else:
            result = []
            for i in CILO.query.filter(CILO.ciloContent.contains(keyword)).all():
                result.append(i)
            if not result:
                flash("No matched CILO")
            return render_template('designer/searchCILO.html', title='search CILO', header='search CILO', result = result)

    return render_template('designer/searchCILO.html', title='search CILO', header='search CILO')





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