from sqlalchemy import Column, String, Integer, orm
from sqlalchemy.orm import relationship, backref, declarative_mixin, declared_attr
from sqlalchemy.sql.schema import ForeignKey
from werkzeug.utils import secure_filename

from app.models.CILOs import CILO
from app.models.base import Base
from app.models.base import db

@declarative_mixin
class Course_preCourse(Base):
    __tablename__='course_precourse'
    course_preCourse_id = Column(Integer, primary_key=True, autoincrement=True)
    course_id = Column(Integer, ForeignKey('course.course_id'), nullable=False)
    preCourse_id = Column(Integer, ForeignKey('course.course_id'), nullable=False)


    # course_id = Column(Integer, ForeignKey('course.course_id'), nullable=False)
    # preCourse_id = Column(Integer, ForeignKey('course.course_id'), nullable=False)
    # father_course = relationship("Course", backref="father_course")
    # pre_course = relationship("Course", backref="pre_course")

    def __init__(self, course_id, preCourse_id):
        super(Course_preCourse,self).__init__()
        self.course_id = course_id
        self.preCourse_id = preCourse_id

    def __str__(self):
        return '<Course_preCourse %r >' % self.course_id

    def __repr__(self):
        return '<Course_preCourse %r %r>' % self.course_id


    def searchPreCoursesByCode(keyword):
        listOfPreCourses = []
        courseObject = Course.searchcurCoursebyCode(keyword)
        if courseObject:
            coursePreCourseObjects = Course_preCourse.query.filter(courseObject.course_id == Course_preCourse.course_id).all()
            for i in coursePreCourseObjects:
                preCourse = Course.query.filter(i.preCourse_id == Course.course_id).first()
                listOfPreCourses.append(preCourse)
            if listOfPreCourses:
                pass
            else:
                print('no pre courses exists')
        return listOfPreCourses

    def searchPreCoursesByName(keyword):
        listOfPreCourses = []
        courseObject = Course.query.filter(Course.courseName == keyword).first()
        if courseObject:
            coursePreCourseObjects = Course_preCourse.query.filter(courseObject.course_id == Course_preCourse.course_id).all()
            for i in coursePreCourseObjects:
                preCourse = Course.query.filter(i.preCourse_id == Course.course_id).first()
                listOfPreCourses.append(preCourse)
            if listOfPreCourses:
                pass
            else:
                print('no pre courses exists')
        return listOfPreCourses

    def searchAftCoursesByCode(keyword):
        listOfAftCourses = []
        courseObject = Course.searchcurCoursebyCode(keyword)
        if courseObject:
            courseAftCourseObjects = Course_preCourse.query.filter(courseObject.course_id == Course_preCourse.preCourse_id).all()
            for i in courseAftCourseObjects:
                aftCourse = Course.query.filter(i.course_id == Course.course_id).first()
                listOfAftCourses.append(aftCourse)
            if listOfAftCourses:
                pass
            else:
                print('no aft courses exists')
        return listOfAftCourses

    def searchAftCoursesByName(keyword):
        listOfAftCourses = []
        courseObject = Course.query.filter(Course.courseName == keyword).first()
        courseAftCourseObjects = Course_preCourse.query.filter(courseObject.course_id == Course_preCourse.preCourse_id).all()
        for i in courseAftCourseObjects:
            aftCourse = Course.query.filter(i.course_id == Course.course_id).first()
            listOfAftCourses.append(aftCourse)
        if listOfAftCourses:
            pass
        else:
            print('no aft courses exists')
        return listOfAftCourses

    def jsonstr(self):
        jsondata = {
            'course_preCourse_id':self.course_preCourse_id,
            'course_id':self.course_id,
            'preCourse_id': self.preCourse_id
        }
        return jsondata


    def __repr__(self):
        return self.course_preCourse_id


@declarative_mixin
class Course(Base):
    __tablename__ = 'course'
    course_id = Column(Integer, primary_key=True, autoincrement=True)
    courseName = Column(String(100), unique=False, nullable=False)
    courseCode = Column(Integer, primary_key=False, unique=True,  nullable=False)
    courseType = Column(String(100), unique=False,nullable=False)
    academicYear = Column(Integer, primary_key=False, nullable=False)
    programme_id = Column(Integer, ForeignKey('programme.programme_id'))

    @declared_attr
    def programme(cls):
        return relationship('Programme', backref='course')

    @declared_attr
    def pre_course(cls):
        return relationship("Course_preCourse", foreign_keys=[Course_preCourse.course_id], backref=backref("father_course", lazy="joined"))

    @declared_attr
    def father_course(cls):
        return relationship("Course_preCourse", foreign_keys=[Course_preCourse.preCourse_id], backref=backref("pre_course", lazy="joined"))



    # course_curCILO = relationship('Course_curCILO', backref='course', lazy=True)
    # course_prevCILO = Base.relationship('Course_prevCILO', backref='course', lazy=True)

    # timestamp = db.Column(db.DateTime, default=datetime.now)
    ######################################################

    def __init__(self , courseName, courseCode, courseType, academicYear, programme_id):
        super(Course,self).__init__()
        self.courseName = courseName 
        self.courseCode = courseCode 
        self.courseType = courseType  
        self.academicYear = academicYear 
        self.programme_id = programme_id

    def __str__(self):
        return '<Course %r>' % self.courseName

    def __repr__(self):
        return '<Course %r>' % self.courseName

    def createCourse(courseName, courseCode, courseType, academicYear, programme_id):
        cilo_id_start = CILO.getLastCILOId()+1
        newCourse = Course(courseName, courseCode, courseType, academicYear, programme_id)
        db.session.add(newCourse)
        db.session.commit()
        return cilo_id_start


    def getLastCourseId():
        print('we are here')
        lastCourse= Course.query.order_by(Course.course_id.desc()).first()
        lastCourseID = lastCourse.course_id
        print("lastcourseid"+str(lastCourseID))
        return lastCourseID
    
    def searchcurCoursebyCode(keyword):
        CourseObject = Course.query.filter(Course.courseCode == keyword).first()
        if CourseObject:
            pass 
        else:
            print('there is no corresponding course')
        return CourseObject
    
    def searchcurCoursebyName(keyword):
        CourseObjects = Course.query.filter(Course.courseName == keyword).all()
        listOfCourses = []
        for i in CourseObjects:
                listOfCourses.append(i)
        if listOfCourses:
            pass    
        else:
            print('there is no corresponding course')
        return listOfCourses 

    def jsonstr(self):

        jsondata = {
            'course_id':self.course_id,
            'courseName':self.courseName,
            'courseCode': self.courseCode,
            'courseType': self.courseType,
            'academicYear': self.academicYear,
            'programme': self.programme
        }
        return jsondata






# class Course_curCILO(Base):
#     course_curCILO_id =  Column(Integer, primary_key=True, autoincrement=True)
#     course_id = Column(Integer, ForeignKey('course.course_id'), nullable=False)
#     curCILO_id = Column(Integer, ForeignKey('cilo.cilo_id'), nullable=False)
#
#     # def __init__(self , course_id, curCILO_ID):
#     #     super(Course,self).__init__(course_id, curCILO_ID)
#
#     def __init__(self , course_id, curCILO_ID):
#         super(Course_curCILO,self).__init__()
#         self.course_id = course_id
#         self.curCILO_id = curCILO_ID
#
#     def createCurCILOforCourse(numOfCILOrecentlyCreated):
#         course_id = Course.getLastCourseId()
#         ciloid = CILO.getLastCILOId()
#         totalNum = numOfCILOrecentlyCreated
#         while totalNum > 0 :
#             new = Course_curCILO(course_id, ciloid - totalNum +1)
#             totalNum -= 1
#             db.session.add(new)
#         db.session.commit()
#         print("create curCILO for course Successfully")
#         return True




