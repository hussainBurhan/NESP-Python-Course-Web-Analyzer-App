# Import necessary modules
from django.shortcuts import render
import operator
import string

# View for the home page
def home(request):
    # Render the home page template
    return render(request, 'index.html')

# View for processing the input text and displaying results
def result(request):
    # Get the input text from the GET request parameters
    article = request.GET['article']

    # Remove punctuation from the input text
    for punctuation in string.punctuation:
        article = article.replace(punctuation, '')

    # Split the input text into a list of words
    words = article.split()

    # Calculate the total word count
    word_count = len(words)

    # Initialize an empty dictionary to store word frequencies
    dict_words = {}

    # Count the frequency of each word in the input text
    for word in words:
        if word in dict_words:
            dict_words[word] += 1
        else:
            dict_words[word] = 1

    # Sort the dictionary by word frequency in descending order
    frequency = sorted(dict_words.items(), key=operator.itemgetter(1), reverse=True)

    # Render the result page template with the relevant data
    return render(request, 'result.html', {'article': article, 'word_count': word_count, 'dict_words': dict_words, 'frequency': frequency})
