#reverse the contents of a files//
nandu = list()
datacom = open('/Users/srinandy/Desktop/nandu.txt', 'r')
for eachline in datacom:
    nandu.append(eachline)

datacom.close()    

datacell = open('/Users/srinandy/Desktop/camel','w')
for i in range (len(nandu)):
    new = nandu[-(i+1)]
    datacell.write(new)

datacell.close() 
