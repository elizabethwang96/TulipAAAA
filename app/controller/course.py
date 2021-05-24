from flask import Blueprint,render_template, request, jsonify
from flask import render_template
from app.models.course import Course, Course_preCourse
from app.models.programme import Programme
from app.models.assessment import Assessment_CILO, Assessment
from flask_bootstrap import Bootstrap
from app.models.base import db
from sqlalchemy import or_,and_,all_,any_
import os
courseBP = Blueprint('course',__name__)

