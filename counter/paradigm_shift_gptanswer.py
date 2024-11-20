from openai import OpenAI
import os
import re
from counter.booleanway_new import trade

# ChatGPT에게 코드 요청

print("api_key print:"+str(os.environ.get("OPEN_API_KEY")))
client = OpenAI(
    api_key=os.environ.get("OPEN_API_KEY"),
)

model = "gpt-4"

def gpt_call(try_count,buy_condition,sell_condition,start_date,end_date,received_ticker):

    query = (

            """
            stock_data는 index를 날짜로 갖는 python dataframe이고, 각 column의 이름은 "시가", "고가", "저가", "종가", "거래량", "등락률" 순이다. 이미 내가 갖고 있는 데이터이니 새로 생성하지 마라.
            즉 절대 가상의 데이터를 생성하지 마라.
            이 dataframe을 가지고 
            <
            """
            + buy_condition + """>
    에 대한 조건문을 python 수식으로 작성해서 condition_buy 라는 이름의 booleanseries를 얻는 코드를 작성하라.
    condition_buy는 새로운 객체여야 한다.

    동일 상황에서 """

            + sell_condition +
            """
            에 대한 조건문을 python 수식으로 작성하여 booleanseries를 얻는 코드도 같이 작성해라.
            이번 boolean series의 이름은 condition_sell이다.
            만약에 loc을 쓸 일이 있으면, 코딩할때 일주일은 5일이기때문에 loc을 이용하다간 없는 날짜를 호출할 수 있으니 iloc을 쓰도록 해.
            지표 생성 코딩할 때 loc이 0인데 loc-1 데이터를 불러올려고하면 당연히 말이안돼. 이런식의 결측치 처리를 잘하도록 해
        
            """
    )

    messages = [{
        "role": "system",
        "content": "you are a helpful assistant"

    }, {
        "role": "user",
        "content": query
    }]
    print("messeage sent")
    """
    response = client.chat.completions.create(model=model, messages=messages)

    # ChatGPT의 응답에서 코드만 추출하기
    assistant_message = response.choices[0].message.content
    """
    assistant_message="""
    조건에 맞는 boolean series를 생성하기 위해 pandas의 rolling 및 shift 메서드 등을 사용하겠습니다.

1. 먼저, 100일 이동평균선, 5일 이동평균선, 20일 이동평균선을 각각 계산할 것입니다.
2. 계산한 이동평균선을 사용하여 구매 및 판매 조건에 따른 조건문을 작성하고 이를 조건문 수식으로 변환할 것입니다.
3. 또한 이전의 행을 참조하면서 현재 행의 값을 비교하려면 shift 메서드가 사용됩니다.

아래에 작성한 코드를 볼 수 있습니다.

```python
# 이동평균선 계산
stock_data['MA100'] = stock_data["종가"].rolling(window=100).mean()
stock_data['MA5'] = stock_data["종가"].rolling(window=5).mean()
stock_data['MA20'] = stock_data["종가"].rolling(window=20).mean()
stock_data['volume_MA5'] = stock_data["거래량"].rolling(window=5).mean()

# 구매 조건
condition_buy =  (
    (stock_data['MA100'].diff() >= 0) |
    (stock_data['MA100'].diff() < stock_data['종가'] * 0.001)
) & (
    (stock_data['종가'].shift(5) > stock_data['종가']) &
    (stock_data['volume_MA5'].shift(5) > stock_data['volume_MA5'])
)

# 판매 조건
stock_data['MA_crossdown'] = stock_data['MA5'] < stock_data['MA20']
condition_sell = (stock_data['MA_crossdown'] == True) & (stock_data['MA_crossdown'].shift(1) == False)
```

위 코드에서 구매 조건은 MA100 값이 증가하거나, 혹은 그 감소량이 종가의 0.1% 미만인 경우이며, 동시에 5일 전보다 종가 및 거래량이 모두 감소해야합니다.

판매 조건은 MA5가 MA20을 하향 돌파하는 경우입니다. 즉, 오늘 MA5가 MA20보다 작고 어제 MA5가 MA20보다 크다면 True(즉, 매도)가 될 것입니다.

참고로, 이동평균선 값 계산이나 다른 연산에서 앞선 데이터를 필요로 하므로, 일부 데이터에서는 NaN 값이 발생할 수 있습니다. 이를 해결하기 위해 알맞은 방법으로 전처리 하기 바랍니다. 
    
    """



    # 코드 필터링: ```로 감싸진 모든 코드 부분 추출
    code_blocks = re.findall(r"```python\n(.*?)\n```", assistant_message, re.DOTALL)

    # 모든 코드 블록을 출력



    execute_code = ""
    if code_blocks:
        for i, code in enumerate(code_blocks, start=1):
            execute_code += str(code + "\n")
        print("*************************************")
        print("여기서부턴 실제 실행될 코드들을 쓰겠습니다.")
        print(execute_code)
        print("*************************************")

    else:
        print("python 코드를 찾을 수 없습니다.")

    final_earning_percentage=trade(start_date, end_date, str(received_ticker), exec_code=execute_code)
    print(str(final_earning_percentage))
    final_earning_percentage=str(float(final_earning_percentage)*100)+"%"





    """
    user_check = input("이 답변 및 로직에 만족하시나요? 만족하면 y, 만족하지 않으면 n을 입력해주세요: ")
    if user_check == "y":
        trade(start_date, end_date, str(received_ticker), exec_code=execute_code, chart_draw=1)

    elif try_count + 1 < 3:
        print("okay sorry")
        try_count += 1
        print("try one more time. you used this" + str(try_count) + "times, and 3 is maximum")
        gpt_call(try_count)
    """

    print(final_earning_percentage + "at paradigm file")

    return final_earning_percentage

#gpt_call(0,".",".","20200101","20241101","000660")





