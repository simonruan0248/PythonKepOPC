import OpenOPC
import pywintypes
import time
import win32timezone

opc = OpenOPC.client()
opcserv='Kepware.KEPServerEX.V6'
opc.connect(opcserv)

pywintypes.datetime = pywintypes.TimeType


tag= ['Channel1.Device1.Tag1']
value = opc.read(tag)
print(value)

#while True:
v = opc.read(tag)  # 读取指定设备Device，组Group，标签Tag的数据
for i in range(len(v)):
    (name, val, qual, time1) = v[i]
print(type(val));
print(type(v));

time.sleep(0.2)
time.sleep(0.2)




#input('Press Enter to exit')