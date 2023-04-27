def replace_upper_special_characters():
    """Função responsável por criar um tradutor de caracteres com acento e maiúsculos para
    sem acento e maiúsculos
    Args:
        No Args.
    Returns:
        (dict) Dicionário correspondente a tradução a ser realizada
    """
    dict_for_translate = {
        'Ã': 'A',
        'Á': 'A',
        'À': 'A',
        'Â': 'A',
        'Ä': 'A',
        'É': 'E',
        'È': 'E',
        'Ê': 'E',
        'Ë': 'E',
        'Í': 'I',
        'Ì': 'I',
        'Î': 'I',
        'Ï': 'I',
        'Ó': 'O',
        'Ò': 'O',
        'Õ': 'O',
        'Ô': 'O',
        'Ö': 'O',
        'Ú': 'U',
        'Ù': 'U',
        'Û': 'U',
        'Ü': 'U',
        'Ç': 'C',
        'Ñ': 'N'
    }

    return str.maketrans(dict_for_translate)
