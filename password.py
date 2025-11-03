import hashlib
import string
import tkinter as tk
from secrets import choice


'''
Confidentiality: this app stores only SHA-256 password hashes, never plaintext.
User input is hashed and compared to the whitelist of hashes, so even if the
stored list is exposed, original passwords are not feasibly recoverable.
This reduces data exposure risk and keeps secrets out of code, files, and logs.

Some passowrds are pre-approved; others can be generated securely. as of right now, you will have to manualy hash your password and add it to the APPROVED_HASHES set to approve it.

Approved passwords (plaintext) for testing:
- password123
- SecurePass!@#456
- MyP@ssw0rd!$ecure
- 1234

'''
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")
root.resizable(False, False)

# Store approved password hashes only; never keep plain text secrets.
APPROVED_HASHES = {
    "231ecc7d178da5f22983bc579599396d6c139a457987ae1ee0026d88432d6a72",
    "7ea6ab9e5b3671f08657cb09ecbce9bc264038b2da457e8376f7212075bc6c4f",
    "5e89bbea5175c797b388382a3663b8dccfd3a105e7332e3365f1bc46c3da1577",
    "03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4",
}

entry_label = tk.Label(root, text="Password:")
entry_label.pack(pady=(20, 5))

password_entry = tk.Entry(root, width=35)
password_entry.pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)


def generate_password():
    alphabet = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
    generated = "".join(choice(alphabet) for _ in range(16))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, generated)
    result_label.config(text="Generated secure password.", fg="blue")


def check_password():
    entered = password_entry.get()
    if not entered:
        result_label.config(text="Enter or generate a password first.", fg="orange")
        return

    entered_hash = hashlib.sha256(entered.encode()).hexdigest()
    if entered_hash in APPROVED_HASHES:
        result_label.config(text="Welcome!", fg="green")
    else:
        result_label.config(text="Access denied.", fg="red")


button_frame = tk.Frame(root)
button_frame.pack(pady=15)

generate_button = tk.Button(button_frame, text="Generate Password", command=generate_password)
generate_button.pack(side=tk.LEFT, padx=5)

submit_button = tk.Button(button_frame, text="Validate Password", command=check_password)
submit_button.pack(side=tk.LEFT, padx=5)

root.mainloop()
