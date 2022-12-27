# PingTrends on WSL2 / Unbuntu

## Aim
1. Obtain a PING latency result 
2. Push onto a KAFKA topic
3. Client 1 - listen to topic and put into Google Sheets store
4. Client 2 - listen to topic and put into local SQLlite store
5. Client 3 - listen to topic and put into local MongoDB store
6. Client 4 - listen to topic and just display


## Hints
1. grabbing right element of result
```
LATENCY=$(ping -c 2 localhost| awk -F '[= ]' '/time/ { print $11}')
```
