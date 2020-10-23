from django import forms


class MatrixDimensionForm(forms.Form):
    row_number = forms.IntegerField(min_value=2, max_value=10)
    column_number = forms.IntegerField(min_value=2, max_value=10)


OPERATION_CHOICES = (
    ("determinant", "Determinant"),
    ("rank", "Rank"),
    ("scalar", "Scalar"),
    ("transpose", "Transpose"),
)


class OperationForm(forms.Form):
    operation = forms.ChoiceField(required=True, choices=OPERATION_CHOICES)
    scalar = forms.IntegerField(required=False)
