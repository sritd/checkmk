# -*- encoding: utf-8 -*-

# yapf: disable
# type: ignore

checkname = 'alcatel_temp_aos7'

info = [['1', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['2', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']]

discovery = {'': [('CPMA', {})]}

checks = {
    '': [('CPMA', {
        'levels': (45, 50)
    }, [(0, u'2 \xb0C', [('temp', 2, 45, 50, None, None)])])]
}
