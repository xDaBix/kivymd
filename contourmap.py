import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
text = "The big brown dog barked loudly at the stranger."
words = nltk.word_tokenize(text)
pos_tags = nltk.pos_tag(words)
grammar = "NP: {<DT>?<JJ>*<NN>}"
chunk_parser = nltk.RegexpParser(grammar)
chunk_tree = chunk_parser.parse(pos_tags)
print(chunk_tree)
chunk_tree.draw()  