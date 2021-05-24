from operator import and_

from sqlalchemy.orm import declared_attr, relationship, declarative_mixin

from app.controller import lecturer
from sqlalchemy import Column, String, Integer, orm, ForeignKey

from app.models.student import Student
from app.models.user import User

@declarative_mixin
class Lecturer(User):
    __tablename__ = 'lecturer'
    lec_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.user_id'), nullable=False)

    @declared_attr
    def user(cls):
        return relationship('User', backref='lecturer')

    def __init__(self, userName, fullName, type,  programme_id, password):
        super(Lecturer,self).__init__(userName, fullName, type, programme_id, password)
    
    def checkPasssword(account, password):
        result = Lecturer.query.filter(and_(Lecturer.userName == account, Lecturer.password == password)).first()
        if result:
            return True
        else:
            return False

    def jsonstr(self):

        jsondata = {
            'lec_id':self.lec_id,
            'userName':self.userName,
            'fullName': self.fullName,
            'type': self.type,
            'password': self.password
        }
        return jsondata

    def __repr__(self):
        return self.lec_id
