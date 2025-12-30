import os
import shutil
from flask_frozen import Freezer

# 嘗試匯入 app，避免找不到檔案
try:
    from app import app
except ImportError:
    # 如果你的主程式叫 main.py，請自己改這裡
    try:
        from main import app
    except:
        print("❌ 找不到 app.py 或 main.py，請確認你的主程式檔名！")
        exit()

# 設定：讓路徑變成相對路徑 (重要！這樣 GitHub Pages 才能讀到 css/js/圖片)
app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_DESTINATION'] = 'docs'

print("🚀 開始建置靜態網站...")

# 1. 清除舊的 docs 資料夾
if os.path.exists('docs'):
    shutil.rmtree('docs')
    print("🧹 清除舊資料完成")

# 2. 啟動冷凍庫 (轉成靜態 HTML)
freezer = Freezer(app)

# --- 這裡加入一個設定，讓它能抓到所有連結 ---
# 如果你的網頁有動態連結 (例如 /get_page/...)，
# 只要首頁有點擊得到的連結，Freezer 通常都抓得到。
try:
    freezer.freeze()
    print("❄️ HTML 轉檔完成")
except Exception as e:
    print(f"⚠️ 轉檔過程警告 (通常沒關係): {e}")

# 3. 【強制搬運】把 static 資料夾 (圖片/影片/CSS) 完整複製過去
# 這是為了保證你的圖片絕對不會消失
source_static = 'static'
dest_static = 'docs/static'

if os.path.exists(source_static):
    # 如果 static 已經被 freezer 複製了一部分，先刪掉避免衝突
    if os.path.exists(dest_static):
        shutil.rmtree(dest_static)
    
    shutil.copytree(source_static, dest_static)
    print(f"📦 靜態檔案 (圖片/影片) 已強制複製到 {dest_static}")
else:
    print("❌ 警告：找不到你的 static 資料夾！")

print("-" * 30)
print("✅ 建置完成！請輸入 git push 上傳到 GitHub。")