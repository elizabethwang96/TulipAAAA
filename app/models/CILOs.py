from sqlalchemy import Column, String, Integer, orm
from sqlalchemy.orm import relationship, backref, declarative_mixin, declared_attr
from sqlalchemy.sql.schema import ForeignKey
from werkzeug.utils import secure_filename
from app.models.base import Base
from app.models.base import db


class CLIO_preCILO:
    pass


@declarative_mixin
class CILO_preCILO(Base):
    __tablename__ = 'cilo_precilo'
    cilo_precilo_id = Column(Integer, primary_key=True, autoincrement=True)
    cilo_id = Column(Integer, ForeignKey('cilo.cilo_id'), nullable=False)
    preCilo_id = Column(Integer, ForeignKey('cilo.cilo_id'), nullable=False)

    # @declared_attr
    # def father_cilo(cls):
    #     relationship("CILO", backref="father_cilo")
    #
    # @declared_attr
    # def pre_cilo(cls):
    #     relationship("CILO", backref="pre_cilo")

    def __init__(self, cilo_id, preCilo_id):
        super(CILO_preCILO,self).__init__()
        self.cilo_id = cilo_id
        self.preCilo_id = preCilo_id

    def jsonstr(self):

        jsondata = {
            'cilo_precilo_id':self.cilo_precilo_id,
            'cilo_id':self.cilo_id,
            'preCilo_id': self.preCilo_id
        }
        return jsondata

    def __repr__(self):
        return self.cilo_precilo_id


@declarative_mixin
class CILO(Base):
    __tablename__ = 'cilo'
    cilo_id = Column(Integer, primary_key=True, autoincrement=True)
    ciloNumber = Column(Integer, primary_key=False, nullable=False)
    ciloContent = Column(String(100), unique=False,nullable=False)
    course_id = Column(Integer, ForeignKey('course.course_id'))

    @declared_attr
    def course(cls):
        return relationship('Course', backref='cilo')
    # course_curCILO = Base.relationship('Course_curCILO', backref='cilo', lazy=True)
    # course_prevCILO = Base.relationship('Course_prevCILO', backref='cilo', lazy=True)

    @declared_attr
    def pre_cilo(cls):
        return relationship("CILO_preCILO", foreign_keys=[CILO_preCILO.cilo_id], backref=backref("father_cilo", lazy="joined"))

    @declared_attr
    def father_cilo(cls):
        return relationship("CILO_preCILO", foreign_keys=[CILO_preCILO.preCilo_id], backref=backref("pre_cilo", lazy="joined"))


    def __init__(self , ciloNumber, ciloContent, course_id):
        super(CILO,self).__init__()
        self.ciloNumber = ciloNumber
        self.ciloContent = ciloContent
        self.course_id = course_id

    def __str__(self):
        return '<CILO %r>' % self.ciloNumber

    def __repr__(self):
        return '<CILO %r>' % self.ciloNumber

    def createCILOs(CILO1, CILO2, CILO3,course_id):
        if CILO3 != "":
            newCILO1 = CILO(1, CILO1, course_id)
            newCILO2 = CILO(2, CILO2, course_id)
            newCILO3 = CILO(3, CILO3, course_id)
            db.session.add(newCILO1)
            db.session.add(newCILO2)
            db.session.add(newCILO3)
            db.session.commit()
            return 3
        else:
            newCILO1 = CILO(1, CILO1, course_id)
            newCILO2 = CILO(2, CILO2, course_id)
            db.session.add(newCILO1)
            db.session.add(newCILO2)
            db.session.commit()
            return 2

    def getLastCILOId():
        lastCILO= CILO.query.order_by(CILO.cilo_id.desc()).first()
        if lastCILO:
            lastCILOID = lastCILO.cilo_id
            # print("lastciloid"+str(lastCILOID))
            return lastCILOID
        else:
            return 0

    def searchCILObyID(CILOID):
        CILOObject = CILO.query.get(CILOID)
        if CILOObject:
            return CILOObject
        else:
            print('there is no corresponding cilo')
        #return CILOObject

    def searchCILObyContent(searchContent):
        #cls.query.filter(类名.属性名.like(‘%值%’))	like模糊查询
        # print(searchContent+ str(type(searchContent)))
        CILOObjects = CILO.query.filter(CILO.ciloContent.contains(searchContent)).all()
        listOfCILOs = []
        for i in CILOObjects:
            listOfCILOs.append(i)
        return listOfCILOs

    def jsonstr(self):

        jsondata = {
            'cilo_id':self.cilo_id,
            'ciloNumber':self.ciloNumber,
            'ciloContent': self.ciloContent
        }
        return jsondata

    # def getFileData():
    #     return self.fileData
# from sqlalchemy import Column, String, Integer, orm
# from werkzeug.utils import secure_filename
# class File():
#     def __init__(self ,fileData, fileAddress):
#         self.fileData = fileData
#         self.fileAddress = fileAddress

#     # def getFileData():
#     #     return self.S

