# mouse_auto_click

需要使用系統管理元身份執行

## Winodws system

透過 python venv
```
py -3.10 -m venv ./.venv
./.venv/Script/Activate.ps1
python -m pip install -r requirements.txt
python ./app.py
```
開啟後將滑鼠移動到要自動點擊的位置，按下h鍵(如果沒有反應需多按幾次)，就可開始點擊，要結束時再次按下h鍵(一樣如果沒有反應需多按幾次)，就可停止點擊接下來就可到終端機關閉。