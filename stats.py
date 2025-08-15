def word_counter(text):
    return len(text.split())

def char_counter(text):
    text = text.lower()
    counter = {}
    for character in text:
        counter[character] = counter.get(character, 0) + 1
    return counter

def sort_dict(dictionary):
    return dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
