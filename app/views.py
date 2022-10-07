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
    language = ''
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
                output = translator.translate(initial, dest=language)
                output1 = output.text
                break

    # if language == "mr":
    #     output = translator.translate(initial, dest="mr")
    # elif language == "hi":
    #     output = translator.translate(initial, dest="hi")
    # elif language == "de":
    #     output = translator.translate(initial, dest="de")
    # else:
    #     output = translator.translate(initial, dest="en")

    # print(output)

    # for i in language_options:
    #     print(i, language_options[i])

    context = {
        'input': initial,
        'output1': output1,
        # 'output2': output.pronunciation,
        'languageGuide': languageGuide
    }
    return render(request, "index.html", context=context)
