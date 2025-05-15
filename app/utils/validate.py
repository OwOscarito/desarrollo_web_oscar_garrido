import re
import filetype

# Generic string validator
def validate_string(string, min_length=0, max_length=100):
    if min_length <= len(string) <= max_length:
        return True
    return False

# Where
def validate_location(region, com):
    if not region or not com:
        return False
    
    return 

def validate_sector(sector):
    return validate_string(sector, 0, 100)

def validate_name(name):
    if not name:
        return False
    return validate_string(name, 1, 200)

def validate_email(email):
    EMAIL_REGEX = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

    if not email:
        return False
    if not validate_string(email, 1, 100):
        return False
    return re.match(EMAIL_REGEX, email)



def validate_img(img):
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


