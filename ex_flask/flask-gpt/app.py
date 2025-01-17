from flask import Flask, request, render_template, redirect, render_template_string
import base64
import openai
import re
import os

app = Flask(__name__)
Key = '승인 받은 API 키'
client = openai.OpenAI(api_key=Key)

def encode_image(img_path):
    with open(img_path, 'rb') as file:
        return base64.b64encode(file.read()).decode('utf-8')

def clean_res(text):
    res_text = text.replace("```html","").replace("```","").replace('"','')
    return res_text

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    price = request.form['price']
    file_path = os.path.join('uploads', file.filename)
    file.save(file_path)
    base64_img = encode_image(file_path)
    res = client.chat.completions.create(
        model='gpt-4o',
        messages = [
            {'role':'system', 'content':'이미지가 어떤 제품인지 `제품명`, `카테고리`, `컬러` '},
            {'role':'user', 'content':[
                {'type':'text', 'text':'제품 판매를 위한 상품 정보를 찾아줘'},
                {'type':'image_url', 'image_url':{
                    'url':f'data:image/png;base64,{base64_img}'
                }}
            ]}
        ],
        temperature=0.0
    )
    prod = res.choices[0].message.content
    print(prod)
    completion = client.chat.completions.create(
        model='gpt-4o',
        messages = [
            {'role':'system'
            , 'content':f'''너는 상품 판매 담당자야.
                            상품의 정보를 가지고 판매 관련 서류를 작성해줘. 상품 가격은: {price}원.
                            작성내용은 html 문서 형식으로 div tag 안에 넣을 내용을 작성해줘'''}
            ,{'role':'user', 'content':prod}
        ]
    )
    print('result: ', completion.choices[0].message.content)
    clean_text = clean_res(completion.choices[0].message.content)
    return render_template_string('<div>{{sales_plan | safe}}</div>', sales_plan=clean_text)

if __name__ == '__main__':
    app.run(debug=True)