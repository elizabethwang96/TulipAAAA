from sqlalchemy import Column, String, Integer, orm, and_
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.orm import relationship, backref, declarative_mixin, declared_attr
from app.models.base import Base

@declarative_mixin
class User(Base):
    # __abstract__ = True # 抽象类 不会生成表
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    userName = Column(String(50), unique=True,nullable=False)
    fullName = Column(String(50), unique=False,nullable=False)
    type = Column(Integer)
    programme_id = Column(Integer, ForeignKey('programme.programme_id'))

    @declared_attr
    def programme(cls):
        return relationship('Programme', backref='user')

    password = Column('password', String(100))

    def __str__(self):
        return '<Role %r>' % self.userName

    def __init__(self, userName, fullName, type, programme, programme_id, password):
        super(User,self).__init__()
        self.userName = userName
        self.fullName = fullName
        self.type = type
        self.programme = programme
        self.password = password

    def __repr__(self):
        return self.user_id

    def checkPasssword(account, password):
        print('USER'+account+password)
        result = User.query.filter(and_(User.userName == account, User.password == password)).first()
        # print(result)
        if result:
            return True
        else:
            return False