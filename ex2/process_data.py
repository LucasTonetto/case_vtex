from string_utils import replace_upper_special_characters

def strip_column(df_column):
    """Função responsável por retirar espaços em branco no início ou no
    final de uma string para todos os valores de uma coluna de um DataFrame
    Args:
        df_column (pandas.Series) Coluna onde se deseja retirar os espaços
            em branco
    Returns:
        (pandas.Series) Retorna a coluna sem os espaços em branco no início
        ou no final da string
    """
    return df_column.str.strip()

def ascii_format(df_column):
    """Função responsável formatar no padrão ascii a coluna de DataFrame
    informada, retirando acentos e formatando todas as letras para maiúsculo
    Args:
        df_column (pandas.Series) Coluna onde se deseja realizar a formatação
        ascii
    Returns:
        (pandas.Series) Retorna a coluna na formatação ascii
    """
    return df_column.str.upper().str.translate(replace_upper_special_characters())

def remove_not_numbers(df_column):
    """Função responsável por retirar quaisquer caracteres não numéricos de uma coluna
    do DataFrame
    Args:
        df_column (pandas.Series) Coluna onde se deseja realizar remoção dos
        caracteres numéricos
    Returns:
        (pandas.Series) Retorna a coluna somente com caracteres numéricos
    """
    return df_column.replace(to_replace=r'[^0-9]', value='', regex=True)
