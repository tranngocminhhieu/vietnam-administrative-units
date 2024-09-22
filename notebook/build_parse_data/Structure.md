# Part_1_base:
- DICT_long_province_alphanumerics `{'province alphanumeric': 'province key', ...}`
- DICT_long_district_alphanumerics `{'Province English': {'district alphanumeric': 'district key', ...}}`
- DICT_long_ward_alphanumerics `{'Province English': {'District English': {'long ward alphanumeric': 'ward key'}}}` 

- LIST_long_district_alphanumerics `['district alphanumeric', ...]`
- LIST_long_ward_alphanumerics `['long ward alphanumeric', ...]`

- LIST_province_keys_1 `['short province key', ...]`
- LIST_province_keys_2 `['short province key', ...]`
- LIST_province_keys_3 `['short province key', ...]`

- DICT_province_map `{'short province key': {'province': 'Hồ Chí Minh', 'long_province': 'Thành phố Hồ Chí Minh', ...}, ...}`
- DICT_district_map `{'Province English': {'district key': {'level english': {'district': 'Tân Bình', 'long_district': 'Quận Tân Bình', ...}}}}`
- DICT_ward_map `{'Province English':{'District English': {'ward key': {'level english': {'ward': 'Phú Trinh', 'long_ward': 'Phường Phú Trinh', ...}}}}}`

- LIST_duplicated_district_province_keys `['short province key', ...]`
- DICT_duplicated_district_keys `['short district key', ...]`

- LIST_duplicated_ward_district_keys `['short district key', ...]`
- DICT_duplicated_ward_keys `['short ward key', ...]`


- DICT_unique_long_district_alphanumerics `{'long_district_alphanumeric': 'province_key'}`
- DICT_not_unique_long_district_alphanumerics
- LIST_contains_province_key_long_district_alphanumerics
- DICT_unique_district_keys `{'district_key': 'province_key'}`
- DICT_not_unique_district_keys `{'district_key': {'province_key 1': ['ward key', ...], {'province_key 2': ['ward key', ...]}}`

- DICT_alias_province_keys `{'alias province key': 'province key', ...}`

# Part_2_alias:
- DICT_alias_district_keys `{'Province English': {'alias district key': 'district key'}}`
- DICT_half_district_keys `{'Province English': {'half district key': {'district key': ['ward key']}}}`

# Part_3_double_check:
- DICT_double_check_provinces `{'province key': ['province key', ...]}`
- DICT_double_check_districts `{'Province English': {'district key': ['district key', ...]}}`

