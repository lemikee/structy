def substitute_synonyms(sentence, synonyms):
    words = sentence.split(' ')
    subarrays = generate(words, synonyms)
    return [' '.join(subarray) for subarray in subarrays]


def generate(words, synonyms):
    if len(words) == 0:
        return [[]]

    first_word = words[0]
    subarrays_without_first = generate(words[1:], synonyms)

    if first_word in synonyms:
        result = []
        for synonym in synonyms[first_word]:
            result += [[synonym, *subarray]
                       for subarray in subarrays_without_first]
        return result
    else:
        return [[first_word, *subarray] for subarray in subarrays_without_first]
