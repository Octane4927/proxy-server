from flask import Flask, request, Response
import requests
import logging

app = Flask(__name__)

# Set up logging to see what's happening in the server
logging.basicConfig(level=logging.DEBUG)

@app.route('/<path:url>', methods=['GET'])
def proxy(url):
    try:
        # Add "http://" if not present in the URL
        if not url.startswith('http'):
            url = 'http://' + url
        
        # Log the URL being accessed
        app.logger.debug(f"Accessing URL: {url}")
        
        # Make the GET request to the target URL
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        
        # Log the response status
        app.logger.debug(f"Response status: {response.status_code}")
        
        # Return the content and headers from the response
        return Response(response.content, content_type=response.headers['Content-Type'])
    
    except Exception as e:
        app.logger.error(f"Error: {e}")
        return f"Error: {e}"

if __name__ == '__main__':
    # Change port to 10000 for Render compatibility
    app.run(host='0.0.0.0', port=10000, debug=True)
@app.route('/<path:url>', methods=['GET'])
def proxy(url):
    try:
        # Add "http://" if not present in the URL
        if not url.startswith('http'):
            url = 'http://' + url
        
        # Log the URL to check if it's being passed correctly
        app.logger.debug(f"Accessing URL: {url}")
        
        # Make the GET request to the target URL
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        
        # Return the content and headers from the response
        return Response(response.content, content_type=response.headers['Content-Type'])
    
    except Exception as e:
        return f"Error: {e}"


