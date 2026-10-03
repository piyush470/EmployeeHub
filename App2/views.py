from django.shortcuts import render, get_object_or_404,redirect
from .models import Employee,Department

# Create your views here.

def home(request):
    return render(request,'home.html')

def display(request):
    data=Employee.objects.all()
    return render (request,'empdata.html',{'employeedata':data})

def employeeDetails(request, id):
    emp = get_object_or_404(Employee, id=id)

    return render(request, 'employee_details.html', {
        'emp': emp
    })

def addEmpData(request):
    dep_data = Department.objects.all()
    # c_data = Company.objects.all()
    msg = ""

    if request.method == 'POST':
        name = request.POST.get('nm')
        profile_image = request.FILES.get('profile_image')
        age = request.POST.get('ag')
        email = request.POST.get('email')
        salary = request.POST.get('sal')
        address = request.POST.get('add')
        designation = request.POST.get('designation')
        experience = request.POST.get('experience')
        city = request.POST.get('city')
        status = request.POST.get('status')
        dept_id = request.POST.get('dep')   # Returns selected department ID (e.g., '1')
        # comp_id = request.POST.get('comp')  # Returns selected company ID (e.g., '2')

        dept_obj = Department.objects.get(id=dept_id)
        # comp_obj = Company.objects.get(id=comp_id)

        ee = Employee(
            name=name,
            age=age,
            email=email,
            salary=salary,
            address=address,
            department=dept_obj,
            # Company=comp_obj,
            designation=designation,
            experience=experience,
            city=city,
            status=status,
            profile_image=profile_image,
        )
        ee.save()
        msg = "Data Added Successfully"

    return render(request, 'form.html', context={
        'dep_data': dep_data,
        # 'c_data': c_data,
        'msg': msg
    })


def updateEmpData(request, id):
    emp = get_object_or_404(Employee, id=id)
    dep_data = Department.objects.all()
    # c_data = Company.objects.all()

    if request.method == 'POST':
        emp.name = request.POST.get('nm')
        emp.age = request.POST.get('ag')
        emp.email = request.POST.get('email')
        emp.salary = request.POST.get('sal')
        emp.address = request.POST.get('add')

        emp.designation = request.POST.get('designation')
        emp.experience = request.POST.get('experience')
        emp.city = request.POST.get('city')
        emp.status = request.POST.get('status')

        profile_image = request.FILES.get('profile_image')

        if profile_image:
            emp.profile_image = profile_image

        emp.department_id = request.POST.get('dep')
        # emp.Company_id = request.POST.get('comp')

        emp.save()

    return render(request, 'editform.html', context={
        'emp': emp,
        'dep_data': dep_data,
        # 'c_data': c_data
    })


def deleteEmpData(request,id):
    emp=get_object_or_404(Employee,id=id)
    emp.delete()
    return redirect('empdata')


def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')