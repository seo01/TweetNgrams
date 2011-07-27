from io.tweet_iterator import TweetIterator
from io.ngram_dao import NgramDao
from io.normalised_document_dao import NormalisedDocumentDao
from processing.frequency_booster import FrequencyBooster
from processing.token_processor import TokenProcessor
from processing.string_processor import StringProcessor
from nlp.model_builder import ModelBuilder
from nlp.document_builder import DocumentBuilder

def construct_model_builder(normalised_document_dao):
    return ModelBuilder(normalised_document_dao=normalised_document_dao,string_processor=StringProcessor(),token_processor=TokenProcessor())

def construct_document_builder(model,normalised_document_dao):
    return DocumentBuilder(NgramDao(model),normalised_document_dao=normalised_document_dao,string_processor=StringProcessor(),frequency_booster=FrequencyBooster(),token_processor=TokenProcessor())

def main():
    n = 3
    count = 10
    normalised_document_dao=NormalisedDocumentDao()
    mb = construct_model_builder(normalised_document_dao)
    model = mb.extract_ngram_tree_from_documents(TweetIterator("/Users/simon/Documents/git/TweetNgrams/data/book1.txt"),n)
    document_builder = construct_document_builder(model,normalised_document_dao)
    for i in range(count):
        print document_builder.build_document(n)
        print "\n"
    

if __name__ == '__main__':
    main()