from django import forms
from credentials.models import Departments,Courses,Materials

class OrderForm(forms.Form):
    department = forms.ModelChoiceField(queryset=Departments.objects.all(),empty_label='Select your Department')
    course = forms.ModelChoiceField(queryset=Courses.objects.all(), empty_label='Select Course')
    purpose = forms.ChoiceField(choices=[('select purpose','Select your Purpose'),('enquiry', 'For Enquiry'), ('order', 'Place Order'), ('return', 'Return')])
    materials = forms.ModelMultipleChoiceField(queryset=Materials.objects.all(), widget=forms.CheckboxSelectMultiple)

