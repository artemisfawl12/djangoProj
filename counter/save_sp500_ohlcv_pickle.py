import yfinance as yf
import pandas as pd
import pickle
from datetime import datetime


# 1. S&P 500 종목 리스트 수집 (Wikipedia 기준)
def get_sp500_tickers():
    table = pd.read_html("https://en.wikipedia.org/wiki/List_of_S%26P_500_companies")
    df = table[0]
    tickers = df["Symbol"].tolist()
    # 일부 ticker는 '.' 대신 '-' 로 바꿔야 yfinance에 호환됨 (예: BRK.B → BRK-B)
    tickers = [ticker.replace('.', '-') for ticker in tickers]
    print(tickers)
    return tickers


# 2. OHLCV + hl_mean 다운로드 및 저장
def download_and_save_sp500_data(save_path="sp500_data.pkl"):
    tickers = get_sp500_tickers()
    stock_data = {}

    for i, ticker in enumerate(tickers):
        try:
            print(f"[{i + 1}/{len(tickers)}] 다운로드 중: {ticker}")
            df = yf.download(ticker, period="1y", interval="1d", progress=False)
            if df.empty:
                print(f"❗ 데이터 없음: {ticker}")
                continue
            df["hl_mean"] = (df["High"] + df["Low"]) / 2
            stock_data[ticker] = df
        except Exception as e:
            print(f"⚠️ {ticker} 다운로드 실패: {e}")

    # 저장
    with open(save_path, "wb") as f:
        pickle.dump(stock_data, f)

    print(f"\n✅ 저장 완료: {save_path} (총 {len(stock_data)}종목)")
    return stock_data


# 실행
if __name__ == "__main__":
    download_and_save_sp500_data("sp500_ohlcv_1y.pkl")