import os
txtfilename = "pythontxt.txt"
if not os.path.isfile(txtfilename):
    print 'no such file exists'
else:
    txtfile = open(txtfilename,'r')
    for line in txtfile:
        print line
    txtfile.close()
