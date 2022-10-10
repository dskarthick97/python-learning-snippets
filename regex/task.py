import re


def remove_duplicates(sentence):
    pattern = r"\b(\w+)(?:\W\1\b)+"
    return re.sub(pattern, r"\1", sentence, flags=re.IGNORECASE)


sentence_1 = "Good bye bye world world"
sentence_2 = "Ram went went to to his home to"
sentence_3 = "Hello hello world world hello"
print(remove_duplicates(sentence_1))
print(remove_duplicates(sentence_2))
print(remove_duplicates(sentence_3))
