#!/bin/bash
rrdtool create current_sensor.rrd --start N --step 60 \
DS:power:GAUGE:600:U:U \
DS:intensity:GAUGE:600:U:U \
RRA:AVERAGE:0.5:1:1440 \
RRA:AVERAGE:0.5:15:36000 

# 2 fuentes de datos, intensidad en Amperios y potencia aparente en Watios
# los datos se gurdan cada minuto
# media de 1 muestra (no hay media) durante 1440 minutos, es decir 24 horas
# media de 15 muestras (la media de la hora) durante 36000 muestras/horas, es decir 1 mas de un año para tener un detalle elevado
