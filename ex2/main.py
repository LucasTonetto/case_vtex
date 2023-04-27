from pandas_utils import save_chunk, load_csv_data
from process_data import strip_column, ascii_format, remove_not_numbers

def main():
    """Função responsável pelo tratamento e armazenamento da base de dados
    Args:
        No Args.
    Returns:
        Retorna um booleano True|False, de sucesso e falha do processamento
        e armazenamento da base de dados
    """
    data = load_csv_data('data/natal2021.csv', 1000, 'utf-8-sig')

    for chunk_index, chunk in enumerate(data):

        chunk['CITY'] = strip_column(chunk['CITY'])
        chunk['CITY_ASCII'] = ascii_format(chunk['CITY'])
        chunk['PHONE'] = remove_not_numbers(chunk['PHONE'])

        try:
            save_chunk(chunk, chunk_index, "data/natal2021-tratado.csv")
        except:
            print('Erro ao salvar a base de dados!')
            return False
    return True

if __name__ == '__main__':
    main()
