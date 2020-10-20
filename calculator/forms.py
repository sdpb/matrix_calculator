from django import forms

class MatrixDimensionForm(forms.Form):
    row_number = forms.IntegerField(max_value = 10)
    column_number = forms.IntegerField(max_value = 10)

