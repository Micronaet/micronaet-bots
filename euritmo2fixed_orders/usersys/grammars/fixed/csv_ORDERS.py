# -*- coding: utf-8 -*-
from bots.botsconfig import *
from euritmo_ORDERS import recorddefs # same as euritmo

# Syntax: Parameters for translation. 
syntax = { 
    'charset': 'utf-8',
    }

structure = [
    {ID: 'BGM', MIN: 1, MAX: 10000, LEVEL: [
        #{ID: 'RFF', MIN: 0, MAX: 1},
        #{ID: 'RFC', MIN: 0, MAX: 10},

        # NAx max 5 record TODO how realize?
        #{ID: 'NAS', MIN: 0, MAX: 1, LEVEL: [
        #    {ID: 'CTA', MIN: 0, MAX: 5},
        #    ]},
        {ID: 'NAB', MIN: 1, MAX: 1},
        {ID: 'NAD', MIN: 1, MAX: 1},
        #{ID: 'NAI', MIN: 0, MAX: 1},
        #{ID: 'NAC', MIN: 0, MAX: 1},
        #{ID: 'NAM', MIN: 0, MAX: 1},

        #{ID: 'DTM', MIN: 1, MAX: 1},
        #{ID: 'FTX', MIN: 0, MAX: 5},
        #{ID: 'PAT', MIN: 0, MAX: 10},
        #{ID: 'TOD', MIN: 0, MAX: 5},
        {ID: 'LIN', MIN: 1, MAX: 999},# LEVEL: [
        #    {ID: 'MEA', MIN: 0, MAX: 99},
        #    {ID: 'PAC', MIN: 0, MAX: 9999},
        #    {ID: 'DTR', MIN: 0, MAX: 99},
        #    {ID: 'ALD', MIN: 0, MAX: 99},
        #    {ID: 'FTL', MIN: 0, MAX: 99},
        #    {ID: 'LOC', MIN: 0, MAX: 9999, LEVEL: [
        #        {ID: 'DTL', MIN: 0, MAX: 9999},
        #        ]},
        #    ]},
        #{ID: 'CNT', MIN: 0, MAX: 1}
        ]},
    ]

# Add extra fields for filler to same recordset
#recorddefs['BGM'].append(['FillerBGM', 'C', (57, 57), 'AN'])
