import re


class Matrix:

    def __init__(self, dictionary):
        cleaned_dict = clean_dict(dictionary)
        self.n_rows, self.m_columns = get_dimensions(cleaned_dict)
        self.matrix = get_matrix(cleaned_dict, self.n_rows, self.m_columns)

    def __str__(self) -> str:
        return str(self.matrix)


def clean_dict(dictionary):
    pattern = re.compile(r'^(\d\d)$')
    cleaned_dictionary = dict()
    for _ in dictionary:
        if pattern.match(_):
            if re.match('^$', dictionary[_]):
                cleaned_dictionary.update({_: 0})
            else:
                cleaned_dictionary.update({_: int(dictionary[_])})
    return cleaned_dictionary


def get_dimensions(dictionary):
    keys = list(dictionary.keys())
    dimensions = list(map(int, keys[-1]))
    return (dimensions[0] + 1), (dimensions[1] + 1)


def get_matrix(dictionary, n_rows, m_columns):
    matrix = list()
    for n_row in range(n_rows):
        aux_column_list = list()
        for m_column in range(m_columns):
            key = '{}{}'.format(n_row, m_column)
            aux_column_list.append(dictionary[key])
        matrix.append(aux_column_list)
    return matrix
