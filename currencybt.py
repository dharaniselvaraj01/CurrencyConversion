 
currency_list = ['AUD','CAD','CNY','CZK','DKK','EUR','GBP','JPY','NOK','NZD','USD']

dir_pair_dict = {("AUD", "USD"): 0.8371,
            ("CAD", "USD"): 0.8711,
            ("USD", "CNY"): 6.1715,
            ("EUR", "USD"): 1.2315,
            ("GBP", "USD"): 1.5683,
            ("NZD", "USD"): 0.7750,
            ("USD", "JPY"): 119.95,
            ("EUR", "CZK"): 27.6028,
            ("EUR", "DKK"): 7.4405,
            ("EUR", "NOK"): 8.6651
            }

def create_inv_pair(dir_pair):
    inv_pair = {}
    for pair in dir_pair:
        rev_pair = tuple(reversed(pair))
        rate = dir_pair[pair]
        inv_pair[rev_pair] = round(1/rate,4)
    return inv_pair

def create_all_pair(pair1,pair2):
    all_pair = {**pair1,**pair2}
    return all_pair 


inv_pair_dict = create_inv_pair(dir_pair_dict)
all_pair = create_all_pair(dir_pair_dict,inv_pair_dict)

