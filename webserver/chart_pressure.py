import rrdtool
import cfg
import os

def updatePressureCharts():
    path24h = os.path.dirname(__file__) + '/static/img/pressure24.png'
    path1Week = os.path.dirname(__file__) + '/static/img/pressure1Week.png'
    path1Month = os.path.dirname(__file__) + '/static/img/pressure1Month.png'
    rrdtool.graph(path24h,
              '--imgformat', 'PNG',
              '--width', cfg.CHART_WIDTH ,
              '--height', cfg.CHART_HEIGHT,
              '--start', 'end-1d',
              '--color', 'BACK#FFFFFF',
              '--vertical-label', 'hPa',
              '--title', 'Presion atmosferica 24h',
              'DEF:pressure=' + cfg.RRDPATH +':pressure:AVERAGE',
              'LINE2:pressure#3366CC:Presion hPa',
              'GPRINT:pressure:LAST:Actual\: %2.2lf',
              'GPRINT:pressure:AVERAGE:Media\: %2.2lf',
              'GPRINT:pressure:MAX:Max\: %2.2lf',
              'GPRINT:pressure:MIN:Min\: %2.2lf')


    rrdtool.graph(path1Week,
              '--imgformat', 'PNG',
              '--width', cfg.CHART_WIDTH ,
              '--height', cfg.CHART_HEIGHT,
              '--start', 'end-1w',
              '--color', 'BACK#FFFFFF',
              '--vertical-label', 'hPa',
              '--title', 'Presion atmosferica 1 Semana',
              'DEF:pressure=' + cfg.RRDPATH +':pressure:AVERAGE',
              'LINE2:pressure#3366CC:Presion hPa',
              'GPRINT:pressure:LAST:Actual\: %2.2lf',
              'GPRINT:pressure:AVERAGE:Media\: %2.2lf',
              'GPRINT:pressure:MAX:Max\: %2.2lf',
              'GPRINT:pressure:MIN:Min\: %2.2lf')


    rrdtool.graph(path1Month,
              '--imgformat', 'PNG',
              '--width', cfg.CHART_WIDTH ,
              '--height', cfg.CHART_HEIGHT,
              '--start', 'end-4w',
              '--color', 'BACK#FFFFFF',
              '--vertical-label', 'hPa',
              '--title', 'Presion atmosferica 1 Mes',
              'DEF:pressure=' + cfg.RRDPATH +':pressure:AVERAGE',
              'LINE2:pressure#3366CC:Presion hPa',
              'GPRINT:pressure:LAST:Actual\: %2.2lf',
              'GPRINT:pressure:AVERAGE:Media\: %2.2lf',
              'GPRINT:pressure:MAX:Max\: %2.2lf',
              'GPRINT:pressure:MIN:Min\: %2.2lf')




