from django.shortcuts import redirect, render

from .forms import MatrixDimensionForm, OperationForm
from .matrix import Matrix
from .operations import Operate


def get_matrix_dimensions(request):
    if request.method == 'POST':
        form = MatrixDimensionForm(request.POST)
        if form.is_valid():
            row_number = form.cleaned_data['row_number']
            column_number = form.cleaned_data['column_number']

            return redirect(enter_matrix_numbers, row_number, column_number)
    else:
        form = MatrixDimensionForm()

    return render(request, 'login/home.html', {'form': form})


def enter_matrix_numbers(request, n_rows, m_columns):
    rows = range(int(n_rows))
    columns = range(int(m_columns))
    form = OperationForm()
    context = {'n_rows': n_rows, 'm_columns': m_columns,
               'rows': rows, 'columns': columns,
               'form': form}
    return render(request, 'calculator/enter_number.html', context)


def calculate(request):
    operation = None
    result = None
    result_type = None
    if request.method == 'POST':
        form = OperationForm(request.POST)
        if form.is_valid():
            content = request.POST.dict()
            operation = form.cleaned_data['operation']
            matrix = Matrix(content)
            if operation == 'scalar':
                scalar = form.cleaned_data['scalar']
                scalar = 2 if scalar is None else int(scalar)
                result = Operate(matrix.matrix, operation, scalar)
                result = result.result
            else:
                result = Operate(matrix.matrix, operation)
                result = result.result
    print(f"{operation}: {str(type(result))}\n{result}")
    context = {'operation': operation, 'result': result, 'result_type': str(type(result))}
    return render(request, 'calculator/enter_number.html', context)
