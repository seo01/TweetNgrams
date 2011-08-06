#!/usr/bin/python
from optparse import OptionParser
import sys

from io.tweet_iterator import TweetIterator
from io.ngram_dao import NgramDao,import_ngram_dao
from io.normalised_document_dao import NormalisedDocumentDao
from io.document_publisher import DocumentPublisher, FilePublisher
from processing.frequency_booster import FrequencyBooster
from processing.token_processor import TokenProcessor
from processing.string_processor import StringProcessor
from nlp.model_builder import ModelBuilder
from nlp.document_builder import DocumentBuilder

def construct_model_builder(normalised_document_dao):
    return ModelBuilder(normalised_document_dao=normalised_document_dao,string_processor=StringProcessor(),token_processor=TokenProcessor())

def construct_document_builder(ngram_dao,normalised_document_dao):
    return DocumentBuilder(ngram_dao,normalised_document_dao=normalised_document_dao,string_processor=StringProcessor(),frequency_booster=FrequencyBooster(),token_processor=TokenProcessor())

def get_parser():
    parser = OptionParser()
    parser.set_usage(
        """usage: %prog [options]
example: Generate a model from a file and print one document
    %prog -g /Users/simon/Documents/git/TweetNgrams/data/book1.txt
example: Generate a model from a file and export it to another file without generating doc
    %prog -g /Users/simon/Documents/git/TweetNgrams/data/book1.txt -x /Users/simon/Documents/git/TweetNgrams/data/model_book1.json -c 0 -z /Users/simon/Documents/git/TweetNgrams/data/hash_book1.json
example: Read a model and hashes from files and generate 10 documents
    %prog -i /Users/simon/Documents/git/TweetNgrams/data/model_book1.json -d /Users/simon/Documents/git/TweetNgrams/data/hash_book1.json -c 10
example: Read a model and hashes from file, write 10 documents to a new file and update the hashes with the new documents
    %prog -i /Users/simon/Documents/git/TweetNgrams/data/model_book1.json -d /Users/simon/Documents/git/TweetNgrams/data/hash_book1.json -c 10 -w /Users/simon/Documents/git/TweetNgrams/data/new_documents.txt -z /Users/simon/Documents/git/TweetNgrams/data/hash_book1.json
        """)
    parser.add_option("-n", "--ngram", dest="n", type="int",default=3,
                help="Number of tokens in the longest ngrams [default: %default]")
    parser.add_option("-c", "--count", dest="count", type="int",default=1,
                help="Number of documents to generate [default: %default]")
    parser.add_option("-g","--genmodel", dest="genmodel",
                help="If specified a model is generated from the suplied file (incompatible with -i)")
    parser.add_option("-i","--importmodel",dest="importmodel",
                help="Import a model from the suplied file (incompatible with -g)")
    parser.add_option("-d","--importdocumenthash",dest="importdocumenthash",
                help="If the model is imported, you can use this option to specify a file of document hashes")
    parser.add_option("-x","--exportmodel",dest="exportmodel",
                help="The file to export the model to")
    parser.add_option("-z","--exportdocumenthash",dest="exporthash",
                help="The file to export document hashes to")
    parser.add_option("-w","--writedocument",dest="writedocument",
                help="File to write documents to")        
    return parser

def get_options():
    parser = get_parser()
    (options, args) = parser.parse_args()
    return options

def main():
    options = get_options()
    normalised_document_dao=NormalisedDocumentDao()
    if options.importdocumenthash:
        f = open(options.importdocumenthash, 'r')
        normalised_document_dao.import_hashes(f)
        f.close()
    ngram_dao = None
    if options.genmodel:
        mb = construct_model_builder(normalised_document_dao)
        ngram_dao = NgramDao(mb.extract_ngram_tree_from_documents(TweetIterator(options.genmodel),options.n))
    elif options.importmodel:
        f = open(options.importmodel, 'r')
        ngram_dao = import_ngram_dao(f)
        f.close()
    if options.exportmodel:
        f = open(options.exportmodel, 'w')
        ngram_dao.export_json(f)
        f.close()
    if options.exporthash:
        f = open(options.exporthash, 'w')
        normalised_document_dao.export_hashes(f)
        f.close()
    if ngram_dao is None:
        raise Exception("Fatal Exception no model specified, option -i or -g required")
    if options.count:
        document_builder = construct_document_builder(ngram_dao,normalised_document_dao)
        document_publisher = None
        f = None
        if options.writedocument:
            f = open(options.writedocument, 'a')
            document_publisher = FilePublisher(f)
        else:
            document_publisher = DocumentPublisher()
        for i in range(options.count):
            document_publisher.publish(document_builder.build_document(options.n))
        if f:
            f.close()

if __name__ == '__main__':
    main()