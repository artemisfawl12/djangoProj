from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from counter.paradigm_shift_gptanswer import gpt_call
from counter.paradigm_shift_gptanswer import gpt_call_multi
from counter.booleanway_new import chart_draw
from counter.coin_data_collect import upbit_coinlist
from counter.gptanswer_coin import coingpt_call_multi
from counter.coin_data_collect_bitthumb import bithumb_coinlist, request_data_bydate,request_data_byminute
from pykrx import stock
from django.http import JsonResponse
import os
from counter.models import FileLog
from datetime import datetime
import json
import logging

def process(request):
    if request.method=='POST':
        rs_author=request.POST.get('rs_author','')
        rs_author=float(rs_author)
        rs_company=request.POST.get('rs_company','')
        rs_company=float(rs_company)
        rs_portal=request.POST.get('rs_portal', '')
        rs_portal=float(rs_portal)
        total_share_pct=(rs_company+rs_author)/(rs_company+rs_author+rs_portal)
        author_share_pct=rs_author/(rs_company+rs_author)
        mg=request.POST.get('mg','')
        period = request.POST.get('period', '')
        mg=int(mg)
        period=int(period)
        mg_money=request.POST.get('mg_money','')
        mg_money=float(mg_money)
        subtract=request.POST.get('subtract','')
        subtract=int(subtract)
        revenue_1=request.POST.get('revenue_1','0')
        revenue_1=float(revenue_1)
        publish_count = request.POST.get('publish_count', '')
        publish_count=float(publish_count)
        mg_money=publish_count*mg_money # 월 연재횟수랑 곱해줍니다.
        total_money=revenue_1*total_share_pct #이게 에이전시랑 작가 수익 총합, 월별
        if mg==0:
            #월별 mg
            if subtract==0:
                #선차감인경우.
                if total_money>=mg_money:

                    income_total=mg_money*period + author_share_pct*(total_money-mg_money)*period
                    income_month=mg_money + author_share_pct*(total_money-mg_money)
                    #추가정산금 혹은 월별로 나오는 마이너스?
                    surplus_month=author_share_pct*(total_money-mg_money)
                    loss_total=0
                else:
                    income_total = mg_money * period + author_share_pct * (total_money - mg_money)
                    #매출 부족 부분은 마지막 달만 들어간다.
                    surplus_month=author_share_pct * (total_money - mg_money)
                    loss_total=author_share_pct * (total_money - mg_money)


            elif subtract==1:
                #후차감인경우.
                if total_money*author_share_pct>=mg_money:
                    income_total=period*(total_money*author_share_pct)
                    #여기선 mg보다 수익이 많으니까.
                    income_month=total_money*author_share_pct
                    # 추가정산금
                    surplus_month = total_money*author_share_pct-mg_money
                    loss_total=0
                else:
                    #이때는 받을돈이 더 적은거니까, 월별엠지인데 후차감이고 막달만 계산해주자.
                    income_total=period*mg_money-(mg_money-total_money*author_share_pct)
                    loss_total=(mg_money-total_money*author_share_pct)
                    surplus_month=total_money*author_share_pct-mg_money



        elif mg==1:
            #누적 mg
            if subtract==0:
                #선차감인경우.
                if total_money>=mg_money:
                    #: 흑자면 월별 mg이랑 딱히 달라질것은 없다.
                    income_total=mg_money*period + author_share_pct*(total_money-mg_money)*period
                    income_month=mg_money + author_share_pct*(total_money-mg_money)
                    #추가정산금 혹은 월별로 나오는 마이너스?
                    surplus_month=author_share_pct*(total_money-mg_money)
                    loss_total=0
                else:
                    income_total = mg_money * period + author_share_pct * (total_money - mg_money)*period
                    #매출 부족 부분이 전체 들어간다.
                    surplus_month=author_share_pct * (total_money - mg_money)
                    loss_total=author_share_pct * (mg_money-total_money)*period
                    income_month=mg_money


            elif subtract==1:
                #후차감인경우.
                if total_money*author_share_pct>=mg_money:
                    income_total=period*(total_money*author_share_pct)
                    #여기선 mg보다 수익이 많으니까. 딱히 달라질것이없다.
                    income_month=total_money*author_share_pct
                    # 추가정산금
                    surplus_month = total_money*author_share_pct-mg_money
                    loss_total=0
                else:
                    #모든달을 다 합쳐야한다. 사실상 최악의 경우임
                    income_total=period*mg_money-(mg_money-total_money*author_share_pct)
                    surplus_month=total_money*author_share_pct-mg_money
                    loss_total = (mg_money - total_money * author_share_pct)*period
                    income_month = mg_money




        return JsonResponse({'income_total': income_total,'surplus_month': surplus_month, 'income_month':income_month, 'loss_total':loss_total})
    return JsonResponse({'error': 'Invalid request method'}, status=400)



logger=logging.getLogger('counter')
def multi_chart(request, ticker):
    buydict=request.session.get('buy_final')
    buydict = {
        ticker: {datetime.fromisoformat(key): value for key, value in data.items()}
        for ticker, data in buydict.items()
    }

    selldict=request.session.get('sell_final')
    selldict = {
        ticker: {datetime.fromisoformat(key): value for key, value in data.items()}
        for ticker, data in selldict.items()
    }
    totaldict=request.session.get('total_monitor_final')
    totaldict={
        ticker: {datetime.fromisoformat(key): value for key, value in data.items()}
        for ticker, data in totaldict.items()
    }
    #ticker=request.GET.get('ticker')
    user_ip = get_ip(request)
    FileLog.objects.create(ip_address=user_ip, timestamp=datetime.now(), status="ticker received by GET:"+str(ticker))
    #ticker는 참 잘 나오는데 왜 그 뒤는 안될까요?

    date_list=request.session.get('date_list')

    stock_data=stock.get_market_ohlcv(date_list[0], date_list[1], str(ticker))
    html_txt = chart_draw(stock_data,buydict[str(ticker)],selldict[str(ticker)],totaldict[str(ticker)])
    file_name = f"chart_{user_ip}.html"
    html_path = os.path.join(os.path.dirname(__file__), '..', 'templates', 'counter', file_name)

    response = HttpResponse(html_txt, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{ticker}.html"'


    return response
def multi_chart_coin(request, ticker):
    unit=request.session.get('unit')
    buydict=request.session.get('buy_final')
    buydict = {
        ticker: {datetime.fromisoformat(key): value for key, value in data.items()}
        for ticker, data in buydict.items()
    }

    selldict=request.session.get('sell_final')
    selldict = {
        ticker: {datetime.fromisoformat(key): value for key, value in data.items()}
        for ticker, data in selldict.items()
    }
    totaldict=request.session.get('total_monitor_final')
    totaldict={
        ticker: {datetime.fromisoformat(key): value for key, value in data.items()}
        for ticker, data in totaldict.items()
    }
    #ticker=request.GET.get('ticker')
    user_ip = get_ip(request)
    FileLog.objects.create(ip_address=user_ip, timestamp=datetime.now(), status="ticker received by GET:"+str(ticker))
    #ticker는 참 잘 나오는데 왜 그 뒤는 안될까요?

    date_list=request.session.get('date_list')

    if unit==0:
        stock_data=request_data_bydate(date_list[0], date_list[1],str(ticker))
    else:
        stock_data=request_data_byminute(date_list[0], date_list[1],unit, str(ticker))

    html_txt = chart_draw(stock_data,buydict[str(ticker)],selldict[str(ticker)],totaldict[str(ticker)])
    file_name = f"chart_{user_ip}.html"
    html_path = os.path.join(os.path.dirname(__file__), '..', 'templates', 'counter', file_name)

    response = HttpResponse(html_txt, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{ticker}.html"'


    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_txt)



    show_chart(request)


    return response

def multi_result_coin(request):
    if request.method == "POST":
        tickers =request.POST.get('ticker','')
        ticker_list = [ticker.strip() for ticker in tickers.split(',') if ticker.strip()]
        name_ticker_dict={}

        all_codict=coin_ticker_dict()
        ticker_name_dict = {v: k for k, v in all_codict.items()}

        for ticker in ticker_list:
            name=ticker_name_dict[ticker]
            name_ticker_dict[ticker] = name
        name_ticker_dict_json=json.dumps(name_ticker_dict,ensure_ascii=False)


        start_date = request.POST.get('start_date', '')
        end_date = request.POST.get('end_date', '')
        buy_strat = request.POST.get('buy_strat', '')
        sell_strat=request.POST.get('sell_strat','')
        unit=int(request.POST.get('unit'))
        request.session['unit']=unit
        user_ip = get_ip(request)

        #try:
        ret_list = coingpt_call_multi(0, buy_strat, sell_strat, start_date, end_date,unit,ticker_list)
        if len(ret_list[0])==0:
            logger.info("buy final length is 0")
            buy_final = "err"
            sell_final = "err"
            total_final = "err"
            error_list = ["gpt_call_multi error: "]
            ticker_list = []
            buy_final_json = json.dumps(buy_final, ensure_ascii=False)
            sell_final_json = json.dumps(sell_final, ensure_ascii=False)
            total_final_json = json.dumps(total_final, ensure_ascii=False)
            ticker_list_json = json.dumps(ticker_list, ensure_ascii=False)
            error_list_json=json.dumps(error_list,ensure_ascii=False)
            assistant_msg="매수 횟수가 0입니다. 뭔가 이상해요!.\n"+ret_list[10]

            FileLog.objects.create(ip_address=user_ip, timestamp=datetime.now(), status="gptcoin_call multi_len==0")
            # 에러났다고 알려주고 gpt 메시지 보여주는거 넣어야 합니다.



        else:
            buy_final = ret_list[0]
            print(buy_final)
            sell_final = ret_list[1]
            total_monitor_final=ret_list[2]
            total_final=ret_list[3]
            error_list=ret_list[4]
            ticker_list =ret_list[5]
            buydict=ret_list[6]
            selldict=ret_list[7]
            totaldict=ret_list[8]
            date_list=ret_list[9]
            assistant_msg = ret_list[10]
            #이렇게하면 잘 됐을때만 차트 표시가 되는건데.
            buy_dict_iso={}
            sell_dict_iso={}
            for ticker, data in buydict.items():
                if data=="buy_zero":
                    assistant_msg+"\n "+str(ticker)+"의 매수 횟수가 0회입니다. 조건을 만족하는 시점이 없었나봐요"
                    buy_dict_iso[ticker]={}
                else:
                    buy_dict_iso[ticker] = {key.isoformat(): int(value) for key, value in data.items()}
            #여기로 ticker에 대해서, 에러가 났을 경우 data자리에 err str이 들어온다. 그래서 str에 대해 item이 없다고 나오게됨. 원래는 key는 date, value는 수량일걸 ..
            for ticker, data in selldict.items():
                if data=="sell_zero":
                    assistant_msg+"\n "+str(ticker)+"의 매도 횟수가 0회입니다. 조건을 만족하는 시점이 없었나봐요"
                    sell_dict_iso[ticker]={}
                else:
                    sell_dict_iso[ticker] = {key.isoformat(): int(value) for key, value in data.items()}
            total_dict_iso={ticker:{key.isoformat(): int(value) for key, value in data.items()} for ticker,data in totaldict.items()}
            logger.info("session saving started")
            request.session['buy_final']=buy_dict_iso
            request.session['sell_final']=sell_dict_iso
            request.session['total_monitor_final']=total_dict_iso
            request.session['date_list'] = date_list
            logger.info("date final session done")


            logger.info("json start")
            buy_final_json = json.dumps(buy_final, ensure_ascii=False)
            sell_final_json = json.dumps(sell_final, ensure_ascii=False)
            total_final_json = json.dumps(total_final, ensure_ascii=False)
            ticker_list_json=json.dumps(ticker_list, ensure_ascii=False)
            error_list_json = json.dumps(error_list, ensure_ascii=False)
            logger.info("json done")
            FileLog.objects.create(ip_address=user_ip, timestamp=datetime.now(), status="gptcoin_callmulti_success")


        """
        except Exception as e:
            logger.info("Exception at where?"+str(e))
            buy_final = "err"
            sell_final = "err"
            total_final = "err"
            error_list = ["gpt_call_multi error: " + str(e)]
            ticker_list = []
            buy_final_json = json.dumps(buy_final, ensure_ascii=False)
            sell_final_json = json.dumps(sell_final, ensure_ascii=False)
            total_final_json = json.dumps(total_final, ensure_ascii=False)
            ticker_list_json = json.dumps(ticker_list, ensure_ascii=False)
            error_list_json = json.dumps(error_list, ensure_ascii=False)
            # 에러났다고 알려주고 gpt 메시지 보여주는거 넣어야 합니다.
            assistant_msg="gpt 시뮬레이션 함수를 실행하다가 뭔가 오류가 났어요. 관리자에게 문의해주세요: artemisfawl@naver.com"

            FileLog.objects.create(ip_address=user_ip, timestamp=datetime.now(), status="gptcoin_call_failed: "+str(e))
        """


        # 유저의 IP 주소 또는 세션 ID를 활용한 파일명 생성
        user_ip = get_ip(request)  # IP 주소
        """
        # 파일명 조합
        file_name = f"chart_{user_ip}.html"
        html_path = os.path.join(os.path.dirname(__file__), '..', 'templates', 'counter', file_name)

        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html_txt)
        """
        return render(request, 'counter/coinmulti_result.html',
                      {'buy_final': buy_final_json, 'sell_final': sell_final_json,"total_final":total_final_json,"error_list":error_list_json, "ticker_list":ticker_list_json, "name_ticker_dict": name_ticker_dict_json, "assistant_msg":assistant_msg} )

    return render(request, 'counter/coinmulti_form.html')

def multi_result(request):
    if request.method == "POST":
        tickers =request.POST.get('ticker','')
        ticker_list = [ticker.strip() for ticker in tickers.split(',') if ticker.strip()]
        name_ticker_dict={}
        for ticker in ticker_list:
            name = stock.get_market_ticker_name(ticker)
            name_ticker_dict[ticker] = name
        name_ticker_dict_json=json.dumps(name_ticker_dict,ensure_ascii=False)


        start_date = request.POST.get('start_date', '')
        end_date = request.POST.get('end_date', '')
        buy_strat = request.POST.get('buy_strat', '')
        sell_strat=request.POST.get('sell_strat','')
        user_ip = get_ip(request)

        try:
            ret_list = gpt_call_multi(0, buy_strat, sell_strat, start_date, end_date, ticker_list)
            if len(ret_list[0])==0:
                buy_final = "err"
                sell_final = "err"
                total_final = "err"
                error_list = ["gpt_call_multi error: "]
                ticker_list = []
                buy_final_json = json.dumps(buy_final, ensure_ascii=False)
                sell_final_json = json.dumps(sell_final, ensure_ascii=False)
                total_final_json = json.dumps(total_final, ensure_ascii=False)
                ticker_list_json = json.dumps(ticker_list, ensure_ascii=False)
                error_list_json=json.dumps(error_list,ensure_ascii=False)
                assistant_msg="gpt multi call 중 오류 발생.\n"+ret_list[10]

                FileLog.objects.create(ip_address=user_ip, timestamp=datetime.now(), status="gpt_callmulti_len==0")
                # 에러났다고 알려주고 gpt 메시지 보여주는거 넣어야 합니다.



            else:
                buy_final = ret_list[0]
                sell_final = ret_list[1]
                total_monitor_final=ret_list[2]
                total_final=ret_list[3]
                error_list=ret_list[4]
                ticker_list =ret_list[5]
                buydict=ret_list[6]
                selldict=ret_list[7]
                totaldict=ret_list[8]
                date_list=ret_list[9]
                #이렇게하면 잘 됐을때만 차트 표시가 되는건데.
                buy_dict_iso={ticker:{key.isoformat(): value for key, value in data.items()} for ticker,data in buydict.items()}
                sell_dict_iso={ticker:{key.isoformat(): value for key, value in data.items()} for ticker,data in selldict.items()}
                total_dict_iso={ticker:{key.isoformat(): value for key, value in data.items()} for ticker,data in totaldict.items()}
                request.session['buy_final']=buy_dict_iso
                request.session['sell_final']=sell_dict_iso
                request.session['total_monitor_final']=total_dict_iso
                request.session['date_list'] = date_list
                assistant_msg =ret_list[10]

                buy_final_json = json.dumps(buy_final, ensure_ascii=False)
                sell_final_json = json.dumps(sell_final, ensure_ascii=False)
                total_final_json = json.dumps(total_final, ensure_ascii=False)
                ticker_list_json=json.dumps(ticker_list, ensure_ascii=False)
                error_list_json = json.dumps(error_list, ensure_ascii=False)
                FileLog.objects.create(ip_address=user_ip, timestamp=datetime.now(), status="gpt_callmulti_success")








        except Exception as e:
            buy_final = "err"
            sell_final = "err"
            total_final = "err"
            error_list = ["gpt_call_multi error: " + str(e)]
            ticker_list = []
            buy_final_json = json.dumps(buy_final, ensure_ascii=False)
            sell_final_json = json.dumps(sell_final, ensure_ascii=False)
            total_final_json = json.dumps(total_final, ensure_ascii=False)
            ticker_list_json = json.dumps(ticker_list, ensure_ascii=False)
            error_list_json = json.dumps(error_list, ensure_ascii=False)
            # 에러났다고 알려주고 gpt 메시지 보여주는거 넣어야 합니다.
            assistant_msg="gpt 시뮬레이션 함수를 실행하다가 뭔가 오류가 났어요. 재시도 해보세요"

            FileLog.objects.create(ip_address=user_ip, timestamp=datetime.now(), status="gpt_call_failed: "+str(e))


        # 유저의 IP 주소 또는 세션 ID를 활용한 파일명 생성
        user_ip = get_ip(request)  # IP 주소
        """
        # 파일명 조합
        file_name = f"chart_{user_ip}.html"
        html_path = os.path.join(os.path.dirname(__file__), '..', 'templates', 'counter', file_name)

        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html_txt)
        """
        return render(request, 'counter/multi_result.html',
                      {'buy_final': buy_final_json, 'sell_final': sell_final_json,"total_final":total_final_json,"error_list":error_list_json, "ticker_list":ticker_list_json, "name_ticker_dict": name_ticker_dict_json, "assistant_msg":assistant_msg} )

    return render(request, 'counter/multi_form.html')


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

def coin_ticker_data(request):
    name_ticker_dict=coin_ticker_dict()


    return JsonResponse(name_ticker_dict)
def coin_ticker_dict():
    coin_ticker_name_df=bithumb_coinlist()
    name_ticker_dict={}
    for i in range(len(coin_ticker_name_df)):
        name=coin_ticker_name_df.iloc[i]["korean_name"]
        ticker=coin_ticker_name_df.iloc[i]["market"]
        if ticker.split("-")[0]=="KRW":
            name_ticker_dict[name]=ticker

    return name_ticker_dict

def stock_ticker_data(request):
    tickers = stock.get_market_ticker_list()
    name_ticker_dict={}
    for ticker in tickers:
        name = stock.get_market_ticker_name(ticker)
        name_ticker_dict[name]=ticker
    return JsonResponse(name_ticker_dict)

def show_tickersearch(request):
    return render(request,'counter/tickersearch.html')
def coin_tickersearch(request):
    return render(request,'counter/cointickersearch.html')

@csrf_exempt
def delete_file(request):
    if request.method == 'POST':
        # 클라이언트의 IP 주소 가져오기
        try:
            client_ip = get_ip(request)
            # 파일 경로 생성
            filename = f"chart_{client_ip}.html"
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

def file_del_byip(request):
    if request.method == 'POST':
        ip=request.POST.get('ip')
        if not ip:
            return JsonResponse({'error': 'IP 주소가 제공되지 않았습니다.'}, status=400)
        filename = f"chart_{ip}.html"
        file_path = os.path.join(os.path.dirname(__file__), '..', 'templates', 'counter', filename)

        if os.path.exists(file_path):
            os.remove(file_path)
            FileLog.objects.create(ip_address=ip, timestamp=datetime.now(), status="closed and html file deleted")
            return JsonResponse({'status': 'success', 'message': f'{filename} deleted.'})
        else:
            FileLog.objects.create(ip_address=ip, timestamp=datetime.now(),
                                   status="closed and no html file.")
            return JsonResponse({'status': 'not_found', 'message': f'{filename} does not exist.'})

def statistic_view(request):
    logs=FileLog.objects.all()
    return render(request,'counter/statistic.html',{'logs':logs})

def review_view(request):
    if request.method=="POST":
        ip = request.POST.get('ip')
        id = request.POST.get('id', '')
        review_body = request.POST.get('review_body', '')
        review_txt=str(id)+" review: "+str(review_body)
        logger.info(review_txt)
        FileLog.objects.create(ip_address=ip, timestamp=datetime.now(), status="review:"+review_txt)


    return render(request,'counter/reviewpage.html')



