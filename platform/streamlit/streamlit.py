import streamlit as st
import pandas as pd
import numpy as np
from joblib import load
from sklearn.tree import DecisionTreeRegressor
import json

st.title("Housing Price Predictor")

price_label = "Estimated Price:"

columns = [
    "year_built",
    "baths_full",
    "baths_half",
    "lot_sqft",
    "sqft",
    "garage",
    "stories",
    "beds",
    "Tract",
    "Pct_1Car",
    "Pct_2Car",
    "PopulationDensity",
    "EmploymentDensity",
    "JobsNearby",
    "EmploymentEntropy",
    "Walkability",
    "sold_year",
    "sold_month",
    "sold_day",
    "type_commercial",
    "type_condo",
    "type_farm",
    "type_government",
    "type_industrial",
    "type_mobile",
    "type_multi_family",
    "type_other",
    "type_single_family",
    "type_townhomes",
    "city_Acworth",
    "city_Atlanta",
    "city_Bainbridge",
    "city_Bartow",
    "city_Bloomingdale",
    "city_Bronwood",
    "city_Brookhaven",
    "city_Brooks",
    "city_Buford",
    "city_Carrollton",
    "city_Chamblee",
    "city_Cleveland",
    "city_Cohutta",
    "city_Collins",
    "city_Colquitt",
    "city_Concord",
    "city_East Ellijay",
    "city_Eden",
    "city_Elberton",
    "city_Ellijay",
    "city_Enigma",
    "city_Flowery Branch",
    "city_Ga",
    "city_Griffin",
    "city_Hahira",
    "city_Hamilton",
    "city_Helen",
    "city_Hinesville",
    "city_Hull",
    "city_Jesup",
    "city_Jonesboro",
    "city_Kennesaw",
    "city_Lake Spivey",
    "city_Lenox",
    "city_Lincolnton",
    "city_Lithonia",
    "city_Louisville",
    "city_Lowndes",
    "city_Lyons",
    "city_Mableton",
    "city_Manassas",
    "city_Marietta",
    "city_Martin",
    "city_Milledgeville",
    "city_Mitchell",
    "city_Pembroke",
    "city_Pine Mountain",
    "city_Pineview",
    "city_Plainville",
    "city_Richmond Hill",
    "city_Ringgold",
    "city_Roopville",
    "city_Sandersville",
    "city_Sautee Nacoochee",
    "city_Savannah",
    "city_Smyrna",
    "city_Stonecrest",
    "city_Sugar Hill",
    "city_Thomaston",
    "city_Tiger",
    "city_Twin City",
    "city_Valdosta",
    "city_Waco",
    "city_Whigham",
    "city_Wrens",
    "city_Yatesville",
]

cities = [
    "Acworth",
    "Atlanta",
    "Bainbridge",
    "Bartow",
    "Bloomingdale",
    "Bronwood",
    "Brookhaven",
    "Brooks",
    "Buford",
    "Carrollton",
    "Chamblee",
    "Cleveland",
    "Cohutta",
    "Collins",
    "Colquitt",
    "Concord",
    "East Ellijay",
    "Eden",
    "Elberton",
    "Ellijay",
    "Enigma",
    "Flowery Branch",
    "Ga",
    "Griffin",
    "Hahira",
    "Hamilton",
    "Helen",
    "Hinesville",
    "Hull",
    "Jesup",
    "Jonesboro",
    "Kennesaw",
    "Lake Spivey",
    "Lenox",
    "Lincolnton",
    "Lithonia",
    "Louisville",
    "Lowndes",
    "Lyons",
    "Mableton",
    "Manassas",
    "Marietta",
    "Martin",
    "Milledgeville",
    "Mitchell",
    "Pembroke",
    "Pine Mountain",
    "Pineview",
    "Plainville",
    "Richmond Hill",
    "Ringgold",
    "Roopville",
    "Sandersville",
    "Sautee Nacoochee",
    "Savannah",
    "Smyrna",
    "Stonecrest",
    "Sugar Hill",
    "Thomaston",
    "Tiger",
    "Twin City",
    "Valdosta",
    "Waco",
    "Whigham",
    "Wrens",
    "Yatesville",
]

types = [
    "Commercial",
    "Condo",
    "Farm",
    "Government",
    "Industrial",
    "Mobile",
    "Multi Family",
    "Other",
    "Single Family",
    "Townhomes",
]

city_data = json.load(open("platform/streamlit/cities.json", "r"))


@st.cache_data
def load_model():
    return load("platform/streamlit/model.joblib")


def calculate_price(
    sold_date,
    year_built,
    baths_full,
    baths_half,
    lot_sqft,
    sqft,
    garage,
    stories,
    beds,
    type_,
    city,
    tract,
    pct_1car,
    pct_2car,
    population_density,
    employment_density,
    jobs_nearby,
    employment_entropy,
    walkability,
):
    param_dict = {
        "year_built": year_built,
        "baths_full": baths_full,
        "baths_half": baths_half,
        "lot_sqft": lot_sqft,
        "sqft": sqft,
        "garage": garage,
        "stories": stories,
        "beds": beds,
        "Tract": tract,
        "Pct_1Car": pct_1car,
        "Pct_2Car": pct_2car,
        "PopulationDensity": population_density,
        "EmploymentDensity": employment_density,
        "JobsNearby": jobs_nearby,
        "EmploymentEntropy": employment_entropy,
        "Walkability": walkability,
        "sold_year": sold_date.year,
        "sold_month": sold_date.month,
        "sold_day": sold_date.day,
        "type_commercial": 1 if type_ == "Commercial" else 0,
        "type_condo": 1 if type_ == "Condo" else 0,
        "type_farm": 1 if type_ == "Farm" else 0,
        "type_government": 1 if type_ == "Government" else 0,
        "type_industrial": 1 if type_ == "Industrial" else 0,
        "type_mobile": 1 if type_ == "Mobile" else 0,
        "type_multi_family": 1 if type_ == "Multi Family" else 0,
        "type_other": 1 if type_ == "Other" else 0,
        "type_single_family": 1 if type_ == "Single Family" else 0,
        "type_townhomes": 1 if type_ == "townhomes" else 0,
        "city_Acworth": 1 if city == "Acworth" else 0,
        "city_Atlanta": 1 if city == "Atlanta" else 0,
        "city_Bainbridge": 1 if city == "Bainbridge" else 0,
        "city_Bartow": 1 if city == "Bartow" else 0,
        "city_Bloomingdale": 1 if city == "Bloomingdale" else 0,
        "city_Bronwood": 1 if city == "Bronwood" else 0,
        "city_Brookhaven": 1 if city == "Brookhaven" else 0,
        "city_Brooks": 1 if city == "Brooks" else 0,
        "city_Buford": 1 if city == "Buford" else 0,
        "city_Carrollton": 1 if city == "Carrollton" else 0,
        "city_Chamblee": 1 if city == "Chamblee" else 0,
        "city_Cleveland": 1 if city == "Cleveland" else 0,
        "city_Cohutta": 1 if city == "Cohutta" else 0,
        "city_Collins": 1 if city == "Collins" else 0,
        "city_Colquitt": 1 if city == "Colquitt" else 0,
        "city_Concord": 1 if city == "Concord" else 0,
        "city_East Ellijay": 1 if city == "East Ellijay" else 0,
        "city_Eden": 1 if city == "Eden" else 0,
        "city_Elberton": 1 if city == "Elberton" else 0,
        "city_Ellijay": 1 if city == "Ellijay" else 0,
        "city_Enigma": 1 if city == "Enigma" else 0,
        "city_Flowery Branch": 1 if city == "Flowery Branch" else 0,
        "city_Ga": 1 if city == "Ga" else 0,
        "city_Griffin": 1 if city == "Griffin" else 0,
        "city_Hahira": 1 if city == "Hahira" else 0,
        "city_Hamilton": 1 if city == "Hamilton" else 0,
        "city_Helen": 1 if city == "Helen" else 0,
        "city_Hinesville": 1 if city == "Hinesville" else 0,
        "city_Hull": 1 if city == "Hull" else 0,
        "city_Jesup": 1 if city == "Jesup" else 0,
        "city_Jonesboro": 1 if city == "Jonesboro" else 0,
        "city_Kennesaw": 1 if city == "Kennesaw" else 0,
        "city_Lake Spivey": 1 if city == "Lake Spivey" else 0,
        "city_Lenox": 1 if city == "Lenox" else 0,
        "city_Lincolnton": 1 if city == "Lincolnton" else 0,
        "city_Lithonia": 1 if city == "Lithonia" else 0,
        "city_Louisville": 1 if city == "Louisville" else 0,
        "city_Lowndes": 1 if city == "Lowndes" else 0,
        "city_Lyons": 1 if city == "Lyons" else 0,
        "city_Mableton": 1 if city == "Mableton" else 0,
        "city_Manassas": 1 if city == "Manassas" else 0,
        "city_Marietta": 1 if city == "Marietta" else 0,
        "city_Martin": 1 if city == "Martin" else 0,
        "city_Milledgeville": 1 if city == "Milledgeville" else 0,
        "city_Mitchell": 1 if city == "Mitchell" else 0,
        "city_Pembroke": 1 if city == "Pembroke" else 0,
        "city_Pine Mountain": 1 if city == "Pine Mountain" else 0,
        "city_Pineview": 1 if city == "Pineview" else 0,
        "city_Plainville": 1 if city == "Plainville" else 0,
        "city_Richmond Hill": 1 if city == "Richmond Hill" else 0,
        "city_Ringgold": 1 if city == "Ringgold" else 0,
        "city_Roopville": 1 if city == "Roopville" else 0,
        "city_Sandersville": 1 if city == "Sandersville" else 0,
        "city_Sautee Nacoochee": 1 if city == "Sautee Nacoochee" else 0,
        "city_Savannah": 1 if city == "Savannah" else 0,
        "city_Smyrna": 1 if city == "Smyrna" else 0,
        "city_Stonecrest": 1 if city == "Stonecrest" else 0,
        "city_Sugar Hill": 1 if city == "Sugar Hill" else 0,
        "city_Thomaston": 1 if city == "Thomaston" else 0,
        "city_Tiger": 1 if city == "Tiger" else 0,
        "city_Twin City": 1 if city == "Twin City" else 0,
        "city_Valdosta": 1 if city == "Valdosta" else 0,
        "city_Waco": 1 if city == "Waco" else 0,
        "city_Whigham": 1 if city == "Whigham" else 0,
        "city_Wrens": 1 if city == "Wrens" else 0,
        "city_Yatesville": 1 if city == "Yatesville" else 0,
    }
    # return random between 50k and 1m for now
    model = load_model()
    return model.predict(pd.DataFrame(param_dict, index=[0]))


col1, col2 = st.columns(2)

with col1:
    sold_date = pd.to_datetime("today")
    city = st.selectbox("City", cities)
    type_ = st.selectbox("Type", types)
    built_date = st.number_input(
        "Year Built", value=2000, min_value=1900, max_value=2023, step=1
    )

    sqft = st.number_input("Square Footage", value=1500, min_value=0, max_value=999999)

    lot_sqft = st.number_input(
        "Lot Square Footage", value=5000, min_value=0, max_value=999999
    )
with col2:
    beds = st.number_input("Number of Bedrooms", value=3, min_value=0, max_value=99)
    baths_full = st.number_input(
        "Number of Full Baths", value=1, min_value=1, max_value=99, step=1
    )
    baths_half = st.number_input(
        "Number of Half Baths", value=0, min_value=0, max_value=99, step=1
    )

    garage = st.number_input(
        "Number of Garage Spaces", value=1, min_value=0, max_value=99
    )
    stories = st.number_input("Number of Stories", value=1, min_value=1, max_value=999)

tract = city_data[city]["Tract"]
pct_1car = city_data[city]["Pct_1Car"]
pct_2car = city_data[city]["Pct_2Car"]
population_density = city_data[city]["PopulationDensity"]
employment_density = city_data[city]["EmploymentDensity"]
jobs_nearby = city_data[city]["JobsNearby"]
employment_entropy = city_data[city]["EmploymentEntropy"]
walkability = city_data[city]["Walkability"]

num = calculate_price(
    sold_date,
    built_date,
    baths_full,
    baths_half,
    lot_sqft,
    sqft,
    garage,
    stories,
    beds,
    type_,
    city,
    tract,
    pct_1car,
    pct_2car,
    population_density,
    employment_density,
    jobs_nearby,
    employment_entropy,
    walkability,
)

st.metric(price_label, value=f"${int(num[0]):,}")

# Make callback
