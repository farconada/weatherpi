#!/bin/bash
rrdtool create weather.rrd --start N --step 60 \
DS:tempdht22:GAUGE:600:U:U \
DS:tempbmp085:GAUGE:600:U:U \
DS:humidity:GAUGE:600:U:U \
DS:pressure:GAUGE:600:U:U \
RRA:AVERAGE:0.5:1:1440 \
RRA:AVERAGE:0.5:60:720 \
RRA:AVERAGE:0.5:1440:730

# 4 fuentes de datos, temperature DHT22 BMP085 humedad y presion atmosferica
# los datos se gurdan cada minuto
# media de 1 muestra (no hay media) durante 1440 minutos, es decir 24 horas
# media de 60 muestras (la media de la hora) durante 720 muestras/horas, es decir 1 mes
# media de 1440 muestras (1 dia) durante 730 muestras/dias, es decir 2 años
