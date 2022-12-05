filestring = "inflationscript"

f = open("inflationscript1.sh", "w")

count = 2

basestring = "python inflation"

f.write("#!/bin/bash\n")

for i in range(1,147):
    if (i%10 == 0):
        f.close()
        currfilename = filestring + str(count) + ".sh"
        f = open(currfilename, "w")
        count = count + 1
        f.write("#!/bin/bash\n\n" + basestring + str(i) + ".py &\n")
    
    else:
        f.write(basestring + str(i) + ".py &\n")