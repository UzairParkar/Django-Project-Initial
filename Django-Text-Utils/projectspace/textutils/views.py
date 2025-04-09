# pipeline
# - views.index -> the home page of the website, will contain how the website works, what it is.
# also contains navigation to authentication, myprofile, other text utilities.

# - views.removepunc -> remove punctuations from a text
# - views.CapitalizeFirst -> Capitalize the first letter in a string

from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request,'index.html')

def task(request): 
    '''
    Rediecting our Users from index page to the task 
    page where they can fill up the forms for actions
    '''
    return render(request,'task.html',status=200)


def analyze(request):
    text = request.GET.get('text', '')
    actions = request.GET.get('action')
    original_text = text
    print(actions)
    print(request.GET)
    print(original_text)
    print(text)
    if 'removepunc' in actions:
        text = remove_punctuation(text)

    if 'capfirst' in actions:
        text = capitalize_first(text)

    if 'remspaces' in actions:
        text = remove_extra_spaces(text)

    if 'touppercase' in actions:
        text = to_uppercase(text)

    if 'tolowercase' in actions:
        text = to_lowercase(text)

    if 'reversetext' in actions:
        text = reverse_text(text)

    if 'addfullstop' in actions:
        text = add_full_stop(text)

    if 'ispalindrome' in actions:
        text = is_palindrome(text)

    if 'isquestion' in actions:
        text = is_question(text)

    if 'charactercount' in actions:
        text = count_characters(text)

    if 'vowelcount' in actions:
        text = count_vowels(text)

    print(request)
    print(original_text)
    print(text)
    return render(request, 'result.html', {
        'intext': original_text,
        'output': text,
    })

def remove_punctuation(text):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    return ''.join(c for c in text if c not in punctuations)

def capitalize_first(text):
    return text.capitalize()

def remove_extra_spaces(text):
    return ' '.join(text.split())

def to_uppercase(text):
    return text.upper()

def to_lowercase(text):
    return text.lower()

def reverse_text(text):
    return text[::-1]

def add_full_stop(text):
    return text if text.endswith('.') else text + '.'

def is_palindrome(text):
    cleaned = ''.join(c.lower() for c in text if c.isalnum())
    if cleaned == cleaned[::-1]:
        return True
    else:
        return False

def is_question(text):
    if text.strip().endswith('?'):
        return True
    else:
        return False

def count_characters(text):
    return len(text)

def count_vowels(text):
    return sum(1 for c in text if c.lower() in 'aeiou')