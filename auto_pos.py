import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('averaged_perceptron_tagger')

# Open the file in read mode
with open('historic_inventions_plain.txt', 'r') as file:
    # Read each line in the file
    for line in file:
        # Print each line
        print(line.strip())
        sentence = line
        tokens = nltk.word_tokenize(sentence)
        pos_tags = nltk.pos_tag(tokens)
        print(pos_tags)