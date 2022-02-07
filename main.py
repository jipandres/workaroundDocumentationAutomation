from docx import Document
from datetime import datetime

# coding=utf-8
# This is a sample Python script

def generate_document_template(name):
    document = Document()
    document.core_properties.author = 'jipandres'
    document.core_properties.created = datetime.now(tz=None)
    document.core_properties.title = name
    document.core_properties.comments = 'Automatically generated using python-docx'
    document.core_properties.language = 'Uen'
    document.core_properties.version = '0.0.1'
    document.core_properties.revision = 1 #Not updated

    document.add_heading(name, 0)
    document.save(name + '.docx')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Hi, {0}".format(name))
    generate_document_template('JanderKlander')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
