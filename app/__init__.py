from flask import Flask
from app.controller import student,user, lecturer, courseDesigner,course, assessment
import os
# 定义注册蓝图方法
def register_blueprints(app):
  app.register_blueprint(user.userBP,url_prefix='/') # for use to login
  app.register_blueprint(courseDesigner.designerBP, url_prefix='/designer') # for designer
  app.register_blueprint(student.studentBP, url_prefix='/student')  # for designer
  app.register_blueprint(lecturer.nonDesignerBP, url_prefix='/lecturer')  # for non-designer
  app.register_blueprint(course.courseBP, url_prefix='/course')  # for non-designer
  app.register_blueprint(assessment.assessmentBP, url_prefix='/assessment')
  #  # app.register_blueprint(book.bookBP,url_prefix='/book')
  #   app.register_blueprint(student.studentBP,url_prefix='/student')
  # #  app.register_blueprint(teacher.teacherBP,url_prefix='/teacher')
  #   app.register_blueprint(user.userBP,url_prefix='/')
  #   app.register_blueprint(lecturer.lecturerBP,url_prefix='/lecturer')
  #   app.register_blueprint(courseDesigner.courseDesignerBP,url_prefix='/lecturer')
  # #  app.register_blueprint(test.testBP, url_prefix = '/')

# 注册插件(数据库关联)
def register_plugin(app):
    from app.models.base import db
    db.init_app(app)
    # create_all要放到app上下文环境中使用
    with app.app_context():
        db.create_all()


def create_app():
    app = Flask(__name__)
    # app.config.from_object('app.config.setting') # 基本配置(setting.py) 
    app.config.from_object('app.config.secure') # 重要参数配置(secure.py)
    app.config["SECRET_KEY"] = os.urandom(24) # 随机生成密钥
    # 注册蓝图与app对象相关联
    register_blueprints(app)
    # 注册插件(数据库)与app对象相关联
    register_plugin(app)
    # 一定要记得返回app
    return app