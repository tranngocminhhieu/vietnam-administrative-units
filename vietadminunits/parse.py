import re
from unidecode import unidecode
import pickle
import importlib.resources as pkg_resources
from tabulate import tabulate

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
                 ward_level_english=None,
                 province_key=None, district_key=None, ward_key=None
                ):
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

        self.province_key = province_key
        self.district_key = district_key
        self.ward_key = ward_key

    def __repr__(self):
        def safe_format(value):
            return value if value is not None else ""

        return (
            f"AdministrativeUnit:\n"
            f"{'Attribute':<30} | {'Value':<30}\n"
            f"{'-' * 62}\n"
            f"{'province':<30} | {safe_format(self.province):<30}\n"
            f"{'district':<30} | {safe_format(self.district):<30}\n"
            f"{'ward':<30} | {safe_format(self.ward):<30}\n"
            f"{'-' * 62}\n"
            f"{'long_province':<30} | {safe_format(self.long_province):<30}\n"
            f"{'long_district':<30} | {safe_format(self.long_district):<30}\n"
            f"{'long_ward':<30} | {safe_format(self.long_ward):<30}\n"
            f"{'-' * 62}\n"
            f"{'short_district':<30} | {safe_format(self.short_district):<30}\n"
            f"{'short_ward':<30} | {safe_format(self.short_ward):<30}\n"
            f"{'-' * 62}\n"
            f"{'province_english':<30} | {safe_format(self.province_english):<30}\n"
            f"{'district_english':<30} | {safe_format(self.district_english):<30}\n"
            f"{'ward_english':<30} | {safe_format(self.ward_english):<30}\n"
            f"{'-' * 62}\n"
            f"{'long_province_english':<30} | {safe_format(self.long_province_english):<30}\n"
            f"{'long_district_english':<30} | {safe_format(self.long_district_english):<30}\n"
            f"{'long_ward_english':<30} | {safe_format(self.long_ward_english):<30}\n"
            f"{'-' * 62}\n"
            f"{'short_district_english':<30} | {safe_format(self.short_district_english):<30}\n"
            f"{'short_ward_english':<30} | {safe_format(self.short_ward_english):<30}\n"
            f"{'-' * 62}\n"
            f"{'district_level':<30} | {safe_format(self.district_level):<30}\n"
            f"{'ward_level':<30} | {safe_format(self.ward_level):<30}\n"
            f"{'-' * 62}\n"
            f"{'district_level_english':<30} | {safe_format(self.district_level_english):<30}\n"
            f"{'ward_level_english':<30} | {safe_format(self.ward_level_english):<30}\n")


# Load data from pickle
with pkg_resources.open_binary('vietadminunits.data', 'parse.pkl') as f:
    duplicated_district_keys, duplicated_district_province_keys, duplicated_ward_keys, duplicated_ward_district_keys, province_keys_1, province_keys_2, province_keys_3, province_map, district_map, ward_map, double_check_provinces, double_check_districts, half_district_keys, long_district_alphanumerics, unique_district_keys = pickle.load(f)


def replace_from_right(s, old, new):
    pos = s.rfind(old)
    if pos != -1:
        return s[:pos] + new + s[pos + len(old):]
    return s


# Precompile replacement and province regex patterns
grammar_replacements = [(re.compile(rf"\b{old}\b"), new) for old, new in [('qui', 'quy'), ('pak', 'pac'), ('hn', 'ha noi'), ('n\.t', 'nt')]]
province_patterns_1 = re.compile(rf"{'|'.join(province_keys_1)}")
province_patterns_2 = [re.compile(key) for key in province_keys_2]
province_patterns_3 = [re.compile(key) for key in province_keys_3]
long_district_alphanumeric_patterns = re.compile(rf"{'|'.join(long_district_alphanumerics)}")
unique_district_key_patterns = re.compile(rf"{'|'.join(unique_district_keys)}")

def parse_address(address: str, level=3):
    '''
    Parse an address to get Province, District, and Ward information.
    :param address: The address would be best when following ward > district > province structure.
    :param level: Level must be 1 (Province) or 2 (District) or 3 (Ward). For best performance, if you only need to parse the province, set level = 1.
    :return: AdministrativeUnit object with available data.
    '''
    if level not in range(1,4):
        raise ValueError('Level must be 1 (Province) or 2 (District) or 3 (Ward).')

    admin_unit = AdministrativeUnit()

    c_address = unidecode(address).lower()

    # Apply grammar replacements
    for pattern, replacement in grammar_replacements:
        c_address = pattern.sub(replacement, c_address)

    # Removing space have to do after fixing grammar
    c_address = c_address.replace('-', '').replace("'", "").replace(' 0', ' ').replace(' ', '')

    # # Find Province
    # province_key = None
    # results = province_patterns_1.search(c_address)
    # if results:
    #     province_key = results.group(0)
    #
    # if not results:
    #     for pattern in province_patterns_2:
    #         results = pattern.search(c_address)
    #         if results:
    #             province_key = results.group(0)
    #             break
    #
    # if not results:
    #     for pattern in province_patterns_3:
    #         results = pattern.search(c_address)
    #         if results:
    #             province_key = results.group(0)
    #             break
    #
    # if not results:
    #     results = unique_district_key_patterns.search(c_address)
    #     if results:
    #         district_key = results.group(0)
    #         province_key = unique_district_keys[district_key]

    # Find Province
    province_key = None

    # Check province_patterns_1 first
    match = province_patterns_1.search(c_address)
    if match:
        province_key = match.group(0)
    else:
        # Check patterns in province_patterns_2
        for pattern in province_patterns_2:
            match = pattern.search(c_address)
            if match:
                province_key = match.group(0)
                break
        else:
            # Check patterns in province_patterns_3
            for pattern in province_patterns_3:
                match = pattern.search(c_address)
                if match:
                    province_key = match.group(0)
                    break
            else:
                # Check unique_district_key_patterns if no province_key found
                match = unique_district_key_patterns.search(c_address)
                if match:
                    district_key = match.group(0)
                    province_key = unique_district_keys.get(district_key)

    if province_key:

        if province_key in double_check_provinces:
            new_keys = double_check_provinces[province_key]
            for new_key in new_keys:
                if new_key in c_address and c_address.find(new_key) > c_address.find(province_key):
                    province_key = new_key
                    break

        if not long_district_alphanumeric_patterns.search(c_address):
            c_address = replace_from_right(c_address, province_key, '')

        province_data = province_map[province_key]
        admin_unit.province = province_data['province']
        admin_unit.long_province = province_data['long_province']
        admin_unit.province_english = province_data['province_english']
        admin_unit.long_province_english = province_data['long_province_english']
        admin_unit.province_key = province_key
        if level == 1:
            return admin_unit
    else:
        return admin_unit

    # Find District
    district_keys = district_map[admin_unit.province_english]
    district_results = re.search(rf"{'|'.join(district_keys)}", c_address)
    if district_results:
        district_key = district_results.group(0)

        if district_key in double_check_districts:
            new_keys = double_check_districts[district_key]
            for new_key in new_keys:
                if new_key in c_address and c_address.find(new_key) > c_address.find(district_key):
                    district_key = new_key
                    break

        if district_key in half_district_keys:
            tmp_address = replace_from_right(c_address, district_key, '')
            new_keys = half_district_keys[district_key]
            for new_key in new_keys:
                ward_keys = new_keys[new_key]
                if re.search(rf"{'|'.join(ward_keys)}", tmp_address):
                    district_key = new_key
                    break

        district_data = district_keys[district_key]

        # Help avoid wrong data input for unique districts in a province
        if not (province_key in duplicated_district_province_keys and district_key in duplicated_district_keys):
            district_entry = district_data[next(iter(district_data))]
        else:
            if re.search(r'thanhpho|city|tp\.', c_address):
                district_level = 'City'
            elif re.search(r'thixa|town|tx\.', c_address):
                district_level = 'Town'
            elif re.search(r'huyen|district|h\.', c_address):
                district_level = 'District'
            else:
                district_level = duplicated_district_keys[district_key]['default']

                levels = duplicated_district_keys[district_key]['levels']
                for level in levels:
                    ward_keys = levels[level]
                    if re.search(rf"{'|'.join(ward_keys)}", c_address):
                        district_level = level
                        break

            district_entry = district_data[district_level]

        admin_unit.district = district_entry['district']
        admin_unit.long_district = district_entry['long_district']
        admin_unit.short_district = district_entry['short_district']
        admin_unit.district_english = district_entry['district_english']
        admin_unit.long_district_english = district_entry['long_district_english']
        admin_unit.short_district_english = district_entry['short_district_english']
        admin_unit.district_level = district_entry['district_level']
        admin_unit.district_level_english = district_entry['district_level_english']
        admin_unit.district_key = district_key
        if level == 2:
            return admin_unit
    else:
        return admin_unit

    # Find ward
    ward_keys = ward_map[admin_unit.province_english][admin_unit.district_english]

    # Some districts do not have a ward, for instance: Huyện Bạch Long Vĩ, Thành phố Hải Phòng
    if not ward_keys:
        return admin_unit

    ward_results = re.search(rf"{'|'.join(ward_keys)}", c_address)

    if ward_results:
        ward_key = ward_results.group(0)
        ward_data = ward_keys[ward_key]

        if not (district_key in duplicated_ward_district_keys and ward_key in duplicated_ward_keys):
            ward_entry = ward_data[next(iter(ward_data))]
        else:
            if re.search(r'xa|Commune|x\.', c_address):
                ward_level = 'Commune'
            elif re.search(r'phuong|ward|p\.', c_address):
                ward_level = 'Ward'
            elif re.search(r'thitran|town|tt\.', c_address):
                ward_level = 'Town'
            else:
                ward_level = duplicated_ward_keys[ward_key]

            ward_entry = ward_data[ward_level]

        admin_unit.ward = ward_entry['ward']
        admin_unit.long_ward = ward_entry['long_ward']
        admin_unit.short_ward = ward_entry['short_ward']
        admin_unit.ward_english = ward_entry['ward_english']
        admin_unit.long_ward_english = ward_entry['long_ward_english']
        admin_unit.short_ward_english = ward_entry['short_ward_english']
        admin_unit.ward_level = ward_entry['ward_level']
        admin_unit.ward_level_english = ward_entry['ward_level_english']
        admin_unit.ward_key = ward_key

    return admin_unit