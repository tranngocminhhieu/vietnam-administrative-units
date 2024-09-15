import re
from unidecode import unidecode
import pickle
import importlib.resources as pkg_resources

class AdministrativeUnit:
    def __init__(self,
                 province=None,
                 district=None,
                 ward=None,
                 long_province=None,
                 long_district=None,
                 long_ward=None,
                 short_district=None,
                 short_ward=None,
                 province_english=None,
                 district_english=None,
                 ward_english=None,
                 long_province_english=None,
                 long_district_english=None,
                 long_ward_english=None,
                 short_district_english=None,
                 short_ward_english=None,
                 district_level=None,
                 ward_level=None,
                 district_level_english=None,
                 ward_level_english=None):
        self.province = province
        self.district = district
        self.ward = ward
        self.long_province = long_province
        self.long_district = long_district
        self.long_ward = long_ward
        self.short_district = short_district
        self.short_ward = short_ward
        self.province_english = province_english
        self.district_english = district_english
        self.ward_english = ward_english
        self.long_province_english = long_province_english
        self.long_district_english = long_district_english
        self.long_ward_english = long_ward_english
        self.short_district_english = short_district_english
        self.short_ward_english = short_ward_english
        self.district_level = district_level
        self.ward_level = ward_level
        self.district_level_english = district_level_english
        self.ward_level_english = ward_level_english

    def __repr__(self):
        return (f"AdministrativeUnit(province={self.province!r}, "
                f"district={self.district!r}, "
                f"ward={self.ward!r}, "
                f"long_province={self.long_province!r}, "
                f"long_district={self.long_district!r}, "
                f"long_ward={self.long_ward!r}, "
                f"short_district={self.short_district!r}, "
                f"short_ward={self.short_ward!r}, "
                f"province_english={self.province_english!r}, "
                f"district_english={self.district_english!r}, "
                f"ward_english={self.ward_english!r}, "
                f"long_province_english={self.long_province_english!r}, "
                f"long_district_english={self.long_district_english!r}, "
                f"long_ward_english={self.long_ward_english!r}, "
                f"short_district_english={self.short_district_english!r}, "
                f"short_ward_english={self.short_ward_english!r}, "
                f"district_level={self.district_level!r}, "
                f"ward_level={self.ward_level!r}, "
                f"district_level_english={self.district_level_english!r}, "
                f"ward_level_english={self.ward_level_english!r})")

# Load data from pickle
with pkg_resources.open_binary('vnau_parser.data', 'parse.pkl') as f:
    duplicated_district_keys, duplicated_district_province_keys, duplicated_ward_keys, duplicated_ward_district_keys, province_keys_1, province_keys_2, province_map, district_map, ward_map = pickle.load(f)


# Precompile replacement and province regex patterns
grammar_replacements = [(re.compile(rf"\b{old}\b"), new) for old, new in [('qui', 'quy'), ('pak', 'pac')]]
province_patterns_1 = re.compile(rf"{'|'.join(province_keys_1)}")
province_patterns_2 = [re.compile(key) for key in province_keys_2]

def parse_address(address: str, level=3):
    if level not in range(1,4):
        raise ValueError('Level must be 1 (Province) or 2 (District) or 3 (Ward).')

    admin_unit = AdministrativeUnit()

    c_address = unidecode(address).lower().strip()

    # Apply grammar replacements
    for pattern, replacement in grammar_replacements:
        c_address = pattern.sub(replacement, c_address)

    # Removing space have to do after fixing grammar
    c_address = c_address.replace('-', '').replace("'", "").replace(' ', '')


    # Find Province
    results = province_patterns_1.search(c_address)
    if not results:
        for pattern in province_patterns_2:
            results = pattern.search(c_address)
            if results:
                break

    if results:
        province_key = results.group(0)
        c_address = c_address.replace(province_key, '', 1)
        province_data = province_map[province_key]
        admin_unit.province = province_data['province']
        admin_unit.long_province = province_data['long_province']
        admin_unit.province_english = province_data['province_english']
        admin_unit.long_province_english = province_data['long_province_english']
        if level == 1:
            return admin_unit
    else:
        return admin_unit

    # Find District
    district_keys = district_map[admin_unit.province_english]
    district_results = re.search(rf"{'|'.join(district_keys)}", c_address)
    if district_results:
        district_key = district_results.group(0)
        c_address = c_address.replace(district_key, '', 1)

        district_data = district_keys[district_key]

        # Help avoid wrong data input for unique districts in a province
        if not (province_key in duplicated_district_province_keys and district_key in duplicated_district_keys):
            district_entry = district_data[next(iter(district_data))]
        else:
            district_level = 'City' if re.search(r'thanhpho|city', c_address) else 'Town' if re.search(r'thixa|town',
                                                                                                       c_address) else 'District'
            district_entry = district_data[district_level]

        admin_unit.district = district_entry['district']
        admin_unit.long_district = district_entry['long_district']
        admin_unit.short_district = district_entry['short_district']
        admin_unit.district_english = district_entry['district_english']
        admin_unit.long_district_english = district_entry['long_district_english']
        admin_unit.short_district_english = district_entry['short_district_english']
        admin_unit.district_level = district_entry['district_level']
        admin_unit.district_level_english = district_entry['district_level_english']

        if level == 2:
            return admin_unit
    else:
        return admin_unit

    # Find ward
    ward_keys = ward_map[admin_unit.province_english][admin_unit.district_english]
    ward_results = re.search(rf"{'|'.join(ward_keys)}", c_address)
    if ward_results:
        ward_key = ward_results.group(0)
        ward_data = ward_keys[ward_key]

        if not (district_key in duplicated_ward_district_keys and ward_key in duplicated_ward_keys):
            ward_entry = ward_data[next(iter(ward_data))]
        else:
            ward_level = 'Commune' if re.search(r'phong|ward', c_address) else 'Town' if re.search(r'thitran|town', c_address) else 'Commune'
            ward_entry = ward_data[ward_level]

        admin_unit.ward = ward_entry['ward']
        admin_unit.long_ward = ward_entry['long_ward']
        admin_unit.short_ward = ward_entry['short_ward']
        admin_unit.ward_english = ward_entry['ward_english']
        admin_unit.long_ward_english = ward_entry['long_ward_english']
        admin_unit.short_ward_english = ward_entry['short_ward_english']
        admin_unit.ward_level = ward_entry['ward_level']
        admin_unit.ward_level_english = ward_entry['ward_level_english']

    return admin_unit