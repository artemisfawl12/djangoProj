import cv2
import pickle
from scipy.signal import resample
from scipy.spatial.distance import euclidean
import numpy as np
import pandas as pd

def image_process(image,img_range):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # 색상 범위 정의 (빨간색 및 파란색)
    lower_red1 = np.array([0, 70, 50])
    upper_red1 = np.array([10, 255, 255])
    lower_red2 = np.array([170, 70, 50])
    upper_red2 = np.array([180, 255, 255])
    lower_blue = np.array([100, 150, 0])
    upper_blue = np.array([140, 255, 255])

    # 마스크 생성
    mask_red = cv2.inRange(hsv, lower_red1, upper_red1) | cv2.inRange(hsv, lower_red2, upper_red2)
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
    mask = mask_red | mask_blue
    masked_image = cv2.bitwise_and(image, image, mask=mask)

    # 이진화
    gray_masked = cv2.cvtColor(masked_image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray_masked, 50, 255, cv2.THRESH_BINARY)

    # 시계열 추출 (ys 개수가 10개 이상일 때만)
    height, width = binary.shape
    base_height = 5
    aspect_ratio = width / height
    fig_width = aspect_ratio * base_height

    middle_line_final = []
    valid_x_final = []

    for x in range(width):
        ys = np.where(binary[:, x] > 0)[0]
        if len(ys) >= 10:
            y_center = int(np.median(ys))
            middle_line_final.append(height - y_center)
            valid_x_final.append(x)
    from scipy.signal import resample

    # middle_line_final 데이터를 200포인트로 리샘플링
    resampled_y = resample(middle_line_final, img_range)
    return resampled_y
def minmax_normalize(x):
    return (x - np.min(x)) / (np.max(x) - np.min(x) + 1e-8)
def find_best(image_name,img_range_num, data_dict, window_size=120,top_n=5, progress_callback=None):
    #data_dict에 티커별 가격 dataframe 들어오게.
    #resampled에 resampled_y 들어오게
    resampled=image_process(image_name,img_range_num)
    query_series = minmax_normalize(resampled)
    stride = 1
    result_list=[]
    total = len(data_dict)+1
    for key, df in data_dict.items():
        df_new = df[["hl_mean"]].dropna().reset_index(drop=True)
        # dropna()로 제거되지 않은 날짜들만 따로 추출
        valid_dates = df[["High", "Low"]].dropna().index.to_list()

        try:
            scores = []
            indices = []
            for i in range(0, len(df_new) - window_size + 1, stride):
                window = df_new["hl_mean"].iloc[i:i + window_size].values
                #window_resampled = resample(window, 120)
                window_norm = minmax_normalize(window)
                dist = euclidean(query_series, window_norm)
                scores.append(dist)
                indices.append(i)
            best_index = indices[np.argmin(scores)]
            best_date = valid_dates[best_index]
            result = {
                "ticker": key,
                "best_index":best_index,
                "best_date": best_date,
                "best_score": np.min(scores),
            }
            result_list.append(result)
            progress_callback(i + 1, total)

        except:
            print("passed")
            pass

    # 2. DataFrame으로 변환
    df = pd.DataFrame(result_list)
    # 3. 정렬
    df_sorted = df.sort_values("best_score").head(top_n)
    # 4. 상위 top_n개 추출

    # best_window 열 추가
    def get_best_window(row):
        ticktempdf = data_dict[row["ticker"]]
        return ticktempdf["hl_mean"].iloc[row["best_index"]:row["best_index"] + window_size].values

    df_sorted["best_window"] = df_sorted.apply(get_best_window, axis=1)
    top5_list = df_sorted.to_dict(orient="records")
    print("find_best done")

    return top5_list

# 이미지 경로
"""
image_path = "C:/Users/82109/Documents/chartex_2.jpg"

# 이미지 불러오기 및 HSV 변환
image = cv2.imread(image_path)
with open("sp500_ohlcv_1y.pkl", "rb") as f:
    data = pickle.load(f)
top5=find_best(image,120,data,120,5)
print(top5)"""




