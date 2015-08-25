from bots.botsconfig import *

# syntax: parameters for translation. 
syntax = { 
    'charset': 'us-ascii',
    }

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

# TODO the fields in each record. 'BOTSID' is the record tag?
# TODO Date is AN not N
recorddefs = {
    # -------------------------------------------------------------------------
    #                                   BGM
    # -------------------------------------------------------------------------
    # NOTA:
    # In caso di “ordine normale” blank o 105 in TIPORD i qualificatori da 
    # usare 
    # nel documento EDI nel DE 1001(BGM) sono differenti tra D90.1 e D96.a:
    # D90.1 : DE 1001 =105 ordine (come da manuale EDI D90.1)
    # D96.a: DE 1001 = 220 ordine (come da manuale EDI D96.a)
    'BGM': [ # header record
        ['TIPOREC', 'M', (3, 3), 'AN'], # BGM (BOTSID)
            
        # ID-EDI-MITT:
        ['ID-EDI-MITT-1', 'M', (35, 35), 'AN'], # ID sender Piva o EAN/UCC
        ['ID-EDI-MITT-2', 'C', (35, 35), 'AN'], 
        ['ID-EDI-MITT-3', 'C', (35, 35), 'AN'], 

        # ID-EDI-DEST:
        ['ID-EDI-DEST-1', 'M', (35, 35), 'AN'], # ID sender Piva o EAN/UCC
        ['ID-EDI-DEST-2', 'C', (4, 4), 'AN'], 
        ['ID-EDI-DEST-3', 'C', (14, 14), 'AN'], 
            
        ['TIPODOC', 'M', (6, 6), 'AN'], # ORDERS ORDERSP ORDCHG
        ['NUMODOC', 'M', (35, 35), 'AN'],
        ['ORADOC', 'C', (4, 4), 'AN'], # HHMM
            
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
        
    # -------------------------------------------------------------------------
    #                                   RFF
    # -------------------------------------------------------------------------
    # NOTE: 
    # Il Segmento RFF è facoltativo nell'Ordine ed è obbligatorio nella
    # Conferma
    # In caso di dispositivo di consegna seg. BGM campo TIPORD=226 e nella 
    # conferma ordine devono essere obbligatoriamente presenti NUMORDC e 
    # DATAORDC, perché su questi due campi si effettua l'abbinamento con il 
    # relativo Ordine. 
    # NUMORDC e DATAORDC devono essere uguali ai valori di numero e data ordine 
    # presenti nell'ordine.
    'RFF': [
        ['TIPOREC', 'M', (3, 3), 'AN'], # RFF
        
        ['FORDPROM', 'C', (3, 3), 'AN'], # P(romotional), Blank(normal)
        
        ['NUMORDF', 'C', (35, 35), 'AN'], # No in order only confirmation
        ['DATAORDF', 'C', (8, 8), 'AN'], # CCYYMMDD        
        ['ORAORDF', 'C', (4, 4), 'AN'], # HHMM
        
        ['NUMORDC', 'C', (35, 35), 'AN'],
        ['DATAORDC', 'C', (8, 8), 'AN'], # CCYYMMDD        
        ['ORAORDC', 'C', (4, 4), 'AN'], # HHMM
        
        ['NUMPORDF', 'C', (35, 35), 'AN'], # Num. order draft (supplier)
        ['NUMPORDC', 'C', (35, 35), 'AN'], # Num. order draft (customer)                
        ]

    # -------------------------------------------------------------------------
    #                                   RFC
    # -------------------------------------------------------------------------
    # NOTA:
    # Il Segmento RFC è facoltativo nel documento Ordine, e non è da 
    # valorizzare nel documento Conferma Ordine.
    'RFC': [
        ['TIPOREC', 'M', (3, 3), 'AN'], # FRC        
        ['NUMCO', 'M', (35, 35), 'AN'], # Contract number        
        ['DATAINCO', 'C', (8, 8), 'AN'], # CCYYMMDD (start contract) 
        ['DATAFICO', 'C', (8, 8), 'AN'], # CCYYMMDD (end contract)
        ]

    # -------------------------------------------------------------------------
    #                                   NAS
    # -------------------------------------------------------------------------
    'NAS': [
        ['TIPOREC', 'M', (3, 3), 'AN'], # NAS
        ['CODFORN', 'M', (17, 17), 'AN'], # Supplier ID
        
        ['QCODFORN', 'M', (3, 3), 'AN'], 
        # 14 = Cod. EAN / UCC
        # VA = P. IVA
        # 91 = assigned from supplier code 
        # 92 = assigned from customer code
        # ZZ = common code
        
        ['RAGSOCF', 'C', (70, 70), 'AN'], # Supplier
        ['INDIRF', 'C', (70, 70), 'AN'],
        ['CITTAF', 'C', (35, 35), 'AN'],
        ['PROVF', 'C', (9, 9), 'AN'],
        ['CAPF', 'C', (9, 9), 'AN'],
        ['NAZIOF', 'C', (3, 3), 'AN'], # National code
        ['Filler', 'C', (345, 345), 'AN'], # Not used
        ]

    # -------------------------------------------------------------------------
    #                                   NAS
    # -------------------------------------------------------------------------
    'NAS': [
        ['TIPOREC', 'M', (3, 3), 'AN'], # NAS


        

    # 16.3, 'N' >> 
    # quantity is ALWAYS 16 positions; it is written with 3 decimals and 
    # included the decimal sign;
    }
