import datetime
from sqlalchemy import Table, Column, Integer, String, ForeignKey, Date, Text
from sqlalchemy.orm import relationship
from flask_appbuilder import Model

class Gender(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique = True, nullable=False)

    def __repr__(self):
        return self.name

class Country(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique = True, nullable=False)

    def __repr__(self):
        return self.name

class Department(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class Function(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class Benefit(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name

assoc_benefits_employee = Table('benefits_employee', Model.metadata,
                                  Column('id', Integer, primary_key=True),
                                  Column('benefit_id', Integer, ForeignKey('benefit.id')),
                                  Column('employee_id', Integer, ForeignKey('employee.id'))
)


def today():
    return datetime.datetime.today().strftime('%Y-%m-%d')


class EmployeeHistory(Model):
    id = Column(Integer, primary_key=True)
    department_id = Column(Integer, ForeignKey('department.id'), nullable=False)
    department = relationship("Department")
    employee_id = Column(Integer, ForeignKey('employee.id'), nullable=False)
    employee = relationship("Employee")
    begin_date = Column(Date, default=today)
    end_date = Column(Date)


class Employee(Model):
    id = Column(Integer, primary_key=True)
    full_name = Column(String(150), nullable=False)
    address = Column(Text(250), nullable=False)
    fiscal_number = Column(Integer, nullable=False)
    employee_number = Column(Integer, nullable=False)
    department_id = Column(Integer, ForeignKey('department.id'), nullable=False)
    department = relationship("Department")
    function_id = Column(Integer, ForeignKey('function.id'), nullable=False)
    function = relationship("Function")
    benefits = relationship('Benefit', secondary=assoc_benefits_employee, backref='employee')

    begin_date = Column(Date, default=datetime.date.today(), nullable=True)
    end_date = Column(Date, default=datetime.date.today(), nullable=True)

    def __repr__(self):
        return self.full_name

class MenuItem(Model):
    __tablename__ = 'menu_item'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    link = Column(String(150), nullable=False)
    menu_category_id = Column(Integer, ForeignKey('menu_category.id'), nullable=False)
    menu_category = relationship("MenuCategory")

class MenuCategory(Model):
    __tablename__ = 'menu_category'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)


class News(Model):
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    content = Column(String(500), nullable=False)
    date = Column(Date, default=datetime.date.today(), nullable=True)
    newsCat_id = Column(Integer, ForeignKey('news_category.id'), nullable=False)
    newsCat = relationship("NewsCategory")

class NewsCategory(Model):
    __tablename__ = 'news_category'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)

class Abouts_Us(Model):
    __tablename__ = 'aboutus'
    scope = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    content = Column(String(500), nullable=False)
    date = Column(Date, default=datetime.date.today(), nullable=True)
    aboutusCat_scope = Column(Integer, ForeignKey('about_jobsdb.scope'), nullable=False)
    aboutusCat = relationship("AboutJobsdb")

class AboutJobsdb(Model):
    __tablename__ = 'about_jobsdb'
    scope = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    
class JobSeekersdb(Model):
    __tablename__ = 'job_seekersdb'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    
class Employers(Model):
    __tablename__ = 'employers'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    

class CareerInsights(Model):
    __tablename__ = 'careerinsights'
    job_title = Column(String(50), primary_key=True)
    salary = Column(Integer, nullable=False)
    content = Column(String(500), nullable=False)
    date = Column(Date, default=datetime.date.today(), nullable=True)
    job_titleCat_salary = Column(Integer, ForeignKey('insights_category.salary'), nullable=False)
    job_titleCat = relationship("InsightsCategory")

class InsightsCategory(Model):
    __tablename__ = 'insights_category'
    salary = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)