# -*- encoding: utf-8 -*-

# yapf: disable
# type: ignore



checkname = u'fsc_fans'


info = [[u'NULL', u'NULL'], [u'FAN1 SYS', u'4140']]


discovery = {'': [(u'FAN1 SYS', {})]}


checks = {'': [(u'FAN1 SYS', {'lower': (2000, 1000)}, [(0, 'Speed: 4140 RPM', [])])]}
