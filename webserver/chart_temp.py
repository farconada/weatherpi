import rrdtool
import cfg
import os

def updateTempCharts():
	path24h = os.path.dirname(__file__) + '/static/img/temp24.png'
	path1Week = os.path.dirname(__file__) + '/static/img/temp1Week.png'
	path1Month = os.path.dirname(__file__) + '/static/img/temp1Month.png'
	rrdtool.graph(path24h,
	      '--imgformat', 'PNG',
	      '--width', cfg.CHART_WIDTH,
	      '--height', cfg.CHART_HEIGHT,
	      '--start', 'end-1d',
	      '--color', 'BACK#FFFFFF',
	      '--vertical-label', 'C',
	      '--title', 'Temperatura 24h',
	      'DEF:tempbmp085=' + cfg.RRDPATH +':tempbmp085:AVERAGE',
	      'DEF:tempext=' + cfg.RRDSENSORPATH +':tempdht22:AVERAGE',
	      'DEF:humidityext=' + cfg.RRDSENSORPATH +':humidity:AVERAGE',
	      'CDEF:aTRH0=17.271,tempext,*,237.7,tempext,+,/,humidityext,100,/,LOG,+',
	      'CDEF:TdC0=237.7,aTRH0,*,17.271,aTRH0,-,/',
	      'LINE2:TdC0#f70909:Rocio',
	      'LINE2:tempbmp085#3366CC:Temperatura',
	      'AREA:tempext#af5cbd80:Temperatura exterior',
	      'GPRINT:tempbmp085:LAST:Actual\: %2.2lf',
	      'GPRINT:tempbmp085:AVERAGE:Media\: %2.2lf',
	      'GPRINT:tempbmp085:MAX:Max\: %2.2lf',
	      'GPRINT:tempbmp085:MIN:Min\: %2.2lf')

	rrdtool.graph(path1Week,
	      '--imgformat', 'PNG',
	      '--width', cfg.CHART_WIDTH,
	      '--height', cfg.CHART_HEIGHT,
	      '--start', 'end-1w',
	      '--color', 'BACK#FFFFFF',
	      '--vertical-label', 'C',
	      '--title', 'Temperatura 1 Semana',
	      'DEF:tempbmp085=' + cfg.RRDPATH +':tempbmp085:AVERAGE',
	      'DEF:tempext=' + cfg.RRDSENSORPATH +':tempdht22:AVERAGE',
	      'DEF:humidityext=' + cfg.RRDSENSORPATH +':humidity:AVERAGE',
	      'CDEF:aTRH0=17.271,tempext,*,237.7,tempext,+,/,humidityext,100,/,LOG,+',
	      'CDEF:TdC0=237.7,aTRH0,*,17.271,aTRH0,-,/',
	      'LINE2:TdC0#f70909:Rocio',
	      'LINE2:tempbmp085#3366CC:Temperatura',
	      'AREA:tempext#af5cbd80:Temperatura exterior',
	      'GPRINT:tempbmp085:LAST:Actual\: %2.2lf',
	      'GPRINT:tempbmp085:AVERAGE:Media\: %2.2lf',
	      'GPRINT:tempbmp085:MAX:Max\: %2.2lf',
	      'GPRINT:tempbmp085:MIN:Min\: %2.2lf')

	
	rrdtool.graph(path1Month,
	      '--imgformat', 'PNG',
	      '--width', cfg.CHART_WIDTH,
	      '--height', cfg.CHART_HEIGHT,
	      '--start', 'end-4w',
	      '--color', 'BACK#FFFFFF',
	      '--vertical-label', 'C',
	      '--title', 'Temperatura 1 Mes',
	      'DEF:tempbmp085=' + cfg.RRDPATH +':tempbmp085:AVERAGE',
	      'DEF:tempext=' + cfg.RRDSENSORPATH +':tempdht22:AVERAGE',
	      'LINE2:tempbmp085#3366CC:Temperatura',
	      'AREA:tempext#af5cbd80:Temperatura exterior',
	      'GPRINT:tempbmp085:LAST:Actual\: %2.2lf',
	      'GPRINT:tempbmp085:AVERAGE:Media\: %2.2lf',
	      'GPRINT:tempbmp085:MAX:Max\: %2.2lf',
	      'GPRINT:tempbmp085:MIN:Min\: %2.2lf')
