from sqlalchemy import Column, String, Integer, orm
from werkzeug.utils import secure_filename
from app.models.base import Base
class File(Base):
    file_id = Column(Integer, primary_key=True, autoincrement=True)
    fileData = Column(String(100), unique=False,nullable=False)
    fileAddress = Column(String(100), unique=False,nullable=False)
   
    # def __init__(self ,fileData, fileAddress):
    #     super(File,self).__init__(fileData, fileAddress)
    # # def getFileData():
    #     return self.fileData

# from sqlalchemy import Column, String, Integer, orm
# from werkzeug.utils import secure_filename
# class File():
#     def __init__(self ,fileData, fileAddress):
#         self.fileData = fileData
#         self.fileAddress = fileAddress

#     # def getFileData():
#     #     return self.fileData

    def __repr__(self):
        return self.file_id