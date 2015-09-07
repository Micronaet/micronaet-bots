# -*- coding: utf-8 -*-
from bots.botsconfig import *
from euritmo_ORDERS import recorddefs # same as euritmo

# -----------------------------------------------------------------------------
#                             Constant declaration
# -----------------------------------------------------------------------------
FILLER = 'filler_field'

# -----------------------------------------------------------------------------
#                               Utility function
# -----------------------------------------------------------------------------

# TODO: Utility function:
# ----------------
# Format function:
# ----------------
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
# -----------------------------------------------------------------------------

# ---------------------------
# Reach information function:
# ---------------------------
def char_block(block, log=False):
    ''' Return total number of char of the record element passed
        (for fixed elements so all tuples like (3, 3) >> 3 )
        log = write in log if True (TODO put False)
        NOTE: seems that tuple element became integer (record will be parsed!)
    '''
    res = 0
    for item in block:
        res += item[2] # never tuple (pre-parsed, is not the original)
        if log:
            print "[INFO] Block: %s - Total char: %s" % (block, res)
    return res

def total_char_filler(recorddefs, block_particularity, log=False):
    ''' Set filler value in dict for manage filler
        Check all lenght in recorddefs
        Set in block_particularity extra space for filler (first of the list)
    '''
    
    block_length = {} 
    # TODO remove from here (every time check max elements!!)
    for item in block_particularity: # NOTE: use partic key but search in rec.
        # only length 3 (there's a 'BOTS_1$@#%_error' block!!)
        if len(item) == 3:
            block_length[item] = char_block(recorddefs[item], log)
    
    max_char = max(block_length.values()) + 1 # add 1 char (so filler min. 1)
    
    for item in block_particularity:
        block_particularity[item][0] = max_char - block_length[item]
        if log: 
            print "[INFO] Block: %s [%s (max) - %s (len.) = %s (filler)]" % (
                item, max_char, block_length[item], 
                block_particularity[item][0])
    return

# Set extra information for every block elements, format:
# k = block: value = (
#    fill extra space, date, hour, real)
# TODO fill when decide format of number, date etc.
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
    #'merge': False,
    }

structure = [
    {ID: 'BGM', MIN: 1, MAX: 10000, LEVEL: [
        #{ID: 'RFF', MIN: 0, MAX: 1}, # TODO for promotional order?
        #{ID: 'RFC', MIN: 0, MAX: 10}, # (contract)

        # NAx max 5 record TODO how realize?
        {ID: 'NAS', MIN: 0, MAX: 1}, # Supplier info (was mandatory)
        #{ID: 'NAS', MIN: 1, MAX: 1, LEVEL: [ # keep in one line
        #    {ID: 'CTA', MIN: 0, MAX: 5}, # Contact supplier
        #    ]},
        {ID: 'NAB', MIN: 1, MAX: 1}, # Buyer
        {ID: 'NAD', MIN: 1, MAX: 1}, # Destination
        #{ID: 'NAI', MIN: 0, MAX: 1}, # Address invoice # TODO asking...
        #{ID: 'NAC', MIN: 0, MAX: 1}, # Inter-delivery point
        #{ID: 'NAM', MIN: 0, MAX: 1}, # Stock delivery info

        {ID: 'DTM', MIN: 1, MAX: 1}, # Delivery info
        #{ID: 'FTX', MIN: 0, MAX: 5}, # Header extra info (note)
        #{ID: 'PAT', MIN: 0, MAX: 10}, # Payment terms
        #{ID: 'TOD', MIN: 0, MAX: 5}, # Delivery condition
        #{ID: 'CNT', MIN: 0, MAX: 1}, # Summary (was last element)
        {ID: 'LIN', MIN: 1, MAX: 999},# LEVEL: [
        #    {ID: 'MEA', MIN: 0, MAX: 99}, # measure
        #    {ID: 'PAC', MIN: 0, MAX: 9999}, # package
        #    {ID: 'DTR', MIN: 0, MAX: 99}, # delivery date for line
        #    {ID: 'ALD', MIN: 0, MAX: 99}, # discount for line
        #    {ID: 'FTL', MIN: 0, MAX: 99}, # Note for line
        #    {ID: 'LOC', MIN: 0, MAX: 9999, LEVEL: [ # delivery for line
        #        {ID: 'DTL', MIN: 0, MAX: 9999}, # delivery date for line
        #        ]},
        #    ]},
        ]},
    ]

# -----------------------------------------------------------------------------
#      Add extra fields for filler line to have all same char number
# -----------------------------------------------------------------------------
log = True  # TODO change!!
for block in recorddefs:  # TODO check that is insert only once
    if block not in block_particularity: 
        continue # Jump block not used
    if FILLER not in recorddefs[block]:  # else yet created
        # Load extra info for block (es. extra space):
        total_char_filler(recorddefs, block_particularity, log)
        
        tot = block_particularity[block][0]
        recorddefs[block].append([FILLER, 0, tot, 'AN', True, 0, tot, 'A', 1])
        #recorddefs[block].append([FILLER, 'C', (tot, tot), 'AN'])        
