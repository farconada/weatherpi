import rrdtool
import cfg

def updateHumidityCharts():
    path24h = 'static/img/humidity24.png'
    path1Week = 'static/img/humidity1Week.png'
    path1Month = 'static/img/humidity1Month.png'
    rrdtool.graph(path24h,
              '--imgformat', 'PNG',
              '--width', cfg.CHART_WIDTH,
              '--height', cfg.CHART_HEIGHT,
              '--start', 'end-1d',
              '--color', 'BACK#FFFFFF',
              '--vertical-label', '%',
              '--title', 'Humedad 24h',
              'DEF:humidity=' + cfg.RRDPATH +':humidity:AVERAGE',
              'LINE2:humidity#3366CC:Humedad',
              'GPRINT:humidity:LAST:Actual\: %2.2lf',
              'GPRINT:humidity:AVERAGE:Media\: %2.2lf',
              'GPRINT:humidity:MAX:Max\: %2.2lf',
              'GPRINT:humidity:MIN:Min\: %2.2lf')
