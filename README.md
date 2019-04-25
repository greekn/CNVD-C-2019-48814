# CNVD-C-2019-48814

#POC 检测脚本说明：这个poc脚本是直接执行命令不会回显的所以使用ceye 接口进行漏洞检测

默认进行的触发是 dns 加ping 所以需要加标识符，通过ceyeapi返回的数据进行判断。

#usage： poc.py http://192.168.237.128:7001 tag123

![image](https://github.com/greekn/CNVD-C-2019-48814/blob/master/1.png)

![image](https://github.com/greekn/CNVD-C-2019-48814/blob/master/2.png)
