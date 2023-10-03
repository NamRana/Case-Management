import re
from django.shortcuts import render

from .models import clerk, client, custom_user, judge, lawyer

# Create your views here.
def home(request):
    return render(request,'sign_up.htm')
def sign_up(request):
    
    f_name=request.POST['first_name']
    l_name=request.POST['last_name']
    mobile=request.POST['mobile']
    email=request.POST['email']
    profile_pic=request.FILES['profile pic']
    password=request.POST['password1']
    password2=request.POST['password2']
    user_type=request.POST['typeofuser']
    user=custom_user(user_role=user_type
    ,first_name=f_name, last_name=l_name, mobile_no=mobile,email=email,profile_pic=profile_pic)
    user.save()
    print(user)
    if user_type=='user':
        adhar_number=request.POST['adhaar']
        adhar_card=request.FILES['adhaar_card']
        #handle_uploaded_file(request.FILES['adhhar_card'])
        client1=client(user=user,aadhar_no=adhar_number,aadhar=adhar_card)
        client1.save()
        
    else:
        id1=request.POST['id']
        id_card=request.FILES['id_card']
        certificate=request.FILES['certificate']
        add_info=request.POST['add_info']
    if user_type=='clerk':

        s=clerk(user=user,clerk_id=id1,id_proof=id_card,certificate=certificate,add_info=add_info)
        s.save()
    elif user_type=='judge':
        s=judge(user=user,clerk_id=id1,id_proof=id_card,certificate=certificate,add_info=add_info)
        s.save()
    elif user_type=='lawyer':
        s=lawyer(user=user,clerk_id=id1,id_proof=id_card,certificate=certificate,add_info=add_info)
        s.save()
    return render(request,'sign_up.html')

# def handle_uploaded_file(f):
#     print(f)
#     with open('some/file/name.txt', 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)

    