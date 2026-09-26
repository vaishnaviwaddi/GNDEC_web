from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')

def products(request):
    return render(request, 'products.html')
def service(request):
    return render(request, 'service.html')

def contacts(request):
    return render(request, 'contacts.html')


from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Student

# CREATE
class StudentCreateView(CreateView):
    model = Student
    fields = ['name', 'ucn', 'dept', 'email']
    template_name = 'student_form.html'
    success_url = reverse_lazy('student-list')

# READ (List view)
class StudentListView(ListView):
    model = Student
    template_name = 'student_list.html'
    context_object_name = 'students'  # Default is 'object_list'

# READ (Detail view)
class StudentDetailView(DetailView):
    model = Student
    template_name = 'student_detail.html'
    context_object_name = 'student'  # Default is 'object'

# UPDATE
class StudentUpdateView(UpdateView):
    model = Student
    fields = ['name', 'ucn', 'dept', 'email']
    template_name = 'student_form.html'  # Reuses the create form template
    success_url = reverse_lazy('student-list')

# DELETE
class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student_confirm_delete.html'
    success_url = reverse_lazy('student-list')
