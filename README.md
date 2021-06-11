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
```
(venv) C:\Users\Loliconshik\PycharmProjects\pr>python tracert-as.py google.com
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

(venv) C:\Users\Loliconshik\PycharmProjects\pr>python tracert-as.py 8.8.8.8
№    IP                  AS        Country   Provider
0    10.113.224.1        bogon     -         -
1    10.254.253.252      bogon     -         -
2    10.255.201.6        bogon     -         -
3    10.255.101.5        bogon     -         -
4    10.255.100.2        bogon     -         -
5    195.239.186.161     3216      RU        AS PJSC Vimpelcom
6    79.104.235.213                RU
7    72.14.213.116       15169     RU        AS Google LLC
8    108.170.250.146     15169     RU        AS Google LLC
9    209.85.249.158      15169     US        AS Google LLC
10   216.239.57.222      15169     RU        AS Google LLC
11   142.250.56.129      15169     US        AS Google LLC
12   8.8.8.8             15169     US        AS Google LLC

(venv) C:\Users\Loliconshik\PycharmProjects\pr>python tracert-as.py vk.com
№    IP                  AS        Country   Provider
0    10.113.224.1        bogon     -         -
1    10.254.253.252      bogon     -         -
2    10.255.201.6        bogon     -         -
3    10.255.101.5        bogon     -         -
4    10.255.100.2        bogon     -         -
5    195.239.186.161     3216      RU        AS PJSC Vimpelcom
6    195.218.233.125     3216      RU        AS PJSC Vimpelcom
7    213.221.63.170      3216      RU        AS PJSC Vimpelcom
8    93.186.225.208      47541     RU        AS VKontakte Ltd


```
