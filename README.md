# Vietnam administrative units 🇻🇳

This project provides a dataset and Python package to parse and extract administrative units from Vietnamese addresses. It includes data for provinces, districts, and wards, with translations and various formats for both Vietnamese and English.

## Dataset
The dataset contains detailed information about administrative units in Vietnam. You can download it here:

[**vietnam_administrative_units.csv**](https://github.com/tranngocminhhieu/vietnam-administrative-units/blob/main/data/output/vietnam_administrative_units.csv)

**Last updated at**: 2024-09-17.
```text
| province   | district   | ward      | long_province    | long_district   | long_ward        | short_district   | short_ward   | province_english   | district_english   | ward_english   | long_province_english   | long_district_english   | long_ward_english   | short_district_english   | short_ward_english   | district_level   | ward_level   | district_level_english   | ward_level_english   |
|:-----------|:-----------|:----------|:-----------------|:----------------|:-----------------|:-----------------|:-------------|:-------------------|:-------------------|:---------------|:------------------------|:------------------------|:--------------------|:-------------------------|:---------------------|:-----------------|:-------------|:-------------------------|:---------------------|
| Hà Nội     | Ba Đình    | Phúc Xá   | Thành phố Hà Nội | Quận Ba Đình    | Phường Phúc Xá   | Ba Đình          | Phúc Xá      | Ha Noi             | Ba Dinh            | Phuc Xa        | Ha Noi City             | Ba Dinh District        | Phuc Xa Ward        | Ba Dinh                  | Phuc Xa              | Quận             | Phường       | District                 | Ward                 |
| Hà Nội     | Ba Đình    | Trúc Bạch | Thành phố Hà Nội | Quận Ba Đình    | Phường Trúc Bạch | Ba Đình          | Trúc Bạch    | Ha Noi             | Ba Dinh            | Truc Bach      | Ha Noi City             | Ba Dinh District        | Truc Bach Ward      | Ba Dinh                  | Truc Bach            | Quận             | Phường       | District                 | Ward                 |
| Hà Nội     | Ba Đình    | Vĩnh Phúc | Thành phố Hà Nội | Quận Ba Đình    | Phường Vĩnh Phúc | Ba Đình          | Vĩnh Phúc    | Ha Noi             | Ba Dinh            | Vinh Phuc      | Ha Noi City             | Ba Dinh District        | Vinh Phuc Ward      | Ba Dinh                  | Vinh Phuc            | Quận             | Phường       | District                 | Ward                 |
| Hà Nội     | Ba Đình    | Cống Vị   | Thành phố Hà Nội | Quận Ba Đình    | Phường Cống Vị   | Ba Đình          | Cống Vị      | Ha Noi             | Ba Dinh            | Cong Vi        | Ha Noi City             | Ba Dinh District        | Cong Vi Ward        | Ba Dinh                  | Cong Vi              | Quận             | Phường       | District                 | Ward                 |
| Hà Nội     | Ba Đình    | Liễu Giai | Thành phố Hà Nội | Quận Ba Đình    | Phường Liễu Giai | Ba Đình          | Liễu Giai    | Ha Noi             | Ba Dinh            | Lieu Giai      | Ha Noi City             | Ba Dinh District        | Lieu Giai Ward      | Ba Dinh                  | Lieu Giai            | Quận             | Phường       | District                 | Ward                 |
```


- **Source**: Wikipedia, danhmuchanhchinhgso.gov.vn.
- **Process**: Correcting typos, creating new fields.
- **Note**: With `district` and `ward` fields, default to short name, and long name when there are duplicated short names.

## Python package: vietadminunits

### Installation
#### Install from GitHub
```shell
pip install --upgrade git+https://github.com/tranngocminhhieu/vietnam-administrative-units.git
```

### Usage

#### Parse an address

```python
from vietadminunits import parse_address

address = 'p2 q5'

admin_unit = parse_address(address=address, level=3)

province = admin_unit.province
district = admin_unit.district
ward = admin_unit.ward
# ... and more attributes
```

- `address`: The address will give the best results when following the structure: ward > district > province.
- `level`: Specify the administrative level to parse. Must be one of the following:
  - `1` for Province.
  - `2` for District.
  - `3` for Ward. 

For best performance, if you only need to parse the province, set `level = 1`.

```python
print(admin_unit)
```

```text
AdministrativeUnit:
Attribute                      | Value                         
--------------------------------------------------------------
province                       | Hồ Chí Minh                   
district                       | Quận 5                        
ward                           | Phường 2                      
--------------------------------------------------------------
long_province                  | Thành phố Hồ Chí Minh         
long_district                  | Quận 5                        
long_ward                      | Phường 2                      
--------------------------------------------------------------
short_district                 | Quận 5                        
short_ward                     | Phường 2                      
--------------------------------------------------------------
province_english               | Ho Chi Minh                   
district_english               | District 5                    
ward_english                   | Ward 2                        
--------------------------------------------------------------
long_province_english          | Ho Chi Minh City              
long_district_english          | District 5                    
long_ward_english              | Ward 2                        
--------------------------------------------------------------
short_district_english         | District 5                    
short_ward_english             | Ward 2                        
--------------------------------------------------------------
district_level                 | Quận                          
ward_level                     | Phường                        
--------------------------------------------------------------
district_level_english         | District                      
ward_level_english             | Ward                          
```

#### Get datasets

```python
from vietadminunits import get_data
import pandas as pd

data = get_data(fields='*')
district_data = get_data(fields='province, district')

df = pd.DataFrame(data)
```

- `fields`: A list, or a string.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvement, feel free to open a pull request or issue on the [GitHub repository](https://github.com/tranngocminhhieu/vietnam-administrative-units).