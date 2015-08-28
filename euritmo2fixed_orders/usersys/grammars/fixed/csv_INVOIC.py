# -*- coding: utf-8 -*-
from bots.botsconfig import *
from euritmo_INVOIC import recorddefs # same as euritmo

# -----------------------------------------------------------------------------
#                   Syntax: Parameters for translation. 
# -----------------------------------------------------------------------------
syntax = { 
    'charset': 'utf-8',
    }

structure = [
    {ID: 'BGM', MIN: 1, MAX: 1, LEVEL: [
        #{ID: 'RFC', MIN: 0, MAX: 99999},
        
        {ID: 'NAS', MIN: 1, MAX: 1},
        {ID: 'NAI', MIN: 1, MAX: 1},
        #{ID: 'NAP', MIN: 0, MAX: 1},
        #{ID: 'NAA', MIN: 0, MAX: 1},
        #{ID: 'NAT', MIN: 0, MAX: 1},
       
        #{ID: 'FTX', MIN: 0, MAX: 5},
        #{ID: 'PAT', MIN: 0, MAX: 10},
        #{ID: 'TOD', MIN: 0, MAX: 5, LEVEL: [
        #    {ID: 'LOC', MIN: 0, MAX: 2},
        #    ]},
        {ID: 'DET', MIN: 1, MAX: 1, LEVEL: [
        #    {ID: 'DES', MIN: 0, MAX: 10},
        #    {ID: 'RFN', MIN: 0, MAX: 10},
        #    {ID: 'TAX', MIN: 0, MAX: 15},
        #    {ID: 'ALD', MIN: 0, MAX: 15},
        # TODO    {ID: 'NAD', MIN: 1, MAX: 1},
        #    {ID: 'NAE', MIN: 0, MAX: 1},
        #    {ID: 'NAR', MIN: 0, MAX: 1},
        #    {ID: 'NAM', MIN: 0, MAX: 1},
        #    {ID: 'NAF', MIN: 0, MAX: 1},
        #    {ID: 'NAX', MIN: 0, MAX: 1},
        #    {ID: 'FLT', MIN: 0, MAX: 5},
            ]},
        #{ID: 'FTT', MIN: 0, MAX: 5},
        #{ID: 'ALT', MIN: 0, MAX: 15},
        #{ID: 'IVA', MIN: 0, MAX: 10},
        {ID: 'TMA', MIN: 1, MAX: 1},
        ]},
    ]
