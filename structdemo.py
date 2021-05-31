# coding=utf-8
import struct
import socket

host = '127.0.0.1'
port = 6000
bufsize = 256
address = (host, port)


def checkCRC(message):
    crc = 0x00
    for byte in message:
        crc ^= ord(byte)
        for x in range(8):
            if crc & 1:
                crc = (crc >> 1) ^ 0x8408
            else:
                crc = crc >> 1
    return crc


# ----1.2	设备信息
# 设备型号
DeviceType = '\x17\x00\x04' + '\x00' * 20
# 设备生产序列号
DeviceType1 = '\x17\x00\x05' + '\x00' * 20
# 设备经度
DeviceType2 = '\x17\x00\x07' + '\x00' * 20
# 设备纬度
DeviceType3 = '\x17\x00\x08' + '\x00' * 20
# 监控版本信息
DeviceType4 = '\x17\x00\x0A' + '\x00' * 20

# ----1.3	网管参数
# 站点编号
DeviceType5 = '\x07\x01\x01' + '\x00' * 4
# 设备编号
DeviceType6 = '\x04\x01\x02' + '\x00' * 1
# 监控中心IP地址（IP v4）
DeviceType7 = '\x07\x01\x30' + '\x00' * 4
# 监控中心IP地址端口号
DeviceType8 = '\x05\x01\x31' + '\x00' * 2
# 设备端口号
DeviceType9 = '\x05\x01\x39' + '\x00' * 2

# ----1.4	告警和状态
# 功放过温告警
DeviceType10 = '\x04\x03\x06' + '\x00' * 1
# 光收发告警
DeviceType11 = '\x04\x03\x0E' + '\x00' * 1
# 下行输出欠功率告警
DeviceType12 = '\x04\x03\x13' + '\x00' * 1
# 下行驻波比告警
DeviceType13 = '\x04\x03\x14' + '\x00' * 1

# ----1.5	实时采样数据
# 功放温度值
DeviceType14 = '\x04\x05\x01' + '\x00' * 1
# 下行输出功率电平
DeviceType15 = '\x04\x05\x03' + '\x00' * 1
# 下行驻波比值
DeviceType16 = '\x04\x05\x06' + '\x00' * 1
# 上行输出功率电平
DeviceType17 = '\x04\x05\x0D' + '\x00' * 1
# 光收功率
DeviceType18 = '\x04\x05\x0E' + '\x00' * 1
# 光发功率
DeviceType19 = '\x04\x05\x0F' + '\x00' * 1

print "DeviceType:", DeviceType, 'len:', len(DeviceType)
MAP_A = '\x02\xff' + DeviceType
print "MAP_A:", MAP_A, "len:", len(MAP_A)
zhandianbiaohao3 = '\x00'
zhandianbiaohao4 = '\x01'
shebeibianhao = '\xff'
CommunicatePackageFlag = '\x00\x00'  # 低字节在前 0x0000-0x7fff监控发起的通讯
npInterActiveFlag = '\x80'
APID = '\x01'
NP_A = zhandianbiaohao4 + zhandianbiaohao3 + '\x01\x15' + shebeibianhao + CommunicatePackageFlag + npInterActiveFlag + APID + MAP_A

print 'NP_A:', NP_A, "len:", len(NP_A)

AP_C = '\x03\x01' + NP_A
print 'AP_C:', AP_C, "len:", len(AP_C)

print hex(checkCRC(AP_C))

strhex = '\x01\x02\x03\x04\x05'
splitsss = strhex[1:-1]
for i in splitsss:
    print ord(i)

udpclient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    udpclient.sendto(AP_C, address)
    data, server_addr = udpclient.recvfrom(bufsize)
    print("recv", data, server_addr)
