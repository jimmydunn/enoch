import numpy as np
import pandas as pd

pd.set_option('display.mpl_style', 'default') # Make the graphs a bit prettier
pd.set_option('display.max_columns', 30)

grand_tablet = pd.read_csv('grandtablet.csv', encoding='latin1')
air = grand_tablet.iloc[:13,0:12]
water = grand_tablet.iloc[:13,13:25]
earth = grand_tablet.iloc[14:,0:12]
fire = grand_tablet.iloc[14:,13:25]
blackcross = grand_tablet.iloc[0:, 12]

tablets = [air, water, earth, fire]

def get_tablet(mark):
    return tablets[mark]

def god_name(dataframe, tablet):
    god_row = len(dataframe.index) / 2
    first_name = ''
    second_name = ''
    third_name = ''
    i = 0
    while i < 3:
        first_name = first_name + dataframe.iloc[god_row,i]
        i += 1
    while i < 7:
        second_name = second_name + dataframe.iloc[god_row,i]
        i += 1
    while i < 12:
        third_name = third_name + dataframe.iloc[god_row,i]
        i += 1
    
    print 'The God name for the tablet of %s is %s %s %s.' % (tablet, first_name, second_name, third_name)

def king_name(dataframe, tablet):
    start_row = len(dataframe.index) / 2
    start_col = (len(dataframe.columns) / 2) - 2
    king_name = dataframe.iloc[start_row, start_col]
    king_name = king_name + dataframe.iloc[start_row - 1, start_col + 1]
    king_name = king_name + dataframe.iloc[start_row - 1, start_col + 2]
    king_name = king_name + dataframe.iloc[start_row, start_col + 3]
    king_name = king_name + dataframe.iloc[start_row + 1, start_col + 2]
    king_name = king_name + dataframe.iloc[start_row + 1, start_col + 1]
    king_name = king_name + dataframe.iloc[start_row, start_col + 1]
    king_name = king_name + dataframe.iloc[start_row, start_col + 2]
    print 'The Great King of the Watchtower of %s is %s' % (tablet, king_name)

def six_elders(dataframe, tablet):
    elder_mars = ''
    elder_moon = ''
    elder_jupiter = ''
    elder_mercury = ''
    elder_venus = ''
    elder_saturn = ''
    elder_row = len(dataframe.index) / 2
    elder_column = len(dataframe.columns) / 2
    
    while len(elder_mars) < 7:
        elder_mars = elder_mars + dataframe.iloc[elder_row, elder_column - len(elder_mars)]
    
    while len(elder_moon) < 7:
        elder_moon = elder_moon + dataframe.iloc[elder_row - len(elder_moon), elder_column]
    
    while len(elder_jupiter) < 7:
        elder_jupiter = elder_jupiter + dataframe.iloc[elder_row - len(elder_jupiter), elder_column - 1]
    
    while len(elder_mercury) < 7:
        elder_mercury = elder_mercury + dataframe.iloc[elder_row + len(elder_mercury), elder_column - 1]
    
    while len(elder_venus) < 7:
        elder_venus = elder_venus + dataframe.iloc[elder_row, (elder_column - 1) + len(elder_venus)]
    
    while len(elder_saturn) < 7:
        elder_saturn = elder_saturn + dataframe.iloc[elder_row + len(elder_saturn), elder_column]
    
    print 'The name of the Elder of %s in the House of Mars is %s' % (tablet, elder_mars)
    print 'The name of the Elder of %s in the House of the Moon is %s' % (tablet, elder_moon)
    print 'The name of the Elder of %s in the House of Jupiter is %s' % (tablet, elder_jupiter)
    print 'The name of the Elder of %s in the House of Mercury is %s' % (tablet, elder_mercury)
    print 'The name of the Elder of %s in the House of Venus is %s' % (tablet, elder_venus)
    print 'The name of the Elder of %s in the House of Saturn is %s' % (tablet, elder_saturn)

def sephirotic_cross(dataframe, tablet):
    air_summon = ''
    air_control = ''
    water_summon = ''
    water_control = ''
    earth_summon = ''
    earth_control = ''
    fire_summon = ''
    fire_control = ''
    
    while len(air_summon) < 6:
        air_summon = air_summon + dataframe.iloc[0 + len(air_summon), 2]
    
    while len(air_control) < 5:
        air_control = air_control + dataframe.iloc[1, 0 + len(air_control)]
    
    while len(water_summon) < 6:
        water_summon = water_summon + dataframe.iloc[0 + len(water_summon), 9]
    
    while len(water_control) < 5:
        water_control = water_control + dataframe.iloc[1, 7 + len(water_control)]
    
    while len(earth_summon) < 6:
        earth_summon = earth_summon + dataframe.iloc[7 + len(earth_summon), 2]
    
    while len(earth_control) < 5:
        earth_control = earth_control + dataframe.iloc[8, 0 + len(earth_control)]
    
    while len(fire_summon) < 6:
        fire_summon = fire_summon + dataframe.iloc[7 + len(fire_summon), 9]
    
    while len(fire_control) < 5:
        fire_control = fire_control + dataframe.iloc[8, 7 + len(fire_control)]
    
    print '''
    To summon the Angel of Air in the Watchtower of %s, invoke the name %s. 
    Control the angel by invoking the name %s'
    ''' % (tablet, air_summon, air_control)
    
    print '''
    To summon the Angel of Water in the Watchtower of %s, invoke the name %s. 
    Control the angel by invoking the name %s'
    ''' % (tablet, water_summon, water_control)
    
    print '''
    To summon the Angel of Earth in the Watchtower of %s, invoke the name %s. 
    Control the angel by invoking the name %s'
    ''' % (tablet, earth_summon, earth_control)
    
    print '''
    To summon the Angel of Fire in the Watchtower of %s, invoke the name %s. 
    Control the angel by invoking the name %s'
    ''' % (tablet, fire_summon, fire_control)

def kerubic_square(dataframe, tablet):
    air = ''
    water = ''
    earth = ''
    fire = ''
    
    i = 0
    while len(air) < 4:
        if i != 2:
            air = air + dataframe.iloc[0, 0 + i]
            i += 1
        else:
            i += 1
    
    i = 0
    while len(water) < 4:
        if i != 2:
            water = water + dataframe.iloc[0, 7 + i]
            i += 1
        else:
            i += 1
    
    i = 0
    while len(earth) < 4:
        if i != 2:
            earth = earth + dataframe.iloc[7, 0 + i]
            i += 1
        else:
            i += 1
    
    i = 0
    while len(fire) < 4:
        if i != 2:
            fire = fire + dataframe.iloc[7, 7 + i]
            i += 1
        else:
            i += 1
    if tablet == "Air" or tablet == 'Water':
        arch_air = blackcross.iloc[0] + air
        arch_water = blackcross.iloc[0] + water
        arch_earth = blackcross.iloc[7] + earth
        arch_fire = blackcross.iloc[7] + fire
    else:
        arch_air = blackcross.iloc[14] + air
        arch_water = blackcross.iloc[14] + water
        arch_earth = blackcross.iloc[21] + earth
        arch_fire = blackcross.iloc[21] + fire
    
    print 'Ruled by %s, the Kerubic Angel of Air in the Watchtower of %s is %s' % (arch_air, tablet, air)
    print 'Ruled by %s, the Kerubic Angel of Water in the Watchtower of %s is %s' % (arch_water, tablet, water)
    print 'Ruled by %s, the Kerubic Angel of Earth in the Watchtower of %s is %s' % (arch_earth, tablet, earth)
    print 'Ruled by %s, the Kerubic Angel of Fire in the Watchtower of %s is %s' % (arch_fire, tablet, fire)
    
grand_tablet[:]
