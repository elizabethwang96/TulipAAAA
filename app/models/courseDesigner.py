from operator import and_
from sqlalchemy import Column, String, Integer, orm, ForeignKey
from sqlalchemy.orm import declarative_mixin, declared_attr, relationship

from app.models.user import User

@declarative_mixin
class CourseDesigner(User):
    __tablename__ = 'courseDesigner'
    courDes_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('user.user_id'), nullable=False)

    @declared_attr
    def user(cls):
        return relationship('User', backref='courseDesigner')

    def __init__(self, userName, fullName, type, programme_id, password):
        super(CourseDesigner,self).__init__(userName, fullName, type, programme_id, password)



    def checkPasssword(account, password):
        print('designer'+account+password)
        result = CourseDesigner.query.filter(and_(CourseDesigner.userName == account, CourseDesigner.password == password)).first()
        # print(result)
        if result:
            return True
        else:
            return False

    def jsonstr(self):

        jsondata = {
            'courDes_id':self.courDes_id,
            'userName':self.userName,
            'fullName': self.fullName,
            'type': self.type,
            'programme': self.programme,
            'password': self.password
        }
        return jsondata


    def __repr__(self):
        return self.courDes_id