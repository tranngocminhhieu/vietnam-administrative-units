import sqlite3
import importlib.resources as pkg_resources

def get_data(fields='*'):
    '''
    Get data from Vietnam administrative units database.
    :param fields: Default to *. You can input a list of fields, or split fields by comma.
    :return: Records.
    '''
    if isinstance(fields, list):
        fields = ','.join(fields)

    with pkg_resources.path('vietadminunits.data', 'datasets.db') as db_path:
        sql = f'SELECT DISTINCT {fields} FROM vietadminunits'
        with sqlite3.connect(db_path) as con:
            con.row_factory = sqlite3.Row
            cursor = con.cursor()
            result = cursor.execute(sql)
            records = [dict(row) for row in result.fetchall()]
            return records