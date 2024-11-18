from django.http import HttpResponse
from django.shortcuts import render
def count_characters(request):
    if request.method == "POST":
        ticker =request.POST.get('ticker','')
        start_date = request.POST.get('start_date', '')
        end_date = request.POST.get('end_date', '')
        buy_strat = request.POST.get('buy_strat', '')

        buy_navigate="매수전략은 다음과 같습니다: "+buy_strat
        return render(request,'counter/result.html',{'ticker':ticker,'buy_navigate':buy_navigate})

    return render(request,'counter/form.html')
