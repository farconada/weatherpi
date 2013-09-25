import rrdtool
import cfg
import os

def updateCurrentCharts():
    path24h = os.path.dirname(__file__) + '/static/img/current24.png'
    path1Week = os.path.dirname(__file__) + '/static/img/current1Week.png'
    path1Month = os.path.dirname(__file__) + '/static/img/current1Month.png'
    rrdtool.graph(path24h,
              '--imgformat', 'PNG',
              '--width', cfg.CHART_WIDTH,
              '--height', cfg.CHART_HEIGHT,
              '--start', 'end-1d',
              '--color', 'BACK#FFFFFF',
              '--vertical-label', 'Wats',
              '--title', 'Potencia aparente 24h',
              'DEF:power=' + cfg.RRDCURRENTPATH +':power:AVERAGE',
	      'AREA:power#50b680:Potencia aparente para 230V',
              'GPRINT:power:AVERAGE:Media\: %2.2lf',
              'GPRINT:power:MAX:Max\: %2.2lf',
              'GPRINT:power:MIN:Min\: %2.2lf')


    rrdtool.graph(path1Week,
              '--imgformat', 'PNG',
              '--width', cfg.CHART_WIDTH,
              '--height', cfg.CHART_HEIGHT,
              '--start', 'end-1w',
              '--color', 'BACK#FFFFFF',
              '--vertical-label', 'Wats',
              '--title', 'Potencia aparente 1 semana',
              'DEF:power=' + cfg.RRDCURRENTPATH +':power:AVERAGE',
	      'AREA:power#50b680:Potencia aparente para 230V',
              'GPRINT:power:AVERAGE:Media\: %2.2lf',
              'GPRINT:power:MAX:Max\: %2.2lf',
              'GPRINT:power:MIN:Min\: %2.2lf')


    rrdtool.graph(path1Month,
              '--imgformat', 'PNG',
              '--width', cfg.CHART_WIDTH,
              '--height', cfg.CHART_HEIGHT,
              '--start', 'end-1m',
              '--color', 'BACK#FFFFFF',
              '--vertical-label', 'Wats',
              '--title', 'Potencia aparente 1 mes',
              'DEF:power=' + cfg.RRDCURRENTPATH +':power:AVERAGE',
	      'AREA:power#50b680:Potencia aparente para 230V',
              'GPRINT:power:AVERAGE:Media\: %2.2lf',
              'GPRINT:power:MAX:Max\: %2.2lf',
              'GPRINT:power:MIN:Min\: %2.2lf')


