# Mapping Script
import bots.transform as transform

# Load record def elements (use csv for destination)
from bots.usersys.grammars.fixed.csv_INVOIC import recorddefs 

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
    parent = 'BGM'
    fields = [field[0] for field in recorddefs[parent]]
    for field in fields:
        out.put({'BOTSID': parent, field: 
            inn.get({'BOTSID': parent, field: None})})

    # -------------------------------------------------------------------------
    #                            1-N elements
    # -------------------------------------------------------------------------
    # TODO Create dict with particular fields for block 
    # ex. Date fields that need a particular format, quantity elements etc.
    loop_block = (
        #'RFC',
        'NAS', 'NAI',
        #'NAP', 'NAA', 'NAT', 
        #'FTX', 'PAT', 
        #'TOD', 
        #    'LOC'
        'DET',
        #    'DES',
        #    'RFN',
        #    'TAX',
        #    'ALD',
        #    'NAD', # TODO mandatory 
        #    'NAE',
        #    'NAR',
        #    'NAM',
        #    'NAF',
        #    'NAX',
        #    'FLT',
        #'FTT',
        #'ALT',
        #'IVA',
        'TMA',        
        ) 
    for block in loop_block:
        fields = [field[0] for field in recorddefs[block]]

        for item in inn.getloop({'BOTSID': parent}, {'BOTSID': block}):
            item_out = out.putloop({'BOTSID': parent}, {'BOTSID': block})
            for field in fields:
                item_out.put({'BOTSID': block, field:
                    item.get({'BOTSID': block, field: None})})

