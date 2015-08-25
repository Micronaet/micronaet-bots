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
            ['TIPOREC', 'M', (3, 3), 'A'], # BOTSID
            
            # ID-EDI-MITT:
            ['ID-EDI-MITT-1', 'M', (35, 35), 'AN'], # ID sender Piva o EAN/UCC
            ['ID-EDI-MITT-2', 'C', (35, 35), 'AN'], 
            ['ID-EDI-MITT-3', 'C', (35, 35), 'AN'], 

            # ID-EDI-DEST:
            ['ID-EDI-DEST-1', 'M', (35, 35), 'AN'], # EDI ID sender Piva o EAN / UCC
            ['ID-EDI-DEST-2', 'C', (4, 4), 'AN'], 
            ['ID-EDI-DEST-3', 'C', (14, 14), 'AN'], 
            
            ['TIPODOC', 'M', (6, 6), 'AN'], # ORDERS ORDERSP ORDCHG
            ['NUMODOC', 'M', (35, 35), 'AN'],
            ['ORADOC', 'C', (4, 4), 'N'], # HHMM
            
            ['CODAZION', 'C', (3, 3), 'AN'], 
            # ORDER: C, CONF: M [R(ifiutato), A(ccettato), M(odificato)]
            
            ['FLAGIMPE', 'C', (3, 3), 'AN'], 
            # ORDER: C, CONF: M [X99 = impegn., blank= non impegn.]
 
            ['TIPORD', 'C', (3, 3), 'AN'],
            # Blank or 105 = Order (different from D90.1 > 105, D96.a > 220)
            # 211 Blanket order (open)
            # 224 Urgent
            # 226 Call off order (dispos. of delivery)
            # 231 Confirm order from producer
            # YA9 Preallocated order
          ],

    'LIN': [ # line record
            ['BOTSID', 'C', 3, 'A'],
            ['LINENUMBER', 'C', 6, 'N'],         
            ['ARTICLE_GTIN', 'C', 14, 'AN'],         
            ['DESCRIPTION', 'C', 35, 'AN'],         
            ['QUANTITY', 'C', 16.3, 'N'], # quantity is ALWAYS 16 positions; it is written with 3 decimals and included the decimal sign;
          ],
    }
