from sqlalchemy import Column, String, Integer, orm
from sqlalchemy.orm import relationship, declarative_mixin, declared_attr
from sqlalchemy.sql.schema import ForeignKey
from werkzeug.utils import secure_filename
from app.models.base import Base

@declarative_mixin
class GradeRepport(Base):
    __tablename__ = 'gradeReport'

    id = Column(Integer, primary_key=True, autoincrement=True)
    grade = Column(Integer, primary_key=False, nullable=False)
    stu_id = Column(Integer, ForeignKey('student.stu_id'), nullable=False)
    assessment_id = Column(Integer, ForeignKey('assessment.assessment_id'), nullable=False)
    course_id = Column(Integer, ForeignKey('course.course_id'), nullable=False)

    @declared_attr
    def student(cls):
        return relationship("Student", backref="gradeReport")

    @declared_attr
    def assessment(cls):
        return relationship("Assessment", backref="gradeReport")

    @declared_attr
    def course(cls):
        return relationship("Course", backref="gradeReport")