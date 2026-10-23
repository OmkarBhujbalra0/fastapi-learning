import jwt
from datetime import datetime,timedelta,timezone
import base64
import json


SECRET_KEY = 'secretkeyforjwtpythonfileforauthentication'
ALGORITHM = 'HS256'


payload = {
    "sub": "student12345",
    "exp": datetime.now(timezone.utc) + timedelta(seconds=10)
}

token = jwt.encode(payload,SECRET_KEY,algorithm=ALGORITHM)

print(token)

try:
    decodedata = jwt.decode(token,SECRET_KEY,algorithms=ALGORITHM)
except jwt.ExpiredSignatureError:
    print("Token has expired.")

# tampering tokens

header, payload, signature = token.split('.')

data = json.loads(base64.urlsafe_b64decode(payload + "=="))
data['sub'] = "admin"
fake_payload = base64.urlsafe_b64encode(json.dumps(data).encode()).decode().rstrip("=")

fake_token = f"{header}.{fake_payload}.{signature}"

print(fake_token)

try:
    jwt.decode(fake_token,SECRET_KEY,algorithms=ALGORITHM)
except jwt.InvalidSignatureError:
    print("Forged Token Detected.")