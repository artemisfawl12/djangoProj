import requests
import pandas as pd
import time

from datetime import datetime, timedelta, timezone
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import webbrowser
from pykrx import stock
import pandas as pd

"""
url = "https://api.coingecko.com/api/v3/coins/list"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(pd.DataFrame(response.json()))
#가격만 gecko에서 받아오게 할까?
하쉬발 빗썸으로 바꿔야되나?
"""


def bithumb_coinlist():
    url = "https://api.bithumb.com/v1/market/all?isDetails=false"
    headers = {"accept": "application/json"}
    res = requests.get(url, headers=headers)
    coin_list = pd.DataFrame(res.json())
    return coin_list





def request_minutedata_200(time_received, count, unit, market="KRW-BTC"):
    url = "https://api.bithumb.com/v1/candles/minutes/"+str(unit)
    print(time_received)
    params = {
        'market': market,
        'count': count,
        'to': str(time_received)
    }
    headers = {"accept": "application/json"}

    response = requests.get(url, params=params, headers=headers)
    try:
        df = pd.DataFrame(response.json())
        print(df.shape)
        if len(df) >= 1:
            #time.sleep(0.05)
            return df
        else:
            print(response)
            print("waiting")
            time.sleep(5)
            return 0

    except:
        print(response)
        print("waiting")
        time.sleep(5)
        return 0

    # return pd.DataFrame(response.json())

def request_datedata_200(time_received, count, market="KRW-BTC"):
    url = "https://api.bithumb.com/v1/candles/days"
    print(time_received)
    #이거 KST시간으로 바꿔줘야되나...
    params = {
        'market': market,
        'count': count,
        'to': str(time_received)
    }
    headers = {"accept": "application/json"}

    response = requests.get(url, params=params, headers=headers)

    try:
        df = pd.DataFrame(response.json())
        print(df.shape)
        if len(df) >= 1:
            #time.sleep(0.01)
            return df
        else:
            print(response)
            print("waiting")
            time.sleep(5)
            return 0

    except:
        print(response)
        print("waiting")
        time.sleep(5)
        return 0

    #return pd.DataFrame(response.json())

def chart_draw(stock_data, buy_date_dict, sell_date_dict, total_monitoring_dict):
    print(stock_data.iloc[0])
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

    fig.add_trace(go.Scatter(
        x=stock_data.index,
        y=stock_data['거래량'],
        name="Volume",
        mode='lines',
        line=dict(color='magenta')
    ), row=2, col=1)

    # 이동평균선 추가

    """
    buy_signals = pd.DataFrame(list(buy_date_dict.items()), columns=['시간', '수량'])

    fig.add_trace(go.Scatter(
        x=buy_signals['시간'],
        y=stock_data.loc[buy_signals['시간'], '저가'] * 0.95,  # 매수 신호를 차트 아래에 표시
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

    sell_signals = pd.DataFrame(list(sell_date_dict.items()), columns=['시간', '수량'])
    fig.add_trace(go.Scatter(
        x=sell_signals['시간'],
        y=stock_data.loc[sell_signals['시간'], '고가'] * 1.05,  # 매도 신호를 차트 위에 표시
        mode='markers+text',
        marker=dict(color='red', size=20, symbol='triangle-down'),
        hovertext=sell_signals['수량'].apply(lambda x: f"매도: {x}주"),  # 툴팁으로 매도량 표시
        hoverinfo="text",
        name="Sell Signal"
    ), row=1, col=1)

    # 총 자산 그래프

    total_monitoring = pd.DataFrame(list(total_monitoring_dict.items()), columns=["시간", "총 자산"])
    fig.add_trace(go.Scatter(
        x=total_monitoring['시간'],
        y=total_monitoring['총 자산'],
        mode='lines+markers',
        name="Total Assets",
        line=dict(color='purple', width=2),
        marker=dict(size=6)
    ), row=3, col=1)

    """

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

    html_path = 'plotly_candlestick_chart.html'
    fig.write_html(html_path)
    webbrowser.open(html_path)


def request_data_byminute(start_date, end_date, unit, ticker="KRW-BTC"):

    # 문자열을 datetime 객체로 변환
    start_datetime = datetime.strptime(start_date, "%Y%m%d")
    end_datetime = datetime.strptime(end_date, "%Y%m%d")
    unit=int(unit)


    # 원하는 포맷으로 변환
    start_date_formatted = end_datetime.strftime("%Y-%m-%d %H:%M:%S")
    end_date_formatted = end_datetime.strftime("%Y-%m-%d %H:%M:%S")
    # to로 써넣은 직전의 시간까지를 준다!
    timediff = end_datetime - start_datetime
    timediff = timediff.total_seconds() / (60*unit)
    df_to_return = pd.DataFrame()
    i = 0
    endless_param = 0
    while True:
        if endless_param > 1000000:
            break
        if i < int(timediff / 200):
            wanted_time = end_datetime - timedelta(minutes=i * 200 * unit)
            requested_df = request_minutedata_200(wanted_time.strftime("%Y-%m-%d %H:%M:%S"), 200, unit=unit,market=ticker)
            if type(requested_df) == int:
                pass
                print("passed")
            else:
                df_to_return = pd.concat([df_to_return, requested_df], ignore_index=True)
                i += 1

        elif i == int(timediff / 200):
            interval = timediff - 200*i*unit
            if i==0:
                wanted_time=end_datetime
            else:
                pass
            requested_df = request_minutedata_200(wanted_time.strftime("%Y-%m-%d %H:%M:%S"), int(interval), unit=unit,market=ticker)
            if type(requested_df) == int:
                pass
                print("passed")
            else:
                df_to_return = pd.concat([df_to_return, requested_df], ignore_index=True)
                i += 1


        else:
            print("ended")
            break

    stock_data = df_to_return.drop(columns=['market', 'timestamp'])
    stock_data = stock_data.rename(
        columns={'opening_price': '시가', 'high_price': '고가', 'low_price': '저가', 'trade_price': '종가',
                 'candle_acc_trade_volume': '거래량', 'candle_acc_trade_price': '거래금액', 'candle_date_time_kst': '시간',
                 'candle_date_time_utc': 'UTC시간'})

    stock_data = stock_data.set_index('시간')


    return stock_data

def request_data_bydate(start_date, end_date, ticker="KRW-BTC"):


    # 문자열을 datetime 객체로 변환
    start_datetime = datetime.strptime(start_date, "%Y%m%d")


    end_datetime = datetime.strptime(end_date, "%Y%m%d")


    # 원하는 포맷으로 변환
    start_date_formatted = end_datetime.strftime("%Y-%m-%d %H:%M:%S")
    end_date_formatted = end_datetime.strftime("%Y-%m-%d %H:%M:%S")
    # to로 써넣은 직전의 시간까지를 준다!
    timediff = end_datetime - start_datetime
    timediff = timediff.total_seconds() / 86400
    df_to_return = pd.DataFrame()
    i = 0
    endless_param = 0
    while True:
        if timediff > 1000000:
            df_to_return="too large request"
            break
        if i < int(timediff / 200):
            wanted_time = end_datetime - timedelta(days=i * 200)
            requested_df = request_datedata_200(wanted_time.isoformat(), 200, market=ticker)
            if type(requested_df) == int:
                pass
                print("passed")
            else:
                df_to_return = pd.concat([df_to_return, requested_df], ignore_index=True)
                i += 1

        elif i == int(timediff / 200):
            interval = timediff - 200 * i
            if i==0:
                wanted_time=end_datetime
            else:
                pass
            requested_df = request_datedata_200(wanted_time.isoformat(), int(interval),market=ticker)
            if type(requested_df) == int:
                pass
                print("passed")
            else:
                df_to_return = pd.concat([df_to_return, requested_df], ignore_index=True)
                i += 1


        else:
            print("ended")
            break

    stock_data = df_to_return.drop(columns=['market', 'timestamp', 'prev_closing_price', 'change_price', 'change_rate'])
    stock_data = stock_data.rename(
        columns={'opening_price': '시가', 'high_price': '고가', 'low_price': '저가', 'trade_price': '종가',
                 'candle_acc_trade_volume': '거래량', 'candle_acc_trade_price': '거래금액', 'candle_date_time_kst': '시간',
                 'candle_date_time_utc': 'UTC시간'})

    stock_data = stock_data.set_index('시간')



    return stock_data

#print(request_data_byminute("20241201","20241210",1))

#원래 trade에서 쓰던대로 데이터를 가다듬는 함수를 만듭시다.
"""
market	종목 코드	String
candle_date_time_utc	캔들 기준 시각(UTC 기준)
    포맷: yyyy-MM-dd'T'HH:mm:ss	String
candle_date_time_kst	캔들 기준 시각(KST 기준)
    포맷: yyyy-MM-dd'T'HH:mm:ss	String
opening_price	시가	Double
high_price	고가	Double
low_price	저가	Double
trade_price	종가	Double
timestamp	해당 캔들에서 마지막 틱이 저장된 시각	Long
candle_acc_trade_price	누적 거래 금액	Double
candle_acc_trade_volume	누적 거래량	Double
unit	분 단위(유닛)	Integer

모든 코인들의 데이터를 싹 한군데에 넣어놔서, 상대적인 수치도 사용할수 있게하면 어떨까?
한 10개까지 선택 가능하게 한다음에, 이중에서 너맘대로 골라라 식으로 가는거지
그리고 KRW 마켓, BTC 마켓도 구별해야할것.

UTC시간    2024-12-27T14:57:00
시가                 143955000
고가                 143960000
저가                 143782000
종가                 143917000
거래금액          55139445.77338
거래량                 0.383285
unit                       3
Name: 2024-12-27T23:57:00, dtype: object
"""

"""
di={}
chart_draw(stock_data,di,di,di)
stock_data=column_select(stock_data)
print(stock_data)
print(stock_data.columns)
print(type(stock_data.iloc[0]))
"""
"""
lis=upbit_coinlist()
i=0
print(len(lis))
for i in range(len(lis)):
    print(lis.iloc[i]["market"])

tickers = stock.get_market_ticker_list()
name_ticker_dict={}
for ticker in tickers:
    name = stock.get_market_ticker_name(ticker)
    print(name)
"""


