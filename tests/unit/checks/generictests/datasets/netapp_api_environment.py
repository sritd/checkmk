# -*- encoding: utf-8 -*-

# yapf: disable
# type: ignore


checkname = 'netapp_api_environment'

info = [[u'sensor-name PSU2', u'sensor-type fru', u'node-name dmc1-r019-na1a',
         u'discrete-sensor-value GOOD', u'discrete-sensor-state normal',
         u'threshold-sensor-state normal'],
        [u'sensor-name PSU1', u'sensor-type fru', u'node-name dmc1-r019-na1a',
         u'discrete-sensor-value GOOD', u'discrete-sensor-state normal',
         u'threshold-sensor-state normal'],
        [u'sensor-name Fan3', u'sensor-type fru', u'node-name dmc1-r019-na1a',
         u'discrete-sensor-value GOOD', u'discrete-sensor-state normal',
         u'threshold-sensor-state normal'],
        [u'sensor-name Fan2', u'sensor-type fru', u'node-name dmc1-r019-na1a',
         u'discrete-sensor-value GOOD', u'discrete-sensor-state normal',
         u'threshold-sensor-state normal'],
        [u'sensor-name Fan1', u'sensor-type fru', u'node-name dmc1-r019-na1a',
         u'discrete-sensor-value GOOD', u'discrete-sensor-state normal',
         u'threshold-sensor-state normal'],
        [u'sensor-name SP Status', u'sensor-type discrete', u'node-name dmc1-r019-na1a',
         u'discrete-sensor-value IPMI_HB_OK', u'discrete-sensor-state normal',
         u'threshold-sensor-state normal'],
        [u'sensor-name mSATA Status', u'sensor-type discrete', u'node-name dmc1-r019-na1a',
         u'discrete-sensor-value OK', u'discrete-sensor-state normal',
         u'threshold-sensor-state normal'],
        [u'sensor-name mSATA Pres', u'sensor-type discrete', u'node-name dmc1-r019-na1a',
         u'discrete-sensor-value PRESENT', u'discrete-sensor-state normal',
         u'threshold-sensor-state normal'],
        [u'sensor-name CPU0 Temp Margin', u'sensor-type thermal', u'threshold-sensor-value -78',
         u'critical-high-threshold 0', u'warning-high-threshold -10', u'node-name dmc1-r019-na1a',
         u'value-units C', u'threshold-sensor-state normal'],
        [u'sensor-name In Flow Temp', u'sensor-type thermal', u'warning-low-threshold 5',
         u'threshold-sensor-value 16', u'critical-high-threshold 55', u'warning-high-threshold 50',
         u'node-name dmc1-r019-na1a', u'value-units C', u'threshold-sensor-state normal',
         u'critical-low-threshold 0'],
        [u'sensor-name Out Flow Temp', u'sensor-type thermal', u'warning-low-threshold 5',
         u'threshold-sensor-value 23', u'critical-high-threshold 75', u'warning-high-threshold 65',
         u'node-name dmc1-r019-na1a', u'value-units C', u'threshold-sensor-state normal',
         u'critical-low-threshold 0'],
        [u'sensor-name PCI Slot Temp', u'sensor-type thermal', u'warning-low-threshold 5',
         u'threshold-sensor-value 21', u'critical-high-threshold 70', u'warning-high-threshold 60',
         u'node-name dmc1-r019-na1a', u'value-units C', u'threshold-sensor-state normal',
         u'critical-low-threshold 0'],
        [u'sensor-name Smart Bat Temp', u'sensor-type thermal', u'warning-low-threshold 5',
         u'threshold-sensor-value 19', u'critical-high-threshold 70', u'warning-high-threshold 60',
         u'node-name dmc1-r019-na1a', u'value-units C', u'threshold-sensor-state normal',
         u'critical-low-threshold 0'],
        [u'sensor-name CPU0 Error', u'sensor-type discrete', u'node-name dmc1-r019-na1a',
         u'discrete-sensor-value NORMAL', u'discrete-sensor-state normal',
         u'threshold-sensor-state normal'],
        [u'sensor-name CPU0 Therm Trip', u'sensor-type discrete', u'node-name dmc1-r019-na1a',
         u'discrete-sensor-value NORMAL', u'discrete-sensor-state normal',
         u'threshold-sensor-state normal'],
        [u'sensor-name CPU0 Hot', u'sensor-type discrete', u'node-name dmc1-r019-na1a',
         u'discrete-sensor-value NORMAL', u'discrete-sensor-state normal',
         u'threshold-sensor-state normal'],
        [u'sensor-name Memory0 Hot', u'sensor-type discrete', u'node-name dmc1-r019-na1a',
         u'discrete-sensor-value NORMAL', u'discrete-sensor-state normal',
         u'threshold-sensor-state normal'],
        [u'sensor-name PCH Hot', u'sensor-type discrete', u'node-name dmc1-r019-na1a',
         u'discrete-sensor-value NORMAL', u'discrete-sensor-state normal',
         u'threshold-sensor-state normal'],
        [u'sensor-name Ambient Temp 1', u'sensor-type thermal', u'warning-low-threshold 5',
         u'threshold-sensor-value 15', u'critical-high-threshold 52', u'warning-high-threshold 47',
         u'node-name dmc1-r019-na1a', u'value-units C', u'threshold-sensor-state normal',
         u'critical-low-threshold 0'],
        [u'sensor-name Ambient Temp 2', u'sensor-type thermal', u'warning-low-threshold 5',
         u'threshold-sensor-value 15', u'critical-high-threshold 52', u'warning-high-threshold 47',
         u'node-name dmc1-r019-na1a', u'value-units C', u'threshold-sensor-state normal',
         u'critical-low-threshold 0'],
        [u'sensor-name P5V STBY', u'sensor-type voltage', u'warning-low-threshold 4343',
         u'threshold-sensor-value 5075', u'critical-high-threshold 5807',
         u'warning-high-threshold 5660', u'node-name dmc1-r019-na1a', u'value-units mV',
         u'threshold-sensor-state normal', u'critical-low-threshold 4245'],
        [u'sensor-name P3.3V STBY', u'sensor-type voltage', u'warning-low-threshold 3040',
         u'threshold-sensor-value 3264', u'critical-high-threshold 3664',
         u'warning-high-threshold 3568', u'node-name dmc1-r019-na1a', u'value-units mV',
         u'threshold-sensor-state normal', u'critical-low-threshold 2960'],
        [u'sensor-name P1.8V STBY', u'sensor-type voltage', u'warning-low-threshold 1658',
         u'threshold-sensor-value 1804', u'critical-high-threshold 1969',
         u'warning-high-threshold 1949', u'node-name dmc1-r019-na1a', u'value-units mV',
         u'threshold-sensor-state normal', u'critical-low-threshold 1629'],
        [u'sensor-name P1.2V STBY', u'sensor-type voltage', u'warning-low-threshold 1105',
         u'threshold-sensor-value 1193', u'critical-high-threshold 1319',
         u'warning-high-threshold 1299', u'node-name dmc1-r019-na1a', u'value-units mV',
         u'threshold-sensor-state normal', u'critical-low-threshold 1086'],
        [u'sensor-name P0.9V STBY', u'sensor-type voltage', u'warning-low-threshold 853',
         u'threshold-sensor-value 892', u'critical-high-threshold 999',
         u'warning-high-threshold 950', u'node-name dmc1-r019-na1a', u'value-units mV',
         u'threshold-sensor-state normal', u'critical-low-threshold 805'],
        [u'sensor-name P5V', u'sensor-type voltage', u'warning-low-threshold 4343',
         u'threshold-sensor-value 5002', u'critical-high-threshold 5807',
         u'warning-high-threshold 5660', u'node-name dmc1-r019-na1a', u'value-units mV',
         u'threshold-sensor-state normal', u'critical-low-threshold 4245'],
        [u'sensor-name P3.3V', u'sensor-type voltage', u'warning-low-threshold 3040',
         u'threshold-sensor-value 3296', u'critical-high-threshold 3664',
         u'warning-high-threshold 3568', u'node-name dmc1-r019-na1a', u'value-units mV',
         u'threshold-sensor-state normal', u'critical-low-threshold 2960'],
        [u'sensor-name PVDDQ DDR4 AB', u'sensor-type voltage', u'warning-low-threshold 19',
         u'threshold-sensor-value 1212', u'critical-high-threshold 2463',
         u'warning-high-threshold 2454', u'node-name dmc1-r019-na1a', u'value-units mV',
         u'threshold-sensor-state normal', u'critical-low-threshold 9'],
        [u'sensor-name PVTT DDR4 AB', u'sensor-type voltage', u'warning-low-threshold 19',
         u'threshold-sensor-value 591', u'critical-high-threshold 2463',
         u'warning-high-threshold 2454', u'node-name dmc1-r019-na1a', u'value-units mV',
         u'threshold-sensor-state normal', u'critical-low-threshold 9'],
        [u'sensor-name PVCCP CPU0', u'sensor-type voltage', u'warning-low-threshold 19',
         u'threshold-sensor-value 1775', u'critical-high-threshold 2463',
         u'warning-high-threshold 2454', u'node-name dmc1-r019-na1a', u'value-units mV',
         u'threshold-sensor-state normal', u'critical-low-threshold 9'],
        [u'sensor-name P3.3V BATT', u'sensor-type voltage', u'warning-low-threshold 32',
         u'threshold-sensor-value 3040', u'critical-high-threshold 4064',
         u'warning-high-threshold 4048', u'node-name dmc1-r019-na1a', u'value-units mV',
         u'threshold-sensor-state normal', u'critical-low-threshold 16'],
        [u'sensor-name P12V', u'sensor-type voltage', u'threshold-sensor-value 11842',
         u'critical-high-threshold 15810', u'node-name dmc1-r019-na1a', u'value-units mV',
         u'threshold-sensor-state normal', u'critical-low-threshold 0'],
        [u'sensor-name P12V Curr', u'sensor-type current', u'threshold-sensor-value 9828',
         u'critical-high-threshold 21420', u'node-name dmc1-r019-na1a', u'value-units mA',
         u'threshold-sensor-state normal', u'critical-low-threshold 0'],
        [u'sensor-name P12V STBY', u'sensor-type voltage', u'threshold-sensor-value 11842',
         u'critical-high-threshold 15810', u'node-name dmc1-r019-na1a', u'value-units mV',
         u'threshold-sensor-state normal', u'critical-low-threshold 0'],
        [u'sensor-name P12V STBY Curr', u'sensor-type current', u'threshold-sensor-value 764',
         u'critical-high-threshold 3182', u'node-name dmc1-r019-na1a', u'value-units mA',
         u'threshold-sensor-state normal', u'critical-low-threshold 0'],
        [u'sensor-name Sysfan1 Present', u'sensor-type discrete', u'node-name dmc1-r019-na1a',
         u'discrete-sensor-value PRESENT', u'discrete-sensor-state normal',
         u'threshold-sensor-state normal'],
        [u'sensor-name Sysfan1 Fault', u'sensor-type discrete', u'node-name dmc1-r019-na1a',
         u'discrete-sensor-value OK', u'discrete-sensor-state normal',
         u'threshold-sensor-state normal'],
        [u'sensor-name Sysfan1 F1 Speed', u'sensor-type fan', u'warning-low-threshold 1560',
         u'threshold-sensor-value 2880', u'node-name dmc1-r019-na1a', u'value-units RPM',
         u'threshold-sensor-state normal', u'critical-low-threshold 1470'],
        [u'sensor-name Sysfan1 F2 Speed', u'sensor-type fan', u'warning-low-threshold 1560',
         u'threshold-sensor-value 6240', u'node-name dmc1-r019-na1a', u'value-units RPM',
         u'threshold-sensor-state normal', u'critical-low-threshold 1470'],
        [u'sensor-name Sysfan2 Present', u'sensor-type discrete', u'node-name dmc1-r019-na1a',
         u'discrete-sensor-value PRESENT', u'discrete-sensor-state normal',
         u'threshold-sensor-state normal'],
        [u'sensor-name Sysfan2 Fault', u'sensor-type discrete', u'node-name dmc1-r019-na1a',
         u'discrete-sensor-value OK', u'discrete-sensor-state normal',
         u'threshold-sensor-state normal'],
        [u'sensor-name Sysfan2 F1 Speed', u'sensor-type fan', u'warning-low-threshold 1560',
         u'threshold-sensor-value 2820', u'node-name dmc1-r019-na1a', u'value-units RPM',
         u'threshold-sensor-state normal', u'critical-low-threshold 1470'],
        [u'sensor-name Sysfan2 F2 Speed', u'sensor-type fan', u'warning-low-threshold 1560',
         u'threshold-sensor-value 6300', u'node-name dmc1-r019-na1a', u'value-units RPM',
         u'threshold-sensor-state normal', u'critical-low-threshold 1470'],
        [u'sensor-name Sysfan3 Present', u'sensor-type discrete', u'node-name dmc1-r019-na1a',
         u'discrete-sensor-value PRESENT', u'discrete-sensor-state normal',
         u'threshold-sensor-state normal'],
        [u'sensor-name Sysfan3 Fault', u'sensor-type discrete', u'node-name dmc1-r019-na1a',
         u'discrete-sensor-value OK', u'discrete-sensor-state normal',
         u'threshold-sensor-state normal'],
        [u'sensor-name Sysfan3 F1 Speed', u'sensor-type fan', u'warning-low-threshold 1560',
         u'threshold-sensor-value 2820', u'node-name dmc1-r019-na1a', u'value-units RPM',
         u'threshold-sensor-state normal', u'critical-low-threshold 1470'],
        [u'sensor-name Sysfan3 F2 Speed', u'sensor-type fan', u'warning-low-threshold 1560',
         u'threshold-sensor-value 6240', u'node-name dmc1-r019-na1a', u'value-units RPM',
         u'threshold-sensor-state normal', u'critical-low-threshold 1470'],
        [u'sensor-name PSU1 Present', u'sensor-type discrete', u'node-name dmc1-r019-na1a',
         u'discrete-sensor-value PRESENT', u'discrete-sensor-state normal',
         u'threshold-sensor-state normal'],
        [u'sensor-name PSU1 Temp', u'sensor-type thermal', u'warning-low-threshold 5',
         u'threshold-sensor-value 14', u'critical-high-threshold 60', u'warning-high-threshold 50',
         u'node-name dmc1-r019-na1a', u'value-units C', u'threshold-sensor-state normal',
         u'critical-low-threshold 0'],
        [u'sensor-name PSU1 Curr', u'sensor-type current', u'threshold-sensor-value 11000',
         u'node-name dmc1-r019-na1a', u'value-units mA', u'threshold-sensor-state normal'],
        [u'sensor-name PSU1 Fan1 Speed', u'sensor-type fan', u'warning-low-threshold 4600',
         u'threshold-sensor-value 6800', u'node-name dmc1-r019-na1a', u'value-units RPM',
         u'threshold-sensor-state normal', u'critical-low-threshold 4500'],
        [u'sensor-name PSU1 Fan1 Fault', u'sensor-type discrete', u'node-name dmc1-r019-na1a',
         u'discrete-sensor-value OK', u'discrete-sensor-state normal',
         u'threshold-sensor-state normal'],
        [u'sensor-name PSU1 Fan2 Speed', u'sensor-type fan', u'warning-low-threshold 4600',
         u'threshold-sensor-value 6800', u'node-name dmc1-r019-na1a', u'value-units RPM',
         u'threshold-sensor-state normal', u'critical-low-threshold 4500'],
        [u'sensor-name PSU1 Fan2 Fault', u'sensor-type discrete', u'node-name dmc1-r019-na1a',
         u'discrete-sensor-value OK', u'discrete-sensor-state normal',
         u'threshold-sensor-state normal'],
        [u'sensor-name PSU1 Pwr In OK', u'sensor-type discrete', u'node-name dmc1-r019-na1a',
         u'discrete-sensor-value OK', u'discrete-sensor-state normal',
         u'threshold-sensor-state normal'],
        [u'sensor-name PSU1 Pwr Out OK', u'sensor-type discrete', u'node-name dmc1-r019-na1a',
         u'discrete-sensor-value OK', u'discrete-sensor-state normal',
         u'threshold-sensor-state normal'],
        [u'sensor-name PSU1 FAULT', u'sensor-type discrete', u'node-name dmc1-r019-na1a',
         u'discrete-sensor-value OK', u'discrete-sensor-state normal',
         u'threshold-sensor-state normal'],
        [u'sensor-name PSU1 Over Temp', u'sensor-type discrete', u'node-name dmc1-r019-na1a',
         u'discrete-sensor-value OK', u'discrete-sensor-state normal',
         u'threshold-sensor-state normal'],
        [u'sensor-name PSU1 Over Volt', u'sensor-type discrete', u'node-name dmc1-r019-na1a',
         u'discrete-sensor-value OK', u'discrete-sensor-state normal',
         u'threshold-sensor-state normal'],
        [u'sensor-name PSU1 Over Curr', u'sensor-type discrete', u'node-name dmc1-r019-na1a',
         u'discrete-sensor-value OK', u'discrete-sensor-state normal',
         u'threshold-sensor-state normal'],
        [u'sensor-name PSU1 Crest Factor', u'sensor-type current', u'threshold-sensor-value 1384',
         u'critical-high-threshold 2000', u'warning-high-threshold 1728',
         u'node-name dmc1-r019-na1a', u'threshold-sensor-state normal',
         u'critical-low-threshold 1000'],
        [u'sensor-name PSU1 InPwr Monitor', u'sensor-type unknown',
         u'threshold-sensor-value 147000', u'node-name dmc1-r019-na1a', u'value-units mW',
         u'threshold-sensor-state normal'],
        [u'sensor-name PSU2 Present', u'sensor-type discrete', u'node-name dmc1-r019-na1a',
         u'discrete-sensor-value PRESENT', u'discrete-sensor-state normal',
         u'threshold-sensor-state normal'],
        [u'sensor-name PSU2 Temp', u'sensor-type thermal', u'warning-low-threshold 5',
         u'threshold-sensor-value 14', u'critical-high-threshold 60', u'warning-high-threshold 50',
         u'node-name dmc1-r019-na1a', u'value-units C', u'threshold-sensor-state normal',
         u'critical-low-threshold 0'],
        [u'sensor-name PSU2 Curr', u'sensor-type current', u'threshold-sensor-value 12000',
         u'node-name dmc1-r019-na1a', u'value-units mA', u'threshold-sensor-state normal'],
        [u'sensor-name PSU2 Fan1 Speed', u'sensor-type fan', u'warning-low-threshold 4600',
         u'threshold-sensor-value 7000', u'node-name dmc1-r019-na1a', u'value-units RPM',
         u'threshold-sensor-state normal', u'critical-low-threshold 4500'],
        [u'sensor-name PSU2 Fan1 Fault', u'sensor-type discrete', u'node-name dmc1-r019-na1a',
         u'discrete-sensor-value OK', u'discrete-sensor-state normal',
         u'threshold-sensor-state normal'],
        [u'sensor-name PSU2 Fan2 Speed', u'sensor-type fan', u'warning-low-threshold 4600',
         u'threshold-sensor-value 6900', u'node-name dmc1-r019-na1a', u'value-units RPM',
         u'threshold-sensor-state normal', u'critical-low-threshold 4500'],
        [u'sensor-name PSU2 Fan2 Fault', u'sensor-type discrete', u'node-name dmc1-r019-na1a',
         u'discrete-sensor-value OK', u'discrete-sensor-state normal',
         u'threshold-sensor-state normal'],
        [u'sensor-name PSU2 Pwr In OK', u'sensor-type discrete', u'node-name dmc1-r019-na1a',
         u'discrete-sensor-value OK', u'discrete-sensor-state normal',
         u'threshold-sensor-state normal'],
        [u'sensor-name PSU2 Pwr Out OK', u'sensor-type discrete', u'node-name dmc1-r019-na1a',
         u'discrete-sensor-value OK', u'discrete-sensor-state normal',
         u'threshold-sensor-state normal'],
        [u'sensor-name PSU2 FAULT', u'sensor-type discrete', u'node-name dmc1-r019-na1a',
         u'discrete-sensor-value OK', u'discrete-sensor-state normal',
         u'threshold-sensor-state normal'],
        [u'sensor-name PSU2 Over Temp', u'sensor-type discrete', u'node-name dmc1-r019-na1a',
         u'discrete-sensor-value OK', u'discrete-sensor-state normal',
         u'threshold-sensor-state normal'],
        [u'sensor-name PSU2 Over Volt', u'sensor-type discrete', u'node-name dmc1-r019-na1a',
         u'discrete-sensor-value OK', u'discrete-sensor-state normal',
         u'threshold-sensor-state normal'],
        [u'sensor-name PSU2 Over Curr', u'sensor-type discrete', u'node-name dmc1-r019-na1a',
         u'discrete-sensor-value OK', u'discrete-sensor-state normal',
         u'threshold-sensor-state normal'],
        [u'sensor-name PSU2 Crest Factor', u'sensor-type current', u'threshold-sensor-value 1392',
         u'critical-high-threshold 2000', u'warning-high-threshold 1728',
         u'node-name dmc1-r019-na1a', u'threshold-sensor-state normal',
         u'critical-low-threshold 1000'],
        [u'sensor-name PSU2 InPwr Monitor', u'sensor-type unknown',
         u'threshold-sensor-value 157000', u'node-name dmc1-r019-na1a', u'value-units mW',
         u'threshold-sensor-state normal'],
        [u'sensor-name Bat Present', u'sensor-type discrete', u'node-name dmc1-r019-na1a',
         u'discrete-sensor-value PRESENT', u'discrete-sensor-state normal',
         u'threshold-sensor-state normal'],
        [u'sensor-name Bat Temp', u'sensor-type thermal', u'warning-low-threshold 5',
         u'threshold-sensor-value 15', u'critical-high-threshold 58', u'warning-high-threshold 53',
         u'node-name dmc1-r019-na1a', u'value-units C', u'threshold-sensor-state normal',
         u'critical-low-threshold 0'],
        [u'sensor-name Bat Volt', u'sensor-type voltage', u'warning-low-threshold 5600',
         u'threshold-sensor-value 8100', u'critical-high-threshold 8600',
         u'warning-high-threshold 8500', u'node-name dmc1-r019-na1a', u'value-units mV',
         u'threshold-sensor-state normal', u'critical-low-threshold 5500'],
        [u'sensor-name Bat Curr', u'sensor-type current', u'threshold-sensor-value 0',
         u'critical-high-threshold 2600', u'warning-high-threshold 2320',
         u'node-name dmc1-r019-na1a', u'value-units mA', u'threshold-sensor-state normal'],
        [u'sensor-name Bat Rem Cap', u'sensor-type battery_life', u'threshold-sensor-value 3328',
         u'node-name dmc1-r019-na1a', u'value-units mA*hr', u'threshold-sensor-state normal'],
        [u'sensor-name Bat Full Cap', u'sensor-type battery_life', u'threshold-sensor-value 3328',
         u'node-name dmc1-r019-na1a', u'value-units mA*hr', u'threshold-sensor-state normal'],
        [u'sensor-name Bat Charge Curr', u'sensor-type current', u'threshold-sensor-value 0',
         u'critical-high-threshold 2300', u'warning-high-threshold 2200',
         u'node-name dmc1-r019-na1a', u'value-units mA', u'threshold-sensor-state normal'],
        [u'sensor-name Bat Charge Volt', u'sensor-type voltage', u'threshold-sensor-value 8200',
         u'critical-high-threshold 9000', u'warning-high-threshold 8900',
         u'node-name dmc1-r019-na1a', u'value-units mV', u'threshold-sensor-state normal'],
        [u'sensor-name Bat Initial FCC', u'sensor-type battery_life',
         u'threshold-sensor-value 3200', u'node-name dmc1-r019-na1a', u'value-units mA*hr',
         u'threshold-sensor-state normal'],
        [u'sensor-name Bat Dstg Cycles', u'sensor-type counter', u'warning-low-threshold 5',
         u'threshold-sensor-value 21', u'node-name dmc1-r019-na1a', u'value-units cycles',
         u'threshold-sensor-state normal', u'critical-low-threshold 2'],
        [u'sensor-name Bat Power Fault', u'sensor-type discrete', u'node-name dmc1-r019-na1a',
         u'discrete-sensor-value GOOD', u'discrete-sensor-state normal',
         u'threshold-sensor-state normal'],
        [u'sensor-name Bat Dcharge FET', u'sensor-type discrete', u'node-name dmc1-r019-na1a',
         u'discrete-sensor-value ON', u'discrete-sensor-state normal',
         u'threshold-sensor-state normal'],
        [u'sensor-name Bat Charge FET', u'sensor-type discrete', u'node-name dmc1-r019-na1a',
         u'discrete-sensor-value ON', u'discrete-sensor-state normal',
         u'threshold-sensor-state normal'],
        [u'sensor-name Bat Cycle Count', u'sensor-type counter', u'threshold-sensor-value 1',
         u'node-name dmc1-r019-na1a', u'value-units cycles', u'threshold-sensor-state normal'],
        [u'sensor-name Partner Ctrl Pre', u'sensor-type discrete', u'node-name dmc1-r019-na1a',
         u'discrete-sensor-value NOT_PRESENT', u'discrete-sensor-state normal',
         u'threshold-sensor-state normal'],
        [u'sensor-name Attention', u'sensor-type discrete', u'node-name dmc1-r019-na1a',
         u'discrete-sensor-value DEASSERT', u'discrete-sensor-state normal',
         u'threshold-sensor-state normal']]


discovery = {'': [(u'dmc1-r019-na1a / PSU1 FAULT', None),
                  (u'dmc1-r019-na1a / PSU2 FAULT', None)],
             'current': [(u'dmc1-r019-na1a / Bat Charge Curr', None),
                         (u'dmc1-r019-na1a / Bat Curr', None),
                         (u'dmc1-r019-na1a / P12V Curr', None),
                         (u'dmc1-r019-na1a / P12V STBY Curr', None),
                         (u'dmc1-r019-na1a / PSU1 Curr', None),
                         (u'dmc1-r019-na1a / PSU2 Curr', None)],
             'fan_faults': [(u'dmc1-r019-na1a / PSU1 Fan1 Fault', None),
                            (u'dmc1-r019-na1a / PSU1 Fan2 Fault', None),
                            (u'dmc1-r019-na1a / PSU2 Fan1 Fault', None),
                            (u'dmc1-r019-na1a / PSU2 Fan2 Fault', None),
                            (u'dmc1-r019-na1a / Sysfan1 Fault', None),
                            (u'dmc1-r019-na1a / Sysfan2 Fault', None),
                            (u'dmc1-r019-na1a / Sysfan3 Fault', None)],
             'fans': [(u'dmc1-r019-na1a / PSU1 Fan1 Speed', None),
                      (u'dmc1-r019-na1a / PSU1 Fan2 Speed', None),
                      (u'dmc1-r019-na1a / PSU2 Fan1 Speed', None),
                      (u'dmc1-r019-na1a / PSU2 Fan2 Speed', None),
                      (u'dmc1-r019-na1a / Sysfan1 F1 Speed', None),
                      (u'dmc1-r019-na1a / Sysfan1 F2 Speed', None),
                      (u'dmc1-r019-na1a / Sysfan2 F1 Speed', None),
                      (u'dmc1-r019-na1a / Sysfan2 F2 Speed', None),
                      (u'dmc1-r019-na1a / Sysfan3 F1 Speed', None),
                      (u'dmc1-r019-na1a / Sysfan3 F2 Speed', None)],
             'temperature': [(u'dmc1-r019-na1a / Ambient Temp 1', None),
                             (u'dmc1-r019-na1a / Ambient Temp 2', None),
                             (u'dmc1-r019-na1a / Bat Temp', None),
                             (u'dmc1-r019-na1a / CPU0 Temp Margin', None),
                             (u'dmc1-r019-na1a / In Flow Temp', None),
                             (u'dmc1-r019-na1a / Out Flow Temp', None),
                             (u'dmc1-r019-na1a / PCI Slot Temp', None),
                             (u'dmc1-r019-na1a / PSU1 Temp', None),
                             (u'dmc1-r019-na1a / PSU2 Temp', None),
                             (u'dmc1-r019-na1a / Smart Bat Temp', None)],
             'voltage': [(u'dmc1-r019-na1a / Bat Charge Volt', None),
                         (u'dmc1-r019-na1a / Bat Volt', None),
                         (u'dmc1-r019-na1a / P0.9V STBY', None),
                         (u'dmc1-r019-na1a / P1.2V STBY', None),
                         (u'dmc1-r019-na1a / P1.8V STBY', None),
                         (u'dmc1-r019-na1a / P12V STBY', None),
                         (u'dmc1-r019-na1a / P12V', None),
                         (u'dmc1-r019-na1a / P3.3V BATT', None),
                         (u'dmc1-r019-na1a / P3.3V STBY', None),
                         (u'dmc1-r019-na1a / P3.3V', None),
                         (u'dmc1-r019-na1a / P5V STBY', None),
                         (u'dmc1-r019-na1a / P5V', None),
                         (u'dmc1-r019-na1a / PVCCP CPU0', None),
                         (u'dmc1-r019-na1a / PVDDQ DDR4 AB', None),
                         (u'dmc1-r019-na1a / PVTT DDR4 AB', None)]}


checks = {'': [(u'dmc1-r019-na1a / PSU1 FAULT',
                {},
                [(0, u'Sensor state: normal, Sensor value: OK', [])]),
               (u'dmc1-r019-na1a / PSU2 FAULT',
                {},
                [(0, u'Sensor state: normal, Sensor value: OK', [])])],
          'current': [(u'dmc1-r019-na1a / Bat Charge Curr',
                       {},
                       [(0, '0.00 a', [(u'current', 0.0, 2.2, 2.3, None, None)])]),
                      (u'dmc1-r019-na1a / Bat Curr',
                       {},
                       [(0, '0.00 a', [(u'current', 0.0, 2.32, 2.6, None, None)])]),
                      (u'dmc1-r019-na1a / P12V Curr',
                       {},
                       [(0,
                         '9.83 a',
                         [(u'current', 9.828, None, 21.42, None, None)])]),
                      (u'dmc1-r019-na1a / P12V STBY Curr',
                       {},
                       [(0,
                         '0.76 a',
                         [(u'current', 0.764, None, 3.182, None, None)])]),
                      (u'dmc1-r019-na1a / PSU1 Curr',
                       {},
                       [(0, '11.00 a', [(u'current', 11.0, None, None, None, None)])]),
                      (u'dmc1-r019-na1a / PSU2 Curr',
                       {},
                       [(0, '12.00 a', [(u'current', 12.0, None, None, None, None)])])],
          'fan_faults': [(u'dmc1-r019-na1a / PSU1 Fan1 Fault',
                          {},
                          [(0, u'Sensor state: normal, Sensor value: OK', [])]),
                         (u'dmc1-r019-na1a / PSU1 Fan2 Fault',
                          {},
                          [(0, u'Sensor state: normal, Sensor value: OK', [])]),
                         (u'dmc1-r019-na1a / PSU2 Fan1 Fault',
                          {},
                          [(0, u'Sensor state: normal, Sensor value: OK', [])]),
                         (u'dmc1-r019-na1a / PSU2 Fan2 Fault',
                          {},
                          [(0, u'Sensor state: normal, Sensor value: OK', [])]),
                         (u'dmc1-r019-na1a / Sysfan1 Fault',
                          {},
                          [(0, u'Sensor state: normal, Sensor value: OK', [])]),
                         (u'dmc1-r019-na1a / Sysfan2 Fault',
                          {},
                          [(0, u'Sensor state: normal, Sensor value: OK', [])]),
                         (u'dmc1-r019-na1a / Sysfan3 Fault',
                          {},
                          [(0, u'Sensor state: normal, Sensor value: OK', [])])],
          'fans': [(u'dmc1-r019-na1a / PSU1 Fan1 Speed',
                    {},
                    [(0, u'6800 rpm', [(u'fan', 6800.0, None, None, None, None)])]),
                   (u'dmc1-r019-na1a / PSU1 Fan2 Speed',
                    {},
                    [(0, u'6800 rpm', [(u'fan', 6800.0, None, None, None, None)])]),
                   (u'dmc1-r019-na1a / PSU2 Fan1 Speed',
                    {},
                    [(0, u'7000 rpm', [(u'fan', 7000.0, None, None, None, None)])]),
                   (u'dmc1-r019-na1a / PSU2 Fan2 Speed',
                    {},
                    [(0, u'6900 rpm', [(u'fan', 6900.0, None, None, None, None)])]),
                   (u'dmc1-r019-na1a / Sysfan1 F1 Speed',
                    {},
                    [(0, u'2880 rpm', [(u'fan', 2880.0, None, None, None, None)])]),
                   (u'dmc1-r019-na1a / Sysfan1 F2 Speed',
                    {},
                    [(0, u'6240 rpm', [(u'fan', 6240.0, None, None, None, None)])]),
                   (u'dmc1-r019-na1a / Sysfan2 F1 Speed',
                    {},
                    [(0, u'2820 rpm', [(u'fan', 2820.0, None, None, None, None)])]),
                   (u'dmc1-r019-na1a / Sysfan2 F2 Speed',
                    {},
                    [(0, u'6300 rpm', [(u'fan', 6300.0, None, None, None, None)])]),
                   (u'dmc1-r019-na1a / Sysfan3 F1 Speed',
                    {},
                    [(0, u'2820 rpm', [(u'fan', 2820.0, None, None, None, None)])]),
                   (u'dmc1-r019-na1a / Sysfan3 F2 Speed',
                    {},
                    [(0, u'6240 rpm', [(u'fan', 6240.0, None, None, None, None)])])],
          'temperature': [(u'dmc1-r019-na1a / Ambient Temp 1',
                           {},
                           [(0,
                             u'15.0 \xb0C',
                             [('temp', 15.0, 47.0, 52.0, None, None)])]),
                          (u'dmc1-r019-na1a / Ambient Temp 2',
                           {},
                           [(0,
                             u'15.0 \xb0C',
                             [('temp', 15.0, 47.0, 52.0, None, None)])]),
                          (u'dmc1-r019-na1a / Bat Temp',
                           {},
                           [(0,
                             u'15.0 \xb0C',
                             [('temp', 15.0, 53.0, 58.0, None, None)])]),
                          (u'dmc1-r019-na1a / CPU0 Temp Margin',
                           {},
                           [(0,
                             u'-78.0 \xb0C',
                             [('temp', -78.0, -10.0, 0.0, None, None)])]),
                          (u'dmc1-r019-na1a / In Flow Temp',
                           {},
                           [(0,
                             u'16.0 \xb0C',
                             [('temp', 16.0, 50.0, 55.0, None, None)])]),
                          (u'dmc1-r019-na1a / Out Flow Temp',
                           {},
                           [(0,
                             u'23.0 \xb0C',
                             [('temp', 23.0, 65.0, 75.0, None, None)])]),
                          (u'dmc1-r019-na1a / PCI Slot Temp',
                           {},
                           [(0,
                             u'21.0 \xb0C',
                             [('temp', 21.0, 60.0, 70.0, None, None)])]),
                          (u'dmc1-r019-na1a / PSU1 Temp',
                           {},
                           [(0,
                             u'14.0 \xb0C',
                             [('temp', 14.0, 50.0, 60.0, None, None)])]),
                          (u'dmc1-r019-na1a / PSU2 Temp',
                           {},
                           [(0,
                             u'14.0 \xb0C',
                             [('temp', 14.0, 50.0, 60.0, None, None)])]),
                          (u'dmc1-r019-na1a / Smart Bat Temp',
                           {},
                           [(0,
                             u'19.0 \xb0C',
                             [('temp', 19.0, 60.0, 70.0, None, None)])])],
          'voltage': [(u'dmc1-r019-na1a / Bat Charge Volt',
                       {},
                       [(0, '8.20 v', [(u'voltage', 8.2, 8.9, 9.0, None, None)])]),
                      (u'dmc1-r019-na1a / Bat Volt',
                       {},
                       [(0, '8.10 v', [(u'voltage', 8.1, 8.5, 8.6, None, None)])]),
                      (u'dmc1-r019-na1a / P0.9V STBY',
                       {},
                       [(0,
                         '0.89 v',
                         [(u'voltage', 0.892, 0.95, 0.999, None, None)])]),
                      (u'dmc1-r019-na1a / P1.2V STBY',
                       {},
                       [(0,
                         '1.19 v',
                         [(u'voltage', 1.193, 1.299, 1.319, None, None)])]),
                      (u'dmc1-r019-na1a / P1.8V STBY',
                       {},
                       [(0,
                         '1.80 v',
                         [(u'voltage', 1.804, 1.949, 1.969, None, None)])]),
                      (u'dmc1-r019-na1a / P12V STBY',
                       {},
                       [(0,
                         '11.84 v',
                         [(u'voltage', 11.842, None, 15.81, None, None)])]),
                      (u'dmc1-r019-na1a / P12V',
                       {},
                       [(0,
                         '11.84 v',
                         [(u'voltage', 11.842, None, 15.81, None, None)])]),
                      (u'dmc1-r019-na1a / P3.3V BATT',
                       {},
                       [(0,
                         '3.04 v',
                         [(u'voltage', 3.04, 4.048, 4.064, None, None)])]),
                      (u'dmc1-r019-na1a / P3.3V STBY',
                       {},
                       [(0,
                         '3.26 v',
                         [(u'voltage', 3.264, 3.568, 3.664, None, None)])]),
                      (u'dmc1-r019-na1a / P3.3V',
                       {},
                       [(0,
                         '3.30 v',
                         [(u'voltage', 3.296, 3.568, 3.664, None, None)])]),
                      (u'dmc1-r019-na1a / P5V STBY',
                       {},
                       [(0,
                         '5.08 v',
                         [(u'voltage', 5.075, 5.66, 5.807, None, None)])]),
                      (u'dmc1-r019-na1a / P5V',
                       {},
                       [(0,
                         '5.00 v',
                         [(u'voltage', 5.002, 5.66, 5.807, None, None)])]),
                      (u'dmc1-r019-na1a / PVCCP CPU0',
                       {},
                       [(0,
                         '1.77 v',
                         [(u'voltage', 1.775, 2.454, 2.463, None, None)])]),
                      (u'dmc1-r019-na1a / PVDDQ DDR4 AB',
                       {},
                       [(0,
                         '1.21 v',
                         [(u'voltage', 1.212, 2.454, 2.463, None, None)])]),
                      (u'dmc1-r019-na1a / PVTT DDR4 AB',
                       {},
                       [(0,
                         '0.59 v',
                         [(u'voltage', 0.591, 2.454, 2.463, None, None)])])]}
