from textgenrnn import textgenrnn
from data_loader import LoadData, PartOfSpeechTagger

# Preferred wiki pages
article_list =['Economie_van_Nederland', 'Geschiedenis_van_Nederland', 'Economie_(systeem)', 'Bruto_nationaal_product', 'Bruto_binnenlands_product', 'Aandelenindex']

# Scrape data and clean it
object = LoadData(string_list=article_list)
article_text = object.return_data()
sentences = article_text.split('.')

# Create individual phrases based on NPs and VPs
tagged_text = PartOfSpeechTagger(article_text)
tagged_result = tagged_text.tagger()

phrases = tagged_text.tags_to_phrase(tagged_result)
#print(tagged_text.tags_to_phrase(tagged_result))


# Store data in txt file
with open('text.txt', 'w') as f:
    for sentence in phrases:
        f.write("%s\n" % sentence)


# Learn and generate text
textgen = textgenrnn()
textgen.train_from_file('text.txt', num_epochs=6)

