def vowels(text):
    vow = "aeiouAEIOU"
    count = 0

    for c in text:
        if c in vow:
            count += 1

    return count

text = input()
print(vowels(text))