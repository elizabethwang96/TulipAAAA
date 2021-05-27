from sqlalchemy import Column, String, Integer, orm
from sqlalchemy.orm import relationship, declarative_mixin, declared_attr
from sqlalchemy.sql.schema import ForeignKey
from werkzeug.utils import secure_filename
from app.models.base import Base

@declarative_mixin
class Assessment(Base):
    __tablename__ = 'assessment'
    assessment_id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String(100), unique=False, nullable=False)
    course_id = Column(Integer, ForeignKey('course.course_id'), nullable=False)

    @declared_attr
    def course(cls):
        return relationship('Course', backref='assessment')

    def __init__(self, type, course_id):
        super(Assessment,self).__init__()
        self.type = type
        self.course_id = course_id

    def jsonstr(self):

        jsondata = {
            'assessment_id':self.assessment_id,
            # 'assessment_method_id':self.assessment_method_id,
            # 'percentage': self.percentage
        }
        return jsondata

    def __repr__(self):
        return '<assessment %r >' % self.assessment_id

    def __str__(self):
        return '<assessment %r >' % self.assessment_id

    def getLastAssesssmentId():
        lastAssessment = Assessment.query.order_by(Assessment.assessment_id.desc()).first()
        lastAssessmentID = lastAssessment.assessment_id
        return lastAssessmentID


@declarative_mixin
class Assessment_CILO(Base):
    __tablename__ = 'assessment_cilo'
    assessment_cilo_id = Column(Integer, primary_key=True, autoincrement=True)
    assessment_id = Column(Integer, ForeignKey('assessment.assessment_id'), nullable=False)
    cilo_id = Column(Integer, ForeignKey('cilo.cilo_id'), nullable=False)
    percentage = Column(Integer, primary_key=False, nullable=False)
    numOfCilos = Column(Integer, primary_key=False, nullable=False)

    @declared_attr
    def assessment(cls):
        return relationship("Assessment", backref="assessment_cilo")

    @declared_attr
    def cilo(cls):
        return relationship("CILO", backref="assessment_cilo")

    def __init__(self, assessment_id, cilo_id, percentage, numOfCilos):
        super(Assessment_CILO, self).__init__()
        self.assessment_id = assessment_id
        self.cilo_id = cilo_id
        self.percentage = percentage
        self.numOfCilos = numOfCilos

#
# # class Course_Assessment(Base):
#     __tablename__ = 'assessment_course'
#     assessment_course_id = Column(Integer, primary_key=True, autoincrement=True)
#     course_id = Column(Integer, ForeignKey('course.course_id'), nullable=False)
#     assessment_id = Column(Integer, ForeignKey('assessment.assessment_id'), nullable=False)
#
#     def __init__(self , course_id, assessment_id):
#         super(Course_Assessment,self).__init__(course_id, assessment_id)

# class Assessment_CILO(Base):
#     __tablename__ = 'assessment_cilo'
#     assessment_cilo_id =Column(Integer, primary_key=True, autoincrement=True)
#     assessment_id = Column(Integer, ForeignKey('assessment.assessment_id'), nullable=False)
#     cilo_id = Column(Integer, ForeignKey('cilo.cilo_id'), nullable=False)
#     percentage = Column(Integer, primary_key=False, nullable=False)

#     def __init__(self, assessment_id, cilo_id, percentage):
#         super(Assessment_CILO, self).__init__(assessment_id, cilo_id, percentage)

# class AssessmentMethodType(Base):
#     __tablename__ = 'assessmentMethodType'
#     type_id = Column(Integer, primary_key=True, autoincrement=True)
#     type_number = Column(Integer, ForeignKey('course.course_id'), nullable=False)
#     type_name = Column(String(100), unique=False, nullable=False)

#     def __init__(self, type_id, type_number, type_name):
#         super(AssessmentMethodType, self).__init__(type_id, type_number, type_name)
