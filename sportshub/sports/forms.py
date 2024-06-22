
from django import forms
from .models import Register

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Register
        fields = ['stu_name', 'stu_class', 'stu_rollno', 'name']
        labels = {
            'stu_name': "Student Name",
            'stu_class': "Student class",
            'stu_rollno': "Student Rollnumber",
            'name': "Event Name",
        }

    def generate_registration_number(self):
        # Logic to generate registration number
        pass


