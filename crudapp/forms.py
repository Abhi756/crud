from django import forms
from django import forms
from .models import EmployeeDetails

class MyForm(forms.ModelForm):
    class Meta:
        model=EmployeeDetails
        fields=[ "Emp_ser", "NAME", "DESGN", "Qualification",]
        labels={'Emp_ser':"ID","NAME":"NAME","DESGN":"DESIGNATION","Qualification":"EXPERIENCE",}