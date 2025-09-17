def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    new_dict = {}

    for char in text:
        if char.lower() in new_dict:
            new_dict[char.lower()] += 1
        else:
            new_dict[char.lower()] = 1
    return new_dict