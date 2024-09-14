from django.core.paginator import Paginator 
from django.shortcuts import render, redirect, get_object_or_404
from .forms import EmployeeForm
from .models import Employee

def employee_list(request):
    sort_by = request.GET.get('sort_by', 'first_name')  
    sort_order = request.GET.get('order', 'asc')

    # sorting 
    if sort_order == 'desc':
        sort_by = f'-{sort_by}'  

    employee_list = Employee.objects.all().order_by(sort_by)

    paginator = Paginator(employee_list, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'employee_list': page_obj,
        'current_sort_by': request.GET.get('sort_by', 'first_name'),
        'current_sort_order': request.GET.get('order', 'asc')
    }
    
    return render(request, "employee_registrar/employee_list.html", context)


def employee_form(request, id=0):
    if request.method == 'GET':
        if id == 0: #insert
            form = EmployeeForm()
        else: #update
            employee= Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "employee_registrar/employee_form.html",{'form':form})
    else:
        if id==0:
            form = EmployeeForm(request.POST, request.FILES)
        else:
            employee= Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, request.FILES, instance=employee)

        if form.is_valid():
            form.save()
        return redirect('/employee/list')

# def employee_delete(request, id):
#     employee= Employee.objects.get(pk=id)
#     employee.delete()
#     return redirect('/employee/list')


def employee_delete(request, id):
    employee = get_object_or_404(Employee, pk=id)
    employee.delete()
    return redirect('/employee/list')
