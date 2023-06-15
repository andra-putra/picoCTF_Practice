import hashlib
from cryptography.fernet import Fernet
import base64

# This is from the original code
username_trial = b"MORTON"

# Modified function check_key(key, uesrname_trial) from original code
def key_print(username_trial):
    output = ""
    output += (hashlib.sha256(username_trial).hexdigest()[4])
    output += (hashlib.sha256(username_trial).hexdigest()[5])
    output += (hashlib.sha256(username_trial).hexdigest()[3])
    output += (hashlib.sha256(username_trial).hexdigest()[6])
    output += (hashlib.sha256(username_trial).hexdigest()[2])
    output += (hashlib.sha256(username_trial).hexdigest()[7])
    output += (hashlib.sha256(username_trial).hexdigest()[1])
    output += (hashlib.sha256(username_trial).hexdigest()[8])
    return(output)

# These are from the original code
key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_static2_trial = "}"

print(key_part_static1_trial + key_print(username_trial) + key_part_static2_trial)
