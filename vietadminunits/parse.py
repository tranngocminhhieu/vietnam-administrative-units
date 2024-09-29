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


    def to_dict(self):
        return {
            'province': self.province,
            'district': self.district,
            'ward': self.ward,
            'long_province': self.long_province,
            'long_district': self.long_district,
            'long_ward': self.long_ward,
            'short_district': self.short_district,
            'short_ward': self.short_ward,
            'province_english': self.province_english,
            'district_english': self.district_english,
            'ward_english': self.ward_english,
            'long_province_english': self.long_province_english,
            'long_district_english': self.long_district_english,
            'long_ward_english': self.long_ward_english,
            'short_district_english': self.short_district_english,
            'short_ward_english': self.short_ward_english,
            'district_level': self.district_level,
            'ward_level': self.ward_level,
            'district_level_english': self.district_level_english,
            'ward_level_english': self.ward_level_english
        }

    def __repr__(self):
        def safe_format(value):
            return value if value is not None else ""

        return (
            f"AdministrativeUnit:\n"
            f"{'Attribute':<25} | {'Value':<25}\n"
            f"{'-' * 52}\n"
            f"{'province':<25} | {safe_format(self.province):<25}\n"
            f"{'district':<25} | {safe_format(self.district):<25}\n"
            f"{'ward':<25} | {safe_format(self.ward):<25}\n"
            f"{'-' * 52}\n"
            f"{'long_province':<25} | {safe_format(self.long_province):<25}\n"
            f"{'long_district':<25} | {safe_format(self.long_district):<25}\n"
            f"{'long_ward':<25} | {safe_format(self.long_ward):<25}\n"
            f"{'-' * 52}\n"
            f"{'short_district':<25} | {safe_format(self.short_district):<25}\n"
            f"{'short_ward':<25} | {safe_format(self.short_ward):<25}\n"
            f"{'-' * 52}\n"
            f"{'province_english':<25} | {safe_format(self.province_english):<25}\n"
            f"{'district_english':<25} | {safe_format(self.district_english):<25}\n"
            f"{'ward_english':<25} | {safe_format(self.ward_english):<25}\n"
            f"{'-' * 52}\n"
            f"{'long_province_english':<25} | {safe_format(self.long_province_english):<25}\n"
            f"{'long_district_english':<25} | {safe_format(self.long_district_english):<25}\n"
            f"{'long_ward_english':<25} | {safe_format(self.long_ward_english):<25}\n"
            f"{'-' * 52}\n"
            f"{'short_district_english':<25} | {safe_format(self.short_district_english):<25}\n"
            f"{'short_ward_english':<25} | {safe_format(self.short_ward_english):<25}\n"
            f"{'-' * 52}\n"
            f"{'district_level':<25} | {safe_format(self.district_level):<25}\n"
            f"{'ward_level':<25} | {safe_format(self.ward_level):<25}\n"
            f"{'-' * 52}\n"
            f"{'district_level_english':<25} | {safe_format(self.district_level_english):<25}\n"
            f"{'ward_level_english':<25} | {safe_format(self.ward_level_english):<25}\n")

def replace_from_right(s, old, new):
    pos = s.rfind(old)
    if pos != -1:
        return s[:pos] + new + s[pos + len(old):]
    return s

# Load data from pickle
with pkg_resources.open_binary('vietadminunits.data', 'parse.pkl') as f:
    data = pickle.load(f)

## Part_1_base.ipynb:
DICT_long_province_alphanumerics = data['DICT_long_province_alphanumerics']
DICT_long_district_alphanumerics = data['DICT_long_district_alphanumerics'] # Use after getting province
DICT_long_ward_alphanumerics = data['DICT_long_ward_alphanumerics'] # Use after getting district

LIST_safe_long_district_alphanumerics = data['LIST_safe_long_district_alphanumerics']
LIST_safe_long_ward_alphanumerics = data['LIST_safe_long_ward_alphanumerics']

DICT_province_map = data['DICT_province_map']
DICT_district_map = data['DICT_district_map']
DICT_ward_map = data['DICT_ward_map']
DICT_duplicated_ward_map = data['DICT_duplicated_ward_map']

DICT_duplicated_district_keys = data['DICT_duplicated_district_keys']
DICT_duplicated_ward_keys = data['DICT_duplicated_ward_keys']

DICT_unique_long_district_alphanumerics = data['DICT_unique_long_district_alphanumerics']
DICT_not_unique_long_district_alphanumerics = data['DICT_not_unique_long_district_alphanumerics']
LIST_contains_province_key_long_district_alphanumerics = data['LIST_contains_province_key_long_district_alphanumerics']
DICT_unique_district_keys = data['DICT_unique_district_keys']
DICT_not_unique_district_keys = data['DICT_not_unique_district_keys']

DICT_alias_province_keys = data.get('DICT_alias_province_keys', {})

## Part_2_alias_and_half_district_keys.ipynb:
DICT_alias_district_keys = data.get('DICT_alias_district_keys', {}) # Use after getting province
DICT_half_district_keys = data.get('DICT_half_district_keys', {}) # Use after getting province

## Part_3_double_check_keys.ipynb:
DICT_double_check_provinces = data.get('DICT_double_check_provinces', {}) # Use after getting province_key
DICT_double_check_districts = data.get('DICT_double_check_districts', {}) # Use after getting province and district_key
DICT_double_check_wards = data.get('DICT_double_check_wards', {}) # Use after getting ward_key

## Part_4_double_check_inverted_keys.ipynb
DICT_double_check_inverted_provinces = data.get('DICT_double_check_inverted_provinces', {})
# DICT_double_check_inverted_districts = data.get('DICT_double_check_inverted_districts', {})


# Precompile
## From data
PATTERN_long_province_alphanumerics = re.compile(rf"{'|'.join(DICT_long_province_alphanumerics)}".replace('.', '\.')) # For searching
PATTERN_safe_long_district_long_ward_alphanumerics = re.compile(rf"{'|'.join(LIST_safe_long_district_alphanumerics + LIST_safe_long_ward_alphanumerics)}".replace('.', '\.')) # For removing from the address before finding province
PATTERN_safe_long_ward_alphanumerics = re.compile(rf"{'|'.join(LIST_safe_long_ward_alphanumerics)}".replace('.', '\.')) # For removing from the address before finding district

PATTERN_province_keys = re.compile(rf"(?=({'|'.join(DICT_province_map)}))")
PATTERN_alias_province_keys = re.compile(rf"{'|'.join(DICT_alias_province_keys) or 'placeholder'}".replace('.', '\.')) # For searching

PATTERN_unique_long_district_alphanumerics = re.compile(rf"{'|'.join(DICT_unique_long_district_alphanumerics) or 'placeholder'}".replace('.', '\.'))
PATTERN_not_unique_long_district_alphanumerics = re.compile(rf"{'|'.join(DICT_not_unique_long_district_alphanumerics) or 'placeholder'}".replace('.', '\.'))
PATTERN_contains_province_key_long_district_alphanumerics = re.compile(rf"{'|'.join(LIST_contains_province_key_long_district_alphanumerics) or 'placeholder'}".replace('.', '\.'))
PATTERN_unique_district_keys = re.compile(rf"{'|'.join(DICT_unique_district_keys) or 'placeholder'}".replace('.', '\.'))
PATTERN_not_unique_district_keys = re.compile(rf"{'|'.join(DICT_not_unique_district_keys) or 'placeholder'}".replace('.', '\.'))


## Grammar
grammar_replacements = [(re.compile(rf"\b{old}\b"), new) for old, new in [('qui', 'quy'), ('pak', 'pac'), ('hn', 'ha noi'), ('n\.t', 'nt'), ('xa\s?lo\s?ha\s?noi', ''), ('ki', 'ky'), ('duong\s?dien\s?bien\s?phu', '')]]





# People can give P2, Q5, etc. We want to parse it as district and ward, but some streets have name exactly like that.
# So we need to correct it to P.2, Q.5, ... when they are not a street name.
def correct_abbreviation(c_address, abbr):
    pattern = rf'\b{abbr}\d{{1,2}}\b'
    match = re.search(pattern, c_address)
    if match:
        old_text = match.group()
        if not re.search(rf'duong\s?\b{abbr}\d{{1,2}}\b|d\.\s?\b{abbr}\d{{1,2}}\b', c_address):
            c_address = c_address.replace(old_text, old_text.replace(abbr, f'{abbr}.'))
    return c_address

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




    # Prepare address
    c_address = unidecode(address).lower()

    ## Apply grammar replacements
    for pattern, replacement in grammar_replacements:
        c_address = pattern.sub(replacement, c_address)
    c_address = correct_abbreviation(c_address, 'p')
    c_address = correct_abbreviation(c_address, 'q')

    # Thọ Xuân,Đan Phượng,Thành phố Hà Nội
    ## Drop the street part for beatiful address cases
    # pattern_1 = r'\b(phuong|xa|thi\s?tran|p\.|x\.|tt\.)\b'
    # match_1 = re.search(pattern_1, c_address)
    #
    # pattern_2 = r'\b(quan|huyen|thi\s?xa|thanh\s?pho|q\.|h\.|tx\.|tp\.?)\b'
    # match_2 = re.search(pattern_2, c_address)
    #
    # if match_1 and match_2 and match_1.start() < match_2.start():
    #     start = match_1.start()
    #     c_address = c_address[start:]

    ## Removing space have to do after fixing grammar
    c_address = c_address.replace('-', '').replace("'", "").replace(' 0', ' ').replace(' ', '')
    original_address = c_address
    #print('Clean address:', c_address)


    # Find Province
    province_alphanumeric = None
    province_key = None
    
    # -- BEGIN Part 1 data --
    
    # Avoid wrong match. Eg: Phường Bình Thuận, Quận 7 -> Bình Thuận. Only works for long name.
    tmp_address = PATTERN_safe_long_district_long_ward_alphanumerics.sub('', c_address)
    #print('Before Province:', tmp_address)

    # Check province_patterns_1 first, these are unique province_keys
    matches = PATTERN_long_province_alphanumerics.findall(tmp_address)
    if matches:
        province_alphanumeric = matches[-1]
        province_key = DICT_long_province_alphanumerics[province_alphanumeric]
    else:
        matches = PATTERN_province_keys.findall(tmp_address)
        if matches:
            province_key = matches[-1]
        else:
            # Check patterns in province_patterns_2
            # these province_keys are the same some district_keys. Use loop to prioritize some province_key.
            # for pattern in LIST_PATTERN_province_keys_2:
            #     matches = pattern.findall(tmp_address)
            #     if matches:
            #         province_key = matches[-1]
            #         break
            # matches = PATTERN_province_keys_2.findall(tmp_address)
            # if matches:
            #     province_key = matches[-1]
            # else:
            #     # Check patterns in province_patterns_3
            #     # these province_keys are the same some ward_keys. Use loop to prioritize some province_key.
            #     # for pattern in LIST_PATTERN_province_keys_3:
            #     #     matches = pattern.findall(tmp_address)
            #     #     if matches:
            #     #         province_key = matches[-1]
            #     #         break
            #     matches = PATTERN_province_keys_3.findall(tmp_address)
            #     if matches:
            #         province_key = matches[-1]
            #     else:


            matches = PATTERN_alias_province_keys.findall(tmp_address)
            if matches:
                alias_province_key = matches[-1]
                province_key = DICT_alias_province_keys[alias_province_key]

            else:
                # Check long_ward_alphanumeric if no province_key found
                tmp_address = PATTERN_safe_long_ward_alphanumerics.sub('', c_address)
                matches = PATTERN_unique_long_district_alphanumerics.findall(tmp_address)
                if matches:
                    long_district_alphanumeric = matches[-1]
                    province_key = DICT_unique_long_district_alphanumerics[long_district_alphanumeric]
                else:
                    matches = PATTERN_not_unique_long_district_alphanumerics.findall(tmp_address)
                    if matches:
                        long_district_alphanumeric = matches[-1]
                        province_keys = DICT_not_unique_long_district_alphanumerics[long_district_alphanumeric]
                        for tmp_province_key in province_keys:
                            ward_keys = province_keys[tmp_province_key]
                            if re.search(rf"{'|'.join(ward_keys)}".replace('.', '\.'), tmp_address):
                                province_key = tmp_province_key
                                break
                    else:
                        # Check unique district_key if no province_key found
                        matches = PATTERN_unique_district_keys.findall(tmp_address)
                        if matches:
                            district_key = matches[-1]
                            province_key = DICT_unique_district_keys[district_key]
                        else:
                            # Check not unique district_key if no province_key found
                            # But a ward_key must be found in the address
                            count = 0
                            while not province_key and count <= 2:
                                count += 1
                                matches = PATTERN_not_unique_district_keys.findall(tmp_address)
                                if matches:
                                    district_key = matches[-1]
                                    province_keys = DICT_not_unique_district_keys[district_key]
                                    for tmp_province_key in province_keys:
                                        ward_keys = province_keys[tmp_province_key]
                                        if re.search(rf"{'|'.join(ward_keys)}".replace('.', '\.'), tmp_address):
                                            province_key = tmp_province_key
                                            break
                                        else:
                                            tmp_address = tmp_address.replace(district_key, '', 1)


    if province_key:
        # Some district_keys and ward_keys are the same province_key of other provinces, It causes wrong detecting province_key. Eg: Thái Nguyên, Quảng Ngãi, Bình Định have Bình Thuận district.
        # We will do double-check for some province, If we find-out a new province_key placed after current province_key then choose the new province_key
        if province_key in DICT_double_check_provinces:
            new_keys = DICT_double_check_provinces.get(province_key, [])
            match = re.search(rf"{'|'.join(new_keys) or 'placeholder'}", c_address, flags=re.IGNORECASE)
            if match:
                province_key = match.group()


        elif province_key in DICT_double_check_inverted_provinces:
            new_keys = DICT_double_check_inverted_provinces.get(province_key, {})
            match = re.search(rf"{'|'.join(new_keys) or 'placeholder'}", c_address, flags=re.IGNORECASE)
            if match:
                tmp_province_key = match.group()

                # This is a particular case
                if province_key == 'thanhhoa' and tmp_province_key == 'longan' and 'longanh' in c_address:
                    pass
                else:

                    ward_district_keys = DICT_double_check_inverted_provinces.get(province_key, {}).get(tmp_province_key, [])
                    tmp_address = c_address.replace(tmp_province_key, '')
                    for ward_district_key in ward_district_keys:
                        pattern = r'(?=.*' + r')(?=.*'.join(ward_district_key) + r')' # ChatGPT help me
                        if re.search(pattern, tmp_address):
                            province_key = tmp_province_key


        # Normally, We will remove province_key in the address from right-to-left, this help avoid wrong detecting district. Eg: Huyện Lắk, Tỉnh Đắk Lắk; Thành phố Huế, Tỉnh Thừa Thiên Huế.
        # But to support "Find province from district" feature, we will ignore for some long district. Eg: Thành phố Thanh Hóa
        # if not PATTERN_contains_province_key_long_district_alphanumerics.search(c_address):
        #     c_address = replace_from_right(c_address, province_key, '')

        if not PATTERN_contains_province_key_long_district_alphanumerics.search(c_address):
            c_address = replace_from_right(c_address, province_key, '')


        # xathanhminh,tinhdienbien,dienbienphu -> remove dienbien -> can not match dienbienphu
        dienbien_match = re.search(r'dienbienphu|dienbiendong', original_address)
        if dienbien_match:
            dienbien = dienbien_match.group()
            c_address += dienbien

            # # Case: tinhthosontinhquangngai
            # if province_alphanumeric:
            #     if province_alphanumeric == 'tinhhatinh':
            #         if re.search(r'thachhatinh|lochatinh', c_address, flags=re.IGNORECASE):
            #             c_address = replace_from_right(c_address, province_alphanumeric, '')
            #         else:
            #             c_address = replace_from_right(c_address, province_key, '')
            #     elif province_alphanumeric == 'tinhquangngai':
            #         # tinhbinhsontinhquangngai
            #         if re.search(r'binhsontinh|lysontinh', c_address, flags=re.IGNORECASE):
            #             if 'tinhbinh' not in c_address:
            #                 c_address = replace_from_right(c_address, province_alphanumeric, '')
            #             else:
            #                 c_address = replace_from_right(c_address, province_key, '')
            #         else:
            #             c_address = replace_from_right(c_address, province_key, '')
            #     elif province_alphanumeric == 'tinhvinhphuc':
            #         if 'dongtinh' in c_address:
            #             c_address = replace_from_right(c_address, province_key, '')
            #         else:
            #             c_address = replace_from_right(c_address, province_alphanumeric, '')
            #     else:
            #         c_address = replace_from_right(c_address, province_alphanumeric, '')
            #
            # else:
            #     c_address = replace_from_right(c_address, province_key, '')


            #print('After Province', c_address)
        province_data = DICT_province_map[province_key]
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
    district_keys = DICT_district_map.get(admin_unit.province_english, {})
    long_district_alphanumerics = DICT_long_district_alphanumerics.get(admin_unit.province_english, {})

    alias_district_keys = DICT_alias_district_keys.get(admin_unit.province_english, {})
    half_district_keys = DICT_half_district_keys.get(admin_unit.province_english, {})

    district_key = None
    # Should not remove full long_ward_alphanumeric in address due to mistake. Eg: "Thị xã Sơn Tây" will be wrong removed "Xã Sơn Tây"
    tmp_address = PATTERN_safe_long_ward_alphanumerics.sub('', c_address)

    #print('Before District:', tmp_address)

    matches = re.findall(rf"(?=({'|'.join(long_district_alphanumerics)}))".replace('.', '\.'), tmp_address)
    if matches:
        long_district_alphanumeric = matches[-1]
        district_key = long_district_alphanumerics[long_district_alphanumeric]
    else:
        matches = re.findall(rf"(?=({'|'.join(district_keys)}))".replace('.', '\.'), tmp_address)
        if matches:
            district_key = matches[-1]
        else:
            match = re.search(rf"{'|'.join(alias_district_keys) or 'placeholder'}".replace('.', '\.'), tmp_address)
            if match:
                alias_district_key = match.group()
                district_key = alias_district_keys[alias_district_key]
            else:
                # Due to wrong typo. Eg: "Nam Từ Liêm", "Bắc Từ Liêm" are correctly, but people can give "Từ Liêm" only. More eg: Bắc Trà My, Nam Trà My; Gò Công Đông, Gò Công Tây, Gò Công.
                # We will use their ward_keys to choose the true district_key
                # If not found true district_key, don't worry, we added half district keys as alias district_key in the district_map, thus we have default district.
                match = re.search(rf"{'|'.join(half_district_keys) or 'placeholder'}".replace('.', '\.'), tmp_address)
                if match:
                    half_district_key = match.group()
                    # print('half_district_key:', half_district_key)
                    # Set default value
                    district_key = half_district_keys[half_district_key]['default']

                    # print('default district_key:' , district_key)

                    # Try one more time based on ward_keys
                    tmp_district_keys = half_district_keys[half_district_key]['district_keys']
                    tmp_address = replace_from_right(c_address, half_district_key, '') # Remove half_district_key from address
                    for tmp_district_key in tmp_district_keys:
                        tmp_ward_keys = tmp_district_keys[tmp_district_key]
                        if re.match(rf"{'|'.join(tmp_ward_keys)}".replace('.', '\.'), tmp_address):
                            district_key = tmp_district_key
                            break

    # print('Found district keys:', district_key)

    if district_key:
        # Some ward_keys are the same district_key of other districts. Eg: Thanh Trì, Hà Nội và Thanh Trì, Hoàng Mai, Hà Nội
        # We will do double-check for some districts, If we find-out a new district_key that placed after current district_key then choose the new district_key
        if district_key in DICT_double_check_districts.get(admin_unit.province_english, {}):
            new_keys = DICT_double_check_districts.get(admin_unit.province_english, {}).get(district_key, [])
            match = re.search(rf"{'|'.join(new_keys) or 'placeholder'}", original_address)
            if match:
                tmp_district_key = match.group()

                change = True

                # Use Part_3_double_check_keys_CHECK.ipynb
                if district_key == 'sontinh' and tmp_district_key == 'binhson' and 'tinhbinh' in c_address:
                    change = False
                elif district_key == 'hatinh' and tmp_district_key == 'thachha':
                    if re.search(rf"thanhphohatinh|tp\.hatinh|xathachha[^i]|x\.thachha[^i]", c_address):
                        change = False

                    # Diem ket thuc "thachha" < diem bat dau "hatinh" tránh được "thachhatinh"
                    elif (c_address.rfind('thachha') + len('thachha') - 1) < c_address.rfind('hatinh'):
                        change = False

                if change:
                    district_key = tmp_district_key

        district_data = district_keys[district_key]

        duplicated_district_keys = DICT_duplicated_district_keys.get(admin_unit.province_english, {})

        # To avoid wrong data input for unique districts in a province, just get the first item
        if not (district_key in duplicated_district_keys):
            district_entry = district_data[next(iter(district_data))]

        # With duplicated district_keys in a province, we need to find the prefix (suffix) to choose the district level.
        # This problem only occurs with Thành phố, Thị xã, Huyện.
        else:
            if re.search(rf'thanhpho{district_key}|{district_key}city|tp\.{district_key}', c_address):
                district_level = 'City'
            elif re.search(rf'thixa{district_key}|{district_key}town|tx\.{district_key}', c_address):
                district_level = 'Town'
            elif re.search(rf'huyen{district_key}|{district_key}district|h\.{district_key}', c_address):
                district_level = 'District'
            else:
                # If level is not found, we have default level based on Google Trend
                district_level = duplicated_district_keys[district_key]['default']

                # But we can try one more time, use ward_keys in each level to find the true district_key
                levels = duplicated_district_keys[district_key]['levels']
                for level in levels:
                    ward_keys = levels[level]

                    # # District: kyphu, Town: kyphuong
                    # if district_key == 'kyanh' and level == 'District':
                    #     ward_keys = ['kyphu[^o]' if key == 'kyphu' else key for key in ward_keys]

                    if re.search(rf"{'|'.join(ward_keys)}".replace('.', '\.'), c_address):
                        district_level = level
                        break

            district_entry = district_data[district_level]

        c_address = replace_from_right(c_address, district_key, '')

        #print('After District:', c_address)

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
    ward_keys = DICT_ward_map[admin_unit.province_english][admin_unit.district_english]
    long_ward_alphanumerics = DICT_long_ward_alphanumerics[admin_unit.province_english][admin_unit.district_english]

    # Some districts do not have a ward. Eg: Huyện Bạch Long Vĩ, Thành phố Hải Phòng. Return object.
    if not ward_keys:
        return admin_unit

    ward_key = None
    match = re.search(rf"{'|'.join(long_ward_alphanumerics)}".replace('.', '\.'), c_address)
    if match:
        long_ward_alphanumeric = match.group()
        ward_key = long_ward_alphanumerics[long_ward_alphanumeric]
    else:
        match = re.search(rf"{'|'.join(ward_keys)}".replace('.', '\.'), c_address)
        if match:
            ward_key = match.group()

    if ward_key:

        #print('Tìm được ward_key:', ward_key)

        if ward_key in DICT_double_check_wards.get(admin_unit.province_english, {}).get(admin_unit.district_english, {}):
            new_keys = DICT_double_check_wards.get(admin_unit.province_english, {}).get(admin_unit.district_english, {}).get(ward_key, [])
            match = re.search(rf"{'|'.join(new_keys) or 'placeholder'}", original_address)
            if match:
                change = True

                tmp_ward_key = match.group()

                if ward_key == 'haianh' and tmp_ward_key == 'haian' and not 'haianhuyen' in c_address:
                    change = False

                if change:
                    ward_key = tmp_ward_key


        #print('Sau khi double check ward:', ward_key)


        ward_data = ward_keys[ward_key]

        duplicated_ward_keys = DICT_duplicated_ward_keys.get(admin_unit.province_english, {}).get(admin_unit.district_english, {})
        # To avoid wrong data input for unique wards in a district, just get the first item

        #print('duplicated_ward_keys:', duplicated_ward_keys)

        ward_entry = None
        if not (ward_key in duplicated_ward_keys):
            ward_entry = ward_data[next(iter(ward_data))]
            #print('Không nằm trong duplicated ward')


        else:
            #print('Có nằm trong duplicated ward')
            short_names = duplicated_ward_keys.get(ward_key, {})
            #print('short_names:', short_names)
            short_name = None
            if len(short_names) == 1:
                short_name = next(iter(short_names))
            else:
                match = re.search(rf"{'|'.join(short_names)}", address.title(), flags=re.IGNORECASE)
                if match:
                    short_name = match.group()

            #print('shortname:', short_name)

            ward_level = None
            if short_name:
                # Default
                ward_level = short_names.get(short_name, {}).get('default')
                if short_names.get(short_name, {}).get('total') != 1:
                    if re.search(rf'xa{ward_key}|{ward_key}commune|x\.{ward_key}', c_address):
                        ward_level = 'Commune'
                    elif re.search(rf'phuong{ward_key}|{ward_key}ward|p\.{ward_key}', c_address):
                        ward_level = 'Ward'
                    elif re.search(rf'thitran{ward_key}|{ward_key}town|tt\.{ward_key}', c_address):
                        ward_level = 'Town'

            #print('ward_level:', ward_level)

            if short_name and ward_level:
                ward_entry = DICT_duplicated_ward_map.get(admin_unit.province_english, {}).get(admin_unit.district_english, {}).get(short_name, {}).get(ward_level, {})




        # With duplicated ward_keys in a district, we need to find the prefix (suffix) to choose the ward level.
        # This problem only occurs with Xã, Phường, Thị Trấn.
        # else:
        #     if re.search(r'xa|Commune|x\.', c_address):
        #         ward_level = 'Commune'
        #     elif re.search(r'phuong|ward|p\.', c_address):
        #         ward_level = 'Ward'
        #     elif re.search(r'thitran|town|tt\.', c_address):
        #         ward_level = 'Town'
        #     else:
        #         # If level is not found, we have default level based on Google Trend
        #         ward_level = duplicated_ward_keys[ward_key]
        #
        #     ward_entry = ward_data[ward_level]

        if ward_entry:
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


if __name__ == '__main__':
    True
    print(parse_address('Thượng Cát, Từ Liêm, Hà Nội'))