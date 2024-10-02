from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .forms import CustomUserCreationForm
from .models import UploadCSV
from django.utils import timezone
import csv

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            print(form.errors)
    else:
        form = CustomUserCreationForm()
    return render(request, 'authentications/registration.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'authentications/login.html', {'form': form})

@login_required
def dashboard_view(request):
    user_type = request.user.user_type
    context = {
        'user_type': user_type
    }
    return render(request, 'dashboard/index.html', context)

@login_required
def dashboardgraph(request):
    user_type = request.user.user_type
    context = {
        'user_type': user_type
    }
    return render(request, 'dashboard/dashboard.html', context)

def about_us(request):
    user_type = request.user.user_type
    context = {
        'user_type': user_type
    }
    return render(request, 'dashboard/about_us.html', context)

def logout_view(request):
    return render(request, 'authentications/login.html')

@login_required
def upload_csv(request):
    if request.method == 'POST' and request.FILES['csv_file']:
        csv_file = request.FILES['csv_file']
        reader = csv.reader(csv_file.read().decode('utf-8').splitlines())
        next(reader)  # Skip the header row if needed

        try:
            for row in reader:
                UploadCSV.objects.create(
                    survey_name=row[0],  # Adjust according to your CSV and model
                    date_start=row[1],
                    date_close=row[2],
                    crs_num=row[3],
                    crs_name=row[4],
                    crs_year=row[5],
                    dept_name=row[6],
                    crs_dir=row[7],
                    resp_fac=row[8],
                    eval_id=row[9],
                    eval_uname=row[10],
                    eval_email=row[11],
                    t_submit=row[12],
                    mobile=bool(int(row[13])),  # Convert 1/0 to boolean
                    grad_year=row[14],
                    gender=row[15],
                    program=row[16],
                    research_1=row[17],
                    research_2=row[18],
                    research_3=row[19],
                    question_1=row[20],
                    question_2=row[21],
                    question_3=row[22],
                    question_4=row[23],
                    question_5=row[24],
                    question_6=row[25],
                    question_7=row[26],
                    question_8=row[27],
                    question_9=row[28],
                    question_10=row[29],
                    question_11=row[30],
                    question_12=row[31],
                    question_13=row[32],
                    question_14=row[33],
                    question_15=row[34],
                    question_16=row[35],
                    question_17=row[36],
                    question_18=row[37],
                    question_19=row[38],
                    question_20=row[39],
                    question_21=row[40],
                    question_22=row[41],
                    question_23=row[42],
                    question_24=row[43],
                    question_25=row[44],
                    question_26=row[45],
                    question_27=row[46],
                    question_28=row[47],
                    question_29=row[48],
                    question_30=row[49],
                    question_31=row[50],
                    question_32=row[51],
                    # Add other fields as necessary
                )
            messages.success(request, 'CSV data has been successfully uploaded.')
        except Exception as e:
            messages.error(request, f'Error processing file: {e}')
            return redirect('upload_csv')

        return redirect('dashboard')  # Redirect after processing all rows

    else:
        table_data = UploadCSV.objects.all()  # Fetch all uploaded data
        return render(request, 'view_data.html', {'table_data': table_data})
