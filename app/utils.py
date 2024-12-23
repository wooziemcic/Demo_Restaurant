import requests
from flask import current_app

""" def search_restaurants(lat, lon, query="restaurant", limit=10, preferences=None):
    
    #Search for nearby restaurants using Nominatim API and filter based on preferences.
    #:param lat: Latitude of the location.
    #:param lon: Longitude of the location.
    #:param query: Search query (default is "restaurant").
    #:param limit: Maximum number of results to return.
    #:param preferences: Dictionary containing cuisine and allergies to filter results.
    #:return: List of filtered restaurants.
    
    base_url = "https://nominatim.openstreetmap.org/search.php"
    params = {
        "q": f"{query} near {lat},{lon}",
        "format": "jsonv2",
        "limit": limit
    }
    headers = {
        "User-Agent": "RestaurantRecommender/1.0 (your_email@example.com)"
    }

    try:
        # Fetch results from the API
        response = requests.get(base_url, params=params, headers=headers)
        if response.status_code != 200:
            return {"error": f"API request failed with status {response.status_code}"}
        
        results = response.json()

        # Debugging: Log raw results
        print("Raw Results:", results)

        # Apply filters if preferences are provided
        if preferences:
            cuisine = preferences.get("cuisine", "").lower()
            allergies = preferences.get("allergies", [])

            # Debugging: Log preferences
            print("Filtering Preferences:", preferences)

            # Filter by cuisine
            if cuisine:
                results = [
                    place for place in results 
                    if cuisine in place.get("display_name", "").lower()
                ]

            # Filter by allergies
            # Since Nominatim doesn't provide ingredient data, we only filter by name as a fallback
            if allergies:
                results = [
                    place for place in results 
                    if not any(allergy in place.get("display_name", "").lower() for allergy in allergies)
                ]

        # Debugging: Log filtered results
        print("Filtered Results:", results)

        return results

    except Exception as e:
        return {"error": str(e)}
 """

def fetch_restaurants_from_foursquare(lat, lon, preferences=None, limit=10):
    """
    Fetch nearby restaurants using Foursquare Places API and filter based on preferences.
    """
    url = "https://api.foursquare.com/v3/places/search"
    headers = {
        "Authorization": "fsq3PIeaeuj46viOVT3jFRebvtQfmDoIp6DxIBponhp3xaA="
    }
    params = {
        "query": "restaurant",
        "ll": f"{lat},{lon}",
        "radius": 1000,
        "limit": limit
    }

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()

        # Parse the response
        data = response.json()
        restaurants = []
        cuisine = preferences.get("cuisine", "").lower() if preferences else ""
        allergies = preferences.get("allergies", []) if preferences else []

        for place in data.get("results", []):
            categories = [category["name"].lower() for category in place.get("categories", [])]

            # Debugging: Log categories
            print(f"Restaurant: {place['name']}, Categories: {categories}")

            # Filter by cuisine
            if cuisine and not any(cuisine in category for category in categories):
                print(f"Filtered Out (Cuisine): {place['name']} - No matching category for '{cuisine}'")
                continue

            # Format the restaurant data
            restaurants.append({
                "name": place["name"],
                "address": place["location"].get("address", "Unknown"),
                "categories": categories,
                "lat": place["geocodes"]["main"]["latitude"],
                "lon": place["geocodes"]["main"]["longitude"]
            })


        # Debugging: Log final results
        print(f"Filtered Restaurants: {restaurants}")

        return restaurants

    except requests.exceptions.HTTPError as e:
        return {"error": f"HTTPError: {e.response.status_code} - {e.response.text}"}
    except Exception as e:
        return {"error": str(e)}
