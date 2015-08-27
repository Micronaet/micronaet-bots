# Mapping Script
import bots.transform as transform

# Load record def elements (use csv for destination)
from bots.usersys.grammars.fixed.csv_ORDERS import recorddefs 

def main(inn, out):
    """
    inn: the object for the incoming message; 
    via get() and getloop() the content of the message can be accessed.
    
    inn.ta_info contains a python dict with information about in message
    
    out: the object for the outgoing message; 
    via put() and putloop() content is written for this message.
    
    out.ta_info contains a python dict with information about out message
    """
    
    # -------------------------------------------------------------------------
    #                                BGM
    # -------------------------------------------------------------------------
    # Import BGM fields:
    block = 'BGM'
    fields = [field[0] for field in recorddefs[block]]
    for field in fields:
        out.put({'BOTSID': block, field: 
            inn.get({'BOTSID': block, field: None})})

    # -------------------------------------------------------------------------
    #                            1-N elements
    # -------------------------------------------------------------------------
    # TODO Create dict with particular fields for block 
    # ex. Date fields that need a particular format, quantity elements etc.
    loop_block = (
        'NAS', 'NAB', 'NAD', 'NAI', 'NAC', 'NAM', 'DTM', 'CNT', 'LIN')
    for block in loop_block:
        fields = [field[0] for field in recorddefs[block]]

        for item in inn.getloop({'BOTSID': 'BGM'}, {'BOTSID': block}):
            item_out = out.putloop({'BOTSID':'BGM'}, {'BOTSID': block})
            for field in fields:
                item_out.put({'BOTSID': block, field:
                    item.get({'BOTSID': block, field: None})})

    #transform.inn2out(inn, out)
    '''
    out.put(
        {'BOTSID': 'HEA', 'RECEIVER': inn.ta_info['topartner']})
    out.put(
        {'BOTSID': 'HEA', 'MESSAGETYPE': inn.ta_info['messagetype']})

    ORDERNUMBER = inn.get(
        {'BOTSID': 'UNH'}, {'BOTSID': 'BGM', '1004': None}) # get ordernumber from the edifact message
    out.put(
        {'BOTSID': 'HEA', 'ORDERNUMBER': ORDERNUMBER}) # and put it in the outgoing fixed message
    out.ta_info['botskey'] = ORDERNUMBER #to have the ordernumber in the document screen
    
    out.put(
        {'BOTSID': 'HEA', 'ORDERTYPE': inn.get(
            {'BOTSID': 'UNH'},
            {'BOTSID': 'BGM', 'C002.1001': None})}) # combine get and put in one line!!
    out.put(
        {'BOTSID':'HEA', 'ORDERDATE': inn.get(
            {'BOTSID': 'UNH'},
            {'BOTSID': 'DTM', 'C507.2005': '137', 'C507.2380': None})})     #get statement ONLY looks for DTM with qualifier 137

    for lin in inn.getloop({'BOTSID': 'UNH'}, {'BOTSID': 'LIN'}): # for each LIN (nested under UNH):
        lou = out.putloop({'BOTSID': 'HEA'}, {'BOTSID': 'LIN'}) # write a fixed LIN-record
        #note that in this loop get() is used on the lin-object, and put() is used for the lou-object
        lou.put({'BOTSID': 'LIN', 'LINENUMBER': lin.get(
            {'BOTSID': 'LIN', '1082': None})})
        lou.put({'BOTSID': 'LIN', 'ARTICLE_GTIN': lin.get(
            {'BOTSID':'LIN','C212.7140':None})})
        lou.put({'BOTSID': 'LIN', 'DESCRIPTION': lin.get(
            {'BOTSID': 'LIN'}, 
            {'BOTSID': 'IMD', 'C273.7008#1': None})})
        lou.put({'BOTSID': 'LIN', 'QUANTITY': lin.get(
            {'BOTSID':'LIN'}, 
            {'BOTSID': 'QTY', 'C186.6063': '21', 'C186.6060': None})})
    '''
