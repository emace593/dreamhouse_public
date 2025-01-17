import pandas as pd
import io
import json

import google_streetview.api as sv
import googlemaps


from redfin_houses.house_filter import HouseFilter, PropertyTypeEnum
from redfin_houses.redfin import query_house_list


def zip_code_list(zipcode,params=None):
    return query_house_list('zipcode/{}'.format(zipcode),params)

def csv_to_df(csv_file):
    return pd.read_csv(io.StringIO(csv_file))

def get_house_df(zipcode):

    # query for single-family homes
    my_params = HouseFilter(property_type_list=[PropertyTypeEnum.HOUSE])

    my_list = zip_code_list(zipcode,params=my_params)
    return csv_to_df(my_list)

def main(zipcode):

    homes = get_house_df(zipcode)

    home_json = {}

    # image size
    sz = '600x600'

    # API key
    ky = ''

    for idx, row in homes.iterrows():
            
        # setup metadata for json recording
        id = str(idx).zfill(5)
        pth = 'data/{}/gsv_0.jpg'.format(id)
        metadata = {key:row[key] for key in homes.columns}
        metadata['image_path'] = pth
        home_json[id] = metadata

        # setup params for image retrieval
        loc = '{},{}'.format(row['LATITUDE'],row['LONGITUDE'])
        params = [{'size':sz,'location':loc,'key':ky}]

        # retrieve image
        im = sv.results(params)
        im.download_links('data_{}/{}'.format(zipcode,id))

    with open('data_{}/metadata.json'.format(zipcode),'w') as json_out:
        json.dump(home_json,json_out,indent=4)




if __name__=="__main__":
    ZIPCODE = 20176
    main(ZIPCODE)
