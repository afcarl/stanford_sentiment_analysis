import os
import subprocess


# A function to format input string
def __format_string__(s):
    """
    Function to preprocess the string
    to input it to the sentiment analysis
    """
    s = str(s)
    s = s.strip()
    # If the string is not blank then '.' is added at the end.
    if len(s) > 0:
        # Stripping bothside of the string.

        if s[-1] != ".":
            s = s + "."
        return s
    else:
        return s


def get_sentiment(sentence):
    """
    This function takes sentence as input and output the sentiment

    Example 1:
    get_sentiment("You are not good")
    --> ['You are not good.', '  Negative']

    Example 2:
    get_sentiment("You are not good. You are very bad.")
    --> ['You are not good.', '  Negative', 'You are very bad.', '  Negative']

    """
    sentence = __format_string__(sentence)
    # Getting the home path
    home_path = os.path.expanduser('~')

    # Creating a temporary file to write the sentence
    temp_file = home_path + "temp_sentiment.txt"

    # Writting the file
    with open(temp_file, "w") as sentiment_file:
        sentiment_file.write(sentence)

    # The command to get sentiment
    command = '''cd $HOME/.stanford_sentiment_library/stanford-corenlp-full-2015-12-09/ && java -cp "*" -mx5g edu.stanford.nlp.sentiment.SentimentPipeline -file %s''' % temp_file

    # The subprocess command
    subprocess_command = subprocess.Popen(
        [command], shell=True, stdout=subprocess.PIPE)

    # Executing the subprocess command
    sentiment, error = subprocess_command.communicate()

    # Removing the temporary file
    os.remove(temp_file)

    sentiment = filter(None, sentiment.split("\n"))

    return sentiment
