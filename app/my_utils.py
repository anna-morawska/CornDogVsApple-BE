from functools import wraps
from flask import request, abort
from app import app


def limit_content_length(max_length):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            content_length = request.content_length
            if content_length is not None and content_length > max_length:
                abort(413, 'Maximum size of file upload is 4MB.')
            return f(*args, **kwargs)
        return wrapper
    return decorator

def has_allowed_extension(filename):
    if not "." in filename:
        return False
    if filename.rsplit('.', 1)[1].upper() not in app.config['ALLOWED_IMAGE_EXTENSIONS']:
        return False
    return True

def validate_image(file):
    if not file:
        return [False, "Please provide image file"]
    if not file.filename:
        return [False, "Image must have a filename"]
    if not has_allowed_extension(file.filename):
        return [False, "That image extension is not allowed"]
    else: 
        return [True, ""]