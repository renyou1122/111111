import os
import shutil
from flask_frozen import Freezer

# 1. 【關鍵修正】正確匯入 app (前面不可以有空格！)
from cmsimde.flaskapp import app

# 2. 設定
app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_DESTINATION'] = 'docs'

print("🚀 開始建置靜態網站 (CMS版)...")

# 3. 清除舊資料
if os.path.exists('docs'):
    shutil.rmtree('docs')
    print("🧹 舊資料清理完畢")

# 4. 開始轉檔
freezer = Freezer(app)

try:
    freezer.freeze()
    print("❄️  HTML 轉檔完成")
except Exception as e:
    print(f"⚠️ 轉檔過程警告: {e}")

# 5. 【加強版搬運】嘗試搬運 cmsimde 裡的 static 資源
# 因為你的系統比較複雜，圖片可能藏在不同地方，我們都試著搬搬看
static_locations = ['static', 'cmsimde/static', 'content']

for location in static_locations:
    if os.path.exists(location):
        # 目標路徑
        dest = f'docs/{location}'
        
        # 如果是 static 資料夾，我們把它合併到 docs/static
        if location == 'static' or location == 'cmsimde/static':
            dest = 'docs/static'
        
        # 執行複製
        try:
            # 如果目標不存在才複製，避免覆蓋
            if not os.path.exists(dest):
                shutil.copytree(location, dest)
                print(f"📦 已備份資源: {location} -> {dest}")
        except Exception as e:
            pass # 忽略重複複製的錯誤

print("-" * 30)
print("✅ 建置完成！請輸入 git add . && git commit -m 'CMS轉檔' && git push")