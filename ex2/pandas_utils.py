import os
import pandas as pd

def load_csv_data(file_relative_path, chunksize, encoding):
    """Função responsável por carregar um dataFrame a partir de um arquivo CSV
    informado
    Args:
        file_relative_path (string) Caminho relativo do arquivo CSV
        chunksize (int) Quantidade de linhas lidas por vez do CSV
        encoding (string) Encode do arquivo CSV
    Returns:
        (pandas.TextFileReader) Retorna um iterador referente ao arquivo  de
        dados CSV informado
    """
    return pd.read_csv(
        os.path.abspath(file_relative_path),
        chunksize=chunksize,
        encoding=encoding
    )

def save_chunk(data_frame, index, file_relative_path, encoding='utf-8'):
    """Função responsável por salvar os dados processados em um arquivo CSV
    Args:
        data_frame (pandas.DataFrame) DataFrame contendo o conjunto de dados a ser salvo
        index (int) Indíce informando qual a quantidade de iterações até a leitura
        atual do arquivo
        file_relative_path (string) Caminho relativo para salvar o arquivo CSV, 
        com nome e formato do arquivo a ser salvo
        encoding (string) Encode a ser utilizado no arquivo CSV salvo. Por padrão
        é utilizado o utf-8
    Returns:
        No Returns.
    """
    mode = 'w' if index == 0 else 'a'

    header = index == 0

    data_frame.to_csv(
        os.path.abspath(file_relative_path),
        mode=mode,
        header=header,
        index=False,
        encoding=encoding
    )
