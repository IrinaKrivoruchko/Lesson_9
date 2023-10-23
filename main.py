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
with open("First.txt", "w") as first:
    first.write(text_to_write)

with open("First.txt", "r") as first:
    words = first.read().split()

filtered_words = []
for word in words:
    if len(word) >= 7:
        filtered_words.append(word)

with open("Second.txt", "w") as second_file:
    second_file.write(" ".join(filtered_words))

#2
word_count = len(words)

print(f"Count of words in file: {word_count}")

#Additionally
text = """To be, or not to be, that is the question, Whether 'tis nobler in the mind to suffer The slings and arrows 
of outrageous fortune, Or to take arms against a sea of troubles, And by opposing end them? To die: to sleep; No more; 
and by a sleep to say we end The heart-ache and the thousand natural shocks That flesh is heir to, 'tis a consummation 
Devoutly to be wish'd. To die, to sleep"""

word_for_change = "die"
new_word = "***"

text_after_replace, num_of_replacements = text.replace(word_for_change, new_word), text.count(word_for_change)

print(f"Text after replace: \n{text_after_replace}")
print(f"Number of replacements: '{word_for_change}': {num_of_replacements}")