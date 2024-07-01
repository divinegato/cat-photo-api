from flask import Flask, request, jsonify
import logging
from auth import validate_api_key
from database import get_random_photo, upload_photo, get_recent_photos, delete_photo, update_photo

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG,
                    format='[%(asctime)s] [%(levelname)s] [%(module)s] %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

API_KEY = "temp"

@app.route('/api/photos/random', methods=['GET'])
def get_random_cat_photo():
    logging.debug('Request: GET /api/photos/random')
    if not validate_api_key(request.headers.get('API-Key'), API_KEY):
        logging.error('Auth: API key validation failed: Key expired')
        return jsonify({'error': 'Unauthorized'}), 401
    photo = get_random_photo()
    if photo:
        return jsonify({'url': photo}), 200
    else:
        logging.error('Database: Failed to retrieve photo: No documents found')
        return jsonify({'error': 'Not Found'}), 404

@app.route('/api/photos/upload', methods=['POST'])
def upload_cat_photo():
    # TODO

@app.route('/api/photos/recent', methods=['GET'])
def get_recent_cat_photos():
    logging.debug('Request: GET /api/photos/recent')
    if not validate_api_key(request.headers.get('API-Key'), API_KEY):
        logging.error('Auth: API key validation failed')
        return jsonify({'error': 'Unauthorized'}), 401
    photos = get_recent_photos()
    return jsonify({'urls': photos}), 200

@app.route('/api/photos/<photo_id>', methods=['DELETE'])
def delete_cat_photo(photo_id):
    logging.debug(f'Request: DELETE /api/photos/{photo_id}')
    if not validate_api_key(request.headers.get('API-Key'), API_KEY):
        logging.error('Auth: API key validation failed')
        return jsonify({'error': 'Unauthorized'}), 401
    if delete_photo(photo_id):
        return jsonify({'success': True}), 200
    else:
        return jsonify({'error': 'Not Found'}), 404

@app.route('/api/photos/<photo_id>', methods=['PUT'])
def update_cat_photo(photo_id):
    # TODO
  
@app.route('/api/status', methods=['GET'])
def get_status():
    logging.debug('Request: GET /api/status')
    if not validate_api_key(request.headers.get('API-Key'), API_KEY):
        logging.error('Auth: API key validation failed')
        return jsonify({'error': 'Unauthorized'}), 401
    logging.info('Server: Service status: All systems operational')
    return jsonify({'status': 'All systems operational'}), 200

if __name__ == '__main__':
    app.run(port=8080)
