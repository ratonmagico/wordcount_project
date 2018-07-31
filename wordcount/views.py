from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, "home.html")

def count(request):
    fulltext = request.GET["fulltext"]
    wordlist = fulltext.split()
    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1
    wwords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
    print(wwords)
    return render(request, "count.html",
    # VARIABLES COUNT
    {"fulltext":fulltext, "count":len(wordlist), "sortedwords":wwords})

def about(request):
    return render(request, "about.html")
