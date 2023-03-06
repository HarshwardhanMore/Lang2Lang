from django.shortcuts import render, HttpResponse
# pip install googletrans
from googletrans import Translator
import googletrans
from gtts import gTTS

# Create your views here.


def home(request):

    language_options = googletrans.LANGUAGES
    languageGuide = []
    initial = ''
    language = 'eng'
    output = ''
    output1 = ''

    for i in language_options:
        temp = {}
        temp.update({"first": i})
        temp.update({"second": language_options[i].title})
        languageGuide.append(temp)

    if request.method == 'POST':
        language = request.POST['language']
        initial = request.POST.get('lang1')

        translator = Translator()

        for i in languageGuide:
            if str(i["first"]) == str(language):
                output = initial
                if (initial):
                    output = translator.translate(initial, dest=language)
                output1 = output.text
                break

    context = {
        'input': initial,
        'output1': output1,
        # 'output2': output.pronunciation,
        'languageGuide': languageGuide
    }
    return render(request, "index.html", context=context)
