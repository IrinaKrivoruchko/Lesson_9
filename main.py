text_to_write = """To be, or not to be, that is the question,
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune,
Or to take arms against a sea of troubles,
And by opposing end them?
To die: to sleep;
No more; and by a sleep to say we end
The heart-ache and the thousand natural shocks
That flesh is heir to, 'tis a consummation
Devoutly to be wish'd.
To die, to sleep"""

#1
# Записываем текст в файл "First.txt"
with open("First.txt", "w") as first:
    first.write(text_to_write)

# Открываем файл "First.txt" для чтения
with open("First.txt", "r") as first:
    # Читаем содержимое файла и разбиваем его на слова
    words = first.read().split()

# Фильтруем слова, чтобы оставить только те, у которых длина не менее 7 букв
filtered_words = []
for word in words:
    if len(word) >= 7:
        filtered_words.append(word)

# Открываем файл "Second.txt" для записи и записываем отфильтрованные слова в него
with open("Second.txt", "w") as second_file:
    second_file.write(" ".join(filtered_words))

#2
word_count = len(words)

print(f"Count of words in file: {word_count}")