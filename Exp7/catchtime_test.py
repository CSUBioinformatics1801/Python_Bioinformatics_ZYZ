# import time
# begin=time.monotonic()
# while True:
#     print(time.strftime('%Y-%m-%d %H;%M;%S'),end='')
#     time.sleep(1)
#     print('\r',end='')
#     end=time.monotonic()
#     if end-begin>60:
#         break
from time import *
print(strftime('%Y-%m-%d %H;%M;%S'))