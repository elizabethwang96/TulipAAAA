from flask import Blueprint,render_template, request, jsonify
from flask import render_template
from app.models.file import File
from flask_bootstrap import Bootstrap
from app.models.base import db
from sqlalchemy import or_,and_,all_,any_
import os

nonDesignerBP = Blueprint('nonDesigner',__name__)

@nonDesignerBP.route('/home',methods=['GET','POST'])
def nonDesignerMain():
    return render_template('nonDesigner/home.html',title='Non-designer main',header='Non-designer main')

@nonDesignerBP.route('/courseMain',methods=['GET','POST'])
def nonDesignerCourseMainPage():
    return render_template('nonDesigner/courseMain.html',title='Non-designer course main page',header='Non-designer course main page')

@nonDesignerBP.route('/analysis',methods=['GET','POST'])
def analysis():
    return render_template('nonDesigner/analysis.html',title='analysis page',header='analysis page')

@nonDesignerBP.route('/searchCILO',methods=['GET','POST'])
def searchCILO():
    return render_template('nonDesigner/searchCILO.html', title='search CILO', header='search CILO')

@nonDesignerBP.route('/searchCourse',methods=['GET','POST'])
def searchCourse():
    return render_template('nonDesigner/searchCourse.html',title='search course',header='search course')

@nonDesignerBP.route('/visualization',methods=['GET','POST'])
def visualization():
    return render_template('nonDesigner/visualization.html',title='visualization',header='visualization')

@nonDesignerBP.route('/programme',methods=['GET','POST'])
def programme():
    if request.method == 'GET':
        return render_template('nonDesigner/programme.html',title='programme',header='programme')
# from flask import Blueprint,render_template, request
# from app.models.base import db
# from app.models.lecturer import Lecturer

# lecturerBP = Blueprint('lecturer',__name__)

# @lecturerBP.route('', methods=['GET'])
# def get_lecturer():
#     with db.auto_commit():
#         lecturer = Lecturer('tzm',2,'CST','tzmdcm')
#         # 数据库的insert操作
#         db.session.add(lecturer)
#         db.session.commit()
#     return 'hello student'