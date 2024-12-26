import plotly.graph_objects as go
from plotly.subplots import make_subplots
from pykrx import stock
import pandas as pd
import os
from plotly.io import to_html

import logging

loggers=logging.getLogger('counter')

#이게 최초의  코드이다.

#차트 만드는 부분을 따로 빼서 코드의 피로도를 줄인다.

def prepare_data(df):
    #dataframe을 받아서, ticker을 key, value는 index가 날짜이고 나머지가 column인 dictionary??로 만들어서 준다?? 이게 말이되노
    grouped_data = {}
    for ticker, group in df.groupby(level='tickers'):
        grouped_data[ticker] = group.reset_index(level='날짜').to_dict(orient='records')
    return grouped_data

def trade_multiple(start_date, end_date, tickers, exec_code):
    #특정 범위 내 있는 티커들 전부에 대해서 trade를 돌린다
    #매수기록 매도기록을 티커별로 정리한 dataframe을 return 받는다. 매도수량까지 넣으면 3차원이 되는데, 음 ... 분할매매 기능을 넣을진 모르겠으나 그냥 살려두자
    #

    print(tickers)

    date_list=[]
    date_list.append(str(start_date))
    date_list.append(str(end_date))

    buy_date_list=[]
    sell_date_list=[]
    total_monitoring_list=[]
    ticker_list=[]
    failed_ticker_list=[]
    total_onlymoney_df=pd.DataFrame()
    buydatedict_collect={}
    selldatedict_collect={}
    totalmonitoringdict_collect={}
    for ticker in tickers:
        try:
            ret_list=trade(start_date,end_date,ticker,exec_code,100000000,2)
            stock_data = ret_list[0]
            buy_date_dict = ret_list[1]
            sell_date_dict = ret_list[2]
            total_monitoring_dict = ret_list[3]
            #이 3개 받은것을, chart draw를 위해서 좀 밖으로 빼내야 한다.
            buy_price_list = []
            sell_price_list = []
            if len(buy_date_dict)!=0:
                for d in buy_date_dict:
                    buy_price_list.append(stock_data.loc[d, '종가'])

                buy_date_dict_str = {str(key): value for key, value in buy_date_dict.items()}

                buy_date_price_df_temp = pd.DataFrame(list(buy_date_dict_str.items()), columns=['날짜', '수량']).set_index('날짜')
                buy_date_price_df_temp['가격'] = buy_price_list
                buydatedict_collect[ticker]=buy_date_dict

            else:
                data = {
                    "수량": [0],
                    "가격": [0],
                }

                # DataFrame 생성
                buy_date_price_df_temp = pd.DataFrame(data, index=["2000-01-01"])

                # Index 이름 설정
                buy_date_price_df_temp.index.name = "날짜"
                buydatedict_collect[ticker]="err"

            if len(sell_date_dict) != 0:
                for d in sell_date_dict:
                    sell_price_list.append(stock_data.loc[d, '종가'])
                sell_date_dict_str = {str(key): value for key, value in sell_date_dict.items()}
                sell_date_price_df_temp = pd.DataFrame(list(sell_date_dict_str.items()), columns=['날짜', '수량']).set_index(
                    '날짜')
                sell_date_price_df_temp['가격'] = sell_price_list
                selldatedict_collect[ticker] = sell_date_dict

            else:
                data = {
                    "수량": [0],
                    "가격": [0],
                }

                # DataFrame 생성
                sell_date_price_df_temp = pd.DataFrame(data, index=["2000-01-01"])

                # Index 이름 설정
                sell_date_price_df_temp.index.name = "날짜"
                selldatedict_collect[ticker]="err"


            total_monitoring_df_temp = pd.DataFrame(list(total_monitoring_dict.items()),
                                                    columns=["날짜", "총 자산"]).set_index('날짜')

            totalmonitoringdict_collect[ticker] = total_monitoring_dict

            buy_date_list.append(buy_date_price_df_temp)
            sell_date_list.append(sell_date_price_df_temp)
            total_monitoring_list.append(total_monitoring_df_temp)
            ticker_list.append(ticker)
            total_onlymoney_df = total_onlymoney_df.add(total_monitoring_df_temp, fill_value=0)
        except Exception as e:
            failed_ticker_list.append(str(ticker)+": E || "+str(e))
            print(str(ticker)+"failed :"+str(e))

        buydf_final = pd.concat(buy_date_list, keys=ticker_list, names=["tickers", "날짜"])
        # multiindex가 ticker, 날짜이고, 날짜, 수량, 가격 3개의 column을 가진듯 하다 .. .
        selldf_final = pd.concat(sell_date_list, keys=ticker_list, names=["tickers", "날짜"])
        totalmonitordf_final = pd.concat(total_monitoring_list, keys=ticker_list, names=["tickers", "날짜"])
        multi_ret_list = []
        multi_ret_list.append(prepare_data(buydf_final)) #0
        multi_ret_list.append(prepare_data(selldf_final)) #1
        multi_ret_list.append(prepare_data(totalmonitordf_final)) #2
        multi_ret_list.append(total_onlymoney_df.to_json(orient="table", date_format="iso", index=True)) #3
        multi_ret_list.append(failed_ticker_list) #4
        multi_ret_list.append(ticker_list) #5
        multi_ret_list.append(buydatedict_collect)
        multi_ret_list.append(selldatedict_collect)
        multi_ret_list.append(totalmonitoringdict_collect)
        multi_ret_list.append(date_list)

        #Exception 발생시, stock_data에 exec code를 넣게 해놓음, 나머지는 그냥 빈 리스트.

    return multi_ret_list










def chart_draw(stock_data,buy_date_dict, sell_date_dict, total_monitoring_dict):
    fig = make_subplots(
        rows=3, cols=1,
        shared_xaxes=True,
        vertical_spacing=0.04,  # 이걸로 현재는 그래프간 간격을 줄인상태.
        row_heights=[0.5, 0.2, 0.3]
    )
    # Plotly 캔들차트 생성

    fig.add_trace(go.Candlestick(
        x=stock_data.index,
        open=stock_data['시가'],
        high=stock_data['고가'],
        low=stock_data['저가'],
        close=stock_data['종가'],
        name="Candlestick"
    ), row=1, col=1)

    """
    # 이동평균선 추가
    fig.add_trace(go.Scatter(
        x=stock_data.index,
        y=stock_data['5day_sma'],
        mode='lines',
        name='5-day SMA',
        line=dict(color='lightyellow', width=2)
    ), row=1, col=1)

    fig.add_trace(go.Scatter(
        x=stock_data.index,
        y=stock_data['150day_sma'],
        mode='lines',
        name='150-day SMA',
        line=dict(color='blue')
    ), row=1, col=1)

    fig.add_trace(go.Scatter(
        x=stock_data.index,
        y=stock_data['20day_sma'],
        mode='lines',
        name='20-day SMA',
        line=dict(color='red')
    ), row=1, col=1)
    """

    buy_signals = pd.DataFrame(list(buy_date_dict.items()), columns=['날짜', '수량'])

    fig.add_trace(go.Scatter(
        x=buy_signals['날짜'],
        y=stock_data.loc[buy_signals['날짜'], '저가'] * 0.95,  # 매수 신호를 차트 아래에 표시
        mode='markers',
        marker=dict(color='green', size=20, symbol='triangle-up'),
        hovertext=buy_signals['수량'].apply(lambda x: f"매수: {x}주"),  # 툴팁으로 매수량 표시
        hoverinfo="text",
        name="Buy Signal"
    ), row=1, col=1)

    fig.add_trace(go.Bar(
        x=stock_data.index,
        y=stock_data['거래량'],
        name="Volume",
        marker_color='grey'
    ), row=2, col=1)

    # 매도 신호 표시

    sell_signals = pd.DataFrame(list(sell_date_dict.items()), columns=['날짜', '수량'])
    fig.add_trace(go.Scatter(
        x=sell_signals['날짜'],
        y=stock_data.loc[sell_signals['날짜'], '고가'] * 1.05,  # 매도 신호를 차트 위에 표시
        mode='markers+text',
        marker=dict(color='red', size=20, symbol='triangle-down'),
        hovertext=sell_signals['수량'].apply(lambda x: f"매도: {x}주"),  # 툴팁으로 매도량 표시
        hoverinfo="text",
        name="Sell Signal"
    ), row=1, col=1)

    # 총 자산 그래프

    total_monitoring = pd.DataFrame(list(total_monitoring_dict.items()), columns=["날짜", "총 자산"])
    fig.add_trace(go.Scatter(
        x=total_monitoring['날짜'],
        y=total_monitoring['총 자산'],
        mode='lines+markers',
        name="Total Assets",
        line=dict(color='purple', width=2),
        marker=dict(size=6)
    ), row=3, col=1)

    # 레이아웃 설정
    fig.update_layout(
        title='stock simulation CHART',
        xaxis_title='Date',
        yaxis_title='Price',
        xaxis2_title="Date",
        yaxis2_title="Volume",
        xaxis_rangeslider_visible=False,
        xaxis=dict(title_text=""),  # 첫 번째 x축의 표시를 숨김
        xaxis2=dict(title_text=""),  # 두 번째 x축 (거래량 차트)의 표시를 숨김

        showlegend=True
    )

    # html_path = os.path.join(os.path.dirname(__file__), '..', 'templates', 'counter', 'plotly_candlestick_chart_1.html')

    return to_html(fig)


class position:
    def __init__(self,startmoney):
        print("some position defined.")
        #startmoeny는 integer type으로
        self.money=startmoney
        self.currentposition={}
        self.currentposition["cash"]=startmoney

    def sell(self,position_code,current_price,percent=1):
        #percent: 해당 포지션을 얼마 비율로 팔건지
        #current_price: 해당 ticker 주식의 현재 가격을 입력, 종가 기준으로.
        #currentposition[positioncode]: ticker을 key, 해당 주식의 보유수량을 value로 갖는 딕셔너리 형식. cash에는 그냥 액수가 들어가있다.
        if position_code in self.currentposition:
            sell_count=int(self.currentposition[position_code] * percent)
            self.currentposition["cash"] = self.currentposition["cash"] + sell_count * current_price
            self.currentposition[position_code]=self.currentposition[position_code]-int(percent*self.currentposition[position_code])
            return sell_count
        else:
            return 0

            pass

    def buy(self,position_code,current_price,percent=1):
        #해당 금액으로 살수 있는 최대수량을 구매
        if self.currentposition["cash"]*percent>self.currentposition["cash"]:
            print("Error: percent value >1")

        else:
            buy_count=int(self.currentposition["cash"]*percent/current_price)
            if buy_count>0:
                if position_code in self.currentposition:
                    self.currentposition[position_code]+=buy_count
                    self.currentposition["cash"]-=current_price*buy_count
                    return buy_count
                else:
                    self.currentposition[position_code]=buy_count
                    self.currentposition["cash"] -= current_price * buy_count
                    return buy_count

                #차트에서 매수 지점 표시할 때 구매수량을 알려주기 위해 return해준다.

            else:
                pass




    def current(self,code_curprice_dict):
        print("position:"+ str(self.currentposition))
        total_money=0
        for key in code_curprice_dict:
            if key in self.currentposition:
                total_money+=self.currentposition[key]*code_curprice_dict[key]
            else:
                pass

        total_money+=self.currentposition["cash"]
        print("total:"+str(total_money))
        print("")
        return total_money

    def cur_ret(self):
        return self.currentposition

    def total(self,code_curprice_dict):
        total_money = 0
        for key in code_curprice_dict:
            if key in self.currentposition:
                total_money += self.currentposition[key] * code_curprice_dict[key]
        else:
            pass

        total_money += self.currentposition["cash"]
        return total_money


def trade(start_date, end_date, ticker,exec_code, startmoney=100000000, chart_draw_ornot=1):
    loggers.info("trade func in booleanway _ py started")
    print("trade started:"+str(ticker))

    trader=position(startmoney)
    stock_data = stock.get_market_ohlcv(str(start_date), str(end_date), ticker)
    print("stock_Data의 길이:" +str(len(stock_data)))
    print(type(stock_data))
    #stock_data는 index를 날짜로 갖는 dataframe이고, 각 행은 시가, 고가, 저가, 종가, 거래량, 등락률 순으로 데이터를 갖고있다.

    #여기서부터 필요한 지표들(ex)이동평균선) 만드는 영역 시작

    """
    stock_data["5day_sma"]=stock_data['종가'].rolling(window=5).mean()
    stock_data["20day_sma"] = stock_data['종가'].rolling(window=20).mean()
    stock_data["150day_sma"] = stock_data['종가'].rolling(window=150).mean()
    """


    condition_buy=[]
    condition_sell=[]
    condition_list=[]
    print("이제부터 실행할 코드:")
    print(exec_code)
    print("exec code 끝")
    exec(exec_code+
    """condition_list.extend([condition_buy, condition_sell])
    """)
    condition_buy=condition_list[0]
    condition_sell = condition_list[1]
    print("len of condition_buy: this value should be same as length of stock_data "+str(len(condition_buy)))
    print("sold count: " + str(len(condition_sell)))
    loggers.info("len of condition_buy: this value should be same as length of stock_data "+str(len(condition_buy)))
    loggers.info("sold count: " + str(len(condition_sell)))

    # 조건을 만족하는 행들 필터링


    # 여기까지 필요한 지표들 만드는 영역 끝

    #여기서부터 전략 영역 시작.
    sell_date_dict = {}
    buy_date_dict = {}
    total_monitoring_dict={}
    i=0
    for d_d in stock_data.index:

        #previous_d = d_d - timedelta(days=1)
        loc=stock_data.index.get_loc(d_d)
        if i==0:
            print("first day passed")
            prev_loc = loc
            i+=1
        else:
            prev_loc=loc-1
            i+=1
        code_curpricedict = {}
        code_curpricedict[ticker]= stock_data.iloc[loc]["종가"]
        total_monitoring_dict[d_d]=trader.total(code_curpricedict)

        #print( str(stock_data.iloc[loc]["5day_sma"])+" || "+ str(stock_data.iloc[loc]["150day_sma"]))

        #매수 조건

        if condition_buy[d_d]==True:
            buy_percent=1
            received_buy_count=trader.buy(ticker,stock_data.iloc[loc]["종가"],buy_percent)

            #살때마다 구매 날짜 리스트를 만들어 추후 차트에 표기
            if received_buy_count!=0 and received_buy_count!=None:
                #이때 received_buy_count 자리에 0이 올수도, None 이 올수도 있으니 둘다 제외해줘야된다. 아래에서 sell count에서도 마찬가지
                buy_date_dict[d_d]=received_buy_count
                print("날짜:" + str(d_d) + ", " + str(stock_data.iloc[loc]["종가"]) + "에 매수")
                code_curpricedict = {}
                code_curpricedict[ticker] = stock_data.iloc[loc]["종가"]
                trader.current(code_curpricedict)


        #매도 조건
        elif condition_sell[d_d]==True:
            #trader의 sell 함수의 return값은: 실제 매도가 이루어지면 1을 받고, 현재 보유한 주식이 없어 매도가 이루어지지 않았으면 0을 받음.
            received_sell_count=trader.sell(ticker,stock_data.iloc[loc]["종가"],1)
            if received_sell_count!=0 and received_sell_count!=None:
                print("매도가격: " + str(stock_data.iloc[loc]["종가"]))
                code_curpricedict = {}
                code_curpricedict[ticker] = stock_data.iloc[loc]["종가"]
                trader.current(code_curpricedict)

                # 팔때마다 구매 날짜 리스트를 만들어 추후 차트에 표기
                sell_date_dict[d_d] = received_sell_count


            else:
                pass


    #최종 결과 프린트
    end_date_d=pd.to_datetime(str(end_date))
    if end_date_d not in stock_data.index:
        loc = stock_data.index.get_indexer([end_date_d], method='pad')[0]
        end_date_d = stock_data.index[loc]

    code_curpricedict = {}
    code_curpricedict[ticker] = stock_data.loc[end_date_d]["종가"]
    final_money=trader.current(code_curpricedict)


    #차트 그리기: chart_draw가 1일때만 그리자. 이거 이제보니까 chart_draw가 2이면 뭐 어떻게 해야겠는데?
    if chart_draw_ornot==1:
        html_txt=chart_draw(stock_data,buy_date_dict,sell_date_dict,total_monitoring_dict)
        print(final_money)

        ratio = final_money / startmoney
        ratio = format(ratio, '.5f')
        ret_list = []
        ret_list.append(str(ratio))
        ret_list.append(html_txt)
        return ret_list
    elif chart_draw_ornot==2:
        print("chart num==2")
        ret_list=[]
        ret_list.append(stock_data) #0
        ret_list.append(buy_date_dict) #1
        ret_list.append(sell_date_dict) #2
        ret_list.append(total_monitoring_dict) #3
    else:
        print("passed")
        pass

    return ret_list


#trade("20210101","20241101","000660",exec_code=exec_code)

#def market_trade(start_date,end_date,market_name,exec_code,):
    #여기선 마켓에 대해서 할건데,,, 포트폴리오 구성방안 칸과, 각 주식에 대한 전략 칸을 분배를 해야될거같다.
    #그렇다면 포트폴리오 클래스를 만들어서 각 시기별 보유할 종목의 티커? 를 갖고있는다거나 해야겠다.
    #근데 만약에 그런거 없다면 음 .. 그럼그냥 마켓대상인것/아닌것으로 페이지를 쪼갤게 아니고, 포트폴리오 관리 기준 유무로 쪼갤까?
    #그래서 전 종목 대상 시뮬레이션도 가능하게 ...
    #근데사실, 전종목 중에서 PER이 상위 5등안에 들기: 이런 전략이면 상대적인 수치가 없어서 그런거지 전종목에 대해서 알고리즘을 들이민다는 기준에서
    #보면 똑같지않나. 상위 5등안에 들면 매도 ~머 이거랑 머가 다르노 이거야. 이러면 그냥 상대적인 수치를 몇개 만들어서 넣어야되나? 데이터 양이 존나커지는데
    #이러면 음 ... 그냥 절대지표 상대지표 나눠서 지표를 제공하고, TRADE는 똑같이 쓰고, chart만 하나더 만드는게 좋을지도 몰라

