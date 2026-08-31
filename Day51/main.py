from collections import deque

tasks = deque(["下載檔案", "處理資料", "產生報告"])

tasks.append("寄送 Email")

tasks.appendleft("修復錯誤")

current_task = tasks.popleft()

print(f"正在執行：{current_task}")
print(tasks)