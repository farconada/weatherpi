import rrdtool
import cfg

def updateTempCharts():
	path24h = 'static/img/temp24.png'
	path1Week = 'static/img/temp1Week.png'
	path1Month = 'static/img/temp1Month.png'
	rrdtool.graph(path24h,
	      '--imgformat', 'PNG',
	      '--width', cfg.CHART_WIDTH,
	      '--height', cfg.CHART_HEIGHT,
	      '--start', 'end-1d',
	      '--color', 'BACK#FFFFFF',
	      '--vertical-label', 'C',
	      '--title', 'Temperatura 24h',
	      'DEF:tempbmp085=' + cfg.RRDPATH +':tempbmp085:AVERAGE',
	      'LINE2:tempbmp085#3366CC:Temperatura',
	      'GPRINT:tempbmp085:LAST:Actual\: %2.2lf',
	      'GPRINT:tempbmp085:AVERAGE:Media\: %2.2lf',
	      'GPRINT:tempbmp085:MAX:Max\: %2.2lf',
	      'GPRINT:tempbmp085:MIN:Min\: %2.2lf')

