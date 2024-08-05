str = input()
result = []
for char in str:
    if char == " ":
        continue
    result.append(char)
print(set(list(result)))