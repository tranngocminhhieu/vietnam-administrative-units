# Vietnam administrative units 🇻🇳


## Dataset
Download: [vietnam_administrative_units.csv](data%2Foutput%2Fvietnam_administrative_units.csv).

Last updated at: 2024-09-17.
## Python package: vietadminunits

### Installation
#### Install from GitHub
```shell
pip install --upgrade git+https://github.com/tranngocminhhieu/vietnam-administrative-units.git
```


### Parse address
```python
from vietadminunits import parse_address

address = 'Cuối đường kiều mai, dự án bệnh viện hạnh phúc phường phú diễn quận bắc từ liêm HN'

admin_unit = parse_address(address=address, level=3)

print(admin_unit)
```
Output:
```text
AdministrativeUnit:
Attribute                      | Value                         
--------------------------------------------------------------
province                       | Hà Nội                        
district                       | Bắc Từ Liêm                   
ward                           | Phú Diễn                      
--------------------------------------------------------------
long_province                  | Thành phố Hà Nội              
long_district                  | Quận Bắc Từ Liêm              
long_ward                      | Phường Phú Diễn               
--------------------------------------------------------------
short_district                 | Bắc Từ Liêm                   
short_ward                     | Phú Diễn                      
--------------------------------------------------------------
province_english               | Ha Noi                        
district_english               | Bac Tu Liem                   
ward_english                   | Phu Dien                      
--------------------------------------------------------------
long_province_english          | Ha Noi City                   
long_district_english          | Bac Tu Liem District          
long_ward_english              | Phu Dien Ward                 
--------------------------------------------------------------
short_district_english         | Bac Tu Liem                   
short_ward_english             | Phu Dien                      
--------------------------------------------------------------
district_level                 | Quận                          
ward_level                     | Phường                        
--------------------------------------------------------------
district_level_english         | District                      
ward_level_english             | Ward                          
```

```python
print(admin_unit.ward, admin_unit.district, admin_unit.province, sep=', ')
```
Output:
```text
Phú Diễn, Bắc Từ Liêm, Hà Nội
```

### Get data from Vietnam administrative units

```python
from vietadminunits import get_data
import pandas as pd

data = get_data(fields='*')
df = pd.DataFrame(data)

df.head()
```
Output:
```text
|    | province   | district   | ward      | long_province    | long_district   | long_ward        | short_district   | short_ward   | province_english   | district_english   | ward_english   | long_province_english   | long_district_english   | long_ward_english   | short_district_english   | short_ward_english   | district_level   | ward_level   | district_level_english   | ward_level_english   |
|---:|:-----------|:-----------|:----------|:-----------------|:----------------|:-----------------|:-----------------|:-------------|:-------------------|:-------------------|:---------------|:------------------------|:------------------------|:--------------------|:-------------------------|:---------------------|:-----------------|:-------------|:-------------------------|:---------------------|
|  0 | Hà Nội     | Ba Đình    | Phúc Xá   | Thành phố Hà Nội | Quận Ba Đình    | Phường Phúc Xá   | Ba Đình          | Phúc Xá      | Ha Noi             | Ba Dinh            | Phuc Xa        | Ha Noi City             | Ba Dinh District        | Phuc Xa Ward        | Ba Dinh                  | Phuc Xa              | Quận             | Phường       | District                 | Ward                 |
|  1 | Hà Nội     | Ba Đình    | Trúc Bạch | Thành phố Hà Nội | Quận Ba Đình    | Phường Trúc Bạch | Ba Đình          | Trúc Bạch    | Ha Noi             | Ba Dinh            | Truc Bach      | Ha Noi City             | Ba Dinh District        | Truc Bach Ward      | Ba Dinh                  | Truc Bach            | Quận             | Phường       | District                 | Ward                 |
|  2 | Hà Nội     | Ba Đình    | Vĩnh Phúc | Thành phố Hà Nội | Quận Ba Đình    | Phường Vĩnh Phúc | Ba Đình          | Vĩnh Phúc    | Ha Noi             | Ba Dinh            | Vinh Phuc      | Ha Noi City             | Ba Dinh District        | Vinh Phuc Ward      | Ba Dinh                  | Vinh Phuc            | Quận             | Phường       | District                 | Ward                 |
|  3 | Hà Nội     | Ba Đình    | Cống Vị   | Thành phố Hà Nội | Quận Ba Đình    | Phường Cống Vị   | Ba Đình          | Cống Vị      | Ha Noi             | Ba Dinh            | Cong Vi        | Ha Noi City             | Ba Dinh District        | Cong Vi Ward        | Ba Dinh                  | Cong Vi              | Quận             | Phường       | District                 | Ward                 |
|  4 | Hà Nội     | Ba Đình    | Liễu Giai | Thành phố Hà Nội | Quận Ba Đình    | Phường Liễu Giai | Ba Đình          | Liễu Giai    | Ha Noi             | Ba Dinh            | Lieu Giai      | Ha Noi City             | Ba Dinh District        | Lieu Giai Ward      | Ba Dinh                  | Lieu Giai            | Quận             | Phường       | District                 | Ward                 |
```
