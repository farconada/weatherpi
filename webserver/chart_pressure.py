import rrdtool
import cfg

def updatePressureCharts():
    path24h = 'static/img/pressure24.png'
    path1Week = 'static/img/pressure1Week.png'
    path1Month = 'static/img/pressure1Month.png'
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
