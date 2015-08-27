# -*- coding: utf-8 -*-
import datetime
version = '3.2.0'
plugins = [
    # -------------------------------------------------------------------------
    #                                  ORDER
    # -------------------------------------------------------------------------
    {
        'plugintype': u'channel',
        'apop': False,
        'archivepath': u'',
        'askmdn': u'no',
        'certfile': None,
        'charset': u'utf-8',
        'desc': None,
        'filename': u'ORDINI-*.txt',
        'ftpaccount': u'',
        'ftpactive': False,
        'ftpbinary': False,
        'host': u'',
        'idchannel': u'euritmo_order_in',
        'inorout': u'in',
        'keyfile': None,
        'lockname': u'',
        'mdnchannel': u'',
        'parameters': u'',
        'path': u'botssys/infile/euritmo_order_in',
        'port': 0,
        'remove': False,
        'rsrv1': None,
        'rsrv2': None,
        'rsrv3': None,
        'secret': u'',
        'sendmdn': u'no',
        'starttls': False,
        'syslock': False,
        'testpath': u'',
        'type': u'file',
        'username': u'',
    },
    {
        'plugintype': u'channel',
        'apop': False,
        'archivepath': u'',
        'askmdn': u'no',
        'certfile': None,
        'charset': u'utf-8',
        'desc': None,
        'filename': u'order_*.csv',
        'ftpaccount': u'',
        'ftpactive': False,
        'ftpbinary': False,
        'host': u'',
        'idchannel': u'euritmo_order_out',
        'inorout': u'out',
        'keyfile': None,
        'lockname': u'',
        'mdnchannel': u'',
        'parameters': u'',
        'path': u'botssys/infile/outfile/euritmo_order_out',
        'port': 0,
        'remove': False,
        'rsrv1': None,
        'rsrv2': None,
        'rsrv3': None,
        'secret': u'',
        'sendmdn': u'no',
        'starttls': False,
        'syslock': False,
        'testpath': u'',
        'type': u'file',
        'username': u'',
    },
    {
        'plugintype': u'translate',
        'active': True,
        'alt': u'',
        'desc': None,
        'fromeditype': u'fixed',
        'frommessagetype': u'euritmo_ORDERS',
        'frompartner': None,
        'rsrv1': None,
        'rsrv2': None,
        'toeditype': u'fixed',
        'tomessagetype': u'csv_ORDERS',
        'topartner': None,
        'tscript': u'translate_order_euritmo_csv',
    },
    {
        'plugintype': u'routes',
        'active': True,
        'alt': u'',
        'defer': False,
        'desc': None,
        'fromchannel': u'euritmo_order_in',
        'fromeditype': u'fixed',
        'frommessagetype': u'euritmo_ORDERS',
        'frompartner': None,
        'frompartner_tochannel': None,
        'idroute': u'euritmo_order_route',
        'notindefaultrun': False,
        'rsrv1': None,
        'rsrv2': None,
        'seq': 9999,
        'testindicator': u'',
        'tochannel': u'euritmo_order_out',
        'toeditype': u'',
        'tomessagetype': u'',
        'topartner': None,
        'topartner_tochannel': None,
        'translateind': 1,
        'zip_incoming': None,
        'zip_outgoing': None,
    },

    # -------------------------------------------------------------------------
    #                               INVOICE
    # -------------------------------------------------------------------------
    {
        'plugintype': u'channel',
        'apop': False,
        'archivepath': u'',
        'askmdn': u'no',
        'certfile': None,
        'charset': u'utf-8',
        'desc': None,
        'filename': u'invoice*.csv',
        'ftpaccount': u'',
        'ftpactive': False,
        'ftpbinary': False,
        'host': u'',
        'idchannel': u'euritmo_invoic_in',
        'inorout': u'in',
        'keyfile': None,
        'lockname': u'',
        'mdnchannel': u'',
        'parameters': u'',
        'path': u'botssys/infile/euritmo_invoice_in',
        'port': 0,
        'remove': False,
        'rsrv1': None,
        'rsrv2': None,
        'rsrv3': None,
        'secret': u'',
        'sendmdn': u'no',
        'starttls': False,
        'syslock': False,
        'testpath': u'',
        'type': u'file',
        'username': u'',
    },
    {
        'plugintype': u'channel',
        'apop': False,
        'archivepath': u'',
        'askmdn': u'no',
        'certfile': None,
        'charset': u'utf-8',
        'desc': None,
        'filename': u'invoice_*.txt',
        'ftpaccount': u'',
        'ftpactive': False,
        'ftpbinary': False,
        'host': u'',
        'idchannel': u'euritmo_invoic_out',
        'inorout': u'out',
        'keyfile': None,
        'lockname': u'',
        'mdnchannel': u'',
        'parameters': u'',
        'path': u'botssys/infile/outfile/euritmo_invoice_out',
        'port': 0,
        'remove': False,
        'rsrv1': None,
        'rsrv2': None,
        'rsrv3': None,
        'secret': u'',
        'sendmdn': u'no',
        'starttls': False,
        'syslock': False,
        'testpath': u'',
        'type': u'file',
        'username': u'',
    },
    {
        'plugintype': u'translate',
        'active': True,
        'alt': u'',
        'desc': None,
        'fromeditype': u'fixed',
        'frommessagetype': u'euritmo_INVOIC',
        'frompartner': None,
        'rsrv1': None,
        'rsrv2': None,
        'toeditype': u'fixed',
        'tomessagetype': u'csv_INVOIC',
        'topartner': None,
        'tscript': u'translate_invoic_euritmo_csv',
    },
    {
        'plugintype': u'routes',
        'active': True,
        'alt': u'',
        'defer': False,
        'desc': None,
        'fromchannel': u'euritmo_invoic_in',
        'fromeditype': u'fixed',
        'frommessagetype': u'euritmo_INVOIC',
        'frompartner': None,
        'frompartner_tochannel': None,
        'idroute': u'euritmo_invoic_route',
        'notindefaultrun': False,
        'rsrv1': None,
        'rsrv2': None,
        'seq': 9999,
        'testindicator': u'',
        'tochannel': u'euritmo_invoic_out',
        'toeditype': u'',
        'tomessagetype': u'',
        'topartner': None,
        'topartner_tochannel': None,
        'translateind': 1,
        'zip_incoming': None,
        'zip_outgoing': None,
    },
    ]
