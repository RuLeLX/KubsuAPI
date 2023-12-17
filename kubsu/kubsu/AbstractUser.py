'''
AbstractUser this is class what definition all user in system
'''
from Account.models import *
from Account.serializers import *
import re

class Error:
    data = {
        'message': 'User not found!'
    }

class AbstractUser:

    def __init__(self, login, password):
        self.login = login
        self.password = password
  
class JSONstudent(AbstractUser):
  
    def check_login(self): #for student this is id
        check_login = re.match(r's\d{7}', self.login)

        if check_login == None or self.login != check_login.group():
            return False
        return True
    
    def get(self):
        if self.check_login():
            datauser = Students.objects.filter(id_student=self.login, password=self.password).first()
            try:
                if datauser.id_student != '':
                    datauser = StudentSerializer(datauser)
                    return datauser
            except AttributeError:
                return Error
        return False
    
class JSONteacher(AbstractUser):
    
    def check_login(self): #email

        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        
        if re.match(pattern, self.login):
            return True
        return False
    
    def get(self):
        if self.check_login():
            datauser = Teachers.objects.filter(email=self.login, password=self.password).first()
            try:
                if datauser.email != '':
                    datauser = TeacherSerializer(datauser)
                    return datauser
            except AttributeError:
                return Error
        return False

class JSONdecan(AbstractUser):
    
    def check_login(self):
        #For decans special login in database
        if self.login == "superuser":
            return True
        return False
    
    def get(self):
        if self.check_login():
            datauser = Decan.objects.filter(login=self.login, password=self.password).first()
            try:
                if datauser.login != '':
                    datauser = DecanSerializer(datauser)
                    return datauser
            except AttributeError:
                return Error
        return False
####
class UserSystem(AbstractUser):

    classlist = [JSONdecan, JSONstudent, JSONteacher]

    def get(self):
        for User in UserSystem.classlist:
            datauser = User(self.login, self.password).get()
            if datauser != False:
                return datauser
            


    
