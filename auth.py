import logging

def validate_api_key(request_key, valid_key):
    logging.debug(f'Auth: Validating API key: {request_key}')
    if request_key == valid_key:
        logging.info('Auth: API key validation successful')
        return True
    else:
        logging.error('Auth: API key validation failed')
        return False
