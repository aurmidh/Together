from collections import Counter
sentence= input("Insert sentence max 5 words: ")
word_count = Counter(sentence.split())

for word, count in word_count.items():
    print(f"{word}: {count}")

file_name=("Enter file name: ")
with open(file_name, 'w') as file:
    for word, count in word_count.items():
        file.write(f"{word}: {count}")
