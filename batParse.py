import sys, re, os


time = ''

with open(sys.argv[1]) as f:  
    for line in f:
        ## regex not matching negative timezones
        match = re.search('\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\+\d{2}:\d{2}', line)
        time = match.group() if match else time
        print '{},{}'.format(time, line)
