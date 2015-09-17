# -*- coding: utf-8 -*-
###############################################################################
#
#    Copyright (C) 2001-2014 Micronaet SRL (<http://www.micronaet.it>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published
#    by the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

import os
import ConfigParser
from os import listdir
from os.path import isfile, join

# Parameters:
cfg_file = "openerp.cfg" # same directory
config = ConfigParser.ConfigParser()
config.read(cfg_file)

# Path for orders:
path_in = os.path.expanduser(config.get('EDI', 'path_in'))
path_history = os.path.expanduser(config.get('EDI', 'path_history'))
path_out = os.path.expanduser(config.get('EDI', 'path_out'))
path_bot = os.path.expanduser(config.get('EDI', 'path_bot'))

# Path for log:
#schedule_log = os.path.expanduser(config.get('LOG', 'schedule_log'))
#import_log = os.path.expanduser(config.get('LOG', 'import_log'))

run_command = 'python %s --new' % join(
    path_bot, 'bots-engine.py')
    
# Function:
def clean(line, replace='?'):
    ''' Remove all non ascii char over 127 bit
    '''
    res = ''
    for c in line:
        try:
            if ord(c) < 127:
                res += c
            else:
                res += replace
        except:
            res += replace
    return res 
    
# Code:
print "[INFO] Start conversion" 
file_list = [f for f in listdir(path_in) if isfile(join(path_in, f))]
print "[INFO] File found:\n %s" % (file_list, )
for filename in file_list:  
    file_in = join(path_in, filename)
    file_out = join(path_out, filename)
    file_history = join(path_history, filename)
    
    print "[INFO] Start clean file: %s" % file_in
    f_in = open(file_in, 'rb')
    f_out = open(file_out, 'w')
    
    # Clean all lines in input file:
    for line in f_in:
        f_out.write(clean(line))
    
    f_in.close()    
    f_out.close()

    print "[INFO] End clean: %s" % file_in
    
    # Move file in history folder:    
    os.rename(file_in, file_history) 
    print "[INFO] History: %s " % file_history

# Force load in bots:
print "[INFO] Run schedule operation" 
os.system(run_command)
print "[INFO] End conversion" 

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
