from flask import Blueprint, render_template, request, jsonify
from app.utils import fetch_restaurants_from_foursquare


main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('index.html', title="Home")


""" @main_bp.route('/restaurants', methods=['POST'])
def restaurants():
    try:
        data = request.json  # Parse incoming JSON data
        lat = data.get('lat')
        lon = data.get('lon')
        preferences = data.get('preferences', {})

        if not lat or not lon:
            return jsonify({"error": "Latitude and Longitude are required"}), 400

        # Call the utility function
        results = search_restaurants(lat, lon, preferences=preferences)
        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}), 500 """


@main_bp.route('/restaurants', methods=['POST'])
def restaurants():
    data = request.json
    lat = data.get('lat')
    lon = data.get('lon')
    preferences = data.get('preferences', {})

    print(f"Received Preferences: {preferences}")  # Debugging

    if not lat or not lon:
        return jsonify({"error": "Latitude and Longitude are required"}), 400

    results = fetch_restaurants_from_foursquare(lat, lon, preferences)
    print(f"Filtered Results: {results}")  # Debugging

    if "error" in results:
        return jsonify({"error": results["error"]}), 500

    return jsonify(results)