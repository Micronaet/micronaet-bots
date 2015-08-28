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
        #{ID: 'RFC', MIN: 0, MAX: 99999}, # Contract info
        
        {ID: 'NAS', MIN: 1, MAX: 1}, # Supplier info (TODO load here?)
        {ID: 'NAI', MIN: 1, MAX: 1}, # Address invoice info (TODO load here?)
        #{ID: 'NAP', MIN: 0, MAX: 1}, # Payers if different
        #{ID: 'NAA', MIN: 0, MAX: 1}, # Who invoice if different 
        #{ID: 'NAT', MIN: 0, MAX: 1}, # Paper invoice destination 
       
        #{ID: 'FTX', MIN: 0, MAX: 5}, # Header note
        #{ID: 'PAT', MIN: 0, MAX: 10}, # Payment terms 
        #{ID: 'TOD', MIN: 0, MAX: 5, LEVEL: [ # Delivery conditions
        #    {ID: 'LOC', MIN: 0, MAX: 2}, # Delivery point
        #    ]},
        {ID: 'DET', MIN: 1, MAX: 1, LEVEL: [
            {ID: 'DES', MIN: 0, MAX: 10}, # Description # TODO ask
        #    {ID: 'RFN', MIN: 0, MAX: 10}, # Accredit note reference
        #    {ID: 'TAX', MIN: 0, MAX: 15}, # Tax info
        #    {ID: 'ALD', MIN: 0, MAX: 15}, # Discount line
            {ID: 'NAD', MIN: 1, MAX: 1}, # Delivery point 
        #    {ID: 'NAE', MIN: 0, MAX: 1}, # DDT emit.
        #    {ID: 'NAR', MIN: 0, MAX: 1}, # Cess. info
        #    {ID: 'NAM', MIN: 0, MAX: 1}, # Stock delivery 
        #    {ID: 'NAF', MIN: 0, MAX: 1}, # Location delivery
        #    {ID: 'NAX', MIN: 0, MAX: 1}, # Financial refund
        #    {ID: 'FLT', MIN: 0, MAX: 5}, # Row note
            ]},
        #{ID: 'FTT', MIN: 0, MAX: 5}, # Summary note
        #{ID: 'ALT', MIN: 0, MAX: 15}, # Discount info
        #{ID: 'IVA', MIN: 0, MAX: 10}, # Subtotal VAT
        {ID: 'TMA', MIN: 1, MAX: 1}, # Invoice totals
        ]},
    ]
