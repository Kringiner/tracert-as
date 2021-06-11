# tracert-as

Задача по протоколам интернет:
выводит результат трасировки с доп информацией для белых адресов
определяет страну промежуточного IP вместе с верным whois сервером


### Запуск
```
tracert-as.py google.com
```
IP-адрес (или DNS-имя) передается в качестве аргумента командной строки

### Пример работы
(venv) C:\Users\Loliconshik\PycharmProjects\sntp_server>python tracert-as.py google.com
№    IP                  AS        Country   Provider
0    10.113.224.1        bogon     -         -
1    10.254.253.252      bogon     -         -
2    10.255.201.6        bogon     -         -
3    10.255.101.5        bogon     -         -
4    10.255.100.2        bogon     -         -
5    195.239.186.161     3216      RU        AS PJSC Vimpelcom
6    79.104.235.215                RU
7    72.14.205.76        15169     RU        AS Google LLC
8    108.170.250.66      15169     RU        AS Google LLC
9    142.251.49.78       15169     US        AS Google LLC
10   172.253.65.159      15169     US        AS Google LLC
11   172.253.70.51       15169     US        AS Google LLC
12   173.194.73.100      15169     US        AS Google LLC
