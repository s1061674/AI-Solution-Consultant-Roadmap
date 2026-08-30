from collections import Counter

text = "python ai python data ai python code data python"

words = text.split()

counts = Counter(words)

for word, count in counts.most_common(3):
    print(f"{word}: {count}")