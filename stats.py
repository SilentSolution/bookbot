def count_words(t):
    words = t.split()
    return len(words)


def count_each_character(text):
    characters_count = {}
    for character in text:
        lowered = character.lower()
        if lowered in characters_count:
            characters_count[lowered] += 1
        else:
            characters_count[lowered] = 1
    return characters_count