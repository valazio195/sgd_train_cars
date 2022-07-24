import pandas as pd
import numpy as np

def read_data(PATH):
    '''
    Read data from dataset from path
   
    Parameters
    ----------
    PATH : str
        path source of training data, csv.
    
    Returns
    -------
    data : pd.DataFrame
        Data for modeling
    '''
    data = pd.read_csv(PATH)
    
    return data


def change_column(data):
    repl = {"dateCreated": "ad_created",
            "dateCrawled": "date_crawled",
            "fuelType": "fuel_type",
            "lastSeen": "last_seen",
            "monthOfRegistration": "registration_month",
            "notRepairedDamage": "unrepaired_damage",
            "nrOfPictures": "num_of_pictures",
            "offerType": "offer_type",
            "postalCode": "postal_code",
            "powerPS": "power_ps",
            "vehicleType": "vehicle_type",
            "yearOfRegistration": "registration_year",
            "camelCase": "snake_case"}

    data.rename(columns=repl, inplace=True)
    
    return data


def read_and_change(path):
    """Read and checking data."""
    print("start import data")
    data = read_data(path)
    print("done import data")
    print("start checking and set columns")
    data = change_column(data)
    print("done change")
    data = check_read_data_success(df)
    print("done checking read data success")
    return data