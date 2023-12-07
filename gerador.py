import secrets
import string
import app
def generate_secret_key(length=24):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for _ in range(length))

app.secret_key = generate_secret_key()
print(app.secret_key)
