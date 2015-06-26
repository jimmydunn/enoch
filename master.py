import numpy as np
import pandas as pd
import enoch

pd.set_option('display.mpl_style', 'default') # Make the graphs a bit prettier
pd.set_option('display.max_columns', 30)

print '''
Welcome to the grand tablet of Enoch program. What are you interested in accomplishing?
'''
print '''
0 - Hidden Names of God
1 - Great Kings of the Four Watchtowers
2 - Elders of the Four Watchtowers
3 - Calvary Angels
4 - Kerubic Angels
'''

godless = int(raw_input('> '))

print '''
Which Watchtower do you wish to open?'''

print '''
0 - Air
1 - Water
2 - Earth
3 - Fire
'''

names = ['Air', 'Water', 'Earth', 'Fire']
watchtower = int(raw_input('> '))
tablet = enoch.get_tablet(watchtower)
name = names[watchtower]

if godless == 0:
    enoch.god_name(tablet, name)
elif godless == 1:
    enoch.king_name(tablet, name)
elif godless == 2:
    enoch.six_elders(tablet, name)
elif godless == 3:
    enoch.sephirotic_cross(tablet, name)
elif godless == 4:
    enoch.kerubic_square(tablet, name)
else:
    pass
    
