import rrdtool
import cfg
import os

def updateLuzCharts():
    path24h = os.path.dirname(__file__) + '/static/img/luz24.png'
    path1Week = os.path.dirname(__file__) + '/static/img/luz1Week.png'
    path1Month = os.path.dirname(__file__) + '/static/img/luz1Month.png'
    rrdtool.graph(path24h,
              '--imgformat', 'PNG',
              '--width', cfg.CHART_WIDTH ,
              '--height', cfg.CHART_HEIGHT,
              '--start', 'end-1d',
              '--color', 'BACK#FFFFFF',
              '--vertical-label', 'lx',
              '--title', 'Luz 24h',
              'DEF:lux=' + cfg.RRDSENSORPATH +':lux:AVERAGE',
              'LINE2:lux#3366CC:Luz lx',
              'GPRINT:lux:LAST:Actual\: %2.2lf',
              'GPRINT:lux:AVERAGE:Media\: %2.2lf',
              'GPRINT:lux:MAX:Max\: %2.2lf',
              'GPRINT:lux:MIN:Min\: %2.2lf')


    rrdtool.graph(path1Week,
              '--imgformat', 'PNG',
              '--width', cfg.CHART_WIDTH ,
              '--height', cfg.CHART_HEIGHT,
              '--start', 'end-1w',
              '--color', 'BACK#FFFFFF',
              '--vertical-label', 'lx',
              '--title', 'Luz atmosferica 1 Semana',
              'DEF:lux=' + cfg.RRDSENSORPATH +':lux:AVERAGE',
              'LINE2:lux#3366CC:Luz lx',
              'GPRINT:lux:LAST:Actual\: %2.2lf',
              'GPRINT:lux:AVERAGE:Media\: %2.2lf',
              'GPRINT:lux:MAX:Max\: %2.2lf',
              'GPRINT:lux:MIN:Min\: %2.2lf')


    rrdtool.graph(path1Month,
              '--imgformat', 'PNG',
              '--width', cfg.CHART_WIDTH ,
              '--height', cfg.CHART_HEIGHT,
              '--start', 'end-4w',
              '--color', 'BACK#FFFFFF',
              '--vertical-label', 'lx',
              '--title', 'Luz atmosferica 1 Mes',
              'DEF:lux=' + cfg.RRDSENSORPATH +':lux:AVERAGE',
              'LINE2:lux#3366CC:Luz lx',
              'GPRINT:lux:LAST:Actual\: %2.2lf',
              'GPRINT:lux:AVERAGE:Media\: %2.2lf',
              'GPRINT:lux:MAX:Max\: %2.2lf',
              'GPRINT:lux:MIN:Min\: %2.2lf')




