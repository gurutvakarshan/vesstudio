from django_mongokit import connection
from django_mongokit.document import DjangoDocument
from mongokit import *
import datetime
from mongoengine import *

class UserMemberReg(Document):
    role = StringField()
    first_name = StringField()
    last_name = StringField()
    klass = StringField()
    roll_number = IntField()
    birth_date = DateTimeField(default=datetime.datetime.now)
    telephone_number = IntField()
    mobile_number = IntField()
    address = StringField()
    email =  EmailField()
    password = StringField()
    date_creation = DateTimeField(default=datetime.datetime.now)
    meta = {'allow_inheritance': True}

class Admin_Jury_Member_Reg(UserMemberReg):
    activity = StringField()

@connection.register
class Scheduled(DjangoDocument):
    __database__ ='ves_dev'
    __collection__ = 'scheduleds'
    structure = {
        '_type':unicode,
        'to_who' : unicode,
        'p1_start_dt':datetime.datetime,
        'p1_end_dt':datetime.datetime,
        'p2_start_dt':datetime.datetime,
        'p2_end_dt':datetime.datetime,
        'p3_start_dt':datetime.datetime,
        'p3_end_dt':datetime.datetime,
        'date_creation':datetime.datetime
    }

    required_fields = ['to_who','p1_start_dt','p1_end_dt','p2_start_dt','p2_end_dt','p3_start_dt','p3_end_dt']   
    default_values = { 'date_creation':datetime.datetime.utcnow}

@connection.register
class Category(DjangoDocument):
    __database__ = 'ves_dev'
    __collection__ = 'categories'
    structure = {
        '_type':unicode,
        'catname':unicode,
        'catmark':int,
    }

    required_fields = ['catname','catmark']
    default_values = {}

@connection.register
class Subcategory(DjangoDocument):
    __database__ = 'ves_dev'
    __collection__ = 'subcategories'
    structure = {
        '_type':unicode,
        'subcatname': unicode,
        'subcatmark': int,
    }

    required_fields = ['subcatname','subcatmark']
    default_values = {}

@connection.register
class Klass(DjangoDocument):
    __database__ = 'ves_dev'
    __collection__ = 'klasses'
    structure = {
        '_type':unicode,
        'coursetype':unicode,
        'coursename':unicode,
    }

    required_fields = ['coursetype','coursename']
    default_values = {}

@connection.register
class Level1(DjangoDocument):
    __database__ = 'ves_dev'
    __collection__ = 'levels1'
    structure = {
        '_type':unicode,
        'examination_passed': unicode,
        'yop': datetime.datetime,
        'total_mark':int,
        'percentage':int,
        'rank':int,
        'date_creation':datetime.datetime,
    }

    required_fields = ['examination_passed','yop','total_mark','percentage','rank']
    default_values = {'date_creation':datetime.datetime.utcnow}

@connection.register
class Level2(DjangoDocument):
    __database__  = 'ves_dev'
    __collection__ = 'levels2'
    structure = {
        '_type':unicode,
        'selected_subcat': unicode,
        'year':datetime.datetime,
        'event':unicode,
        'description':unicode,
        'date_creation':datetime.datetime,
    }

    required_fields = ['selected_subcat','year','event','description']
    default_values = {'date_creation':datetime.datetime.utcnow}

class Level3(Document)
        selected_subcat = StringField()
        year = StringField()
        event = StringField()
        description = StringField()
        date_creation = DateTimeField(default=datetime.datetime.now)

class Level4(Document)
    selected_subcat = StringField()
    year = DateTimeField(default=datetime.datetime.now)
    event = StringField()
    description = StringField()
    date_creation =  DateTimeField(default=datetime.datetime.now)

class Level5(Document):
    selected_subcat = StringField()
    year = DateTimeField(default=datetime.datetime.now)
    achievement = StringField()
    description = StringField()
    date_creation = DateTimeField(default=datetime.datetime.now)
    
class Level6(Document):
    nss =  StringField()
    rotract_club = StringField()
    llle = StringField()
    acp = StringField()
    others = StringField()
    date_creation = DateTimeField(default=datetime.datetime.now)
    
class Notification(Document):
    who = StringField()
    specific = StringField()
    message = StringField()
    date_creation = DateTimeField(default=datetime.datetime.now)
# from django import forms

# class UploadFileForm(forms.Form):
#     title = forms.CharField(max_length=50)
#     file = forms.FileField()

