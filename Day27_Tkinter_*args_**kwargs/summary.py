def all_mix(a, *args, **kw):
  print(a, args, kw)
  
all_mix(4, 7, 3, 0, x=10, y=64)
# 4 (7, 3, 0) {'x': 10, 'y': 64}
