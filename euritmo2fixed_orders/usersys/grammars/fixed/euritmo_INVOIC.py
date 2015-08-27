# -*- coding: utf-8 -*-
from bots.botsconfig import *

# Syntax: Parameters for translation.
syntax = {
    'charset': 'utf-8',
    }

structure = [
    {ID: 'BGM', MIN: 1, MAX: 1, LEVEL: [
        {ID: 'RFC', MIN: 0, MAX: 99999},
        
        {ID: 'NAS', MIN: 1, MAX: 1},
        {ID: 'NAI', MIN: 1, MAX: 1},
        {ID: 'NAP', MIN: 0, MAX: 1},
        {ID: 'NAA', MIN: 0, MAX: 1},
        {ID: 'NAT', MIN: 0, MAX: 1},
       
        {ID: 'FTX', MIN: 0, MAX: 5},
        {ID: 'PAT', MIN: 0, MAX: 10},
        {ID: 'TOD', MIN: 0, MAX: 5, LEVEL: [
            {ID: 'LOC', MIN: 0, MAX: 2},
            ]},
        {ID: 'DET', MIN: 1, MAX: 1, LEVEL: [
            {ID: 'DES', MIN: 0, MAX: 10},
            {ID: 'RFN', MIN: 0, MAX: 10},
            {ID: 'TAX', MIN: 0, MAX: 15},
            {ID: 'ALD', MIN: 0, MAX: 15},
            {ID: 'NAD', MIN: 1, MAX: 1},
            {ID: 'NAE', MIN: 0, MAX: 1},
            {ID: 'NAR', MIN: 0, MAX: 1},
            {ID: 'NAM', MIN: 0, MAX: 1},
            {ID: 'NAF', MIN: 0, MAX: 1},
            {ID: 'NAX', MIN: 0, MAX: 1},
            {ID: 'FLT', MIN: 0, MAX: 5},
            ]},
        {ID: 'FTT', MIN: 0, MAX: 5},
        {ID: 'ALT', MIN: 0, MAX: 15},
        {ID: 'IVA', MIN: 0, MAX: 10},
        {ID: 'TMA', MIN: 1, MAX: 1},
        ]},
    ]

# TODO Date is AN not N
recorddefs = {
    # -------------------------------------------------------------------------
    #                    BGM Mandatory information (document)
    # -------------------------------------------------------------------------
    'BGM': [ # header record
        ['BOTSID', 'M', (3, 3), 'AN'], # BGM (BOTSID)

        # ID-EDI-MITT: # TODO Create a structured field?
        ['ID-EDI-MITT-1', 'M', (35, 35), 'AN'], # ID sender VAT o EAN/UCC
        ['ID-EDI-MITT-2', 'C', (4, 4), 'AN'],
        ['ID-EDI-MITT-3', 'C', (14, 14), 'AN'],

        # ID-EDI-DEST:
        ['ID-EDI-DEST-1', 'M', (35, 35), 'AN'], # ID sender VAT o EAN/UCC
        ['ID-EDI-DEST-2', 'C', (4, 4), 'AN'],
        ['ID-EDI-DEST-3', 'C', (14, 14), 'AN'],

        ['TIPODOC', 'M', (6, 6), 'AN'], # ORDERS (normal order) ORDERSP ORDCHG
        ['NUMDOC', 'M', (35, 35), 'AN'],
        ['DATADOC', 'M', (8, 8), 'AN'], # CCYYMMDD
        ['ORADOC', 'C', (4, 4), 'AN'], # HHMM

        ['Filler', 'C', (6, 6), 'AN'], # Not used
        ],

    # -------------------------------------------------------------------------
    #                      RFC Reference contract information
    # -------------------------------------------------------------------------
    'RFC': [
        ['BOTSID', 'M', (3, 3), 'AN'], # FRC
        ['NUMCO', 'M', (35, 35), 'AN'], # Contract number
        ['DATAINCO', 'C', (8, 8), 'AN'], # CCYYMMDD (start contract)
        ['DATAFICO', 'C', (8, 8), 'AN'], # CCYYMMDD (end contract)
        ],

    # -------------------------------------------------------------------------
    #                      NAS (Supplier information) NAD 3055 = SU
    # -------------------------------------------------------------------------
    'NAS': [ # (NAD/3035 = SU)
        ['BOTSID', 'M', (3, 3), 'AN'], # NAS
        ['CODFORN', 'M', (17, 17), 'AN'], # Supplier ID

        ['QCODFORN', 'M', (3, 3), 'AN'],
        # 14 = Cod. EAN / UCC
        # VA = P. IVA
        # 91 = assigned from supplier code
        # 92 = assigned from customer code

        ['RAGSOCF', 'C', (70, 70), 'AN'], # Supplier
        ['INDIRF', 'C', (70, 70), 'AN'],
        ['CITTAF', 'C', (35, 35), 'AN'],
        ['PROVF', 'C', (9, 9), 'AN'],
        ['CAPF', 'C', (9, 9), 'AN'],
        ['NAZIOF', 'C', (3, 3), 'AN'], # National code

        ['PIVANAZF', 'M', (35, 35), 'AN'],
        ['TRIBUNALE', 'C', (35, 35), 'AN'],
        ['LICIMPEXP', 'C', (35, 35), 'AN'],
        ['CCIAA', 'C', (35, 35), 'AN'],
        ['CAPSOC', 'C', (35, 35), 'AN'],

        ['CODFISC', 'C', (35, 35), 'AN'],
        ['PIVAINT', 'C', (35, 35), 'AN'],

        ['TELEFONO', 'C', (25, 25), 'AN'],
        ['TELEFAX', 'C', (25, 25), 'AN'],
        ['TELEX', 'C', (25, 25), 'AN'],
        ['EMAIL', 'C', (70, 70), 'AN'],

        ['NUREGCOOPF', 'M', (35, 35), 'AN'],
        ['NUREGRAEE', 'C', (16, 16), 'AN'],
        ['NUREGPILE', 'C', (16, 16), 'AN'],
        ],

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

        ['RAGSOCI', 'M', (70, 70), 'AN'],
        ['INDIRI', 'M', (70, 70), 'AN'],
        ['CITTAI', 'M', (35, 35), 'AN'],
        ['PROVI', 'M', (9, 9), 'AN'],
        ['CAPI', 'M', (9, 9), 'AN'],
        ['NAZIOI', 'C', (3, 3), 'AN'], # National code

        ['PIVANAZI', 'M', (35, 35), 'AN'],
        ['NUREGCOOP', 'M', (35, 35), 'AN'], # REA
        ['CODFISCA', 'M', (35, 35), 'AN'],
        ],

    # -------------------------------------------------------------------------
    #              NAP Payers information if different from address
    # -------------------------------------------------------------------------
    'NAP': [
        ['BOTSID', 'M', (3, 3), 'AN'], # NAI

        ['CODFORP', 'M', (17, 17), 'AN'], # Ean / UCC, location, VAT
        ['QCODFORP', 'M', (3, 3), 'AN'],
        # 14 = EAN / UCC
        # VA = VAT
        # 91 = code assigned by supplier
        # 92 = code assigned by customer

        ['RAGSOCP', 'C', (70, 70), 'AN'],
        ['INDIRP', 'C', (70, 70), 'AN'],
        ['CITTAP', 'C', (35, 35), 'AN'],
        ['PROVP', 'C', (9, 9), 'AN'],
        ['CAPP', 'C', (9, 9), 'AN'],
        ['NAZIOP', 'C', (3, 3), 'AN'], # National code
        ['PIVANAZP', 'C', (35, 35), 'AN'],

        ['FILLER', 'C', (51, 51), 'AN'],
        ]

    # -------------------------------------------------------------------------
    #                 NAA Who create invoice if different
    # -------------------------------------------------------------------------
    'NAA': [
        ['BOTSID', 'M', (3, 3), 'AN'], # NAI

        ['CODFATA', 'M', (17, 17), 'AN'], # Ean / UCC, location, VAT
        ['QCODFATA', 'M', (3, 3), 'AN'],
        # 14 = EAN / UCC
        # VA = VAT
        # 91 = code assigned by supplier
        # 92 = code assigned by customer

        ['RAGSOCA', 'C', (70, 70), 'AN'],
        ['INDIRA', 'C', (70, 70), 'AN'],
        ['CITTAA', 'C', (35, 35), 'AN'],
        ['PROVA', 'C', (9, 9), 'AN'],
        ['CAPA', 'C', (9, 9), 'AN'],
        ['NAZIOA', 'C', (3, 3), 'AN'], # National code
        ['PIVANAZA', 'C', (35, 35), 'AN'],

        ['FILLER', 'C', (51, 51), 'AN'],
        ]

    # -------------------------------------------------------------------------
    #              NAT Part that receive sheet invoice
    # -------------------------------------------------------------------------
    'NAT': [
        ['BOTSID', 'M', (3, 3), 'AN'], # NAI

        ['CODFATO', 'M', (17, 17), 'AN'], # Ean / UCC, location, VAT
        ['QCODFATO', 'M', (3, 3), 'AN'],
        # 14 = EAN / UCC
        # VA = VAT
        # 91 = code assigned by supplier
        # 92 = code assigned by customer

        ['RAGSOCO', 'C', (70, 70), 'AN'],
        ['INDIRO', 'C', (70, 70), 'AN'],
        ['CITTAO', 'C', (35, 35), 'AN'],
        ['PROVO', 'C', (9, 9), 'AN'],
        ['CAPO', 'C', (9, 9), 'AN'],
        ['NAZIOO', 'C', (3, 3), 'AN'], # National code
        ['PIVANAZO', 'C', (35, 35), 'AN'],

        ['FILLER', 'C', (51, 51), 'AN'],
        ]

    # -------------------------------------------------------------------------
    #                 FTX Extra information and notes (header)
    # -------------------------------------------------------------------------
    # Nota:
    # Per le transazioni EDI che rientrano nell'ambito di applicazione
    # dell'art. 62 del decreto legge 24 gennaio 2012 (convertito dalla legge
    # 24 marzo 2012, n° 27) e' possibile inserire nel campo NOTE la
    # dicitura “Assolve gli obblighi di cui all'articolo 62, comma 1, del
    # decreto legge 24 gennaio 2012, n. 1, convertito, con modificazioni,
    # dalla legge 24 marzo 2012, n. 27."
    'FTX': [
        ['BOTSID', 'M', (3, 3), 'AN'], # FTX
        ['DIVISA', 'C', (3, 3), 'AN'], # ITL = Lira, EUR = Euro
        ['NOTE', 'C', (350, 350), 'AN'], # Extra info for payment
        ],

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

        ['BANCACOD', 'C', (35, 35), 'AN'],
        # Format: ABI(5) - CAB(5) - C/C(23)
        ['BANCADESC', 'C', (35, 35), 'AN'], # Bank name
        ['FACTOR', 'C', (35, 35), 'AN'],

        ['CODPAG', 'C', (3, 3), 'AN'],
        # Payment code:
        # 1 = Direct paymenyt
        # 35 = Bank document payment

        ['MEZZOPAG', 'C', (3, 3), 'AN'],
        # 10 = Cash
        # 20 = Cheque
        # 23 = Circular cheque
        # 30 = Bank transfer
        # 31 = Bank transfer
        # 42 = Payment via CC bank
        # 70 = Trat
        # 15E = RID
        # 74 = Bank ric.
        # 97 = Fin. Compensation
        ],

    # -------------------------------------------------------------------------
    #              TOD Delivery condition, transport
    # -------------------------------------------------------------------------
    'TOD': [
        ['BOTSID', 'M', (3, 3), 'AN'],

        ['CODCONS', 'M', (3, 3), 'AN'],
        # 2 = Delivery condition
        # 3 = Cost anc delivery condition

        ['CODCOST', 'M', (3, 3), 'AN'],
        # Transport costs to:
        # PP = sender
        # CC = receiver

        ['CODCOND', 'C', (3, 3), 'AN'], # INCOTERMS
        ['DESCOND1', 'M', (70, 70), 'AN'],
        ['DESCOND2', 'M', (70, 70), 'AN'],
        ],

    # -------------------------------------------------------------------------
    #                LOC Delivery point information (article level)
    # -------------------------------------------------------------------------
    'LOC': [
        ['BOTSID', 'M', (3, 3), 'AN'], # LOC
        ['CODCONS', 'M', (17, 17), 'AN'], # EAN / UCC VAT
        ['QCODCONS', 'M', (3, 3), 'AN'],
        # 14 = EAN / UCC
        # VA = VAT
        # 91 = Vendor assigned code
        # 92 = Customer assigned code
        # ZZ = Common defined code

        # Delivery point:
        ['RAGSOCD', 'C', (70, 70), 'AN'],
        ['INDIRD', 'C', (70, 70), 'AN'],
        ['CITTAD', 'C', (35, 35), 'AN'],
        ['PROVD', 'C', (9, 9), 'AN'], # Province code
        ['CAPD', 'C', (9, 9), 'AN'],
        ['NAZIOD', 'C', (3, 3), 'AN'], # Country code
        ],

    # -------------------------------------------------------------------------
    #                      DET Document line
    # -------------------------------------------------------------------------
    'DET': [
        ['BOTSID', 'M', (3, 3), 'AN'],

        ['NUMRIGA', 'C', (6, 6), 'AN'],
        ['IDSOTTOR', 'C', (3, 3), 'AN'],
        # 1 = present
        # blank = not present

        ['NUMSRIGA', 'C', (6, 6), 'AN'],
        ['CODEANCU', 'C', (35, 35), 'AN'], # EAN / UCC / TU
        ['TIPCODCU', 'C', (3, 3), 'AN'],
        ['CODEANTU', 'C', (35, 35), 'AN'], # EAN / UCC / TU
        ['CODFORTU', 'C', (35, 35), 'AN'], # EAN / UCC / TU
        ['CODDISTTU', 'C', (35, 35), 'AN'], # EAN / UCC / TU

        ['TIPQUANT', 'M', (3, 3), 'AN'],
        # L01 = Vendita
        # L02 = Reso
        # L03 = Omaggio
        # L04 = Vuoti
        # L05 = Imballi
        # L06 = Cauzioni
        # L07 = Diff. quantità
        # L08 = Diff. prezzo
        # L09 = Sconto merce
        # L10 = Accredito per contestazione
        # L11 = Add/Accr sola IVA
        # L12 = Campione gratuito
        # L13 = Materiale pubblicitario cartaceo
        # L14 = Materiale pubblicitario non cartaceo
                
        ['QTACONS', 'M', (16, 16), 'AN'], # 12 + 3, 12.3 TODO N
        ['UDMQCONS', 'C', (3, 3), 'AN'],
        # PCE = pezzi
        # KGM = chilogrammi
        # MTR = metri
        # MTK= metri quadri
        # LTR = litri
        # CMT = Centimetri
        # GRM = Grammi
        # MLT = Millilitri
        # P1 = Percentuale
        # HLT = Ettolitri
        # CT = cartone
        # CU = Consumer Unit
        # TU = Trade Unit

        ['QTAFATT', 'M', (16, 16), 'AN'],
        ['UDMQFATT', 'C', (3, 3), 'AN'],
        
        ['NRCUINTU', 'C', (16, 16), 'AN'],
        ['UDMNRCUINTU', 'C', (3, 3), 'AN'],
        
        ['PRZUNI', 'C', (16, 16), 'AN'],
        ['TIPOPRZ', 'C', (3, 3), 'AN'],
        # AAA = prezzo netto
        # AAB = prezzo lordo
        # INF = Prezzo per info.
        # Obbl. se e’ significativo PRZUNI
        ['UDMPRZUN', 'C', (3, 3), 'AN'],
        # PCE = pezzi
        # KGM = chilogrammi
        # MTR = metri
        # MTK= metri quadri
        # LTR = litri
        # CMT = Centimetri
        # GRM = Grammi
        # MLT = Millilitri
        # P1 = Percentuale
        # HLT = Ettolitri
        # CT = cartone
        # CU = Consumer Unit
        # TU = Trade Unit
        
        ['PRZUN2', 'C', (16, 16), 'AN'],
        ['TIPOPRZ2', 'C', (3, 3), 'AN'],
        # AAA = prezzo netto
        # AAB = prezzo lordo
        # INF = Prezzo per info.
        # Obbl. se e’ significativo PRZUNI
        ['UDMPRZUN2', 'C', (3, 3), 'AN'],
        # PCE = pezzi
        # KGM = chilogrammi
        # MTR = metri
        # MTK= metri quadri
        # LTR = litri
        # CMT = Centimetri
        # GRM = Grammi
        # MLT = Millilitri
        # P1 = Percentuale
        # HLT = Ettolitri
        # CT = cartone
        # CU = Consumer Unit
        # TU = Trade Unit

        ['IMPORTO', 'C', (16, 16), 'AN'],
        ['DIVRIGA', 'C', (3, 3), 'AN'],

        ['IMPORTO2', 'C', (16, 16), 'AN'],
        ['DIVRIGA2', 'C', (3, 3), 'AN'],
        ],
        
    # -------------------------------------------------------------------------
    #                      DES Line description
    # -------------------------------------------------------------------------
    'DES': [
        ['BOTSID', 'M', (3, 3), 'AN'],
        ['DESCR', 'M', (175, 175), 'AN'],
        ],

    # -------------------------------------------------------------------------
    #                      RFN Accredit note reference
    # -------------------------------------------------------------------------
    'RFN': [
        ['BOTSID', 'M', (3, 3), 'AN'],
        
        ['TIPORIF', 'C', (3, 3), 'AN'],
        # IV = Fattura
        # ZZ = Concordato fra le parti
        # CD = Nota di credito
        # DL = Nota di debito
        # ALQ = Numero bolla di reso
        
        ['RIFACCADD', 'C', (35, 35), 'AN'], # EAN / UCC / TU
        ['DATARIF', 'C', (8, 8), 'AN'],
        ],
                
    # -------------------------------------------------------------------------
    #                      TAX Tax information
    # -------------------------------------------------------------------------
    'TAX': [
        ['BOTSID', 'M', (3, 3), 'AN'],
        
        ['TIPOTASS', 'C', (3, 3), 'AN'],
        # VAT = IVA
        # I01 = Imposta oli lubrificanti
        # I02 = Imposta di fabbricazione
        # I03 = Contrassegno di stato
        
        ['DESCRIZ', 'C', (35, 35), 'AN'], # EAN / UCC / TU

        ['CATIMP', 'C', (3, 3), 'AN'],
        # Vedi elenco succ. inoltre:
        # S = Soggetto a tassazione
        # X = Esente
        # G = Non imp. Art. 8
        # E = Restanti non imp./esclusi
        # H = Aliquota massima
        # Z = esente
        
        ['ALIQIVA', 'C', (7, 7), 'AN'], # 3.4
        ['IMPORTO', 'C', (16, 16), 'AN'], # 12.3
        ],

    # -------------------------------------------------------------------------
    #                      ALD Tax information
    # -------------------------------------------------------------------------
    #Nota:
    #CONTRIBUTO RAEE (WEEE)
    #A seguito della Direttiva RAEE recepita in Italia con Dlgs 151/05 del 
    #25/07/05 che regolamenta lo smaltimento dei rifiuti elettrotecnici ed 
    #elettronici (per i prodotti elencati nelle categorie dell’allegato 1A del
    #testo di legge), è possibile riportare il costo (così come sul documento 
    #cartaceo) di tale contributo all'interno del segmento ALD valorizzando 
    #il campo TIPOSCADD = "AEO" (Eco contributo RAEE – WEEE) ed il relativo 
    #importo nel campo IMPORTO.
    
    #Nota:
    #CONTRIBUTO CONAI E CONTRIBUTO GESTIONE PFU
    #Il codice qualificatore "VEJ = protezione ambientale o servizio di 
    #smaltimento", utilizzato per indicare il contributo CONAI, può anche 
    #essere utilizzato per indicare il contributo ambientale per la gestione 
    #degli pneumatici fuori uso (PFU). Il DM n. 82 del 11/04/11 (pubblicato in
    #gazzetta ufficiale n. 131 del 08/06/11) richiede infatti ai produttori di 
    #pneumatici l’indicazione del contributo in oggetto in modo chiaro e 
    #distinto in fattura, differenziato per le diverse tipologie di pneumatici
    #(allegato E del DM n. 82 del 11/04/11).
    #Nel caso si dovesse indicare in fattura sia il contributo CONAI sia il 
    #contributo per la gestione dei PFU è possibile ripetere il segmento 
    #indicando con lo stesso qualificatore (VEJ) sia il contributo CONAI che il    
    #contributo per la gestione dei PFU. Più in particolare, per il contributo
    #per la gestione dei PFU si dovrà utilizzare il segmento ALD, nella stessa 
    #modalità con la quale viene utilizzato per la gestione del contributo
    #CONAI; quindi sarà da inserire il qualificatore AAI nel campo TIPONOTA 
    #del segmento FTL, e successivamente nel campo NOTE del segmento FTL si 
    #dovrà inserire la dichiarazione “contributo per la gestione dei PFU 
    #assolto".
    'ALD': [
        ['BOTSID', 'M', (3, 3), 'AN'],

        ['INDSCADD', 'M', (3, 3), 'AN'],
        # A = Sconto
        # C = Addebito
        # N = Cond. Speciale
        
        ['DESCR', 'C', (35, 35), 'AN'], # EAN / UCC / TU
        ['INDSEQ', 'C', (3, 3), 'AN'],

        ['TIPOSCADD', 'C', (6, 6), 'AN'],
        # DI = Sconto incondizionato
        # PC = Imballo
        # FI = Oneri finanziari
        # IS = Rimborso bolli per fattura (servizi in fattura)
        # FC = Costo trasporto
        # VAB = Sconto carico (sconto volume)
        # SER = Servizi
        # TD = Sconto commerciale
        # PAD = Sconto promozionale
        # RAD = Cauzione vuoto
        # VEJ = Protezione ambientale o servizio di smaltimento 
        # X14 = Attività promozionali preferenziali
        # 64E = Premi
        # EAB = Sconto pagamento (vecchio codice X01)
        # X13 = Ammontare imponibile soggetto a sconto
        # Inoltre il campo può non essere valorizzato, indicando abbuono o        
        # addebito generico
        # AEO = Eco contributo
        # RAEE (WEEE)
        # SIAE = Addebito SIAE
        # SPEVTR = Contributo Stazione Sperimentale Vetro

        ['IMPORTO', 'C', (16, 16), 'AN'], # +12.3
        ['PERC', 'C', (7, 7), 'AN'], # +3.4
        ['FLGPRZUN', 'C', (3, 3), 'AN'],
        #Lasciare a blank se lo sconto è applicato
        #all'importo di riga. 
        #Assegnare "X31" se l'importo è uno sconto unitario.
        #Non previsto nel subset 901        

