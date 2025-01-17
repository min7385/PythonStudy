# pip install openai
from openai import OpenAI
import os
# key = os.environ['OPENAI_API_KEY']
# print(key)
key = '승인 받은 API 키'
client = OpenAI(api_key=key)
system = """
    너는 음식점 AI 비서
    다음은 우리 음식점의 메뉴
    - 삼겹살
    - 대패 삼겹살
    - 물냉면
    삼겹살 1인분 5000원, 대패 3000원, 물냉 2000원
    해당 메뉴 말고 다른 메뉴는 없어!
"""
message = [{'role':'system', 'content':system}]

def ask(text):
    user_input = {'role':'user', 'content':text}
    message.append(user_input)
    res = client.chat.completions.create(model='gpt-3.5-turbo', messages=message)
    bot_text = res.choices[0].message.content
    # 대화 내용을 추가
    bot_res = {'role':'assistant', 'content':bot_text}
    message.append(bot_res)
    return bot_text
while True:
    user = input("주문하세요: ")
    bot = ask(user)
    print(f'bot: {bot}')