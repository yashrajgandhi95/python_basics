import os
lines = 'hello world \n python is easy'
txtfilename = "pythontxt.txt"
if not os.path.isfile(txtfilename):
    txtfile = open(txtfilename,'w')
    txtfile.write(lines)
    txtfile.close()


