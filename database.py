import logging

def get_random_photo():
    logging.debug('Database: Querying random cat photo')
    return "http://cat-photo-api.com.cat/photos/whiskers_on_pillow.jpg"

def upload_photo(file):
    logging.debug(f'Upload: Received file: {file.filename}')
    return True

def get_recent_photos():
    logging.debug('Database: Querying recent cat photos')
    return [
        "http://cat-photo-api.com.cat/photos/sleepy_cat.jpg",
        "http://cat-photo-api.com.cat/photos/playful_kitten.jpg",
        "http://cat-photo-api.com.cat/photos/grumpy_cat.jpg",
        "http://cat-photo-api.com.cat/photos/happy_cat.jpg",
        "http://cat-photo-api.com.cat/photos/mysterious_cat.jpg"
    ]

def delete_photo(photo_id):
    logging.debug(f'Database: Deleting photo with ID: {photo_id}')
    return True

def update_photo(photo_id, file):
    logging.debug(f'Database: Updating photo with ID: {photo_id}')
    return False  # Simulate permission denied error
