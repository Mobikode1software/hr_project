from django.shortcuts import get_object_or_404, render , redirect
from django.http import HttpResponse,Http404, HttpResponseRedirect
from django.contrib.auth import authenticate , login as loginUser , logout
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from mobikode_app.form import EmployForm
from mobikode_app.models import Employ, Record #RejectedEmploy
from django.contrib.auth.decorators import login_required
from django.template import loader

from django.shortcuts import (get_object_or_404,render,HttpResponseRedirect)
from django.contrib.auth.models import User



from .constants import ALERT_RECORD_UPDATE, HOME_PAGE_PRIORITY, HR_DETAILS, MYTEAM_PAGE_PRIORITY, SUPER_USER_AA, SUPERUSER_DETAILS, SUPER_USER_AP
import re
from django.contrib import messages
from openpyxl import Workbook
from django.http import HttpResponse
@login_required(login_url='login')



def home(request):
    if request.user.is_authenticated:
        user = request.user
        form = EmployForm()
        loggedInUser= str(request.user)
        initials = get_initials(loggedInUser)
        employs = Employ.objects.filter(user = user)
        return render(request , 'index.html' , context={'form' : form, 'employs': employs, 'initials': initials})

def get_initials(username):
    initials = re.findall('[A-Z]', username)
    return ''.join(initials)

def login(request):
    if request.method == 'GET':
        form1 = AuthenticationForm()
        context = {
            "form" : form1
        }
        return render(request , 'login.html' , context=context )
    else:
        form = AuthenticationForm(data=request.POST)
        print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username = username , password = password)

            if user is not None:  
                loginUser(request , user)
                return redirect('home')
        else:
            context = {
                "form" : form
            }
            return render(request , 'login.html' , context=context )

login_required(login_url='login')

def addnew(request):
        if request.user.is_authenticated:
            user= request.user
            print(user)
        form = EmployForm(request.POST, request.FILES)
        loggedInUser= str(request.user)
        disable_status(form, loggedInUser)
        if form.is_valid():
            print(form.cleaned_data)
            employ = form.save(commit=False)
            employ.user= user
            employ.save()
            print(employ)
            return redirect("home")
        else: 
            return render(request , 'ad.html' , context={'form' : form})

     
def update_data(request,id ):  
    loggedInUserPriority = ''
    if request.method == 'POST':
        pi = Employ.objects.get(pk=id)  
        fm =  EmployForm(request.POST, request.FILES, instance = pi)

        loggedInUser= str(request.user)
        for x in HR_DETAILS:
            if(x['value']== loggedInUser):
                loggedInUserPriority= x['priority']
        current_path= request.path
        result = f"/{id}/edit"
        
        if fm.is_valid():  
            fm.save()
            if current_path == result and loggedInUserPriority== 1:
                status = request.Status
                print(f"1###{status}#########################")
                #employ_data = Employ.objects.filter(Status=status)
                return redirect("myTeam_view"); 
            elif current_path == result and loggedInUserPriority== 0:
                status = request.Status
                print(f"2###{status}#########################")
                return redirect("home") 
            else:
                status = request.Status
                print(f"###{status}#########################")
                return redirect("home")           
    else:
        pi = Employ.objects.get(pk=id) 
        fm =  EmployForm(instance = pi) 
        loggedInUser= str(request.user)
        disable_status(fm, loggedInUser)
    return render(request, "updateemp.html" , {'form':fm})
    

def delete(request , id ):
    print(id)
    Employ.objects.get(pk = id).delete()
    return redirect('home') 

# Updated function by Shital N. to delete record as below
def delete_view(request, id):    
    print(id)
    Employ.objects.get(pk = id).delete()
    messages.error(request, "Record deleted successfully!!")
    return redirect('myTeam_view') 


def signout(request):
    logout(request)
    return redirect('login')


def myTeam_view(request):
        logginguser= str(request.user)
        hrList=[]
        superUserList=[]   
    
        for x in SUPERUSER_DETAILS:
            superUserList.append(x)   
        if logginguser == SUPER_USER_AA or logginguser == SUPER_USER_AP:
                for x in HR_DETAILS:
                    #print(x['reportTo'])
                    if(x['reportTo'] == 'AA'):
                        hrList.append(x)
                        #  print(hrList)
                context= get_record(request, hrList, superUserList)
                return render(request , 'myTeam.html', context);        
        else:  
            for x in HR_DETAILS:
                    #  print(x['reportTo'])
                    if(x['reportTo'] == 'PB'):
                        hrList.append(x)
            context= get_record(request, hrList, superUserList)   
            return render(request , 'myTeam.html', context);   
            
            
def get_record(request, hr_data, superUserList):
    user_records=[]
    superUserData=[]
  
    if request.method == 'POST':
        selected_option = str(request.POST.get('my_select'))
        selected_option_superuser = str(request.POST.get('my_select_superuser'))
        # print(f"Selected option: {selected_option}")
        if request.POST.get('my_select') is not None:
            specific_user = get_object_or_404(User, username=selected_option)
            user_records = get_records_added_by_user(specific_user)
        else:
            selected_option_superuser = str(request.POST.get('my_select_superuser'))
            specific_superuser = get_object_or_404(User, username=selected_option_superuser)
            superUserData= get_records_added_by_user(specific_superuser)   
        context={
            'hrUserList': hr_data,  
            'superUserList': superUserList,
            'employs': user_records,
            'superUserData': superUserData,
            'selectedOption': selected_option,
            'selectedOptionSuperuser': selected_option_superuser,
        }
        return context 
    else:
        context={
            'hrUserList': hr_data,  
            'superUserList': superUserList,
            'selectedOption': None,
            'selectedOptionSuperuser': None,
        }
        return context
       
def get_records_added_by_user(user):
    records = Employ.objects.filter(user=user)
    return records

def disable_status(form, loggedInUser):
    for x in HR_DETAILS:
        #  print(x['reportTo'])
        if(x['value'] == loggedInUser and x['priority'] == 0 ):
            form.fields['status'].widget.attrs['disabled'] = True # text input


# update_data function by Shital N. refer for below code
def myTeamView(request):
    if request.method == 'POST':
        id = request.GET.get('id')
        param_page_type = request.GET.get('pageType')
        pi = Employ.objects.get(pk=id) 
        fm =  EmployForm(request.POST, request.FILES, instance = pi)
        loggedInUser= str(request.user)
        for x in HR_DETAILS:
            if(x['value']== loggedInUser):
                loggedInUserPriority= x['priority']

        if fm.is_valid():
            fm.save()
            if param_page_type== MYTEAM_PAGE_PRIORITY and loggedInUserPriority== 1:
                #print(request.FILES)
                messages.success(request, "Record updated successfully!!")
                return redirect("myTeam_view"); 
            elif param_page_type== HOME_PAGE_PRIORITY and loggedInUserPriority== 1:
                return redirect("home") 
            elif param_page_type== HOME_PAGE_PRIORITY and loggedInUserPriority== 0:
                return redirect("home")
            else:
                return redirect("home")
    else:
        id = request.GET.get('id')
        param_page_type = request.GET.get('pageType')
        pi = Employ.objects.get(pk=id)  
        fm = EmployForm(instance = pi) 
        loggedInUser= str(request.user)
        disable_status(fm, loggedInUser)
        return render(request, "updateemp.html" , {'form':fm})





def download_data_as_excel(request):
    if request.user.is_authenticated:
        user = request.user
        employ_data = Employ.objects.filter(user=user)

    # Create an Excel workbook and add a worksheet
    workbook = Workbook()
    worksheet = workbook.active

    # Write the headers
    headers = ['Name', 'Skill', 'Experience', 'Relevant Experience', 'Company', 'Availability', 'Offer', 'CTC', 'ECTC', 'Location', 'Contact', 'Mail ID', 'Reason for Job Change', 'Passport', 'Status', 'User']
    worksheet.append(headers)

    # Write the data
    for employ in employ_data:
        row = [
            employ.Name,
            employ.Skill,
            employ.Experience,
            employ.Relevant_Experience,
            employ.Company,
            employ.Availability,
            employ.Offer,
            employ.CTC,
            employ.ECTC,
            employ.Location,
            employ.Contact,
            employ.Mail_id,
            employ.Reason_for_job_change,
            employ.PassPort,
            employ.status,
            employ.user.username,
        ]
        worksheet.append(row)

    # Set the response headers
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=employ_data.xlsx'

    # Save the workbook to the response
    workbook.save(response)

    return response



