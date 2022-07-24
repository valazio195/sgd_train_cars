import pandas as pd
import numpy as np
from sklearn import preprocessing

def feature_eng(data):
    data['ad_created'] = pd.to_datetime(data['ad_created'])
    data['date_crawled'] = pd.to_datetime(data['date_crawled'])
    data['last_seen'] = pd.to_datetime(data['last_seen'])

    data[["ad_created", "date_crawled", "last_seen"]].info()

    data['odometer'] = data['odometer'].str.replace("km", "")

    data['odometer'] = data['odometer'].str.replace(",", "")

    data['price'] = data['price'].str.replace("$", "")

    data['price'] = data['price'].str.replace(",", "")

    data[['price', 'odometer']] = data[['price', 'odometer']].astype('int64')

    data = data.drop(columns=['seller', 'offer_type'])

    data = data.drop(columns=['num_of_pictures'])

    data = data.drop(columns=['name', 'postal_code'])

    data = data[(data['price'] >= 500) & (data['price'] <= 40000)]


    for i in data.select_dtypes('object').columns:
        data[i].fillna(data[i].mode()[0], inplace=True)

    for j in data.select_dtypes('int64').columns:
        data[j].fillna(data[j].median(), inplace=True)
    
    col_norm = ['registration_year', 'power_ps', 'odometer', 'registration_month']

    data[col_norm] = normalize(X=data[col_norm])

    label1 = preprocessing.LabelEncoder()
    label2 = preprocessing.LabelEncoder()
    label3 = preprocessing.LabelEncoder()
    label4 = preprocessing.LabelEncoder()

    label1.fit(data['vehicle_type'].values)
    label2.fit(data['model'].values)
    label3.fit(data['fuel_type'].values)
    label4.fit(data['brand'].values)

    data['vehicle_type'] = label1.transform(data['vehicle_type'].values)
    data['model'] = label2.transform(data['model'].values)
    data['fuel_type'] = label3.transform(data['fuel_type'].values)
    data['brand'] = label4.transform(data['brand'].values)

    data['abtest'] = data['abtest'].replace({'control': 1, 'test': 0})
    data['gearbox'] = data['gearbox'].replace({'automatik': 1, 'manuell': 0})
    data['unrepaired_damage'] = data['unrepaired_damage'].replace({'ja': 1, 'nein': 0})
    