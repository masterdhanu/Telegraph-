import os

ENVIRONMENT = bool(os.environ.get('ENVIRONMENT', False))

if ENVIRONMENT:
    try:
        API_ID = int(os.environ.get('API_ID', 0))
    except ValueError:
        raise Exception("Your API_ID is not a valid integer.")
    API_HASH = os.environ.get('API_HASH', None)
    BOT_TOKEN = os.environ.get('BOT_TOKEN', None)
    try:
        OWNER_ID = int(os.environ.get('OWNER_ID', 0))
    except ValueError:
        raise Exception("Your OWNER_ID is not a valid integer.")
    DATABASE_URL = os.environ.get('DATABASE_URL', None)
    DATABASE_URL = DATABASE_URL.replace("postgres", "postgresql")  # Sqlalchemy dropped support for "postgres" name.
    # https://stackoverflow.com/questions/62688256/sqlalchemy-exc-nosuchmoduleerror-cant-load-plugin-sqlalchemy-dialectspostgre
    MUST_JOIN = os.environ.get('MUST_JOIN', None)
    if MUST_JOIN.startswith("@"):
        MUST_JOIN = MUST_JOIN.replace("@", "")
else:
    # Fill the Values
    API_ID = 10434273
    API_HASH = "526aef9b5156f182c7887fa7ba63c7b5"
    BOT_TOKEN = "6391255953:AAFzo4wHRCuRwkGFxH5nOeDThglYAgR7TX4"
    DATABASE_URL = "postgres://orarhqso:gnhzffTPci-6LRRmF0qwyAgktu-Dy7Gz@manny.db.elephantsql.com/orarhqso"
    MUST_JOIN = "WaifuSnatcherbotSupport"
    OWNER_ID = 1749188073
