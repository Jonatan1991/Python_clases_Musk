from datetime import timedelta
delta = timedelta(days=50, seconds=27, microseconds=10, milliseconds=29000, minutes=5, hours=8, weeks=2)
print(delta)

dela = timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
print(dela)

d1 = timedelta(days=10)
d2 = timedelta(days=2)
print(d1 + d2)
print(d1 - d2)
print(d2 - d1)
print(d1 / d2)
print(d1 // d2)
print(d1 % d2)

print(d1 * 2)
print(d1 * 2.5)

print(abs(-d1))
print(str(d1), type(str(d1)))
print(repr(d1))

print(d1 == d2)
print(d1 > d2)

