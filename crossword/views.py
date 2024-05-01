# Create your views here.
from django.shortcuts import render, get_object_or_404,HttpResponse
from django.http import JsonResponse
from .models import Crossmap, Word, CrossmapResult,WordResult
from django.core.paginator import Paginator
import json
from django.contrib.auth.decorators import login_required
from .utils import getScore,checkWord
@login_required
def crossword_detail(request, level ,id):
    crossmap = get_object_or_404(Crossmap, pk=id)
    words = Word.objects.filter(crossmap=crossmap).order_by('row')
    words_text = list(words.values_list('text',flat=True))
    words_json = json.dumps(words_text)
    if request.method == "POST":
        words_json = request.POST.get('words')
        wordlist = json.loads(words_json)
        
        score = getScore(words_text,wordlist)
        check = checkWord(words_text,wordlist)
        result=CrossmapResult.objects.filter(user= request.user,crossmap=crossmap).first()
        if result is None:
            result = CrossmapResult(user=request.user,crossmap=crossmap,score=score)
            result.save()
            row = 1
            for word_item in wordlist:
                text_result = WordResult(crossmap_result=result,text=word_item,row=row,wordCheck=check[row-1])
                text_result.save()
                row+=1

        else:
            text_result=WordResult.objects.filter(crossmap_result=result)
            for i in range(len(text_result)):
                text_result[i].text=wordlist
                text_result[i].wordCheck=check[i]
                text_result[i].save()
            result.score=score
            result.save()
        return JsonResponse({'words':wordlist,'score':score})
    # Prepare data for the template (grid, clues)
    else:
        return render(request, 'crossword/crossword_detail.html', {'crossmap': crossmap, 'words': words,'words_json':words_json})

@login_required
def crossword_list(request,level):
    if (level > 3 or level <0):
        return HttpResponse('No level like that') 
    level_text = ['A1','A2','B1','B2']
    crossmap = Crossmap.objects.filter(level=level)
    paginator = Paginator(crossmap,6)
    page = request.GET.get('page')
    crosslist = paginator.get_page(page)
    return render(request, 'crossword/crossword_list.html',{'crosslist':crosslist,'level':level_text[level]})

@login_required
def crossword_result(request,id):
    crossmap=get_object_or_404(Crossmap, pk=id)
    words = Word.objects.filter(crossmap=crossmap).order_by('row')
    words_clue = list(words.values_list('clue',flat=True))
    crossmap_result=CrossmapResult.objects.filter(user=request.user,crossmap=crossmap).first()
    word_result=WordResult.objects.filter(crossmap_result=crossmap_result)
    word_result_text = list(word_result.values_list('text',flat=True))
    words_json = json.dumps(word_result_text)
    check_word= list(word_result.values_list('wordCheck',flat=True))
    check_json = json.dumps(check_word)
    print(check_json)
    print(words_json)
    context={
        'title':crossmap.title,
        'score':crossmap_result.score,
        'words':words_json,
        'clue':words_clue,
        'check':check_json
    }
    return render(request,'crossword/crossword_result.html',context)
