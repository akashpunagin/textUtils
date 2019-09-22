from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    params = {'name':'akash','place':'mars'}
    return render(request,"index.html",params)

def analize(request):
    # get the text
    djtext = request.POST.get('text','This is default value')

    # get checkbox value
    is_rem_pun = request.POST.get('removepunc','off')
    is_fullcaps = request.POST.get('fullcaps','off')
    is_newlineremove = request.POST.get('newlineremove','off')
    is_spaceremove = request.POST.get('spaceremove','off')
    is_charcount = request.POST.get('charcount','off')

    purpose = []

    if is_rem_pun == 'on':
        analized = ""
        punctuations = "!@#$%^&*()_+"
        for char in djtext:
            if char not in punctuations:
                analized = analized + char
        purpose.append("Removed Punctuations")
        djtext = analized

    if(is_fullcaps =="on"):
        analized = ""
        for char in djtext:
            analized = analized + char.upper()
        purpose.append("Change to UPPERCASE")
        djtext = analized

    if(is_newlineremove =="on"):
        analized = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analized = analized + char
        purpose.append("Remove new line")
        djtext = analized

    if(is_spaceremove == "on"):
        analized = ""
        analized = " ".join(djtext.split())
        print("djtext ", djtext)
        print("analized ",analized)
        purpose.append("Remove Space")
        djtext = analized

    if(is_charcount =="on"):
        count = 0
        for char in djtext:
            count = count + 1
        purpose.append("Charecter Count")
        params = {'purpose':purpose,'analized_text':count,'text':djtext}

    if(is_rem_pun!="on" and is_fullcaps!="on" and is_charcount!="on" and is_newlineremove!="on" and is_spaceremove!="on"):
        return HttpResponse("You didn't check the checkbox!")

    if is_charcount != "on":
        params = {'purpose':purpose,'analized_text':analized}

    return render(request,'analize.html',params)
