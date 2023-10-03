from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here

class custom_user(AbstractUser):
    judge = "0"
    clerk = "1"
    lawyer = "2"
    client = "3"
    
    user_role_choice =(
        (judge,"judge"),
        (clerk,"clerk"),
        (lawyer,"lawyer"),
        (client,"client")
    )


    user_role = models.CharField(max_length=1,choices=user_role_choice,null=True,blank=True)
    first_name = models.CharField(max_length=100,null=True,blank=True)
    larst_name = models.CharField(max_length=100,null=True,blank=True)
    mobile_no = models.CharField(max_length=100,null=True,blank=True)
    profile_pic = models.ImageField(upload_to="Profile_pic/",null=True,blank=True)

    # def __str__(self) -> str:
    #     return str(self.first_name + self.last_name)

    
class judge(models.Model):
    user = models.ForeignKey("home.custom_user",on_delete=models.CASCADE,null=True,blank=True)
    reg_no = models.CharField(max_length=250,blank=True,null=True)
    id_proof = models.FileField(upload_to="id_proof/",null=True,blank=True)
    certificate = models.FileField(upload_to="certificate/",blank=True,null=True)
    add_info = models.TextField(blank=True,null=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.reg_no +"---Verification--->"+ str(self.is_verified)

class clerk(models.Model):
    user = models.ForeignKey("home.custom_user",on_delete=models.CASCADE,null=True,blank=True)
    clerk_id = models.CharField(max_length=250,blank=True,null=True)
    id_proof = models.FileField(upload_to="id_proof/",null=True,blank=True)
    certificate = models.FileField(upload_to="certificate/",blank=True,null=True)
    add_info = models.TextField(blank=True,null=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.clerk_id +"---Verification--->"+ str(self.is_verified)

class lawyer(models.Model):
    user = models.ForeignKey("home.custom_user",on_delete=models.CASCADE,null=True,blank=True)
    reg_no = models.CharField(max_length=250,blank=True,null=True)
    id_proof = models.FileField(upload_to="id_proof/",null=True,blank=True)
    certificate = models.FileField(upload_to="certificate/",blank=True,null=True)
    add_info = models.TextField(blank=True,null=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.reg_no +"---Verification--->"+ str(self.is_verified)

class client(models.Model):
    aadhar_no =models.CharField(max_length=20,null=True,blank=True)
    aadhar = models.FileField(upload_to="aadhar/",null=True,blank=True)

class court(models.Model):
    name = models.CharField(max_length=2000,null=True,blank=True)
    location = models.CharField(max_length=1000,null=True,blank=True)
    contact = models.IntegerField(blank=True,null=True)
    bar_association = models.CharField(max_length=300,null=True,blank=True)


class civil(models.Model):

    national_security = '0'
    state_security = '1'
    institute_or_govt_officials = '2'
    women = '3'
    judge_pref = '4'
    default = '5'

    priority_level = (
        (national_security,"nantional_security"),
        (state_security,'state_security'),
        (institute_or_govt_officials,'institute_or_govt_officials'),
        (women,'women'),
        (judge_pref,'judge_pref'),
        (default,'default')

    )
    crn = models.CharField(max_length=500,null=True,blank=True)
    name  = models.CharField(max_length=500,null=True,blank=True)
    type = models.CharField(max_length=500,null=True,blank=True)
    info= models.CharField(max_length=500,null=True,blank=True)
    enroll_date = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    petitioner= models.CharField(max_length=500,null=True,blank=True)
    plawyer= models.CharField(max_length=500,null=True,blank=True)
    respondent= models.CharField(max_length=500,null=True,blank=True)
    rlawyer= models.CharField(max_length=500,null=True,blank=True)
    proof = models.FileField(upload_to='proof/',blank=True,null=True)
    priority = models.CharField(max_length=1,choices=priority_level,default = '5',blank=True,null=True)
    status = models.CharField(max_length=200,blank=True,null=True)
    hearing_date = models.DateField(auto_now_add=True,blank=True,null=True)
    court_id = models.CharField(max_length=16,blank=True,null=True)

class criminal(models.Model):
    national_security = '0'
    state_security = '1'
    institute_or_govt_officials = '2'
    women = '3'
    judge_pref = '4'
    default = '5'

    priority_level = (
        (national_security,"nantional_security"),
        (state_security,'state_security'),
        (institute_or_govt_officials,'institute_or_govt_officials'),
        (women,'women'),
        (judge_pref,'judge_pref'),
        (default,'default')

    )
    crn = models.CharField(max_length=500,null=True,blank=True)
    name  = models.CharField(max_length=500,null=True,blank=True)
    type = models.CharField(max_length=500,null=True,blank=True)
    info= models.CharField(max_length=500,null=True,blank=True)
    enroll_date = models.DateTimeField(auto_now_add=True,null=True,blank=True)
    petitioner= models.CharField(max_length=500,null=True,blank=True)
    plawyer= models.CharField(max_length=500,null=True,blank=True)
    respondent= models.CharField(max_length=500,null=True,blank=True)
    rlawyer= models.CharField(max_length=500,null=True,blank=True)
    proof = models.FileField(upload_to='proof/',blank=True,null=True)
    priority = models.CharField(max_length=1,choices=priority_level,default = '5',blank=True,null=True)
    status = models.CharField(max_length=200,blank=True,null=True)
    hearing_date = models.DateField(auto_now_add=True,blank=True,null=True)
    court_id = models.CharField(max_length=16,blank=True,null=True)
    fir_no = models.CharField(max_length=14,blank=True,null=True)




