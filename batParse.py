import sys, re, os

print "date, value"

with open(sys.argv[1]) as f:  
    for line in f:
        ## regex not matching negative timezones
        match = re.search('\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\+\d{2}:\d{2}', line)

        if match:
            # found date but theres no data on this line skip printing this line
            date = match.group()
            continue
        else:
            print '{},{}'.format(date, line.rstrip('\n'))
