# -*- coding: utf-8 -*-
from bots.botsconfig import *

# Syntax: Parameters for translation. 
syntax = { 
    'charset': 'utf-8',
    }

structure = [{
    ID: 'BGM', MIN: 1, MAX: 10000, 
    # TODO
    ]

recorddefs = {
    'BGM': [ # header record
        ['BOTSID', 'M', (3, 3), 'AN'], # BGM (BOTSID)
        ['ID-EDI-MITT-1', 'M', (35, 35), 'AN'], # ID sender Piva o EAN/UCC
        ],
    # TODO     
    }
