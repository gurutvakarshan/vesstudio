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
class Scheduled(Document)
    to_who = StringField()
    p1_start_dt = DateTimeField(default=datetime.datetime.now)
    p1_end_dt = DateTimeField(default=datetime.datetime.now)
    p2_start_dt = DateTimeField(default=datetime.datetime.now)
    p2_end_dt = DateTimeField(default=datetime.datetime.now)
    p3_start_dt = DateTimeField(default=datetime.datetime.now) 
    p3_end_dt = DateTimeField(default=datetime.datetime.now)
    date_creation = DateTimeField(default=datetime.datetime.now)

class Category(Document)
    catname = StringField()
    catmark = StringField()

class Subcategory(Document)
    subcatname = StringField()
    subcatmark = FloatField()

class Klass(Document)
    coursetype = StringField()
    coursename = StringField()

class Level1(Document)
    examination_passed = StringField()
    yop = StringField()
    total_mark = IntField()
    percentage = FloatField()
    rank = IntField()
    date_creation = DateTimeField(default=datetime.datetime.now)

class Level2(Document)
    selected_subcat = StringField()
    year = StringField()
    event = StringField() 
    description = StringField()
    date_creation = DateTimeField(default=datetime.datetime.now)
    
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

