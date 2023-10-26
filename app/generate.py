from itsdangerous import URLSafeTimedSerializer, SignatureExpired, BadData
from app.config import Config

secret_key = Config.SECRET_KEY

s = URLSafeTimedSerializer(secret_key)


def confirm_token(token, expiration=3600):
    try:
        email = s.loads(token, salt='email-confirm', max_age=expiration)
        return email
    except SignatureExpired:
        # Token has expired
        return None
    except BadData:
        # Token is invalid or has been tampered with
        return None


def verify_reset_token(token, expiration=3600):
    try:
        email = s.loads(token, salt='reset-password', max_age=expiration)  # Max token age of 1800 seconds (30 minutes)
        return email
    except SignatureExpired:
        # Token has expired
        return None
    except BadData:
        # Token is invalid
        return None