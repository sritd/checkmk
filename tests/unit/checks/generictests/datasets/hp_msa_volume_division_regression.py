# -*- encoding: utf-8 -*-

# yapf: disable
# type: ignore

checkname = 'hp_msa_volume'

info = [
    [u'volumes', u'1', u'durable-id', u'V0'],
    [u'volumes', u'1', u'virtual-disk-name', u'IMSAKO2B1_U1_B01-04'],
    [u'volumes', u'1', u'storage-pool-name', u'IMSAKO2B1_U1_B01-04'],
    [u'volumes', u'1', u'volume-name', u'IMSAKO2B1_U1_B01-04_v0001'],
    [u'volumes', u'1', u'size', u'1198.9GB'],
    [u'volumes', u'1', u'size-numeric', u'2341789696'],
    [u'volumes', u'1', u'total-size', u'1198.9GB'],
    [u'volumes', u'1', u'total-size-numeric', u'2341789696'],
    [u'volumes', u'1', u'allocated-size', u'1198.9GB'],
    [u'volumes', u'1', u'allocated-size-numeric', u'2341789696'],
    [u'volumes', u'1', u'storage-type', u'Linear'],
    [u'volumes', u'1', u'storage-type-numeric', u'0'],
    [u'volumes', u'1', u'preferred-owner', u'A'],
    [u'volumes', u'1', u'preferred-owner-numeric', u'1'],
    [u'volumes', u'1', u'owner', u'A'],
    [u'volumes', u'1', u'owner-numeric', u'1'],
    [u'volumes', u'1', u'serial-number', u'00c0ff1ec44a00008425415501000000'],
    [u'volumes', u'1', u'write-policy', u'write-back'],
    [u'volumes', u'1', u'write-policy-numeric', u'1'],
    [u'volumes', u'1', u'cache-optimization', u'standard'],
    [u'volumes', u'1', u'cache-optimization-numeric', u'0'],
    [u'volumes', u'1', u'read-ahead-size', u'Adaptive'],
    [u'volumes', u'1', u'read-ahead-size-numeric', u'-1'],
    [u'volumes', u'1', u'volume-type', u'standard'],
    [u'volumes', u'1', u'volume-type-numeric', u'0'],
    [u'volumes', u'1', u'volume-class', u'standard'],
    [u'volumes', u'1', u'volume-class-numeric', u'0'],
    [u'volumes', u'1', u'profile-preference', u'Standard'],
    [u'volumes', u'1', u'profile-preference-numeric', u'0'],
    [u'volumes', u'1', u'snapshot', u'No'],
    [u'volumes', u'1', u'volume-qualifier', u'N/A'],
    [u'volumes', u'1', u'volume-qualifier-numeric', u'0'],
    [u'volumes', u'1', u'blocks', u'2341789696'],
    [u'volumes', u'1', u'capabilities', u'dmscer'],
    [u'volumes', u'1', u'volume-parent'], [u'volumes', u'1', u'snap-pool'],
    [u'volumes', u'1', u'replication-set'], [u'volumes', u'1', u'attributes'],
    [
        u'volumes', u'1', u'virtual-disk-serial',
        u'00c0ff1ec44a00001e23415500000000'
    ], [u'volumes', u'1', u'volume-description'],
    [u'volumes', u'1', u'wwn', u'600C0FF0001EC44A8425415501000000'],
    [u'volumes', u'1', u'progress', u'0%'],
    [u'volumes', u'1', u'progress-numeric', u'0'],
    [u'volumes', u'1', u'container-name', u'IMSAKO2B1_U1_B01-04'],
    [
        u'volumes', u'1', u'container-serial',
        u'00c0ff1ec44a00001e23415500000000'
    ], [u'volumes', u'1', u'allowed-storage-tiers', u'N/A'],
    [u'volumes', u'1', u'allowed-storage-tiers-numeric', u'0'],
    [u'volumes', u'1', u'threshold-percent-of-pool', u'0'],
    [u'volumes', u'1', u'reserved-size-in-pages', u'0'],
    [u'volumes', u'1', u'allocate-reserved-pages-first', u'Disabled'],
    [u'volumes', u'1', u'allocate-reserved-pages-first-numeric', u'0'],
    [u'volumes', u'1', u'zero-init-page-on-allocation', u'Disabled'],
    [u'volumes', u'1', u'zero-init-page-on-allocation-numeric', u'0'],
    [u'volumes', u'1', u'raidtype', u'RAID10'],
    [u'volumes', u'1', u'raidtype-numeric', u'10'],
    [u'volumes', u'1', u'pi-format', u'T0'],
    [u'volumes', u'1', u'pi-format-numeric', u'0'],
    [u'volumes', u'1', u'health', u'Warning'],
    [u'volumes', u'1', u'health-numeric', u'0'],
    [u'volumes', u'1', u'health-reason', u'There', u'is', u'a', u'warning'],
    [u'volumes', u'1', u'health-recommendation'],
    [u'volumes', u'1', u'volume-group', u'UNGROUPEDVOLUMES'],
    [u'volumes', u'1', u'group-key', u'VGU'],
    [u'volumes', u'1', u'serial-number', u'00c0ff1ec44a00008425415501000000'],
    [u'volumes', u'2', u'durable-id', u'V3'],
    [u'volumes', u'2', u'virtual-disk-name', u'IMSAKO2B1_U1_B05-08'],
    [u'volumes', u'2', u'storage-pool-name', u'IMSAKO2B1_U1_B05-08'],
    [u'volumes', u'2', u'volume-name', u'IMSAKO2B1_U1_B05-08_v0001'],
    [u'volumes', u'2', u'size', u'1198.9GB'],
    [u'volumes', u'2', u'size-numeric', u'2341789696'],
    [u'volumes', u'2', u'total-size', u'1198.9GB'],
    [u'volumes', u'2', u'total-size-numeric', u'2341789696'],
    [u'volumes', u'2', u'allocated-size', u'1198.9GB'],
    [u'volumes', u'2', u'allocated-size-numeric', u'2341789696'],
    [u'volumes', u'2', u'storage-type', u'Linear'],
    [u'volumes', u'2', u'storage-type-numeric', u'0'],
    [u'volumes', u'2', u'preferred-owner', u'B'],
    [u'volumes', u'2', u'preferred-owner-numeric', u'0'],
    [u'volumes', u'2', u'owner', u'B'],
    [u'volumes', u'2', u'owner-numeric', u'0'],
    [u'volumes', u'2', u'serial-number', u'00c0ff1ec10b00009925415501000000'],
    [u'volumes', u'2', u'write-policy', u'write-back'],
    [u'volumes', u'2', u'write-policy-numeric', u'1'],
    [u'volumes', u'2', u'cache-optimization', u'standard'],
    [u'volumes', u'2', u'cache-optimization-numeric', u'0'],
    [u'volumes', u'2', u'read-ahead-size', u'Adaptive'],
    [u'volumes', u'2', u'read-ahead-size-numeric', u'-1'],
    [u'volumes', u'2', u'volume-type', u'standard'],
    [u'volumes', u'2', u'volume-type-numeric', u'0'],
    [u'volumes', u'2', u'volume-class', u'standard'],
    [u'volumes', u'2', u'volume-class-numeric', u'0'],
    [u'volumes', u'2', u'profile-preference', u'Standard'],
    [u'volumes', u'2', u'profile-preference-numeric', u'0'],
    [u'volumes', u'2', u'snapshot', u'No'],
    [u'volumes', u'2', u'volume-qualifier', u'N/A'],
    [u'volumes', u'2', u'volume-qualifier-numeric', u'0'],
    [u'volumes', u'2', u'blocks', u'2341789696'],
    [u'volumes', u'2', u'capabilities', u'dmscer'],
    [u'volumes', u'2', u'volume-parent'], [u'volumes', u'2', u'snap-pool'],
    [u'volumes', u'2', u'replication-set'], [u'volumes', u'2', u'attributes'],
    [
        u'volumes', u'2', u'virtual-disk-serial',
        u'00c0ff1ec10b0000e423415500000000'
    ], [u'volumes', u'2', u'volume-description'],
    [u'volumes', u'2', u'wwn', u'600C0FF0001EC10B9925415501000000'],
    [u'volumes', u'2', u'progress', u'0%'],
    [u'volumes', u'2', u'progress-numeric', u'0'],
    [u'volumes', u'2', u'container-name', u'IMSAKO2B1_U1_B05-08'],
    [
        u'volumes', u'2', u'container-serial',
        u'00c0ff1ec10b0000e423415500000000'
    ], [u'volumes', u'2', u'allowed-storage-tiers', u'N/A'],
    [u'volumes', u'2', u'allowed-storage-tiers-numeric', u'0'],
    [u'volumes', u'2', u'threshold-percent-of-pool', u'0'],
    [u'volumes', u'2', u'reserved-size-in-pages', u'0'],
    [u'volumes', u'2', u'allocate-reserved-pages-first', u'Disabled'],
    [u'volumes', u'2', u'allocate-reserved-pages-first-numeric', u'0'],
    [u'volumes', u'2', u'zero-init-page-on-allocation', u'Disabled'],
    [u'volumes', u'2', u'zero-init-page-on-allocation-numeric', u'0'],
    [u'volumes', u'2', u'raidtype', u'RAID10'],
    [u'volumes', u'2', u'raidtype-numeric', u'10'],
    [u'volumes', u'2', u'pi-format', u'T0'],
    [u'volumes', u'2', u'pi-format-numeric', u'0'],
    [u'volumes', u'2', u'health', u'OK'],
    [u'volumes', u'2', u'health-numeric', u'0'],
    [u'volumes', u'2', u'health-reason'],
    [u'volumes', u'2', u'health-recommendation'],
    [u'volumes', u'2', u'volume-group', u'UNGROUPEDVOLUMES'],
    [u'volumes', u'2', u'group-key', u'VGU'],
    [u'volume-statistics', u'1', u'bytes-per-second', u'2724.3KB'],
    [u'volume-statistics', u'1', u'bytes-per-second-numeric', u'2724352'],
    [u'volume-statistics', u'1', u'iops', u'66'],
    [u'volume-statistics', u'1', u'number-of-reads', u'11965055'],
    [u'volume-statistics', u'1', u'number-of-writes', u'80032996'],
    [u'volume-statistics', u'1', u'data-read', u'1241.3GB'],
    [u'volume-statistics', u'1', u'data-read-numeric', u'1241361379840'],
    [u'volume-statistics', u'1', u'data-written', u'6462.6GB'],
    [u'volume-statistics', u'1', u'data-written-numeric', u'6462660316672'],
    [u'volume-statistics', u'1', u'allocated-pages', u'0'],
    [u'volume-statistics', u'1', u'percent-tier-ssd', u'0'],
    [u'volume-statistics', u'1', u'percent-tier-sas', u'0'],
    [u'volume-statistics', u'1', u'percent-tier-sata', u'0'],
    [u'volume-statistics', u'1', u'percent-allocated-rfc', u'0'],
    [u'volume-statistics', u'1', u'pages-alloc-per-minute', u'0'],
    [u'volume-statistics', u'1', u'pages-dealloc-per-minute', u'0'],
    [u'volume-statistics', u'1', u'shared-pages', u'0'],
    [u'volume-statistics', u'1', u'write-cache-hits', u'93581599'],
    [u'volume-statistics', u'1', u'write-cache-misses', u'345571865'],
    [u'volume-statistics', u'1', u'read-cache-hits', u'29276023'],
    [u'volume-statistics', u'1', u'read-cache-misses', u'54728207'],
    [u'volume-statistics', u'1', u'small-destages', u'36593447'],
    [u'volume-statistics', u'1', u'full-stripe-write-destages', u'4663277'],
    [
        u'volume-statistics', u'1', u'read-ahead-operations',
        u'4804068203594569116'
    ], [u'volume-statistics', u'1', u'write-cache-space', u'74'],
    [u'volume-statistics', u'1', u'write-cache-percent', u'8'],
    [u'volume-statistics', u'1', u'reset-time', u'2015-05-22', u'13:54:36'],
    [u'volume-statistics', u'1', u'reset-time-numeric', u'1432302876'],
    [
        u'volume-statistics', u'1', u'start-sample-time', u'2015-08-21',
        u'11:51:17'
    ],
    [u'volume-statistics', u'1', u'start-sample-time-numeric', u'1440157877'],
    [
        u'volume-statistics', u'1', u'stop-sample-time', u'2015-08-21',
        u'11:51:48'
    ],
    [u'volume-statistics', u'1', u'stop-sample-time-numeric', u'1440157908'],
    [u'volume-statistics', u'2', u'volume-name', u'IMSAKO2B1_U1_B05-08_v0001'],
    [
        u'volume-statistics', u'2', u'serial-number',
        u'00c0ff1ec10b00009925415501000000'
    ], [u'volume-statistics', u'2', u'bytes-per-second', u'1064.9KB'],
    [u'volume-statistics', u'2', u'bytes-per-second-numeric', u'1064960'],
    [u'volume-statistics', u'2', u'iops', u'45'],
    [u'volume-statistics', u'2', u'number-of-reads', u'9892573'],
    [u'volume-statistics', u'2', u'number-of-writes', u'76500553'],
    [u'volume-statistics', u'2', u'data-read', u'1242.5GB'],
    [u'volume-statistics', u'2', u'data-read-numeric', u'1242509234176'],
    [u'volume-statistics', u'2', u'data-written', u'6572.7GB'],
    [u'volume-statistics', u'2', u'data-written-numeric', u'6572795755008'],
    [u'volume-statistics', u'2', u'allocated-pages', u'0'],
    [u'volume-statistics', u'2', u'percent-tier-ssd', u'0'],
    [u'volume-statistics', u'2', u'percent-tier-sas', u'0'],
    [u'volume-statistics', u'2', u'percent-tier-sata', u'0'],
    [u'volume-statistics', u'2', u'percent-allocated-rfc', u'0'],
    [u'volume-statistics', u'2', u'pages-alloc-per-minute', u'0'],
    [u'volume-statistics', u'2', u'pages-dealloc-per-minute', u'0'],
    [u'volume-statistics', u'2', u'shared-pages', u'0'],
    [u'volume-statistics', u'2', u'write-cache-hits', u'83182170'],
    [u'volume-statistics', u'2', u'write-cache-misses', u'359922110'],
    [u'volume-statistics', u'2', u'read-cache-hits', u'28226639'],
    [u'volume-statistics', u'2', u'read-cache-misses', u'54120346'],
    [u'volume-statistics', u'2', u'small-destages', u'32838729'],
    [u'volume-statistics', u'2', u'full-stripe-write-destages', u'4893881'],
    [
        u'volume-statistics', u'2', u'read-ahead-operations',
        u'4804068203594574099'
    ], [u'volume-statistics', u'2', u'write-cache-space', u'73'],
    [u'volume-statistics', u'2', u'write-cache-percent', u'8'],
    [u'volume-statistics', u'2', u'reset-time', u'2015-04-29', u'11:47:48'],
    [u'volume-statistics', u'2', u'reset-time-numeric', u'1430308068'],
    [
        u'volume-statistics', u'2', u'start-sample-time', u'2015-08-21',
        u'11:51:17'
    ],
    [u'volume-statistics', u'2', u'start-sample-time-numeric', u'1440157877'],
    [
        u'volume-statistics', u'2', u'stop-sample-time', u'2015-08-21',
        u'11:51:47'
    ],
    [u'volume-statistics', u'2', u'stop-sample-time-numeric', u'1440157907']
]

discovery = {
    '': [
        (u'IMSAKO2B1_U1_B01-04_v0001', None),
        (u'IMSAKO2B1_U1_B05-08_v0001', None)
    ],
    'df':
    [(u'IMSAKO2B1_U1_B01-04_v0001', {}), (u'IMSAKO2B1_U1_B05-08_v0001', {})],
    'io': [('SUMMARY', 'diskstat_default_levels')]
}

checks = {
    '': [
        (
            u'IMSAKO2B1_U1_B01-04_v0001', {}, [
                (
                    1,
                    u'Status: warning (There is a warning), container name: IMSAKO2B1_U1_B01-04 (RAID10)',
                    []
                )
            ]
        ),
        (
            u'IMSAKO2B1_U1_B05-08_v0001', {}, [
                (
                    0,
                    u'Status: OK, container name: IMSAKO2B1_U1_B05-08 (RAID10)',
                    []
                )
            ]
        )
    ],
    'df': [
        (
            u'IMSAKO2B1_U1_B01-04_v0001', {
                'trend_range': 24,
                'show_levels': 'onmagic',
                'inodes_levels': (10.0, 5.0),
                'magic_normsize': 20,
                'show_inodes': 'onlow',
                'levels': (80.0, 90.0),
                'show_reserved': False,
                'levels_low': (50.0, 60.0),
                'trend_perfdata': True
            }, [
                (0, u'IMSAKO2B1_U1_B01-04 (RAID10)', []),
                (
                    2,
                    '100% used (1.09 of 1.09 TB), (warn/crit at 80.0%/90.0%)',
                    [
                        (
                            u'IMSAKO2B1_U1_B01-04_v0001', 1143452, 914761.6,
                            1029106.8, 0, 1143452
                        ), ('fs_size', 1143452, None, None, None, None)
                    ]
                )
            ]
        ),
        (
            u'IMSAKO2B1_U1_B05-08_v0001', {
                'trend_range': 24,
                'show_levels': 'onmagic',
                'inodes_levels': (10.0, 5.0),
                'magic_normsize': 20,
                'show_inodes': 'onlow',
                'levels': (80.0, 90.0),
                'show_reserved': False,
                'levels_low': (50.0, 60.0),
                'trend_perfdata': True
            }, [
                (0, u'IMSAKO2B1_U1_B05-08 (RAID10)', []),
                (
                    2,
                    '100% used (1.09 of 1.09 TB), (warn/crit at 80.0%/90.0%)',
                    [
                        (
                            u'IMSAKO2B1_U1_B05-08_v0001', 1143452, 914761.6,
                            1029106.8, 0, 1143452
                        ), ('fs_size', 1143452, None, None, None, None)
                    ]
                )
            ]
        )
    ],
    'io': [
        (
            'SUMMARY', {}, [
                (
                    0, 'Read: 0.00 B/s', [
                        ('disk_read_throughput', 0.0, None, None, None, None)
                    ]
                ),
                (
                    0, 'Write: 0.00 B/s', [
                        ('disk_write_throughput', 0.0, None, None, None, None)
                    ]
                )
            ]
        )
    ]
}
