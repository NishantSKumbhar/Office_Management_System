from django.shortcuts import render, HttpResponse
from .models import Employee

def emp_table(request):
	emps = Employee.objects.all()

	context = {
		'title' : 'Employee | Table',
		'emps' : emps
	}
	return render(request, 'Emp_Operations/table_listed.html', context)

def emp_card(request):

	emps = Employee.objects.all()
	context = {
		'title' : 'Employee | Table',
		'emps' : emps
	}
	return render(request, 'Emp_Operations/card_listed.html', context)


def emp_add(request):
	context = {
		'title' : 'Employee | Add',	
	}


	if request.method == 'POST':
		fname = request.POST['xfname']
		lname = request.POST['xlname']
		sal = int(request.POST['xsalary'])
		bns = int(request.POST['xbonus'])
		depart = request.POST['xdepartment']
		loc = request.POST['xlocation']
		rl = request.POST['xrole']
		im = request.POST['ximg']
		cnum = int(request.POST['xcnum'])	
		d = request.POST['xhdate']

		new_emp = Employee(f_name=fname, l_name=lname, salary=sal, bonus=bns, department=depart, location=loc, role=rl, img_url=im, phone_no=cnum, hr_date=d)
		new_emp.save()

		#return HttpResponse('<h1>Employee Added Successfully</h1>')
		return render(request, 'Emp_Operations/add_emp.html', context)	


	elif request.method == 'GET':
		return render(request, 'Emp_Operations/add_emp.html', context)
	else:
		return HttpResponse('<h1>404 Page Not Found</h1>')
	
	

def remove_emp(request, emp_id=0):
	if emp_id:
		try:
			emp = Employee.objects.get(id=emp_id)
			emp.delete()
			return HttpResponse("deleted Successfully")
		except:
			return HttpResponse("Please Enter a Valid Employee Id")
	emps = Employee.objects.all()
	context = {
		'title' : 'Fork InfoSystems | Remove',
		'emps' : emps
	}
	return render(request, 'Emp_Operations/remove_emp.html', context)


def home(request):

	context = {
		'title' : 'Fork InfoSystems | Home',
	}
	return render(request, 'Emp_Operations/home.html', context)

def about(request):

	context = {
		'title' : 'Fork InfoSystems | About',
	}
	return render(request, 'Emp_Operations/about.html', context)

def contact(request):

	context = {
		'title' : 'Fork InfoSystems | Contact',
	}
	return render(request, 'Emp_Operations/contact.html', context)