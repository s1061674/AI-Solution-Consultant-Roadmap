from pathlib import Path
import json

file = Path("data/student.json")

# 1. 讀取 JSON
data = json.loads(file.read_text())

# 2. 修改資料
data["score"] = 999

# 3. 存回 JSON
file.write_text(json.dumps(data, indent=4))

# 4. 驗證
print(file.read_text())