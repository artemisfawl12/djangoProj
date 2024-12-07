from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from counter.paradigm_shift_gptanswer import gpt_call
from pykrx import stock
from django.http import JsonResponse
import os
from counter.models import FileLog
from datetime import datetime

def get_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR', 'unknown_ip')
    return ip
def show_chart(request):
    user_ip = get_ip(request)  # IP 주소
    file_name = f"chart_{user_ip}.html"
    return render(request,'counter/'+file_name)
def count_characters(request):
    if request.method == "POST":
        ticker =request.POST.get('ticker','')
        start_date = request.POST.get('start_date', '')
        end_date = request.POST.get('end_date', '')
        buy_strat = request.POST.get('buy_strat', '')
        sell_strat=request.POST.get('sell_strat','')
        user_ip = get_ip(request)

        try:
            ret_list=gpt_call(0,buy_strat,sell_strat,start_date,end_date,received_ticker=ticker)

            FileLog.objects.create(ip_address=user_ip,timestamp=datetime.now(),status="gpt_call_success")

        except Exception as e:
            ret_list=[]
            ret_list.append(" ")
            ret_list.append("ERROR OCCURED:"+str(e)+"\n 뭔가 잘못됐는데요?")
            ret_list.append("<p><strong>에러가 발생해서 차트도 표시되지 않아요.</strong></p>")
            FileLog.objects.create(ip_address=user_ip, timestamp=datetime.now(), status="gpt_call_failed")

        final_earning_percent_str=ret_list[0]
        final_earning_percent_str="최종 수익률: "+final_earning_percent_str
        assistant_msg=ret_list[1]
        html_txt=ret_list[2]

        # 유저의 IP 주소 또는 세션 ID를 활용한 파일명 생성
        user_ip = get_ip(request)  # IP 주소

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

@csrf_exempt
def delete_file(request):
    if request.method == 'POST':
        # 클라이언트의 IP 주소 가져오기
        try:
            client_ip = get_ip(request)
            # 파일 경로 생성
            filename = f"{client_ip}.html"
            file_path = os.path.join(os.path.dirname(__file__), '..', 'templates', 'counter', filename)

            # 파일 삭제
            if os.path.exists(file_path):
                os.remove(file_path)
                FileLog.objects.create(ip_address=client_ip, timestamp=datetime.now(), status="closed and html file deleted")
                return JsonResponse({'status': 'success', 'message': f'{filename} deleted.'})
            else:
                FileLog.objects.create(ip_address=client_ip, timestamp=datetime.now(),
                                       status="closed and no html file.")
                return JsonResponse({'status': 'not_found', 'message': f'{filename} does not exist.'})
        except:
            FileLog.objects.create(ip_address=client_ip, timestamp=datetime.now(), status="some error occured, maybe no ip address..")
            return JsonResponse({'status': 'error', 'message': 'IP 주소를 가져올 수 없습니다.'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})



def statistic_view(request):
    logs=FileLog.objects.all()
    return render(request,'counter/statistic.html',{'logs':logs})


