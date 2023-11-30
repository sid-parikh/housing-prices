import pandas as pd
import json

df = pd.read_csv('./data.csv')
df = df.drop_duplicates(subset=['city'])
df = df.drop(columns=['property_id', 'is_new_construction', 'is_for_rent', 'is_subdivision', 'is_contingent', 'is_price_reduced', 'is_pending', 'is_foreclosure', 'is_plan', 'is_coming_soon', 'is_new_listing', 'year_built', 'baths_3qtr', 'sold_date', 'sold_price', 'baths_full', 'name', 'baths_half', 'lot_sqft', 'sqft', 'baths', 'sub_type', 'baths_1qtr', 'garage', 'stories', 'beds', 'type', 'list_date', 'list_price', 'status', 'postal_code', 'state', 'state_code', 'county', 'address_line', 'latitude', 'longitude', 'tags'])
j = df.set_index('city').to_json('cities.json', orient='index')

df.to_csv('data_two.csv', index=False)