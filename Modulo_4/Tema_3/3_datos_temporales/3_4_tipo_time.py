from datetime import time



t= time (12, 10, 0, 0)
print(t)

t1 = time.fromisoformat('04:23:01')
print(t1)
t2 = time.fromisoformat('04:23:01+04:00')
print(t2)