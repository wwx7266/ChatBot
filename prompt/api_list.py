api_list_prompt = ("我们有以下api可以调用，分别用来解决不同的网络问题 "
                   "1. /api/reboot/ 用于重启路由器"
                   "2. /api/wifi_speed_test/{STA_MAC} 用于测试{STA_MAC}链接速度"
                   "3. /api/upgrade_bandwidth/ 用于升级带宽"
                   "其中 STA_MAC 代表了设备的MAC地址")

instruction = ("以下是解决故障的历史经验，请总结，并输出需要调用的API及其执行的顺序"
               "1. 当用户发现无法连接wifi时，执行重启路由器"
               "2. 当用户发现卡顿时，执行重启路由器，若重启路由器还卡顿时，需要执行宽带测速，当宽带测速不达标时，需要升级带宽")
