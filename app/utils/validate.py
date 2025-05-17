import re
import filetype
from app.database import db
# Generic string validator
def valid_string(string, min_length=0, max_length=100):
    if min_length <= len(string) <= max_length:
        return True
    return False

# Where
def valid_location(region, com):
    if not region or not com:
        return False

    return True

def valid_sector(sector):
    if not sector:
        return True
    return valid_string(sector, 0, 100)
    
# Who
def valid_name(name):
    if not name:
        return False
    return valid_string(name, 1, 200)

def valid_email(email):
    EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if not email:
        return False
    if not valid_string(email, 1, 100):
        return False
    return re.match(EMAIL_REGEX, email)

def valid_phone(phone):
    PHONE_REGEX = r'^\+?[0-9]{7,15}$'

    if not phone:
        return True
    if not valid_string(phone, 1, 20):
        return False
    return re.match(PHONE_REGEX, phone)


def valid_img(img):
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "webp"}
    ALLOWED_MIMETYPES = {"image/jpeg", "image/png", "image/gif"}

    # check if a file was submitted
    if img is None:
        return False

    # check if the browser submitted an empty file
    if img.filename == "":
        return False
    
    # check file extension
    ftype_guess = filetype.guess(img)
    if ftype_guess.extension not in ALLOWED_EXTENSIONS:
        return False
    # check mimetype
    if ftype_guess.mime not in ALLOWED_MIMETYPES:
        return False
    return True

def validate_where(region, com, sector):
    if not region or not com:
        return False
    return True
