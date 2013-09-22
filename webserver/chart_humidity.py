import rrdtool
import cfg
import os

def updateHumidityCharts():
    path24h = os.path.dirname(__file__) + '/static/img/humidity24.png'
    path1Week = os.path.dirname(__file__) + '/static/img/humidity1Week.png'
    path1Month = os.path.dirname(__file__) + '/static/img/humidity1Month.png'
    rrdtool.graph(path24h,
              '--imgformat', 'PNG',
              '--width', cfg.CHART_WIDTH,
              '--height', cfg.CHART_HEIGHT,
              '--start', 'end-1d',
              '--color', 'BACK#FFFFFF',
              '--vertical-label', '%',
              '--title', 'Humedad 24h',
              'DEF:humidity=' + cfg.RRDPATH +':humidity:AVERAGE',
	      'DEF:humidityext=' + cfg.RRDSENSORPATH +':humidity:AVERAGE',
              'LINE2:humidity#3366CC:Humedad',
	      'AREA:humidityext#af5cbd80:Humedad exterior',
              'GPRINT:humidity:LAST:Actual\: %2.2lf',
              'GPRINT:humidity:AVERAGE:Media\: %2.2lf',
              'GPRINT:humidity:MAX:Max\: %2.2lf',
              'GPRINT:humidity:MIN:Min\: %2.2lf')


    rrdtool.graph(path1Week,
              '--imgformat', 'PNG',
              '--width', cfg.CHART_WIDTH,
              '--height', cfg.CHART_HEIGHT,
              '--start', 'end-1w',
              '--color', 'BACK#FFFFFF',
              '--vertical-label', '%',
              '--title', 'Humedad 1 Semana',
              'DEF:humidity=' + cfg.RRDPATH +':humidity:AVERAGE',
	      'DEF:humidityext=' + cfg.RRDSENSORPATH +':humidity:AVERAGE',
              'LINE2:humidity#3366CC:Humedad',
	      'AREA:humidityext#af5cbd80:Humedad exterior',
              'GPRINT:humidity:LAST:Actual\: %2.2lf',
              'GPRINT:humidity:AVERAGE:Media\: %2.2lf',
              'GPRINT:humidity:MAX:Max\: %2.2lf',
              'GPRINT:humidity:MIN:Min\: %2.2lf')


    rrdtool.graph(path1Month,
              '--imgformat', 'PNG',
              '--width', cfg.CHART_WIDTH,
              '--height', cfg.CHART_HEIGHT,
              '--start', 'end-4w',
              '--color', 'BACK#FFFFFF',
              '--vertical-label', '%',
              '--title', 'Humedad 1 Mes',
              'DEF:humidity=' + cfg.RRDPATH +':humidity:AVERAGE',
	      'DEF:humidityext=' + cfg.RRDSENSORPATH +':humidity:AVERAGE',
              'LINE2:humidity#3366CC:Humedad',
	      'AREA:humidityext#af5cbd80:Humedad exterior',
              'GPRINT:humidity:LAST:Actual\: %2.2lf',
              'GPRINT:humidity:AVERAGE:Media\: %2.2lf',
              'GPRINT:humidity:MAX:Max\: %2.2lf',
              'GPRINT:humidity:MIN:Min\: %2.2lf')




