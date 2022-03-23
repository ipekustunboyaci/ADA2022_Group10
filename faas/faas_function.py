def closest_store(request):
    from geopy import distance

    def get_store_distances():
        from google.cloud import bigquery
        query = """
            SELECT *
            FROM `faas-345008.store_coordinates.test_store_coordinates`
            """

        client = bigquery.Client()

        query_job = client.query(query)
        stores_info_list = [{'store_id':row['store_id'], 'lat':row['lat'], 'lon':row['lon']}for row in query_job]
        return stores_info_list

    stores_info_list = get_store_distances()
    request_json = request.get_json()
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