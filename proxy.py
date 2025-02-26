from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route('/<path:url>')
def proxy(url):
    try:
        response = requests.get(f"http://{url}", headers={'User-Agent': 'Mozilla/5.0'})
        return Response(response.content, content_type=response.headers['Content-Type'])
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

