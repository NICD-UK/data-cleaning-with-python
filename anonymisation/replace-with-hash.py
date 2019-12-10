# **************************************************************** 
# NICD - Text Replace Whole Words with One Way Hash Example
#
# replace-with-hash.py
#
# Example on how to replace whole words using word endings
# 
# Words are replaced with a SHA256 hash of the replaced string - this hashing deterministic is not reversible
# 
# **************************************************************** 

import re
import hashlib

targets = [
    "Stephen Brown",
    "Stephen",
    "Pat Smith",
    "Pat"
]

text = "stephen Brown garden wordstephenword pat smith dispatch stephen wordbrownwords"

def hash_entity(en):
    return "entity_" + hashlib.sha256(en.encode("utf8")).hexdigest()

print("Original Text")
print(text)

for target in targets:
    target_regex = re.compile(r'\b%s\b' % target.lower(), re.I)
    text = re.sub(target_regex, hash_entity(target.lower()), text)


print("Cleaned Text")
print(text)
