import re
import numpy as np
import pandas as pd
from unidecode import unidecode
import pickle
import importlib.resources as pkg_resources

class Unit(object):
    def __init__(self, province=None, district=None, province_english=None, district_english=None):
        self.province = province
        self.district = district
        self.province_english = province_english
        self.district_english = district_english

    def __repr__(self):
        return f'Unit(province={self.province}, district={self.district}, province_english={self.province_english}, district_english={self.district_english})'


with pkg_resources.open_binary('vnau_parser.data', 'data.pkl') as f:
    df, df_province, duplicated_district_keys, duplicated_district_province_keys, province_keys_1, province_keys_2 = pickle.load(f)

# Pickle
grammar_replacements = [
    ('qui', 'quy'), # Phú Quý
    ('pak', 'pac') # Krông Pắc
]

def parse_address(address: str, level=2):
    if level not in range(1,3):
        raise ValueError('Level must be between 1 and 2. Province level = 1, District level = 2.')

    u_address = unidecode(address)
    c_address = str(u_address).lower().strip().strip(',')

    for replacement in grammar_replacements:
        c_address = re.sub(rf"\b{replacement[0]}\b", replacement[1], c_address)

    c_address = c_address.replace('-', '').replace(' ', '')


    # Find Province
    results = re.search(rf"{'|'.join(province_keys_1)}", c_address)
    if not results:
        for province_key in province_keys_2:
            results = re.search(province_key, c_address)
            if results:
                break

    if results:
        province_key = results.group(0)
        province = df_province.loc[df_province.province_key == province_key, 'province'].values[0]
        province_english = df_province.loc[df_province.province_key == province_key, 'province_english'].values[0]
        if level == 1:
            return Unit(province=province, province_english=province_english)
    else:
        return Unit()

    # Find District
    district_Keys = df[df.province_english == province_english].district_key.tolist()
    results = re.search(rf"{'|'.join(district_Keys)}", c_address)
    if results:
        district_key = results.group(0)
        # print(province_key, district_key)
        if not (province_key in duplicated_district_province_keys and district_key in duplicated_district_keys):
            district = df.loc[(df.province_english == province_english) & (df.district_key == district_key), 'district_long'].values[0]
            district_english = df.loc[(df.province_english == province_english) & (df.district_key == district_key), 'district_long_english'].values[0]
        else:
            if re.search(r'thanhpho|city', c_address):
                level_english = 'City'
            elif re.search(r'thixa|town', c_address):
                level_english = 'Town'
            else:
                level_english = ''
            district = df.loc[(df.province_key == province_key) & (df.district_key == district_key) & (df.level_english == level_english), 'district_long'].values[0]
            district_english = df.loc[(df.province_key == province_key) & (df.district_key == district_key) & (df.level_english == level_english), 'district_long_english'].values[0]
    else:
        district_key, district, district_english = None, None, None

    return Unit(province=province, district=district, province_english=province_english,
                district_english=district_english)