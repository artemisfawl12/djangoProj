import plotly.graph_objects as go
from plotly.subplots import make_subplots
import webbrowser
from pykrx import stock
import pandas as pd
import os

#이게 최초의  코드이다.


exec_code:str="""
stock_data['MA_100'] = stock_data['종가'].rolling(window=100).mean()

# The difference from the previous day is less than 0.1% of the current price or maintains or increases
condition_MA = ((stock_data['MA_100'].pct_change() > -0.001) | (stock_data['MA_100'].diff() >= 0))

# The stock price has been consistently falling compared to 2.5 days ago
condition_price = (stock_data['종가'] < stock_data['종가'].shift(periods=3))

# Trading volume has also fallen compared to 5 days ago
condition_volume = (stock_data['거래량'] < stock_data['거래량'].shift(periods=5))

# Combine conditions with &
condition_buy = condition_MA & condition_price & condition_volume


# Selling condition
# Finding the maximum price since the recent buying point
stock_data['Since_Buy_Max'] = stock_data.loc[condition_buy, '종가'].cummax()

# Compare the current price to 5% decrease from the highest price since the recent buying point
condition_sell = (stock_data['종가'] < stock_data['Since_Buy_Max'] * 0.95)

"""

#차트 만드는 부분을 따로 빼서 코드의 피로도를 줄인다.

def chart_draw(stock_data,buy_date_dict, sell_date_dict, total_monitoring_dict):


    # 차트 그리기
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

    html_path = os.path.join(os.path.dirname(__file__), '..', 'templates', 'counter', 'plotly_candlestick_chart_1.html')
    fig.write_html(html_path)

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

    trader=position(startmoney)
    stock_data = stock.get_market_ohlcv(str(start_date), str(end_date), ticker)
    print("stock_Data의 길이:" +str(len(stock_data)))
    print(type(stock_data))
    #stock_data는 index를 날짜로 갖는 dataframe이고, 각 행은 시가, 고가, 저가, 종가, 거래량, 등락률 순으로 데이터를 갖고있다.

    #여기서부터 필요한 지표들(ex)이동평균선) 만드는 영역 시작

    stock_data["5day_sma"]=stock_data['종가'].rolling(window=5).mean()
    stock_data["20day_sma"] = stock_data['종가'].rolling(window=20).mean()
    stock_data["150day_sma"] = stock_data['종가'].rolling(window=150).mean()


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
    print("bought count: "+str(len(condition_buy)))
    print("sold count: " + str(len(condition_sell)))
    print(condition_buy)
    print(condition_sell)

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
            print(str(d_d)+"매도 신호")
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


    #차트 그리기: chart_draw가 1일때만 그리자.
    if chart_draw_ornot==1:
        chart_draw(stock_data,buy_date_dict,sell_date_dict,total_monitoring_dict)
    else:
        pass

    print(final_money)

    ratio=final_money / startmoney
    print(ratio)
    ratio=format(ratio,'.5f')
    print(ratio)
    return ratio

#trade("20210101","20241101","000660",exec_code=exec_code)