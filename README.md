# SecureCodingRepo
A repo for SDEV 245 secure coding classs

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
