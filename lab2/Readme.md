Скрипт написан на языке Python, запускается через docker.

Собираем образ:
```
docker build . -t lab2 -f Dockerfile
```
Запускаем образ:
```
docker run --rm -i -t lab2
```
Запускаем скрипт (в качестве хоста можем взять например google.com):
```
python3 mtu.py google.com
```

***Использование***
```
usage: python3 mtu.py [-h] [-c COUNT] host

positional arguments:
  host                  host address

optional arguments:
  -h, --help            show this help message and exit
  -c COUNT, --count COUNT
                        option of ping command: stop after sending count ECHO_REQUEST packets
```