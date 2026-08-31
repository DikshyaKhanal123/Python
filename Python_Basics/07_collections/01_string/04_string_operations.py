word = "  I love Python  "

print(f"original string: {word}")

print(f"length of string {len(word)}")
print(f"first character: {word[0]}")

print(f"reverse: {word[::-1]}")

print(f"Uppercase: {word.upper()}")
print(f"lowercase: {word.lower()}")

print(f"split: {word.split()}")

print(f"position of love: {word.find('love')}")

print(f" python in word:  {'python' in word}")
print(f" Python in word:  {'Python' in word}")

print(f"Number of o is: {word.count('o')}")

print(f"remove space from both sides : {word.strip()}")

print(f"make title : {word.title()}")

print(f"replace pyhton with java : {word.replace('Python', 'java')}")

print(f"string repetition :{word*3}")