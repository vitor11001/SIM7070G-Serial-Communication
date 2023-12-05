import os


COMANDS_AT_GENERALS = [
    'AT+CMEE=1',
    'AT+CPIN?',
    'AT+CSQ',
    'AT+CGATT?',
    'AT+CMNB=1',
    'AT+COPS?',
    'AT+CGNAPN',
    'AT+CNACT=0,1',
]

# COMANDS_AT_GENERALS = [
#     'AT+CFUN=0',
#     'AT+CGDCONT=1,,"wl.vivo.com.br"',
#     'AT+CFUN=1',
#     'AT+CGNAPN',
#     'AT+CNACT=0,1',
# ]

COMANDS_AT_MQTT = [
    'AT+SMCONF="CLIENTID","mqttx_7"',
    'AT+SMCONF="URL","dev-mqtt.senfio.com.br","1883"',
    f'AT+SMCONF="USERNAME","{os.environ["MQTT_USERNAME"]}"',
    f'AT+SMCONF="PASSWORD","{os.environ["MQTT_PASSWORD"]}"',
    'AT+SMCONN',
    'AT+SMUNSUB="senfio/monitore/explorer/jiga/+"',
    'AT+SMSUB="senfio/monitore/explorer/jiga/+",1',
    'AT+SMPUB="senfio/monitore/explorer/jiga/321",5,1,1',
    'hello',
    'AT+SMPUB="senfio/monitore/explorer/jiga/321",1,1,1',
    "",
    'AT+SMUNSUB="senfio/monitore/explorer/jiga/+"',
    'AT+SMDISC',
]

COMANDS_AT_GNSS = [
    'AT+SGNSCMD=1,0',
]
