import requests
import pandas as pd
import time

from datetime import datetime, timedelta
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
"""


def upbit_coinlist():
    url = "https://api.upbit.com/v1/market/all"
    headers = {"accept": "application/json"}
    res = requests.get(url, headers=headers)
    coin_list = pd.DataFrame(res.json())
    return coin_list


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
"""


def request_minutedata_200(time_received, count, market="KRW-BTC"):
    url = "https://api.upbit.com/v1/candles/minutes/1"
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
            time.sleep(0.1)
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
    url = "https://api.upbit.com/v1/candles/days"
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
            time.sleep(0.1)
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

def chart_draw(stock_data, buy_date_dict, sell_date_dict, total_monitoring_dict):
    # 차트 그리기
    fig = make_subplots(
        rows=3, cols=1,
        shared_xaxes=True,
        vertical_spacing=0.04,  # 이걸로 현재는 그래프간 간격을 줄인상태.
        row_heights=[0.5, 0.2, 0.3]
    )
    # Plotly 캔들차트 생성

    fig.add_trace(go.Candlestick(
        x=stock_data['candle_date_time_kst'],
        open=stock_data['opening_price'],
        high=stock_data['high_price'],
        low=stock_data['low_price'],
        close=stock_data['trade_price'],
        name="Candlestick"
    ), row=1, col=1)

    fig.add_trace(go.Scatter(
        x=stock_data['candle_date_time_kst'],
        y=stock_data['candle_acc_trade_volume'],
        name="Volume",
        mode='lines',
        line=dict(color='magenta')
    ), row=2, col=1)

    # 이동평균선 추가

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


def request_data_byminute(start_date, end_date, ticker="KRW-BTC"):
    # 문자열을 datetime 객체로 변환
    start_datetime = datetime.strptime(start_date, "%Y%m%d")
    end_datetime = datetime.strptime(end_date, "%Y%m%d")

    # 원하는 포맷으로 변환
    start_date_formatted = end_datetime.strftime("%Y-%m-%d %H:%M:%S")
    end_date_formatted = end_datetime.strftime("%Y-%m-%d %H:%M:%S")
    # to로 써넣은 직전의 시간까지를 준다!
    timediff = end_datetime - start_datetime
    timediff = timediff.total_seconds() / 60
    df_to_return = pd.DataFrame()
    i = 0
    endless_param = 0
    while True:
        if endless_param > 1000000:
            break
        if i < int(timediff / 200):
            wanted_time = end_datetime - timedelta(minutes=i * 200)
            requested_df = request_minutedata_200(wanted_time.strftime("%Y-%m-%d %H:%M:%S"), 200, market=ticker)
            if type(requested_df) == int:
                pass
                print("passed")
            else:
                df_to_return = pd.concat([df_to_return, requested_df], ignore_index=True)
                i += 1

        elif i == int(timediff / 200):
            interval = timediff - 200 * i
            requested_df = request_minutedata_200(wanted_time.strftime("%Y-%m-%d %H:%M:%S"), int(interval))
            if type(requested_df) == int:
                pass
                print("passed")
            else:
                df_to_return = pd.concat([df_to_return, requested_df], ignore_index=True)
                i += 1


        else:
            print("ended")
            break


    return df_to_return

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
            requested_df = request_datedata_200(wanted_time.strftime("%Y-%m-%d %H:%M:%S"), 200, market=ticker)
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
            requested_df = request_datedata_200(wanted_time.strftime("%Y-%m-%d %H:%M:%S"), int(interval))
            if type(requested_df) == int:
                pass
                print("passed")
            else:
                df_to_return = pd.concat([df_to_return, requested_df], ignore_index=True)
                i += 1


        else:
            print("ended")
            break


    return df_to_return

def column_select(df):
    columns_to_select=['candle_date_time_kst','opening_price', 'high_price', 'low_price', 'trade_price', 'candle_acc_trade_price', 'candle_acc_trade_volume']
    return df[columns_to_select]
"""
stock_data=request_data_bydate("20241201","20241220","KRW-BTC")
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


