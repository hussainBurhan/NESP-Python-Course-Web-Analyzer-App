from django.shortcuts import render
import operator
import string

def home(request):
    return render(request, 'index.html')

def result(request):
    article = request.GET['article']
    for punctuation in string.punctuation:
        article = article.replace(punctuation, '')
    
    words = article.split()
    word_count = len(words)

    dict_words = {}

    for word in words:
        if word in dict_words:
            dict_words[word] += 1
        else:
            dict_words[word] = 1

    frequency = sorted(dict_words.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, 'result.html', {'article': article, 'word_count': word_count, 'dict_words': dict_words, 'frequency': frequency})