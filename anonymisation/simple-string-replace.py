import re

targets = [
    "Stephen Brown",
    "Stephen",
    "Pat Smith",
    "Pat"
]

text = "stephen Brown garden wordstephenword pat smith dispatch stephen wordbrownwords"

text_replacement = "XX"

print("Original Text")
print(text)

for target in targets:
    target_regex = re.compile(r'\b%s\b' % target.lower(), re.I)
    text = re.sub(target_regex, text_replacement, text)

print("\n Cleaned Text")
print(text)
