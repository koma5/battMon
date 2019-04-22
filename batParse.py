import sys, re, os

data = {}

print "date, NAME, STATUS, PRESENT, TECHNOLOGY, CYCLE_COUNT, VOLTAGE_MIN_DESIGN, VOLTAGE_NOW, CURRENT_NOW, CHARGE_FULL, CHARGE_FULL_DESIGN, CHARGE_NOW, CAPACITY, CAPACITY_LEVEL, MODEL_NAME, MANUFACTURER, SERIAL_NUMBER"

with open(sys.argv[1]) as f:  
    for line in f:
        ## regex not matching negative timezones
        date_match = re.search('\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\+\d{2}:\d{2}', line)
        match = re.search("POWER_SUPPLY_([A-Z_]*)=([A-Za-z0-9\-]*)", line)

        if date_match and len(data) > 0:
            # found next date need to print previous data point
            print ','.join([date,
                    data['NAME'],
                    data['STATUS'],
                    data['PRESENT'],
                    data['TECHNOLOGY'],
                    data['CYCLE_COUNT'],
                    data['VOLTAGE_MIN_DESIGN'],
                    data['VOLTAGE_NOW'],
                    data['CURRENT_NOW'] if data.has_key('CURRENT_NOW') else data['POWER_NOW'],
                    data['CHARGE_FULL'] if data.has_key('CHARGE_FULL') else data['ENERGY_FULL'],
                    data['CHARGE_FULL_DESIGN'] if data.has_key('CHARGE_FULL_DESIGN') else data['ENERGY_FULL_DESIGN'],
                    data['CHARGE_NOW'] if data.has_key('CHARGE_NOW') else data['ENERGY_NOW'],
                    data['CAPACITY'],
                    data['CAPACITY_LEVEL'],
                    data['MODEL_NAME'],
                    data['MANUFACTURER'],
                    data['SERIAL_NUMBER']])

            data = {}

        if date_match:
            date = date_match.group()
        else:
            data[match.group(1)] = match.group(2)
