from docx import Document
from datetime import datetime

class WorkaroundDocument:
    def __init__(self, author, productName):
        self.document = Document()
        self.document.core_properties.author = author
        self.document.core_properties.created = datetime.now(tz=None)
        self document.core_properties.title = 'Workaround for Continuous Delivery' #TODO: Add Product version
        self.document.core_properties.comments = 'Automatically generated using python-docx'
        self.document.core_properties.language = 'Uen'
        self.document.core_properties.version = '0.0.1'
        self.document.core_properties.revision = 1  # Not updated

    def addWorkaroundAfterDeployment (text):
        print 'Adding workaround after deployment'

    def addWorkaroundAfterUpgrade ():
        print 'Adding WA'

    #Other addWAs methods

    #other methods:
    # def save(filename)

