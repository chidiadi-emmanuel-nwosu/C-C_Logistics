from itsdangerous import URLSafeTimedSerializer, SignatureExpired, BadData
import secrets

s = URLSafeTimedSerializer(secrets.token_hex(16))

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