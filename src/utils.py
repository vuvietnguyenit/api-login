import hashlib

import yaml

with open("config.yaml", "r") as f:
    config = yaml.load(f, Loader=yaml.FullLoader)


def hashmd5(val: str):
    salt = "vunv"
    password = val + salt
    password_encrypted = hashlib.md5(password.encode())
    return password_encrypted.hexdigest()