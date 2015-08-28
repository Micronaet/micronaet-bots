# -*- coding: utf-8 -*-
from bots.botsconfig import *
from euritmo_ORDERS import recorddefs # same as euritmo

# -----------------------------------------------------------------------------
#                             Utility function:
# -----------------------------------------------------------------------------
# TODO: Utility function:
# Format function:
def format_date(value, separator='-', format_type='ISO'):
    ''' Format input date in accounting value    
        value = text value of date (8 or 6 char ISO input)
        separator = if present split date single value
        format_type = 'ISO', 'IT', 'EN' for 3 type of formats
        
        @return text
    '''    
    return value

def format_time(value, separator=':', format_type='HM'):
    ''' Format input date in accounting value    
        value = text value of date (6 or 4 char)
        separator = if present used for separate time
        format_type = 'HM', 'HMS' formats
        
        @return text value
    '''    
    return value

def format_real(value, tuple_format, decimal=',', thousand=''):
    ''' Format text value as IIIIIIDDD value in correct text with separators
    '''
    return value

# Reach information function:
def total_char(recorddef):
    ''' Return total number of char of the record element passed
        (for fixed elements so all tuples like (3, 3)
    '''
    res = 0
    for item in recorddef:
        if item[2] == tuple:
            res += item[2][0] # equal to [1]
        else:
            pass # raise error    
    return res

def total_chat(recorddefs, block_particularity):
    ''' Set filler value in dict for manage filler
        Check all lenght in recorddefs
        Set in block_particularity extra space for filler (first of the list)
    '''
    
    block_length = {} 
    for item recorddefs:
        block_length[item] = total_char(recorddefs[item])
    
    max_char = max(block_length.values()) + 1 # add 1 char (so filler min. 1)
    
    for item block_particularity:
        block_particularity[item][0] = max_char - block_length[item]        
    return

# Set extra information for every block elements, format:
# k = block: value = (
#    date, hour, real, fill extra space)
block_particularity = { 
    'BGM': [0, (), (), (), ],
    #'RFF': [0, (), (), (), ],
    #'RFC': [0, (), (), (), ],

    #'NAS': [0, (), (), (), ],
    #'CTA': [0, (), (), (), ],

    'NAB': [0, (), (), (), ],
    'NAD': [0, (), (), (), ],
    'NAI': [0, (), (), (), ],
    'NAC': [0, (), (), (), ],
    'NAM': [0, (), (), (), ],

    'DTM': [0, (), (), (), ],
    #'FTX': [0, (), (), (), ],
    #'PAT': [0, (), (), (), ],
    #'TOD': [0, (), (), (), ],
    'CNT': [0, (), (), (), ],

    'LIN': [0, (), (), (), ],
    #'MEA': [0, (), (), (), ],
    #'PAC': [0, (), (), (), ],
    #'DTR': [0, (), (), (), ],
    #'ALD': [0, (), (), (), ],
    #'FTL': [0, (), (), (), ],
    #'LOC': [0, (), (), (), ],
    #'DTL': [0, (), (), (), ],
    }
    
# -----------------------------------------------------------------------------
#                   Syntax: Parameters for translation. 
# -----------------------------------------------------------------------------
syntax = { 
    'charset': 'utf-8',
    'merge': False,
    }

structure = [
    {ID: 'BGM', MIN: 1, MAX: 10000, LEVEL: [
        #{ID: 'RFF', MIN: 0, MAX: 1},
        #{ID: 'RFC', MIN: 0, MAX: 10},

        # NAx max 5 record TODO how realize?
        {ID: 'NAS', MIN: 0, MAX: 1},
        #{ID: 'NAS', MIN: 0, MAX: 1, LEVEL: [ # keep in one line
        #    {ID: 'CTA', MIN: 0, MAX: 5},
        #    ]},
        {ID: 'NAB', MIN: 1, MAX: 1},
        {ID: 'NAD', MIN: 1, MAX: 1},
        {ID: 'NAI', MIN: 0, MAX: 1}, # original not mandatory
        {ID: 'NAC', MIN: 0, MAX: 1}, # original not mandatory
        {ID: 'NAM', MIN: 0, MAX: 1}, # original not mandatory

        {ID: 'DTM', MIN: 1, MAX: 1},
        #{ID: 'FTX', MIN: 0, MAX: 5}, # original not mandatory
        #{ID: 'PAT', MIN: 0, MAX: 10}, # original not mandatory
        #{ID: 'TOD', MIN: 0, MAX: 5}, # original not mandatory
        {ID: 'CNT', MIN: 0, MAX: 1}, # original not mandatory (was last element)
        {ID: 'LIN', MIN: 1, MAX: 999},# LEVEL: [
        #    {ID: 'MEA', MIN: 0, MAX: 99}, # original not mandatory
        #    {ID: 'PAC', MIN: 0, MAX: 9999}, # original not mandatory
        #    {ID: 'DTR', MIN: 0, MAX: 99}, # original not mandatory
        #    {ID: 'ALD', MIN: 0, MAX: 99}, # original not mandatory
        #    {ID: 'FTL', MIN: 0, MAX: 99}, # original not mandatory
        #    {ID: 'LOC', MIN: 0, MAX: 9999, LEVEL: [
        #        {ID: 'DTL', MIN: 0, MAX: 9999}, # original not mandatory
        #        ]},
        #    ]},
        ]},
    ]

# -----------------------------------------------------------------------------
#      Add extra fields for filler line to have all same char number
# -----------------------------------------------------------------------------
# TODO
#for block in recorddefs:  # TODO check that is insert only once
#    # Load data
#    tot = block_particularity[block]
#    total_chat(recorddefs, block_particularity)
    recorddefs[block].append(['Account_filler', 'C', (tot, tot), 'AN'])
