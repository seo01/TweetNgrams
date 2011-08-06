TweetNgrams ReadMe
==================
Tweet ngrams generates new unique documents based on given documents as a model. It was designed to generate tweets (hence the name) but will work with any corpus.

Get the damn thing to do something
----------------------------------
1. Download the repo
2. Go to the src directory
> cd {downloads}/TweetNgrams/src
3. Set this directory as your python path
> export PYTHONPATH=`pwd`
4. See the options
> nlp/nlp_cli.py -h
5. Given a text file with one document per line (e.g. one tweet per line if generating tweets) as a model, generate a new unique document.
> nlp/nlp_cli.py -g {filename}

The rest should be apparent from the help text.

WTF!?! Why is this useful
-------------------------
There are two main uses for generating documents: To generate spam or generate filler. The most useful example of generating spam is to manipulate people analysing twitter. The most useful example of generating filler is as an alternative to Lorum Ipsum modelled on more representative text.

Testing
-------
Testing is done using [nose](http://packages.python.org/nose/) and [unittest](http://docs.python.org/library/unittest.html). From the src folder execute nose:
> nosetests


 