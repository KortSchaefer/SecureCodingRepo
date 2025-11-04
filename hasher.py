import hashlib
from secrets import choice

"""To add salts, I might have an external database
 that has a list of salts mapped to each approved password hash."""

PasswordDatabase = {
    # pre-hashed passwords with their salts
    "231ecc7d178da5f22983bc579599396d6c139a457987ae1ee0026d88432d6a72": "s@lt1",
    "0046d8f8865a213767d5888d5ca9e45fe4cc629d65bf31bfd308ed519e404483": "s@lt2",
    
}
p2bhashed = input("Enter password to hash: ")
hashed = hashlib.sha256(p2bhashed.encode()).hexdigest()
print(f"SHA-256 Hash: {hashed}")

move = int(hashlib.sha256(p2bhashed.encode()).hexdigest(), 16) % 1000
print(f"Numeric hash value: {move}")

valueshift = move //100 + (move //10)%10 + move %10
print(f"Value shift: {valueshift}")

salt = hashed[:valueshift]  # Example of deriving a salt from the hash
print(f"Using salt: {p2bhashed}{salt}")

salted_hash = hashlib.sha256((p2bhashed + salt).encode()).hexdigest()
print(f"Salted SHA-256 Hash: {salted_hash}")

if salted_hash in PasswordDatabase:
    print("Password is approved.")
else:
    print("Password is not approved.")


