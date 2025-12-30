import os
import shutil
from flask_frozen import Freezer

# 1. 這裡改成抓取真正的 CMS 系統 (前面不能有空格)
from cmsimde.flaskapp import app

# 2. 設定
app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_DESTINATION'] = 'docs'

# 3. 強制讓機器人知道「期末報告」在哪裡
# 這樣就算首頁沒連結，它也會幫你印出來！
@freezer.register_generator
def get_page():
    # 這裡填入你動態網址 '/get_page/' 後面的那個名字
    yield {'name': '第七組的分組期末報告'}

print("🚀 開始建置靜態網站...")

# 4. 清除舊資料
if os.path.exists('docs'):
    shutil.rmtree('docs')

# 5. 轉檔
freezer = Freezer(app)
try:
    freezer.freeze()
    print("❄️  HTML 轉檔完成")
except Exception as e:
    print(f"⚠️ 轉檔警告: {e}")

# 6. 搬運圖片 (包含 cmsimde 資料夾內的圖片)
static_locations = ['static', 'cmsimde/static', 'content']
for location in static_locations:
    if os.path.exists(location):
        dest = 'docs/static'
        if not os.path.exists(dest):
            try:
                shutil.copytree(location, dest)
                print(f"📦 已備份資源: {location}")
            except:
                pass

print("-" * 30)
print("✅ 建置完成！請輸入 git add . && git commit -m 'Final' && git push")