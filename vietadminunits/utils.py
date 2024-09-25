import re
from unidecode import unidecode

# We should update pattern if the dataset has been updated
province_prefix = re.compile('^(tinh|thanh\spho)\s|^tp\.', flags=re.IGNORECASE)
district_prefix = re.compile('^(quan|huyen|thi\sxa|thanh\spho)\s|^tp\.', flags=re.IGNORECASE)
district_exception = re.compile('^quan\s(\d{1,2}|ba|hoa|son)$', flags=re.IGNORECASE)
ward_prefix = re.compile(r'^(phuong|xa|huyen|thi\stran)\s', flags=re.IGNORECASE)
ward_exception = re.compile(r'^(phuong\s\d{1,2}|phuong\slien|phuong\smai|phuong\sliet|phuong\scanh|phuong\sdinh|phuong\scach|phuong\strung|phuong\sduc|phuong\stu|phuong\sdo|phuong\sthien|xa\sphin|phuong\stien|huyen\stung|phuong\svien|xa\stong|xa\sdung|xa\sho|phuong\slam|phuong\stien|phuong\sgiao|phuong\sdong|phuong\snam|phuong\sson|huyen\sson|xa\sly|phuong\sson|phuong\slau|phuong\svien|phuong\svi|phuong\skhoan|phuong\slieu|phuong\smao|phuong\sky|phuong\schieu|phuong\scong|phuong\sdinh|phuong\snghi|xa\sluong|phuong\sduc|phuong\ssai|phuong\sson|phuong\shai|xa\sbang|huyen\shoi|phuong\sthanh|phuong\sthinh|phuong\stra|phuong\sbinh|phuong\sphu|xa\sphien)$', flags=re.IGNORECASE)

def to_key(text, level:int):
    if level not in range(1,4):
        raise ValueError('Level must be 1 (Province) or 2 (District) or 3 (Ward).')

    if not isinstance(text, str):
        return text

    c_text = unidecode(text).strip().lower()

    if level == 1:
        c_text = province_prefix.sub('', c_text)
    if level == 2:
        if not district_exception.search(c_text):
            c_text = district_prefix.sub('', c_text)

    if level == 3:
        if not ward_exception.search(c_text):
            c_text = ward_prefix.sub('', c_text)

    c_text = re.sub(r"\s0|[^a-z0-9]", '', c_text)

    return c_text

def to_alphanumeric(text):
    if not isinstance(text, str):
        return text
    c_text = unidecode(text).strip().lower()
    c_text = re.sub(r'[^a-z0-9]', '', c_text)  # Loại bỏ tất cả ký tự không phải chữ thường hoặc số
    return c_text


alphanumeric_prefix = re.compile(pattern=r'^(quan|huyen|thixa|thanhpho|phuong|xa|thitran)', flags=re.IGNORECASE)
def abbreviate_alphanumeric_prefix(text):
    match = alphanumeric_prefix.search(text)
    prefix = match.group()
    abbreviations = {
        'quan': 'q.',
        'huyen': 'h.',
        'thixa': 'tt.',
        'thanhpho': 'tp.',
        'phuong': 'p.',
        'xa': 'x.',
        'thitran': 'tt.'
    }
    abbreviation = abbreviations[prefix]
    new_text = re.sub(rf"^{prefix}", abbreviation, text)
    return new_text


if __name__ == '__main__':
    print(to_key('Phường Phú Trinh', level=3))
    print(to_key('Phường 05', level=3))
    print(to_key('Quận 3', level=2))
    print(to_key('Quận Ba dinh', level=2))
    print(to_key('huyen son', level=3))


    # print('Finding mistake prefixes')
    # from vietadminunits.datasets import get_data
    # import pandas as pd
    # df = pd.DataFrame(get_data())
    # print('Province:', df[df.province_english.str.contains('^Tinh')]['province_english'].unique().tolist())
    # print('District:', df[df.district_english.str.contains('^Quan\s|^Huyen\s')]['district_english'].unique().tolist())
    # print('Ward:' ,df[df.ward_english.fillna('').str.contains('^Phuong\s|^Xa\s')]['ward_english'].unique().tolist())