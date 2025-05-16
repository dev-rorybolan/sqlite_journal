import bcrypt

password = b"nothing" # enter your password
salt = bcrypt.gensalt()
hashed = bcrypt.hashpw(password, salt)

hashed_str = hashed.decode('utf-8')

with open("password.txt", "w") as f:
    f.write(hashed_str)

print("Hash saved to password file!")
