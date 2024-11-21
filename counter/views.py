from django.http import HttpResponse
from django.shortcuts import render
from counter.paradigm_shift_gptanswer import gpt_call

def show_chart(request):
    return render(request,'counter/plotly_candlestick_chart_1.html')
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


        return render(request,'counter/result.html',{'ticker':ticker,'buy_navigate':final_earning_percent_str,'assistant_msg':assistant_msg})

    return render(request,'counter/form.html')
