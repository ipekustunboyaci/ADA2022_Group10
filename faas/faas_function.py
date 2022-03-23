def calc_store_distance(request):
    from geopy import distance

    def get_store_distances():
        from google.cloud import bigquery
        query = """
            SELECT *
            FROM `faas-345008.store_coordinates.test_store_coordinates`
            """

        client = bigquery.Client()

        query_job = client.query(query)
        store_info = [{'store_id':row['store_id'], 'lat':row['lat'], 'lon':row['lon']}for row in query_job]
        return store_info

    store_info = get_store_distances()
    request_json = request.get_json()
    user_lat = request_json['lat']
    user_lon = request_json['lon']
    
    user_coordinates = (user_lat, user_lon)
    store_coordinates = (store_info[0]['lat'], store_info[0]['lon'])
    result = distance.distance(user_coordinates, store_coordinates).km
    return result
