import sys, re, os


time = ''

with open(sys.argv[1]) as f:  
    line = f.readline()
    while line:
        line = f.readline()
        ## regex not matching negative timezones
        match = re.search('\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\+\d{2}:\d{2}', line)
        time = match.group() if match else time
        print '{},{}'.format(time, line)
