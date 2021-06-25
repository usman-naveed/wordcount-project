from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')     #you can pass in a
                                            #dict and call that in the html file using {{}}

def foo(request):
    return HttpResponse("<h1>Foo foo fighters are pretty cool</h1>")

def count(request):
    full_text = request.GET['full_text']      # this is how you access HTML variables
    full_text_split = full_text.split()
    total_words = len(full_text_split)
    count_of_each_word = dict()
    for i in full_text_split:
        if i not in count_of_each_word.keys():
            count_of_each_word[i] = 1
        else:
            count_of_each_word[i] +=1

    sorted_dict = sorted(count_of_each_word.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'full_text': full_text, 'count': total_words, 'sorted_dict': sorted_dict})

def about(request):
    return render(request, 'about.html')
