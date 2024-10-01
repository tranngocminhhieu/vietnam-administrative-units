import sqlite3
import os

# Get the directory of the current script (parse.py)
current_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the path to the datasets.db file
data_path = os.path.join(current_dir, 'data', 'datasets.db')

def get_data(fields='*'):
    '''
    Get data from Vietnam administrative units database.
    :param fields: Default to *. You can input a list of fields, or split fields by comma.
    :return: Records.
    '''
    if isinstance(fields, list):
        fields = ','.join(fields)


    sql = f'SELECT DISTINCT {fields} FROM vietadminunits'
    with sqlite3.connect(data_path) as con:
        con.row_factory = sqlite3.Row
        cursor = con.cursor()
        result = cursor.execute(sql)
        records = [dict(row) for row in result.fetchall()]
        return records


if __name__ == '__main__':
    print(data_path)
    print(get_data('province'))