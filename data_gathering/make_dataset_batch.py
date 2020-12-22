import pandas as pd
import io
import json

import google_streetview.api as sv
import googlemaps


from redfin_houses.house_filter import HouseFilter, PropertyTypeEnum
from redfin_houses.redfin import query_house_list

import os
import csv


def zip_code_list(zipcode,params=None):
    return query_house_list('zipcode/{}'.format(zipcode),params)

def csv_to_df(csv_file):
	try:
		return pd.read_csv(io.StringIO(csv_file))
	except pd.errors.EmptyDataError:
		return pd.DataFrame()

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
	ZIPCODES = []
	with open('zipcode_list.csv','r') as csv_in:
		zc_reader = csv.reader(csv_in)
		for row in zc_reader:
			ZIPCODES.append(row[0])
	

	for ZIPCODE in ZIPCODES:
		try:
			os.mkdir('data_{}'.format(ZIPCODE))
		except FileExistsError:
			print('possibly overwriting')
		main(ZIPCODE)
