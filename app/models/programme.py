from sqlalchemy.orm import relationship, backref

from app.controller.lecturer import programme
from sqlalchemy import Column, String, Integer, orm, ForeignKey
from werkzeug.utils import secure_filename
from app.models.base import Base

class Programme(Base):
    __tablename__ = 'programme'
    programme_id = Column(Integer, primary_key=True, autoincrement=True)
    programmeName = Column(String(100), primary_key=True, unique=True, nullable=False)
    # course_id = Column(Integer, ForeignKey('course.course_id'))
    # user_id = Column(Integer, ForeignKey('user.user_id'))

    def __init__(self, programmeName):
        super(Programme,self).__init__()
        self.programmeName = programmeName

    def jsonstr(self):

        jsondata = {
            'programme_id':self.programme_id,
            'programmeName':self.programmeName
        }
        return jsondata

    def __repr__(self):
        return '<Role %r>' % self

