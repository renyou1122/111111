from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

# 這是補回來的！讓系統知道怎麼讀取其他頁面
@app.route('/get_page/<page_name>')
def get_page(page_name):
    # 這裡假設你的報告檔案放在 templates 資料夾，且副檔名是 .html
    # 如果你的檔案叫 "第七組的分組期末報告.html"，那 page_name 就會自動對應
    return render_template(f'{page_name}.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)