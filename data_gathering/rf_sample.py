import pandas as pd 
import io 

from redfin_houses.house_filter import HouseFilter, PropertyTypeEnum, PriceEnum, SqftEnum, BathEnum, LotEnum
from redfin_houses.redfin import query_house_list

def zip_code_list(zipcode,params=None):
    return query_house_list('zipcode/{}'.format(zipcode),params)

def csv_to_df(csv_file):
    return pd.read_csv(io.StringIO(csv_file))

my_params = HouseFilter(property_type_list=[PropertyTypeEnum.HOUSE],max_price=PriceEnum.PRICE_900k)

zipcode = 20176

my_list = zip_code_list(zipcode,params=my_params)
print(my_list)
my_df = csv_to_df(my_list)

print(my_df.columns)