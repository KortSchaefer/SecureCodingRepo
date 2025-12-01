import hashlib
import hmac
import json
import os


print("Midterm Login System")

DB_PATH = "users.txt"


def hash_password(password: str) -> str:
    """Simple SHA-256 hash for demo purposes (no salt)."""
    return hashlib.sha256(password.encode()).hexdigest()


def verify_password(password: str, expected_hex: str) -> bool:
    return hmac.compare_digest(hash_password(password), expected_hex)


def load_users() -> dict:
    if not os.path.exists(DB_PATH):
        defaults = {
            "user1": {"hash": hash_password("password1"), "access": "1"},
            "user2": {"hash": hash_password("password2"), "access": "2"},
            "user3": {"hash": hash_password("password3"), "access": "2"},
        }
        save_users(defaults)
        return defaults
    with open(DB_PATH, "r", encoding="utf-8") as f:
        try:
            data = json.load(f)
            migrated = False
            # migrate legacy list or string values
            for name, value in list(data.items()):
                if isinstance(value, str):
                    data[name] = {"hash": value, "access": "1"}
                    migrated = True
                elif isinstance(value, list) and len(value) == 2:
                    data[name] = {"hash": value[0], "access": value[1]}
                    migrated = True
            if migrated:
                save_users(data)
            return data
        except json.JSONDecodeError:
            return {}


def save_users(users: dict) -> None:
    with open(DB_PATH, "w", encoding="utf-8") as f:
        json.dump(users, f)


def mainloop(username: str, users: dict):
    while True:
        print("\n\n\n\n\n\nWelcome to the secure area!")
        print("Commands: whoami, list_users (admin), stats (admin), exit")
        command = input(">> ").strip().lower()
        access = users[username]["access"]
        if command == "exit":
            print("Logging out...")
            break
        elif command == "whoami":
            print(f"You are logged in as: {username}")
        elif command == "list_users":
            if access == "2":
                print("Registered users:")
                for user in users.keys():
                    print(f"- {user}")
            else:
                print("Permission denied: admin only.")
        elif command == "stats":
            if access == "2":
                print(f"Total registered users: {len(users)}")
            else:
                print("Permission denied: admin only.")
        else:
            print(f"Unknown command: {command}")

    print("Goodbye!")


users = load_users()

print("would you like to:")
print("1. Register")
print("2. Login")
choice = input("[1 or 2]: ")

if choice == "1":
    print("Register Username:")
    new_username = input()
    print("Register Password:")
    new_password = input()
    print("Access level (1=user, 2=admin):")
    access = input().strip() or "1"
    users[new_username] = {"hash": hash_password(new_password), "access": access}
    save_users(users)
    print(users)
    print("Registration Successful")
    
elif choice == "2":
    print("Login Username:")
    username = input()
    print("Login Password:")
    password = input()
    record = users.get(username)
    if record and verify_password(password, record["hash"]):
        print("Login Successful")
        mainloop(username, users)
    else:
        print("Invalid credentials")
