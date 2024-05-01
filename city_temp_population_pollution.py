import pandas as pd
import requests

# Load the dataset
df = pd.read_excel('city_water_body_temp.xlsx')
df.head()
def remove_dash(string):
  return string.replace("-"," ")
df['city'] = df['city'].apply(remove_dash)
import requests
# Simplifying the dataset for this example
df['Population'] = None  # Initialize the population column with None

# Assuming that the dataset has columns 'City' and 'pollution_level'
cities = df['city'].unique()
print("city",cities)
# Function to get data for a city including its human population and water pollution
def get_city_data(city_name, api_key):
    api_url = f'https://api.api-ninjas.com/v1/city?name={city_name}'
    response = requests.get(api_url, headers={'X-Api-Key': api_key})
    if response.status_code == requests.codes.ok and response.json() != []:
        city_info = response.json()[0]  # Assuming the first item in the response is the city info
        return city_info.get('population', 'Population data not available')
    else:
        return 'Population data not available'

# Replace 'YOUR_API_KEY' with your actual API key
api_key = 'Xel4GDUJF5R+qCZ3SzUx5w==VicUwc3FhpuNx5BJ'
for city in cities:
    # Fetching population data for each city and storing it in the DataFrame
    population_data = get_city_data(city, api_key)
    df.loc[df['city'] == city, 'Population'] = population_data

print(df)
df.to_excel('city_temp_population.xlsx',index=False)
df_water_pollution = pd.read_csv('USwaterpollutions.csv')
df_water_pollution.head()
def lowercase(string):
  return string.lower()
df_water_pollution['City'] = df_water_pollution['City'].apply(lowercase)
df_water_pollution.head()
df_water_pollution.rename(columns={"City":"city"},inplace=True)
df_merged = df.merge(df_water_pollution,on='city',how='inner')
df_merged.to_excel('city_temp_population_pollution_data.xlsx',index=False)


