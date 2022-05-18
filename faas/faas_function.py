# FaaS to determine nearest store using geocoding and lon lat calculations on resulting coordinates
def closest_store(request):

    from geopy import distance
    def get_address_coordinates(address: str):
        import requests

        # Bijltjespad%2068%20Amsterdam
        def format_address(address):
            without_commas = address.replace(',', ' ')
            without_dubble_space = without_commas.replace('  ', ' ').strip()
            replaced_spaces = without_dubble_space.replace(' ', '%20')
            return replaced_spaces

        api_key = <your own key>
        address_api_argument = format_address(address)
        url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address_api_argument}&key={api_key}"
        print(url)
        print(requests.get(url).json()['results'][0]['geometry']['location'])
        location = requests.get(url).json()['results'][0]['geometry']['location']
        coordinates = (location['lat'], location['lng'])
        return coordinates

    def get_store_locations():
        from google.cloud import bigquery
        query = """
            SELECT *
            FROM `ada-2022-349811.store_coords.coords`
            """

        client = bigquery.Client()

        query_job = client.query(query)
        stores_info_list = [{'store_id':row['store_id'], 'lat':row['lat'], 'lon':row['lon']}for row in query_job]
        return stores_info_list

    stores_info_list = get_store_locations()

    request_json = request.get_json()

    if 'address' in request_json:
        user_coordinates = get_address_coordinates(request_json['address'])
    else:
        user_lat = request_json['lat']
        user_lon = request_json['lon']
        user_coordinates = (user_lat, user_lon)
    
    
    shortest_distance = None
    closest_store = None
    for store_info in stores_info_list:
        store_coordinates = (store_info['lat'], store_info['lon'])
        current_distance = distance.distance(user_coordinates, store_coordinates).km
        if(not shortest_distance or shortest_distance > current_distance):
            shortest_distance = current_distance
            closest_store = store_info['store_id']
    return str(closest_store)

