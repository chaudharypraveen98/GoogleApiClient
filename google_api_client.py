import requests
from urllib.parse import urlencode

GOOGLE_API_KEY = "ENTER YOUR OWN API KEY"


class GoogleMapsClient(object):
    lat = None
    lng = None
    data_type = "json"
    default_address = None
    api_key = None

    def __init__(self, api_key=None, default_address=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if api_key is None:
            raise Exception("Api key not found")
        self.api_key = api_key
        self.default_address = default_address
        if default_address is not None:
            self.get_url_and_log_lat()
        else:
            raise Exception("default address not set")

    def get_url_and_log_lat(self, location=None):
        loc_query = self.default_address
        if location is not None:
            loc_query = location
        base_url = f"https://maps.googleapis.com/maps/api/geocode/{self.data_type}"
        paramaters = {
            "address": loc_query,
            "key": self.api_key
        }
        url_params = urlencode(paramaters)
        endpoint = f"{base_url}?{url_params}"
        r = requests.get(endpoint)
        if r.status_code not in range(200, 299):
            return {}
        log_lat = {}
        try:
            log_lat = r.json()['results'][0]['geometry']['location']
            print(log_lat)
        except:
            pass
        self.lat = log_lat.get("lat")
        self.lng = log_lat.get("lng")
        return self.lat, self.lng

    def search(self, keyword="Mexican Food", location="Faridabad", radius=1000):
        if location is not None:
            self.get_url_and_log_lat(location)
        endpoint = f"https://maps.googleapis.com/maps/api/place/nearbysearch/{self.data_type}"
        search_param = {
            "key": self.api_key,
            "location": f"{self.lat},{self.lng}",
            "radius": radius,
            "keyword": keyword,
        }
        search_param_encode = urlencode(search_param)
        place_url = f"{endpoint}?{search_param_encode}"
        r = requests.get(place_url)
        if r.status_code not in range(200, 299):
            return {}
        return r.json()

    def detail(self, place_id="ChIJqW9BqQe6j4AR0il4CC315_s", fields=["name", "rating", "formatted_phone_number"]):
        detail_base_url = "https://maps.googleapis.com/maps/api/place/details/json"
        detail_param = {
            "place_id": place_id,
            "fields": ",".join(fields),
            "key": self.api_key,
        }
        detail_param_encode = urlencode(detail_param)
        detail_url = f"{detail_base_url}?{detail_param_encode}"
        r = requests.get(detail_url)
        if r.status_code not in range(200, 299):
            return {}
        return r.json()
