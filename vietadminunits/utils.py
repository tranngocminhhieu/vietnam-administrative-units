import re
from unidecode import unidecode

def to_key(text, level:int):
    if level not in range(1,4):
        raise ValueError('Level must be 1 (Province) or 2 (District) or 3 (Ward).')

    if not isinstance(text, str):
        return text

    c_text = unidecode(text).strip().lower()

    if level == 1:
        c_text = re.sub(r'^Tinh\s|^Thanh\sPho\s|TP\.', '', c_text, flags=re.IGNORECASE)

    if level == 2:
        if not re.search(r'^Quan\s\d{1,2}|^Quan\sBa$|^Quan\sHoa$|^Quan\sSon$', c_text, flags=re.IGNORECASE):
            c_text = re.sub(r'^Quan\s|^Huyen\s|^Thanh\sPho\s|TP\.|^Thi\sxa\s', '', c_text, flags=re.IGNORECASE)

    if level == 3:
        if not re.search(r'^Phuong\s\d{1,2}$|^phuong\slien$|^phuong\smai$|^phuong\sliet$|^phuong\scanh$|^phuong\sdinh$|^phuong\scach$|^phuong\strung$|^phuong\sduc$|^phuong\stu$|^phuong\sdo$|^phuong\sthien$|^phuong\stien$|^phuong\svien$|^phuong\slam$|^phuong\sgiao$|^phuong\sdong$|^phuong\snam$|^phuong\sson$|^phuong\slau$|^phuong\svi$|^phuong\skhoan$|^phuong\slieu$|^phuong\smao$|^phuong\sky$|^phuong\schieu$|^phuong\scong$|^phuong\snghi$|^phuong\ssai$|^phuong\shai$|^phuong\sthanh$|^phuong\sthinh$|^phuong\stra$|^phuong\sbinh$|^phuong\sphu$|^xa\sphin$|^xa\stong$|^xa\sdung$|^xa\sho$|^xa\sly$|^xa\sluong$|^xa\sbang$|^xa\sphien$', c_text, flags=re.IGNORECASE):
            c_text = re.sub(r'^phuong\s|^xa\s|^thi\stran\s', '', c_text, flags=re.IGNORECASE)

    c_text = re.sub(r"\-|\'|\s0|\s", '', c_text)

    return c_text

if __name__ == '__main__':
    print(to_key('Phường Phú Trinh', level=3))
    print(to_key('Phường 5', level=3))
    print(to_key('Quận 3', level=2))
    print(to_key('Quận Ba Đình', level=2))


    print('Finding mistake prefixes')
    from vietadminunits.datasets import get_data
    import pandas as pd
    df = pd.DataFrame(get_data())
    print('Province:', df[df.province_english.str.contains('^Tinh')]['province_english'].unique().tolist())
    print('District:', df[df.district_english.str.contains('^Quan\s|^Huyen\s')]['district_english'].unique().tolist())
    print('Ward:' ,df[df.ward_english.fillna('').str.contains('^Phuong\s|^Xa\s')]['ward_english'].unique().tolist())