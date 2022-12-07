# Домашнее задание 1.

Лабораторная работа в файле *lab1.unl*, ниже выводы с устройств, подтверждающие работоспособность конфигурации.

Линк между коммутаторами уровня доступ заблокирован протоколом STP. Проверить это можно с помощью *wireshark*.

***Client 1:***
```
VPCS> ip 10.0.10.2 255.255.255.0 10.0.10.1
Checking for duplicate address...
VPCS : 10.0.10.2 255.255.255.0 gateway 10.0.10.1

VPCS> show ip

NAME        : VPCS[1]
IP/MASK     : 10.0.10.2/24
GATEWAY     : 10.0.10.1
DNS         : 
MAC         : 00:50:79:66:68:05
LPORT       : 20000
RHOST:PORT  : 127.0.0.1:30000
MTU         : 1500

VPCS> ping 10.0.20.2

84 bytes from 10.0.20.2 icmp_seq=1 ttl=63 time=1.313 ms
84 bytes from 10.0.20.2 icmp_seq=2 ttl=63 time=1.377 ms
84 bytes from 10.0.20.2 icmp_seq=3 ttl=63 time=1.195 ms
84 bytes from 10.0.20.2 icmp_seq=4 ttl=63 time=1.255 ms
84 bytes from 10.0.20.2 icmp_seq=5 ttl=63 time=1.218 ms
```

***Client 1:***
```
VPCS> ip 10.0.20.2 255.255.255.0 10.0.20.1
Checking for duplicate address...
VPCS : 10.0.20.2 255.255.255.0 gateway 10.0.20.1

VPCS> show ip

NAME        : VPCS[1]
IP/MASK     : 10.0.20.2/24
GATEWAY     : 10.0.20.1
DNS         : 
MAC         : 00:50:79:66:68:06
LPORT       : 20000
RHOST:PORT  : 127.0.0.1:30000
MTU         : 1500

VPCS> ping 10.0.10.2

84 bytes from 10.0.10.2 icmp_seq=1 ttl=63 time=1.228 ms
84 bytes from 10.0.10.2 icmp_seq=2 ttl=63 time=1.132 ms
84 bytes from 10.0.10.2 icmp_seq=3 ttl=63 time=1.179 ms
84 bytes from 10.0.10.2 icmp_seq=4 ttl=63 time=1.155 ms
84 bytes from 10.0.10.2 icmp_seq=5 ttl=63 time=1.114 ms
```