from django.core.exceptions import ValidationError


def validate_cpf(value):
    if not value.isdigit():
        raise ValidationError('CPF deve conter apenas números.', 'digits')

    if len(value) != 11:
        raise ValidationError('CPF deve ter 11 números.', 'length')

def cpf_is_digits(value):
    """
    This function receives the Brazilian CPF and returns True if it contains only digits or False if not.
    :param value: A string with the number of Brazilian CPF
    :return: True or False
    """
    if value.isdigit():
        return True
    else:
        return False


def cpf_has_correct_length(value):
    """
    This function receives the Brazilian CPF and returns True if the length of CPF is 11 or False if not.
    :param value: A string with the number of Brazilian CPF
    :return:
    """
    if len(value) != 11:
        return False
    else:
        return True


def cpf_is_valid(value):
    """
    This function receives the Brazilian CPF and returns True if the CPF is valid or False if not valid
    :param value: A string with the number of Brazilian CPF
    :return: True or False
    """

    value = [int(digit) for digit in value]
    intermediate = value[:9]
    list_values_to_calc = [10, 9, 8, 7, 6, 5, 4, 3, 2]

    while len(intermediate) < 11:
        estimate = sum(x * y for (x, y) in zip(intermediate, list_values_to_calc)) % 11
        intermediate.append((0, 11 - estimate)[estimate >= 2])
        list_values_to_calc.insert(0, 11)

    if value[-2:] != intermediate[-2:]:
        return False
    else:
        return True


def format_cpf(value):
    """
    This function returns the Brazilian CPF with the normal format.
    :param value is a string with the number of Brazilian CPF like 12345678911
    :return: Return a sting with teh number in the normal format like 123.456.789-11
    """
    return f'{value[:3]}.{value[3:6]}.{value[6:9]}-{value[9:]}'
