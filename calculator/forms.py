from django import forms

class MatrixDimensionForm(forms.Form):
    first_number = forms.IntegerField(max_value = 10)
    second_number = forms.IntegerField(max_value = 10)
