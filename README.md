# stanford_sentiment_analysis
A simple python library for sentiment analysis with Stanford CoreNLP.

The paper for this stanford library is:--
Manning, Christopher D., Mihai Surdeanu, John Bauer, Jenny Finkel, Steven J. Bethard, and David McClosky. 2014. The Stanford CoreNLP Natural Language Processing Toolkit In Proceedings of the 52nd Annual Meeting of the Association for Computational Linguistics: System Demonstrations, pp. 55-60.

The java version of stanford sentiment analysis is downloaded from (http://stanfordnlp.github.io/CoreNLP/)


# How to install this python library(Make sure you have git installed)
open terminal with (Alt + Ctrl + t)

### Install and configure java first (provide password when needed)
1. sudo add-apt-repository ppa:webupd8team/java
2. sudo apt-get update
3. sudo apt-get install oracle-java8-installer
4. sudo apt-get install oracle-java8-set-default

### Need to clone and install the python library (provide password when needed)
1. git clone https://github.com/KnHuq/stanford_sentiment_analysis.git
2. cd stanford_sentiment_analysis
3. sudo chmod +x install.sh
4. sudo ./install.sh 

Now its jone!
#open python 
>>> python
>>> from stanford_sentiment import get_sentiment
>>> get_sentiment("It is good")
['It is good.', '  Positive']
>>> get_sentiment("It is not good")
['It is not good.', '  Negative']
>>> get_sentiment("It is not good. He is very bad boy")
['It is not good.', '  Negative', 'He is very bad boy.', '  Negative']

N.B: This library uses Stanford CoreNLP java api to extract the sentiment from the text. This library is created for the ease of the python developer.
You are welcome to contribute in this repo. Thank you.
