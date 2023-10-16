def count_word_frequencies(text):
    word_list = text.split()
    word_freq = {}    
    for word in word_list:
        word = word.lower()
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    
    return word_freq
text = "This is a sample text. This text is used for testing word frequencies."
word_frequencies = count_word_frequencies(text)
for word, frequency in word_frequencies.items():
    print(f"{word}: {frequency}")
