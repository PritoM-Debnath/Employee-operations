from django.db.models import Q
from django.core.paginator import Paginator 
from django.shortcuts import render, redirect, get_object_or_404
from .forms import EmployeeForm
from .models import Employee

# def employee_list(request):
#     sort_by = request.GET.get('sort_by', 'first_name')  
#     sort_order = request.GET.get('order', 'asc')

#     # sorting 
#     if sort_order == 'desc':
#         sort_by = f'-{sort_by}'  

#     employee_list = Employee.objects.all().order_by(sort_by)

#     paginator = Paginator(employee_list, 4)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)

#     context = {
#         'employee_list': page_obj,
#         'current_sort_by': request.GET.get('sort_by', 'first_name'),
#         'current_sort_order': request.GET.get('order', 'asc')
#     }
    
#     return render(request, "employee_registrar/employee_list.html", context)


def employee_list(request):
    # Sorting
    sort_by = request.GET.get('sort_by', 'first_name')  
    sort_order = request.GET.get('order', 'asc')

    if sort_order == 'desc':
        sort_by = f'-{sort_by}'  

    # Fetching the employee list
    employee_list = Employee.objects.all()

    # Search parameters
    full_name_query = request.GET.get('full_name', '').strip()
    email_query = request.GET.get('email', '').strip()
    mobile_query = request.GET.get('mobile', '').strip()
    dob_query = request.GET.get('dob', '').strip()

    # Filtering based on search queries
    if full_name_query:
        # employee_list = employee_list.filter(
        #     Q(first_name__icontains=full_name_query) | Q(last_name__icontains=full_name_query)
        # )
        name_parts = full_name_query.split()
        if len(name_parts) == 1:
            # Either first name or last name is provided
            employee_list = employee_list.filter(
                Q(first_name__icontains=name_parts[0]) | Q(last_name__icontains=name_parts[0])
            )
        elif len(name_parts) >= 2:
            # First name and last name are provided
            first_name_input = name_parts[0]
            last_name_input = "".join(name_parts[1:])  # In case last name has multiple parts
            employee_list = employee_list.filter(
                Q(first_name__icontains=first_name_input) & Q(last_name__icontains=last_name_input)
            )
    if email_query:
        employee_list = employee_list.filter(email__icontains=email_query)
    if mobile_query:
        employee_list = employee_list.filter(mobile__icontains=mobile_query)
    if dob_query:
        employee_list = employee_list.filter(date_of_birth=dob_query)

    # Sorting the filtered results
    employee_list = employee_list.order_by(sort_by)

    # Pagination
    paginator = Paginator(employee_list, 4)  # Show 4 employees per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'employee_list': page_obj,
        'current_sort_by': request.GET.get('sort_by', 'first_name'),
        'current_sort_order': request.GET.get('order', 'asc'),
        'full_name_query': full_name_query,
        'email_query': email_query,
        'mobile_query': mobile_query,
        'dob_query': dob_query,
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


def employee_delete(request, id):
    employee = get_object_or_404(Employee, pk=id)
    employee.delete()
    return redirect('/employee/list')
