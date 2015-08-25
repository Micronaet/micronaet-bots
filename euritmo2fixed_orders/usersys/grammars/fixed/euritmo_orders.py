from bots.botsconfig import *

# syntax: parameters for translation. 
syntax = { 
    'charset': 'us-ascii',
    }

# structure: the sequence of the records, and min/max repeats. Records can be 'nested'
structure = [
    {ID: 'BGM', MIN: 1, MAX: 10000, LEVEL: [
        {ID: 'RFF', MIN: 0, MAX: 1},
        {ID: 'RFC', MIN: 0, MAX: 10},
        
        # NAx max 5 record TODO how realize?
        {ID: 'NAS', MIN: 0, MAX: 1, LEVEL: [
            {ID: 'CTA', MIN: 0, MAX: 5},            
            ]},
        {ID: 'NAB', MIN: 1, MAX: 1},
        {ID: 'NAD', MIN: 1, MAX: 1},
        {ID: 'NAI', MIN: 0, MAX: 1},
        {ID: 'NAC', MIN: 0, MAX: 1},
        {ID: 'NAM', MIN: 0, MAX: 1},
        
        {ID: 'DTM', MIN: 1, MAX: 1},
        {ID: 'FTX', MIN: 0, MAX: 5},
        {ID: 'PAT', MIN: 0, MAX: 10},
        {ID: 'TOD', MIN: 0, MAX: 5, LEVEL: [
            {ID: 'MEA', MIN: 0, MAX: 99},
            {ID: 'PAC', MIN: 0, MAX: 9999},
            {ID: 'DTR', MIN: 0, MAX: 99},
            {ID: 'ALD', MIN: 0, MAX: 99},
            {ID: 'FLT', MIN: 0, MAX: 99},
            {ID: 'LOC', MIN: 0, MAX: 9999, LEVEL: [
                {ID: 'DLT', MIN: 0, MAX: 9999},                
                ]},
            ]},            
        {ID: 'CNT', MIN: 0, MAX: 1},
        ]},
    ]

# the fields in each record. 'BOTSID' is the record tag.
recorddefs = {
    'BGM': [ # header record
            ['BOTSID', 'C', 3, 'A'],
            ['MESSAGETYPE', 'M', 20, 'AN'], # field 'MESSAGETYPE' is Mandatory, amx 20 positions, and alphanumeric
            ['SENDER', 'C', (13, 13), 'N'], # field 'SENDER' is Conditional, min 13, max 13 and Numeric
            ['RECEIVER', 'C', 13, 'AN'],         
            ['ORDERNUMBER', 'C', 17, 'AN'],         
            ['ORDERDATE', 'C', 12, 'AN'],          
            ['ORDERTYPE', 'C', 3, 'AN'],          
            ['BUYER_ID', 'C', 13, 'AN'],         
            ['SUPPLIER_ID', 'C', 13, 'AN'],         
            ['DELIVERYPLACE_ID', 'C', 13, 'AN'],         
            ['DELIVERY_DATE', 'C', 12, 'AN'],          
          ],
    'LIN': [ # line record
            ['BOTSID', 'C', 3, 'A'],
            ['LINENUMBER', 'C', 6, 'N'],         
            ['ARTICLE_GTIN', 'C', 14, 'AN'],         
            ['DESCRIPTION', 'C', 35, 'AN'],         
            ['QUANTITY', 'C', 16.3, 'N'], # quantity is ALWAYS 16 positions; it is written with 3 decimals and included the decimal sign;
          ],
    }
