import yfinance as yf
import pandas as pd
import pickle
from datetime import timedelta

# 기존 파일 로딩
with open("stock_data.pkl", "rb") as f:
    stock_data = pickle.load(f)

for ticker in stock_data.keys():
    old_df = stock_data[ticker]
    last_date = old_df.index[-1].date()

    # 다음날부터 오늘까지 받기
    start_date = last_date + timedelta(days=1)
    new_df = yf.download(ticker, start=start_date.strftime("%Y-%m-%d"))

    if not new_df.empty:
        new_df["hl_mean"] = (new_df["High"] + new_df["Low"]) / 2
        combined_df = pd.concat([old_df, new_df])
        stock_data[ticker] = combined_df.drop_duplicates()

# 덮어쓰기
with open("stock_data.pkl", "wb") as f:
    pickle.dump(stock_data, f)