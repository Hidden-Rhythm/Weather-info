from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import requests
import json

app = Flask(__name__)
CORS(app)

# API Configuration
API_KEY = "YOUR_WEATHERAPI_KEY_HERE"
BASE_URL = "http://api.weatherapi.com/v1"

@app.route('/')
def index():
    """Serve the main page"""
    return render_template('index.html')

@app.route('/api/weather', methods=['GET'])
def get_weather():
    """Fetch real-time weather data from WeatherAPI.com"""
    city = request.args.get('city', 'Gurgaon')
    
    try:
        # Current weather with real-time data
        current_url = f"{BASE_URL}/current.json?key={API_KEY}&q={city}&aqi=yes"
        current_response = requests.get(current_url, timeout=10)
        
        # Forecast
        forecast_url = f"{BASE_URL}/forecast.json?key={API_KEY}&q={city}&days=5&aqi=yes&alerts=yes"
        forecast_response = requests.get(forecast_url, timeout=10)
        
        if current_response.status_code == 200 and forecast_response.status_code == 200:
            current_data = current_response.json()
            forecast_data = forecast_response.json()
            
            # Debug: Print to console to verify real data
            print(f"✅ Real-time data fetched for: {city}")
            print(f"🌡️ Temperature: {current_data['current']['temp_c']}°C")
            print(f"💧 Humidity: {current_data['current']['humidity']}%")
            
            result = {
                'success': True,
                'current': current_data,
                'forecast': forecast_data
            }
            return jsonify(result)
        else:
            return jsonify({
                'success': False,
                'error': 'City not found. Please check the spelling.'
            }), 404
            
    except requests.exceptions.Timeout:
        return jsonify({
            'success': False,
            'error': '⏰ Request timeout. Please check your internet connection.'
        }), 408
    except requests.exceptions.ConnectionError:
        return jsonify({
            'success': False,
            'error': '📡 Connection error. Please check your internet connection.'
        }), 503
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'⚠️ Unexpected error: {str(e)}'
        }), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)