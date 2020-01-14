from multiprocessing import Pool, cpu_count
from sqlalchemy import create_engine
from geosupport import Geosupport, GeosupportError
import pandas as pd
import json
import os

g = Geosupport()

def geocode(input):
    # collect inputs
    #uid = input.pop('uid')
    hnum = input.pop('house_number')
    sname = input.pop('street_name')
    borough = input.pop('borough')

    try:
        geo = g['1B'](street_name=sname, house_number=hnum, borough=borough, mode='tpad')
        #print(geo)
    except GeosupportError as e:
        geo = e.result

    geo = parse_output(geo)
    geo.update(input)
    return geo

def parse_output(geo):
    bbl = geo.get('BOROUGH BLOCK LOT (BBL)', '')
    bbl10 = bbl.get('BOROUGH BLOCK LOT (BBL)', '')

    return dict(
        geo_hnum = geo.get('House Number - Display Format', ''),
        geo_sname = geo.get('First Street Name Normalized', ''),
        geo_borough = geo.get('First Borough Name', ''),
        geo_bbl = bbl10,
        geo_tpad_new_bin = geo.get('TPAD New BIN', ''),
        geo_tpad_new_bin_status = geo.get('TPAD New BIN Status', ''),
        geo_tpad_dm_bin_status = geo.get('TPAD BIN Status (for DM job)', ''),
        geo_tpad_conflict_flag = geo.get('TPAD Conflict Flag', ''),
        geo_tpad_bin_status = geo.get('TPAD BIN Status', ''),
        geo_return_code = geo.get('Geosupport Return Code (GRC)', ''),
        geo_return_code_2 = geo.get('Geosupport Return Code 2 (GRC 2)', ''),
        geo_message = geo.get('Message', ''),
        geo_message_2 = geo.get('Message 2', 'msg2 err'),
        geo_reason_code = geo.get('Reason Code', ''),
    )

if __name__ == '__main__':
    # connect to postgres db
    #recipe_engine = create_engine(os.environ['RECIPE_ENGINE'])
    engine = create_engine(os.environ['BUILD_ENGINE'])

    # read in housing table
    #df = pd.read_sql("SELECT job_number, job_number||status_date AS uid, address_house, address_street, boro,\
    #                    co_earliest_effectivedate, status_q, status_a, x_outlier\
    #                                  FROM developments WHERE co_earliest_effectivedate > ' ';", recipe_engine)
    df = pd.read_csv("input/housing-development.csv");
    df = df.loc[df['co_earliest_effectivedate'] > ' ']
    print(df.head())

    #get the row number
    df = df.rename(columns={'address_house':'house_number',
                            'address_street':'street_name',
                            'boro':'borough'})

    records = df.to_dict('records')

    print('geocoding begins here ...')
    # Multiprocess
    with Pool(processes=cpu_count()) as pool:
        it = pool.map(geocode, records, 10000)

    print('geocoding finished, dumping to postgres ...')
    pd.DataFrame(it).to_sql('housing_geocode', engine, if_exists='replace', chunksize=10000, index=False)
