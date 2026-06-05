numbers = input("Enter: ")

freq = {}
for num in numbers.split():
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1
print(freq)