def sort_words_in_sentence(sentence):
    words = sentence.split()
    words.sort(key=str.lower)
    sorted_sencentes = ''.join(words)
    return sorted_sencentes

sentence = "This is a man world"
sorted_result = sort_words_in_sentence(sentence)
print("Sorted Sentence", sorted_result)

