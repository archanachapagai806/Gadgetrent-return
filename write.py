def writedic(myDictionary):
    file=open("products.txt","w")
    
    for values in myDictionary:
        file.write(str(values[1])+","+str(values[2])+","+str(values[3])+","+str(values[4]))
        file.write("\n")
    file.close()