from django import forms

class IndexForm(forms.Form):
    class_name = forms.CharField(label='class name', max_length=100)

