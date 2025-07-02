import re
import filetype
from datetime import datetime
from app.database import db

# Generic string validator
def valid_string(string, min_length=0, max_length=100):
    return (min_length <= len(string) <= max_length)

# Where
def valid_location(regionId, communeId):
    if not regionId or not communeId:
        return False
    print(f"regionId: {regionId}, communeId: {communeId}")
    region = db.get_region_by_id(regionId)
    commune = db.get_commune_by_id(communeId)
    print(f"region: {region}, commune: {commune}")
    if not region or not commune:
        return False
    if region.id != commune.region_id:
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
    PHONE_REGEX = r'^\+\d{3}\.\d{8}$'

    if not phone:
        return True
    if not valid_string(phone, 1, 20):
        return False
    return re.match(PHONE_REGEX, phone)

def valid_contact(contact_id):
    if not valid_string(contact_id, 4, 50):
        return False
    return True

def valid_date(date):
    if not date:
        return False
    try:
        date = datetime.strptime(date, '%Y-%m-%dT%H:%M')
    except ValueError:
        return False
    return True

def valid_end_date(start_date, end_date):
    if not start_date or not end_date:
        return False
    try:
        start_date = datetime.strptime(start_date, '%Y-%m-%dT%H:%M')
        end_date = datetime.strptime(end_date, '%Y-%m-%dT%H:%M')
    except ValueError:
        return False
    if start_date > end_date:
        return False
    return True

def valid_description(description):
    COLUMNS = 50
    ROWS = 10
    DESCRIPTION_LENGTH = COLUMNS * ROWS
    if not description:
        return True

    return valid_string(description, 0, DESCRIPTION_LENGTH)

def valid_other_topic(other_topic):
    return valid_string(other_topic, 3, 15)

def valid_topic(topic):
    if not topic:
        return False
    if topic not in db.Tema.__members__:
        return False
    return True

def valid_img(img):
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif", "webp"}
    ALLOWED_MIMETYPES = {"image/jpeg", "image/png", "image/gif", "image/webp"}
    # check if the file is empty
    if img is None:
        return True
    # check if the browser submitted an empty file
    if img.filename == "":
        return False
    
    # check file extension
    ftype_guess = filetype.guess(img)
    if ftype_guess is None:
        return False
    if ftype_guess.extension not in ALLOWED_EXTENSIONS:
        return False
    # check mimetype
    if ftype_guess.mime not in ALLOWED_MIMETYPES:
        return False
    return True

def valid_photos(photos):
    if len(photos) == 0:
        return False
    for photo in photos:
        if not valid_img(photo):
            return False
    return True


def valid_comment_name(name):
    if not name:
        return False
    if not valid_string(name, 3, 200):
        return False
    return True

def valid_comment_text(text):
    COLUMNS = 50
    ROWS = 4
    if not text:
        return False
    if not valid_string(text, 5, COLUMNS * ROWS):
        return False
    return True