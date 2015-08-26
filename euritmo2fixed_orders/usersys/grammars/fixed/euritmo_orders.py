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
    #                    BGM Mandatory information (document)
    # -------------------------------------------------------------------------
    # NOTA:
    # In caso di “ordine normale” blank o 105 in TIPORD i qualificatori da 
    # usare 
    # nel documento EDI nel DE 1001(BGM) sono differenti tra D90.1 e D96.a:
    # D90.1 : DE 1001 =105 ordine (come da manuale EDI D90.1)
    # D96.a: DE 1001 = 220 ordine (come da manuale EDI D96.a)
    'BGM': [ # header record
        ['BOTSID', 'M', (3, 3), 'AN'], # BGM (BOTSID)
            
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
    #                  RFF Reference information about document
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
        ['BOTSID', 'M', (3, 3), 'AN'], # RFF
        
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
    #                      RFC Reference contract information
    # -------------------------------------------------------------------------
    # NOTA:
    # Il Segmento RFC è facoltativo nel documento Ordine, e non è da 
    # valorizzare nel documento Conferma Ordine.
    'RFC': [
        ['BOTSID', 'M', (3, 3), 'AN'], # FRC        
        ['NUMCO', 'M', (35, 35), 'AN'], # Contract number        
        ['DATAINCO', 'C', (8, 8), 'AN'], # CCYYMMDD (start contract) 
        ['DATAFICO', 'C', (8, 8), 'AN'], # CCYYMMDD (end contract)
        ]

    # -------------------------------------------------------------------------
    #                      NAS (Supplier information) NAD 3055 = SU
    # -------------------------------------------------------------------------
    'NAS': [
        ['BOTSID', 'M', (3, 3), 'AN'], # NAS
        ['CODFORN', 'M', (17, 17), 'AN'], # Supplier ID
        
        ['QCODFORN', 'M', (3, 3), 'AN'], 
        # 14 = Cod. EAN / UCC
        # VA = P. IVA
        # 91 = assigned from supplier code 
        # 92 = assigned from customer code
        # ZZ = common defined code
        
        ['RAGSOCF', 'C', (70, 70), 'AN'], # Supplier
        ['INDIRF', 'C', (70, 70), 'AN'],
        ['CITTAF', 'C', (35, 35), 'AN'],
        ['PROVF', 'C', (9, 9), 'AN'],
        ['CAPF', 'C', (9, 9), 'AN'],
        ['NAZIOF', 'C', (3, 3), 'AN'], # National code
        ['Filler', 'C', (345, 345), 'AN'], # Not used
        ]

    # -------------------------------------------------------------------------
    #                     CTA Supplier contact information
    # -------------------------------------------------------------------------
    'CTA': [
        ['BOTSID', 'M', (3, 3), 'AN'], # CTA
        
        ['FUNZCONT', 'C', (3, 3), 'AN'],
        # AP = Accounting
        # IC = Generic for information
        # OC = Order contact
        # SA = Sale admin
        # SD = Delivery 

        ['TELEFONO', 'C', (25, 25), 'AN'],
        ['FAX', 'C', (25, 25), 'AN'],
        ['TELEX', 'C', (25, 25), 'AN'],
        ['EMAIL', 'C', (70, 70), 'AN'],
        ]

    # -------------------------------------------------------------------------
    #                     NAB Buyer information NAD 3035 = BY
    # -------------------------------------------------------------------------
    'NAB': [
        ['BOTSID', 'M', (3, 3), 'AN'], # NAB
        ['CODBUYER', 'M', (17, 17), 'AN'], # Ean / UCC, location, VAT
        ['QCODBUY', 'M', (3, 3), 'AN'], 
        # 14 = EAN / UCC
        # VA = VAT
        # 91 = code assigned by supplier
        # 92 = code assigned by customer
        # ZZ = common defined code

        ['RAGSOCB', 'C', (70, 70), 'AN'], 
        ['INDIRB', 'C', (70, 70), 'AN'], 
        ['CITTAB', 'C', (35, 35), 'AN'],
        ['PROVB', 'C', (9, 9), 'AN'],
        ['CAPB', 'C', (9, 9), 'AN'],
        ['NAZIOB', 'C', (3, 3), 'AN'], # National code
        ['Filler', 'C', (86, 86), 'AN'], # Not used
        ]
        
    # -------------------------------------------------------------------------
    #              NAD Delivery point information NAD 3035 = DP
    # -------------------------------------------------------------------------
    'NAD': [
        ['BOTSID', 'M', (3, 3), 'AN'], # NAD
        ['CODCONS', 'M', (17, 17), 'AN'], # Ean / UCC, location, VAT
        ['QCODCONS', 'M', (3, 3), 'AN'], 
        # 14 = EAN / UCC
        # VA = VAT
        # 91 = code assigned by supplier
        # 92 = code assigned by customer
        # ZZ = common defined code

        ['RAGSOCD', 'C', (70, 70), 'AN'], 
        ['INDIRD', 'C', (70, 70), 'AN'], 
        ['CITTAD', 'C', (35, 35), 'AN'],
        ['PROVD', 'C', (9, 9), 'AN'],
        ['CAPD', 'C', (9, 9), 'AN'],
        ['NAZIOD', 'C', (3, 3), 'AN'], # National code
        ['Filler', 'C', (86, 86), 'AN'], # Not used
        ]
        
    # -------------------------------------------------------------------------
    #              NAI Invoice addresser information NAD 3035 = IV
    # -------------------------------------------------------------------------
    'NAI': [
        ['BOTSID', 'M', (3, 3), 'AN'], # NAI
        ['CODFATT', 'M', (17, 17), 'AN'], # Ean / UCC, location, VAT
        ['QCODFATT', 'M', (3, 3), 'AN'], 
        # 14 = EAN / UCC
        # VA = VAT
        # 91 = code assigned by supplier
        # 92 = code assigned by customer
        # ZZ = common defined code

        ['RAGSOCI', 'C', (70, 70), 'AN'], 
        ['INDIRI', 'C', (70, 70), 'AN'], 
        ['CITTAI', 'C', (35, 35), 'AN'],
        ['PROVI', 'C', (9, 9), 'AN'],
        ['CAPI', 'C', (9, 9), 'AN'],
        ['NAZIOI', 'C', (3, 3), 'AN'], # National code
        ['Filler', 'C', (86, 86), 'AN'], # Not used
        ]
        
    # -------------------------------------------------------------------------
    #             NAC Stock receive point information NAD 3035 = IC
    # -------------------------------------------------------------------------
    'NAC': [
        ['BOTSID', 'M', (3, 3), 'AN'], # NAC
        ['CODMAGI', 'M', (17, 17), 'AN'], # Ean / UCC, location, VAT
        ['QCODMAGI', 'M', (3, 3), 'AN'], 
        # 14 = EAN / UCC
        # VA = VAT
        # 91 = code assigned by supplier
        # 92 = code assigned by customer
        # ZZ = common defined code

        ['RAGSOCC', 'C', (70, 70), 'AN'], 
        ['INDIRC', 'C', (70, 70), 'AN'], 
        ['CITTAC', 'C', (35, 35), 'AN'],
        ['PROVC', 'C', (9, 9), 'AN'],
        ['CAPC', 'C', (9, 9), 'AN'],
        ['NAZIOC', 'C', (3, 3), 'AN'], # National code
        ['Filler', 'C', (86, 86), 'AN'], # Not used
        ]
        
    # -------------------------------------------------------------------------
    #            NAM Stock delivery point information NAD 3035 = PW
    # -------------------------------------------------------------------------
    'NAM': [
        ['BOTSID', 'M', (3, 3), 'AN'], # NAC
        ['CODMAGP', 'M', (17, 17), 'AN'], # Ean / UCC, location, VAT
        ['QCODMAGP', 'M', (3, 3), 'AN'], 
        # 14 = EAN / UCC
        # VA = VAT
        # 91 = code assigned by supplier
        # 92 = code assigned by customer
        # ZZ = common defined code

        ['RAGSOCM', 'C', (70, 70), 'AN'], 
        ['INDIRM', 'C', (70, 70), 'AN'], 
        ['CITTAM', 'C', (35, 35), 'AN'],
        ['PROVM', 'C', (9, 9), 'AN'],
        ['CAPM', 'C', (9, 9), 'AN'],
        ['NAZIOM', 'C', (3, 3), 'AN'], # National code
        ['Filler', 'C', (86, 86), 'AN'], # Not used
        ]
        
    # -------------------------------------------------------------------------
    #                    DTM Delivery date information
    # -------------------------------------------------------------------------
    'DTM': [
        ['BOTSID', 'M', (3, 3), 'AN'], # DTM
        ['DATACONS', 'M', (8, 8), 'AN'], # CCYYMMDD
        ['ORACONS', 'C', (4, 4), 'AN'], # HHMM
        
        ['TIPODATAC', 'M', (3, 3), 'AN'],
        # 002 = date / time delivery requested
        # 064 = no delivery before date-hour
        # 069 = mandatory date-hour delivery granted
        
        ['DATACON2', 'M', (8, 8), 'AN'], # CCYYMMDD
        ['ORACON2', 'C', (4, 4), 'AN'], # HHMM
        
        ['TIPODATA2', 'M', (3, 3), 'AN'],
        # 063 = no delivery after date-hour
        # only present if TIPODATAC = 064
        ]
        
    # -------------------------------------------------------------------------
    #                 FTX Extra information and notes (header)
    # -------------------------------------------------------------------------
    # Nota:
    # Per le transazioni EDI che rientrano nell’ambito di applicazione 
    # dell’art. 62 del decreto legge 24 gennaio 2012 (convertito dalla legge 
    # 24 marzo 2012, n° 27) è possibile inserire nel campo NOTE la
    # dicitura “Assolve gli obblighi di cui all’articolo 62, comma 1, del 
    # decreto legge 24 gennaio 2012, n. 1, convertito, con modificazioni, 
    # dalla legge 24 marzo 2012, n. 27.”
    'FTX': [
        ['BOTSID', 'M', (3, 3), 'AN'], # FTX
        ['DIVISA', 'C', (3, 3), 'AN'], # ITL = Lira, EUR = Euro
        ['NOTE', 'C', (210, 210), 'AN'], # Extra info for payment
        ]
        
    # -------------------------------------------------------------------------
    #              PAT Terms information, payment mode
    # -------------------------------------------------------------------------
    'PAT': [
        ['BOTSID', 'M', (3, 3), 'AN'], # PAT
        
        ['TIPOCOND', 'M', (3, 3), 'AN'],
        # 20 = Penalty terms
        # 21 = Split payment
        # 22 = Discount
        # 10E = Complete payment

        ['DATASCAD', 'C', (8, 8), 'AN'], # CCYYMMDD
        
        # CONDPAG:
        ['RIFTERMP', 'M', (3, 3), 'AN'], # Payment term ref.
        # 1 = Order date
        # 5 = Invoice date
        # 9 = Receive date
        # 21 = Receive goods
        # 66 = Specific date
        # 70 = Emission date (transport document)
        # 81 = Start date transport
        ['RELTERMP', 'C', (3, 3), 'AN'], # Temporal relation
        # 1 = Reference date
        # 3 = Date after ref.
        # 6 = End month from reference date
        # 7 = End month after receive
        # 12E = 15 / last day of month for payment
        ['UNTEMP', 'C', (3, 3), 'AN'],
        # D = Days
        # W = Weeks
        # M = Months
        # Y = Years
        ['NUNTEMP', 'C', (3, 3), 'AN'], # Payment term ref.

        ['IMPORTO', 'C', (16, 16), 'AN'], # 12 + 3 N for 12.3
        ['DIVISA', 'C', (3, 3), 'AN'], # ISO code for currency
        ['PERC', 'C', (7, 7), 'AN'], # 3 + 4 N for 3.4
        ['DESCRIZ', 'C', (35, 35), 'AN'], # Payment description
        
        ['BANCADOC', 'C', (35, 35), 'AN'],
        # Format: ABI(5) - CAB(5) - C/C(23)
        ['BANCADESC', 'C', (35, 35), 'AN'], # Bank name
        ['FACTOR', 'C', (35, 35), 'AN'],

        ['CODPAG', 'C', (3, 3), 'AN'], 
        # Payment code:
        # 1 = Direct paymenyt
        # 35 = Bank document payment

        ['MEZZOPAG', 'C', (3, 3), 'AN'],
        # 10 = Cach
        # 20 = Cheque
        # 23 = Circular cheque
        # 30 = Bank transfer
        # 31 = Bank transfer
        # 42 = Payment via CC bank
        # 70 = Trat
        # 15E = RID
        # 74 = Bank ric.
        # 97 = Fin. Compensation
        ]
        
    # -------------------------------------------------------------------------
    #              TOD Delivery condition, transport
    # -------------------------------------------------------------------------
    'TOD': [
        ['BOTSID', 'M', (3, 3), 'AN'], # TOD
        
        ['CODCONS', 'M', (3, 3), 'AN'], 
        # 2 = Delivery condition
        # 3 = Cost anc delivery condition

        ['CODCONT', 'M', (3, 3), 'AN'], 
        # Transport costs to:
        # PP = sender
        # CC = receiver

        ['CODCOND', 'C', (3, 3), 'AN'], # INCOTERMS
        ['DESCOND1', 'M', (70, 70), 'AN'], 
        ['DESCOND2', 'M', (70, 70), 'AN'], 
        ]
        
    # -------------------------------------------------------------------------
    #                      LIN Details information
    # -------------------------------------------------------------------------
    'LIN': [
        ['BOTSID', 'M', (3, 3), 'AN'], # LIN
        
        ['NUMRIGA', 'C', (6, 6), 'AN'], # Number of line # TODO N
        ['CODEANCU', 'C', (35, 35), 'AN'], # EAN / UCC UPC of CU
        
        ['TIPOCODCU', 'C', (3, 3), 'AN'], 
        # EN = code EAN / UCC
        # UP = UPC

        ['CODEANTU', 'C', (35, 35), 'AN'], # EAN / UCC / TU
        ['CODFORTU', 'C', (35, 35), 'AN'], # TU code (from prod.)
        ['CODDISTU', 'C', (35, 35), 'AN'], # TU code (from distr.)
        ['DESART', 'M', (35, 35), 'AN'], # Description item
        ['FLINPROM', 'C', (3, 3), 'AN'],
        # P = Promotional order
        # Blank = normal order

        ['QTAORD', 'M', (15, 15), 'AN'], # 12 + 3, 12.3 TODO N
        ['UDMQORD', 'C', (3, 3), 'AN'],
        # CT = Pack
        # PCE = Piece
        # KGM = Kg
        # MTR = Meter
        # MTK = MQ
        # LTR = Liter
        # CU = Consumer unit
        # TU = Trade unit
        # Note: Mandatory if present QTAORD
        
        ['PRZUNI', 'C', (15, 15), 'AN'], # 12 + 3, 12.3 # TODO N        
        ['TIPOPRZ', 'C', (3, 3), 'AN'], 
        # AAA= Net
        # AAB = Lord
        # Nota: Mandatory if PRZUNI
        
        ['UDMPRZUN', 'C', (3, 3), 'AN'],
        # CT = Pack
        # PCE = Piece
        # KGM = Kg
        # MTR = Meter
        # MTK = MQ
        # LTR = Liter
        # CU = Consumer unit
        # TU = Trade unit
        # Note: Mandatory if present PRZUNI

        ['NRCUINTU', 'C', (15, 15), 'AN'], # 12 + 3, 12.3 # TODO N        
        ['CODAZIOL', 'C', (3, 3), 'AN'], 
        # Mandatory NOT present in order
        # Mandatory present in order
        
        ['QTACONF', 'C', (15, 15), 'AN'], # 12 + 3, 12.3 # TODO N        
        ['UDMQCONF', 'C', (3, 3), 'AN'],
        # CT = Pack
        # PCE = Piece
        # KGM = Kg
        # MTR = Meter
        # MTK = MQ
        # LTR = Liter
        # CU = Consumer unit
        # TU = Trade unit
        # Note: Mandatory if present QTACONF
        
        ['PRZUN2', 'C', (15, 15), 'AN'], # 12 + 3, 12.3 # TODO N        
        ['TIPOPRZ2', 'C', (3, 3), 'AN'], 
        # AAA= Net
        # AAB = Lord
        # Nota: Mandatory if PRZUNI
        ['UDMPRZUN2', 'C', (3, 3), 'AN'],
        # CT = Pack
        # PCE = Piece
        # KGM = Kg
        # MTR = Meter
        # MTK = MQ
        # LTR = Liter
        # CU = Consumer unit
        # TU = Trade unit
        # Note: Mandatory if present PRZUN2
        ]

    # -------------------------------------------------------------------------
    #                      MEA Product measure product
    # -------------------------------------------------------------------------
    'MEA': [
        ['BOTSID', 'M', (3, 3), 'AN'], # MEA
        ['QUALMISURA', 'M', (3, 3), 'AN'],
        # PD = Physical dimension (order product)
        ['IDDIMENCOD', 'C', (3, 3), 'AN'],
        # AAA = Net unit
        # AAB = Lord unit
        # DBX = BRIX grade (EAN UCC)
        # DN = Density
        # HT = Height
        # LN = Length
        # UCO = Unit for pack
        # WD = Width
        # LAY = Number of layer
        # ULY = Number of unit
        ['SIGNIMISCOD', 'C', (3, 3), 'AN'],
        # 3 = Nearest
        # 4 = Exactly equal
        ['QUALUNIMIS', 'M', (3, 3), 'AN'],
        # CMT = Centimeter
        # GRM = Grams
        # KGM = Kg
        # LTR = Liter
        # MLT = Milliliter
        # MTR = Meter
        # PCE = Piece
        # MTK = Square meter
        ['VALOMISURA', 'C', (15, 15), 'AN'], # 12 + 3, 12.3 # TODO N        
        ['RANGEMIN', 'C', (15, 15), 'AN'], # 12 + 3, 12.3 # TODO N        
        ['RANGEMAS', 'C', (15, 15), 'AN'], # 12 + 3, 12.3 # TODO N        
        ]

    # -------------------------------------------------------------------------
    #                      PAC Pack information
    # -------------------------------------------------------------------------
    'PAC': [
        ['BOTSID', 'M', (3, 3), 'AN'], # PAC
        
        ['QTAIMB', 'M', (15, 15), 'AN'], # 12 + 3, 12.3, number of pack #TODO N   
        ['INFIMBACOD', 'C', (3, 3), 'AN'], 
        # 50 = Coded with EAN / UCC (13 or 8)
        # 51 = Pack coded ITF-14 ITF-6
        # 52 = Coded package with UCC / EAN-128
        
        ['CONIMBCOD', 'C', (3, 3), 'AN'],
        # 1 = Pack cost to supplier
        # 2 = Pack cost to client
        # 3 = Pack cost not to pay (to return)
        # 4E = Loaned (EAN UCC code)
        # 5E = Interchangable (EAN UCC code)
        # 6E = Deposit (EAN UCC code)
        # 7E = Not reusable (EAN UCC code)
        ['IDETIPIMB', 'C', (3, 3), 'AN'],
        # 08 = Lost pallet
        # 09 = Pallet to return (EAN UCC code)
        # 201 = Pallet ISO 1 (EAN UCC code)
        # PK = Pack
        # DPE = Expositors
        # 200 = Pallet ISO 0 
        # 203 = 1/4 EURO pallet
        ['RESPAGIMBREST', 'C', (3, 3), 'AN'],
        # 1 = Customer pay
        # 2 = Free
        # 3 = SUpplier pay
        ]
                
    # -------------------------------------------------------------------------
    #          DTR Delivery date information and level order line
    # -------------------------------------------------------------------------
    # Note: Con questo record DTR il fornitore, in fase di conferma, può 
    # indicare la schedulazione delle
    # consegne a livello di singola riga ordine del cliente. Ciò significa che
    # a fronte di una riga d’ordine
    # del cliente il fornitore conferma, sempre a livello di riga, le quantità,
    # i prezzi, e inserisce nel DTR la
    # schedulazione delle consegne (più record DTR per le diverse date 
    # schedulate dal fornitore) con le
    # relative quantità. Quindi in caso di conferma ordine un LIN con più DTR.
    # Il totale della quantità riportata nei vari record DTR deve essere uguale
    # alla quantità riportata nel record LIN.
    'DTR': [
        ['BOTSID', 'M', (3, 3), 'AN'], # DTR

        ['DATRCONS', 'M', (8, 8), 'AN'], # CCYYMMDD
        ['ORARCONS', 'C', (4, 4), 'AN'], # HHMM
        ['TIPODATRC', 'M', (3, 3), 'AN'],
        # 002 = date / time request
        # 064 = not before date / time
        # 069 = delivery mandatory

        ['DATRCON2', 'C', (8, 8), 'AN'], # CCYYMMDD
        ['ORARCON2', 'C', (4, 4), 'AN'], # HHMM
        ['TIPODATR2', 'C', (3, 3), 'AN'],
        # 063 = not after date / time (present if TIPODATAC = 064)
        
        ['QTACONS', 'C', (15, 15), 'AN'], # 12 + 3, 12.3        
        ]

    # -------------------------------------------------------------------------
    #                  ALD Discount or charge information
    # -------------------------------------------------------------------------
    'ALD': [
        ['BOTSID', 'M', (3, 3), 'AN'], # ALD
        ['INDSCADD', 'M', (3, 3), 'AN'],
        # A = Discount
        # C = Charge
        # N = Special condition
        ['DESCR', 'C', (35, 35), 'AN'],
        ['INDSEQ', 'C', (3, 3), 'AN'], # Sequence
        ['TIPOSCADD', 'C', (6, 6), 'AN'],
        # DI = Iconditioned discount
        # PC = Package        
        # FI = Financial charge
        # IS = Refund invoice service
        # FC = Transport cost
        # VAB = Load discoint
        # SER = Service
        # TD = Commercial discount
        # PAD = Promotional discount
        # RAD = Bail
        # VEJ = Environment protection
        # X14 = Promotional activity
        # 64E = Annual prize
        # EAB = (ex. X01) ) Discount payment
        # X13 = Amount on discount
        # RAA = Prize
        # AEO = Eco contribute SIAE (WEE)
        # SIAE = SIAE
        # SPEVTR = Sperimental station glass
        ['IMPORTO', 'C', (16, 16), 'AN'], # 12 + 3, 12.3
        ['PERC', 'C', (7, 7), 'AN'], # 4 + 3, 4.3
        ['FLGPRZUN', 'M', (3, 3), 'AN'],
        # Blank if discount in line
        # X31 if amount is a unit discount 
        # No 901
        ]
        
    # -------------------------------------------------------------------------
    #                    FTL Note for document line
    # -------------------------------------------------------------------------
    # Poiché nel subset Indicod basato sulla directory 90.1 non esiste segmento
    # FTX a livello di riga dettaglio, non esiste corrispondenza tra il record 
    # user FTL e un record di flat/standard.
    # E’ previsto per uso futuro nella directory 96A.
    # Tale record non viene convertito verso partner che usino il subset
    # Indicod basato sulla directory 90.1 e perciò ne e’ sconsigliato l’uso.
    'FTL': [
        ['BOTSID', 'M', (3, 3), 'AN'], # FTL
        
        ['NOTE', 'M', (140, 140), 'AN'],
        
        
        
        
        
        
        

        
        
        
        
        
        
        
        
        
        
        
        
         
        
        




    # 16.3, 'N' >> 
    # quantity is ALWAYS 16 positions; it is written with 3 decimals and 
    # included the decimal sign;
    }
