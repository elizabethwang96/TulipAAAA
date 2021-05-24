from operator import and_
from sqlalchemy import Column, String, Integer, orm, ForeignKey
from sqlalchemy.orm import declared_attr, declarative_mixin, relationship

from app.models.user import User

@declarative_mixin
class Student(User):
    __tablename__ = 'student'
    stu_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.user_id'), nullable=False)

    @declared_attr
    def user(cls):
        return relationship('User', backref='student')


    def __init__(self, userName, fullName, type, programme_id, password):
        super(Student,self).__init__(userName, fullName, type, programme_id, password)
    
    def checkPasssword(account, password):
        result = (Student.query.filter(and_(Student.userName == account, Student.password == password))).first()
        # print(result)
        # result2 = (Student.query.filter(and_( Student.userName == account, Student.password == password)))
        # print(result2)
        #print(result.userName+ result.password)
        if result:
            return True
        else:
            return False

    def jsonstr(self):

        jsondata = {
            'stu_id':self.stu_id,
            'userName':self.userName,
            'fullName': self.fullName,
            'type': self.type,
            'programme': self.programme,
            'password': self.password
        }
        return jsondata

    def __repr__(self):
        return self.stu_id