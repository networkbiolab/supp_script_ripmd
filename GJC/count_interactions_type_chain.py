file=open("consensus_as_list","r")
saved=[]
for line in file:
	saved.append(line[:-1])
print ("subunit1\tsubunit2\ttype\tquantity")	
for i in range (1,13):
	j=i+1
	while j<13:
		dictio={"hb":0,"salt":0,"cp":0,"pp":0,"rr":0}
		for line in saved:
			splt1=line.split(":")[1]
			splt2=line.split(":")[3]
			if ("P"+str(i)==splt1 and "P"+str(j)==splt2 ) or ("P"+str(j)==splt1 and "P"+str(i)==splt2):
				if "Hydrogen Bond" in line:
					dictio["hb"]+=1
				if "Salt Bridge" in line:
					dictio["salt"]+=1
				if "Cation-Pi" in line:
					dictio["cp"]+=1					
				if "Pi-Pi" in line:
					dictio["pp"]+=1
				if "Arg-Arg" in line:
					dictio["rr"]+=1			
		if dictio["cp"]>0:
			print ("P"+str(i)+"\tP"+str(j)+"\tCation-Pi\t"+str(dictio["cp"]))
		if dictio["hb"]>0:
			print ("P"+str(i)+"\tP"+str(j)+"\tHB\t"+str(dictio["hb"]))
		if dictio["salt"]>0:
			print ("P"+str(i)+"\tP"+str(j)+"\tsalt\t"+str(dictio["salt"]))
		if dictio["pp"]>0:
			print ("P"+str(i)+"\tP"+str(j)+"\tpi-pi\t"+str(dictio["pp"]))
		if dictio["rr"]>0:
			print ("P"+str(i)+"\tP"+str(j)+"\targ-arg\t"+str(dictio["rr"]))	

		j+=1
		
