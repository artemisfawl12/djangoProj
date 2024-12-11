import openai
from openai import OpenAI
import os
import re
from counter.booleanway_new import trade
from counter.booleanway_new import trade_multiple
import logging
from pykrx import stock


logger=logging.getLogger('counter')

# ChatGPT에게 코드 요청

client = OpenAI(
    api_key=os.environ.get("OPEN_API_KEY")
)

model = "gpt-3.5-turbo"

def gpt_call_multi(try_count, buy_condition, sell_condition, start_date, end_date, received_ticker_list):
    #새로운 차트의 필요성이 느껴진다. char draw 값이 0일 때, 포트폴리오 변화와 총자산 변화정도를 보여줄 수 있는 것이 필요합니다.
    logger.info("gpt_call_multi function started")


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

    logger.info("query:" + query)
    logger.info("message to gpt sent")

    response = client.chat.completions.create(model=model, messages=messages)
    logger.info("message to gpt received")

    # ChatGPT의 응답에서 코드만 추출하기
    assistant_message = response.choices[0].message.content

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
        logger.info("python code not found")
    

    ret_list = trade_multiple(start_date, end_date, received_ticker_list, exec_code=execute_code)


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

    return ret_list



def gpt_call(try_count,buy_condition,sell_condition,start_date,end_date,received_ticker):
    logger.info("gpt_call function started")

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

    logger.info("query:"+query)
    logger.info("message to gpt sent")
    response = client.chat.completions.create(model=model, messages=messages)
    logger.info("message to gpt received")

    # ChatGPT의 응답에서 코드만 추출하기
    assistant_message = response.choices[0].message.content




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
        logger.info("python code not found")

    trade_received_list=trade(start_date, end_date, str(received_ticker), exec_code=execute_code)
    final_earning_percentage=trade_received_list[0]
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

    ret_list=[final_earning_percentage,assistant_message]
    ret_list.append(trade_received_list[1])

    return ret_list

"""
testlis=["000660","005930"]
answer=gpt_call_multi(0,"5일 이평선이 100일 이평선 상향돌파","5일 이평선이 20일 이평선 하향돌파","20200101","20241101",testlis)
print("총자산 start")
print(answer[3])
"""





