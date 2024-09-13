import re
from unidecode import unidecode
import pickle
import importlib.resources as pkg_resources

class AdministrativeUnit(object):
    def __init__(self, province=None, district=None, province_english=None, district_english=None, ward=None):
        self.province = province
        self.district = district
        self.province_english = province_english
        self.district_english = district_english
        self.ward = ward

    def __repr__(self):
        return f'AdministrativeUnit(province={self.province}, district={self.district}, province_english={self.province_english}, district_english={self.district_english}, ward={self.ward})'


with pkg_resources.open_binary('vnau_parser.data', 'data.pkl') as f:
    duplicated_district_keys, duplicated_district_province_keys, duplicated_ward_keys, duplicated_ward_district_keys, province_keys_1, province_keys_2, province_map, district_map, ward_map = pickle.load(f)

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

    c_address = c_address.replace('-', '').replace("'", "").replace(' ', '')


    # Find Province
    results = re.search(rf"{'|'.join(province_keys_1)}", c_address)
    if not results:
        for province_key in province_keys_2:
            results = re.search(province_key, c_address)
            if results:
                break

    if results:
        province_key = results.group(0)
        province = province_map[province_key]['province']
        province_english = province_map[province_key]['province_english']
        if level == 1:
            return AdministrativeUnit(province=province, province_english=province_english)
    else:
        return AdministrativeUnit()

    # Find District
    district_keys = district_map[province_english]
    results = re.search(rf"{'|'.join(district_keys)}", c_address)
    if results:
        district_key = results.group(0)

        # Help avoid wrong data input for unique districts in a province
        if not (province_key in duplicated_district_province_keys and district_key in duplicated_district_keys):

            district = district_keys[district_key][next(iter(district_keys[district_key]))]['district']
            district_english = district_keys[district_key][next(iter(district_keys[district_key]))]['district_english']

        else:
            if re.search(r'thanhpho|city', c_address):
                level_english = 'City'
            elif re.search(r'thixa|town', c_address):
                level_english = 'Town'
            else:
                level_english = 'District'

            district = district_keys[district_key][level_english]['district']
            district_english = district_keys[district_key][level_english]['district_english']

            if level == 2:
                return AdministrativeUnit(province=province, district=district, province_english=province_english, district_english=district_english)
    else:
        return AdministrativeUnit(province=province, province_english=province_english)

    ward_keys = ward_map[province_english][district_english]
    results = re.search(rf"{'|'.join(ward_keys)}", c_address)
    if results:
        ward_key = results.group(0)
        if not (district_key in duplicated_ward_district_keys and ward_key in duplicated_ward_keys):
            ward = ward_keys[ward_key][next(iter(ward_keys[ward_key]))]
        else:
            if re.search(r'xa|commune', c_address):
                ward_level_english = 'Commune'
            elif re.search(r'thitran|town', c_address):
                ward_level_english = 'Town'
            else:
                ward_level_english = 'Ward'

            ward = ward_keys[ward_key][ward_level_english]

        return AdministrativeUnit(province=province, district=district, province_english=province_english, district_english=district_english, ward=ward)
    else:
        return AdministrativeUnit(province=province, district=district, province_english=province_english, district_english=district_english)