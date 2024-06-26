import pyotp

# Replace with your actual email
email = "your-email@example.com"

# Shared secret is email + "HENNGECHALLENGE003"
shared_secret = email + "HENNGECHALLENGE003"

# Generate TOTP password
totp = pyotp.TOTP(shared_secret, digits=10, digest='sha512')
totp_password = totp.now()

print("Generated TOTP Password:", totp_password)
