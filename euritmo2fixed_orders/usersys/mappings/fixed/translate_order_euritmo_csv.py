# Mapping Script
import bots.transform as transform

# Load record def elements (use csv for destination)
from bots.usersys.grammars.fixed.csv_ORDERS import (
    recorddefs,    # fields definition
    FILLER_FIELD,  # Filler field name
    format_string, # Convert string function
    )

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
    #                         Export data for external
    # -------------------------------------------------------------------------    
    out.ta_info['botskey'] = "%s_%s_%s" % (
        inn.get({'BOTSID': 'BGM', 'DATADOC': None}),
        inn.get({'BOTSID': 'BGM', 'NUMDOC': None}),
        inn.get({'BOTSID': 'BGM'}, {'BOTSID': 'DTM', 'DATACONS': None}),
        )

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
    # TODO ex. field that need a particular format (quantity elements etc.)
    loop_block = (
        # 'RFF', 'RFC',
        #'NAS', # > 'CTA' (not needed in accounting as in mandatory)
        'NAB', 'NAD', 
        #'NAI', 'NAC', 'NAM', 
        'DTM', 
        #'CNT', 
        'LIN',
        )

    for block in loop_block:
        fields = [field[0] for field in recorddefs[block]]

        for item in inn.getloop({'BOTSID': 'BGM'}, {'BOTSID': block}):
            item_out = out.putloop({'BOTSID':'BGM'}, {'BOTSID': block})
            for field in fields:
                value = format_string(
                    item.get({'BOTSID': block, field: None} or ''))
                item_out.put({'BOTSID': block, field: value})
            else:
                # Always add filler fields with spage in every element
                item_out.put({'BOTSID': block, FILLER_FIELD: ' '})
