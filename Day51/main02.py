from collections import deque

history = deque(maxlen=3)

history.append("YouTube")
history.append("GitHub")
history.append("ChatGPT")
history.append("Google")

print(history)