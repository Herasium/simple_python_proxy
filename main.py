from flask import Flask, request, jsonify
import base64
import requests

app = Flask("app")

@app.route('/<path:encoded_url>', methods=['GET'])
def proxy(encoded_url):
    try:
        url = base64.urlsafe_b64decode(encoded_url).decode('utf-8')
        response = requests.get(url)
        return jsonify({
            'status_code': response.status_code,
            'data': response.text
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
