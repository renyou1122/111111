from flask_frozen import Freezer
from main import app  # 把 app 改成 main
import shutil
import os

# 1. 設定冷凍庫
# FREEZER_RELATIVE_URLS = True 代表產生的連結會自動修正
# (這樣放在 GitHub Pages 的子目錄才不會破圖)
app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_DESTINATION'] = 'docs'  # 我們把靜態檔存在 'docs' 資料夾，方便 GitHub 抓取

freezer = Freezer(app)

# 2. 清除舊的 docs 資料夾 (如果有)
if os.path.exists('docs'):
    shutil.rmtree('docs')
    print("🧹 清除舊的靜態檔案...")

# 3. 開始冷凍 (轉檔)
print("❄️ 開始將 Flask 轉為靜態網站...")
try:
    freezer.freeze()
    print("✅ 成功！靜態網站已產生在 'docs' 資料夾中。")
    print("👉 裡面包含了 index.html 和 static 資料夾。")
except Exception as e:
    print(f"❌ 發生錯誤：{e}")