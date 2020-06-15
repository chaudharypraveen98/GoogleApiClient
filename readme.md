# **Google Map Api Client**

##### This is Api client is made by me for simple and quick integration. It will find places in a location such as parks, malls, hotels and much more. This provides methods to find the places based on place id and search places with with their some names.

### **How to setup the Api Client :-**
1. Make a project on Google Cloud Platfrom. Be sure to enable billing feature. It won't cost you untill you make thousand of requests. Then enable <a href="https://developers.google.com/maps/documentation/geocoding/start">GEOCODING API</a> and <a href="https://developers.google.com/places/web-service/intro">PLACES API</a> in your project section.
2. First run the `requirements.txt` to install the dependencies by the below code:-
<br>`python3 install -r requirements.txt`
3. Enter your own api key in **GOOGLE_API_KEY** in python code.
4. That's all, Hurray.

### **How to use the Api:**
1. **First make a object of the api class. Give a default address. You can add the For example** :-
<br>`client = GoogleMapsClient(api_key=GOOGLE_API_KEY,default_address="Enter_the_desired_location")`
2. **This Api provides two method:**
<br> - 2.1 Search places in a location
<br> - 2.2 Find a place using the Place ID.
3. **Using the Search places. Basic syntax** :-
<br>`client.search(keyword="ANYTHING",location="ANY",radius="")`
<br>It has three parameters:<br/>
<br> -**_keyword_**:It can be anything that you want to search like mall, hotel , restaurant, park and much more.
<br> -**_location_**: It can be anywhere. It is optional as it will search places in default_address.
<br> -**_radius_**: It is the radius of area to search. It is in meters and the default value is set as 1000. You can change it by giving value in parameter.<br/>
<br>sample example:-
<br>`client.search(keyword="mall",location="faridabad",radius=3000)`
4. **Using the Place method. Basic syntax** :-
<br>`client.detail(self, place_id="ENTER_THE_PLACE_ID", fields=[ENTER THE FIELD YOU WANT TO FIND])`
<br> Currently the google provide four fields:- "name", "rating", "formatted_phone_number". You can use anyone. Dont pass the field parameter if you want all the parameters as it is already intialized in the code
<br>sample example for all field:-
<br>`client.detail(place_id="ChIJqW9BqQe6j4AR0il4CC315_s")`
<br>sample example for particular field:-
<br>`client.detail(place_id="ChIJqW9BqQe6j4AR0il4CC315_s", fields=["name"])`


**Note** :-  This Api will give the json response.