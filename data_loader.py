"""

Developed by: L. Smalbil

N.B. Install the following before usage:

#nltk.download('averaged_perceptron_tagger')
#nltk.download('alpino')

"""

import bs4 as bs
import urllib.request
import ssl
import re
from nltk.tag import PerceptronTagger
from nltk.corpus import alpino as alp
ssl._create_default_https_context = ssl._create_unverified_context

class LoadData:
    def __init__(self, string_list):
        self.string_list = string_list

    def return_data(self):
        """
        Usage:

        article_list =['Economie_van_Nederland', 'Aandelenindex']

        object = LoadData(string_list=article_list)
        article_text = object.return_data()
        print(type(article_text))

        :return:
        """

        # Get all texts as list of strings
        total_list = []
        for article in self.string_list:
            raw_html = urllib.request.urlopen('https://nl.wikipedia.org/wiki/'+article)

            raw_html = raw_html.read()

            article_html = bs.BeautifulSoup(raw_html, 'lxml')
            article_paragraphs = article_html.find_all('p')
            article_text = ''

            for para in article_paragraphs:
                article_text += para.text

            #article_text = article_text.lower()
            article_text = re.sub(r'[^A-Za-z. ]', '', article_text)
            total_list.append(article_text)

        article_text = '-'.join(total_list)

        return article_text

"""
def prepareForNLP(text):
    sentences = nltk.sent_tokenize(text)
    sentences = [nltk.word_tokenize(sent) for sent in sentences]
    sentences = [nltk.pos_tag(sent) for sent in sentences]
    return sentences
"""

class PartOfSpeechTagger:
    def __init__(self, string):
        self.string = string

    def tagger(self):
        """
        Usage:

        training_corpus = list(alp.tagged_sents())
        tagger = PerceptronTagger(load=True)

        tagger.train(training_corpus)

        #sent = 'NLTK is een goeda taal voor het leren over NLP'.split()

        print(tagger.tag(article_text.split()))
        :return:
        """

        # Load Corpus
        training_corpus = list(alp.tagged_sents())
        tagger = PerceptronTagger(load=True)

        # Build tagger
        tagger.train(training_corpus)

        return tagger.tag(self.string.split())


    def tags_to_phrase(self, tagged_result):
        phrase = []

        current_string = ''
        for word_pair in tagged_result:
            # Cut-off along verbs and preps, also check for start of sent. using isupper()
            if (word_pair[1] != 'verb') and (word_pair[1] != 'prep') and (word_pair[0][0].isupper() == False):
                current_string += ' ' + word_pair[0]
            else:
               if word_pair[0][0].isupper() == False:
                    current_string += ' ' + word_pair[0]  # also add verb or prep to previous string
                    phrase.append(current_string)
                    current_string = ''
                    current_string += ' ' + word_pair[0]
               else:
                    phrase.append(current_string)
                    current_string = ''
                    current_string += ' ' + word_pair[0]

        return phrase


