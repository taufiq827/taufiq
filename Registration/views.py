from django.shortcuts import render
from .models import Book, Student, Borrowing,Course,Mentor
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def index(request):
    context = {
        'greeting':1,
    }
    return render (request,"index.html", context)

def view(request):
    context = {
        'firstname': 'Ahmad',
        'greeting': 1
    }
    return render(request, 'view.html', context)

from .models import Course  

from django.shortcuts import render
from .models import Course

def course(request):
    if request.method == 'POST':
        c_code = request.POST['code']
        c_desc = request.POST['desc']
        data = Course(code=c_code, description=c_desc)
        data.save()  
        message = 'Data saved'
    else:
        message = ''
    
    
    courses = Course.objects.all().values()
    
    context = {
        'message': message,
        'courses': courses,  
    }
    
    return render(request, 'course.html', context)


   

def database (request):
    student = Student.objects.all().values()
    book = Book.objects.all().values()
    borrowing = Borrowing.objects.all().values()
    context = {
        'student' : student,
        'book' : book,
        'borrowing' : borrowing,
        
    }
    return render (request,'database.html',context)
    
def mentor(request):
    if request.method == 'POST':
        men_id = request.POST['menid']
        men_name = request.POST['menname']
        men_room_no = request.POST['menroomno']
        data = Mentor(menid=men_id, menname=men_name, menroomno=men_room_no)
        data.save()  
        message = 'Data saved'
    else:
        message = ''
    
    
    Mentors = Mentor.objects.all().values()
    
    context = {
        'message': message,
        'mentor': mentor,  
    }
    
    return render(request, 'mentor.html', context)

def update_course(request,code):
    data=Course.objects.get(code=code)
    dict = {
        'code':code
    }
    return render (request,'update_course.html',dict)

def save_update_course(request, code):
    c_desc = request.POST['desc']
    data = Course.objects.get(code=code)
    data.description = c_desc
    data.save()
    return HttpResponseRedirect(reverse("course"))

def delete_course(request,code):
    data = Course.objects.get(code=code)
    data.delete()
    return HttpResponseRedirect(reverse('course'))
    

def search_course(request):
    if request.method == 'GET':
        c_code = request.GET.get('c_code')

        if c_code:
            data=Course.objects.filter(code=c_code.upper())
        else:
            data =None

        context = {
            'data': data
        }
        
        return render(request, "search_course.html", context)

    return render(request, "search_course.html")
# Create your views here.
 