from django.http import HttpResponse
from django.shortcuts import render
from counter.paradigm_shift_gptanswer import gpt_call
from pykrx import stock
from django.http import JsonResponse
import os


def show_chart(request):
    user_ip = request.META.get('REMOTE_ADDR', 'unknown_ip')  # IP 주소
    file_name = f"chart_{user_ip}.html"
    return render(request,'counter/'+file_name)
def count_characters(request):
    if request.method == "POST":
        ticker =request.POST.get('ticker','')
        start_date = request.POST.get('start_date', '')
        end_date = request.POST.get('end_date', '')
        buy_strat = request.POST.get('buy_strat', '')
        sell_strat=request.POST.get('sell_strat','')

        ret_list=gpt_call(0,buy_strat,sell_strat,start_date,end_date,received_ticker=ticker)

        final_earning_percent_str=ret_list[0]
        final_earning_percent_str="최종 수익률: "+final_earning_percent_str
        assistant_msg=ret_list[1]
        html_txt=ret_list[2]

        # 유저의 IP 주소 또는 세션 ID를 활용한 파일명 생성
        user_ip = request.META.get('REMOTE_ADDR', 'unknown_ip')  # IP 주소

        # 파일명 조합
        file_name = f"chart_{user_ip}.html"
        html_path = os.path.join(os.path.dirname(__file__), '..', 'templates', 'counter',file_name)

        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html_txt)

        return render(request,'counter/result.html',{'ticker':ticker,'buy_navigate':final_earning_percent_str,'assistant_msg':assistant_msg})

    return render(request,'counter/form.html')

def stock_ticker_data(request):
    tickers = stock.get_market_ticker_list()
    name_ticker_dict={}
    for ticker in tickers:
        name = stock.get_market_ticker_name(ticker)
        name_ticker_dict[name]=ticker
    return JsonResponse(name_ticker_dict)

def show_tickersearch(request):
    return render(request,'counter/tickersearch.html')
