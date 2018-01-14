from django_mongokit import connection
from django_mongokit.document import DjangoDocument
from mongokit import *
import datetime
connection = Connection()

@connection.register
class User(Document):
    __database__ = "tutorial"
    __collection__ = "users"
    structure = {
        "_type": unicode,
        "name": unicode,
        "is_registered": bool,
    }
    default_values = {"is_registered": False}

@connection.register
class ProfessionalUser(User):
    structure = {
        "activity": unicode,
    }

    def professional_stuff(self):
        return "stuff"

@connection.register
class UserMemberReg(DjangoDocument):
    __database__ = 'ves_dev'
    __collection__ = 'contestants_reg'
    structure = {
        '_type': unicode,
        'role': unicode,
        'first_name': unicode,
        'last_name':unicode,
        'klass':unicode,
        'roll_number':int,
        'birth_date': datetime.datetime,
        'telephone_number':unicode,
        'mobile_number':unicode,
        'address':unicode,
        'email':unicode,
        'password':unicode,
        'date_creation':datetime.datetime,
    }

    required_fields = ['role','first_name','last_name','klass','roll_number','birth_date','mobile_number','address','email','password','date_creation']
    default_values = {'date_creation':datetime.datetime.utcnow}

@connection.register
class admin_jury_member_reg(user_member_reg):
    __database__ = 'ves_dev'
    __collection__ = 'admins_juries_reg'
    structure = {
        'activity':unicode,
    }

    required_fields = ['activity']
    default_values = {}

@connection.register
class scheduled(DjangoDocument):
    __database__ ='ves_dev'
    __collection__ = 'scheduleds'
    structure = {
        '_type':unicode,
        'p1_start_dt':datetime.datetime,
        'p1_end_dt':datetime.datetime,
        'p2_start_dt':datetime.datetime,
        'p2_end_dt':datetime.datetime,
        'p3_start_dt':datetime.datetime,
        'p3_end_dt':datetime.datetime,
        'date_creation':datetime.datetime
    }

    required_fields = ['p1_start_dt','p1_end_dt','p2_start_dt','p2_end_dt','p3_start_dt','p3_end_dt']   
    default_values = { 'date_creation':datetime.datetime.utcnow}

@connection.register
class category(DjangoDocument):
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
class subcategory(DjangoDocument):
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
class klass(DjangoDocument):
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
class level1(DjangoDocument):
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
class level2(DjangoDocument):
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

@connection.register
class level3(DjangoDocument):
    __database__  = 'ves_dev'
    __collection__ = 'levels3'
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


@connection.register
class level4(DjangoDocument):
    __database__  = 'ves_dev'
    __collection__ = 'levels4'
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


@connection.register
class level5(DjangoDocument):
    __database__  = 'ves_dev'
    __collection__ = 'levels5'
    structure = {
        '_type':unicode,
        'selected_subcat': unicode,
        'year':datetime.datetime,
        'achievement':unicode,
        'description':unicode,
        'date_creation':datetime.datetime,
    }

    required_fields = ['selected_subcat','year','achievement','description']
    default_values = {'date_creation':datetime.datetime.utcnow}



@connection.register
class level6(DjangoDocument):
    __database__ = 'ves_dev'
    __collection__ = 'levels6'
    structure = {
        '_type':unicode,
        'nss':unicode,
        'rotract_club':unicode,
        'llle':unicode,
        'acp':unicode,
        'others':list,
        'date_creation':datetime.datetime,
    }

    required_fields = ['nss','rotract_club','llle','acp','others']
    default_values = {"date_creation":datetime.datetime.utcnow}



