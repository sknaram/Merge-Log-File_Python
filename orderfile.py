#BY SAI NARAM
Zero = open("C:/Users/saiknaram/Downloads/HomeWork/HomeWork/Dir0/fruit.log", 'r'); #Storing locations of all log files
One = open("C:/Users/saiknaram/Downloads/HomeWork/HomeWork/Dir1/fruit.log", 'r');
Two = open("C:/Users/saiknaram/Downloads/HomeWork/HomeWork/Dir2/fruit.log", 'r');
Three = open("C:/Users/saiknaram/Downloads/HomeWork/HomeWork/Dir3/fruit.log", 'r');
Four = open("C:/Users/saiknaram/Downloads/HomeWork/HomeWork/Dir4/fruit.log", 'r');
Out = open("C:/Users/saiknaram/Downloads/HomeWork/HomeWork/Output.log", 'w');
Hour = {}; #Dictionary because I want to keep track of file location and its hour
HourSorted = []; #List because dictionaries cannot be sorted. 
filenames = [Zero, One, Two, Three, Four]; #Keeping them here for easy compare later
Kiwi_0 = []; #Empty list

	
for line in Zero.readline() and range(0,1): #Just need the first line, hence using range(0,1)
	data = Zero.readline();
	Hour[Zero] = data[7:9];
#	print Hour;
	
for line in One.readline() and range(0,1):
	data = One.readline();
	Hour[One] = data[7:9];
#	print Hour;

for line in Two.readline() and range(0,1):
	data = Two.readline();
	Hour[Two] = data[7:9];
#	print Hour;	

for line in Three.readline() and range(0,1):
	data = Three.readline();
	Hour[Three] = data[7:9];
#	print Hour; #These were all for sanity checks

for line in Four.readline() and range(0,1):
	data = Four.readline();
	Hour[Four] = data[7:9];
#	print Hour;

for key, value in sorted(Hour.iteritems(), key=lambda (k,v): (v,k)): #Got this code from StackOverflow and sorted the dictionary into a list
   HourSorted.append(key);
   HourSorted.append(value);
#  print HourSorted;

for a in range(0,len(HourSorted)-1, 2): #If the item in HourSorted matches filenames items then write lines into output file
	for b in range(0,len(filenames)-1,1):
		if(HourSorted[a] == filenames[b]):
			for line in filenames[b]:
				Out.write(line);
			
for j in range(0,len(HourSorted)-1,2): #This list has file location and numbers. I only needed the file locations, so ignored the numbers
	for line in HourSorted[j]: 
		if "Kiwi" in line: #If Kiwi is found, slice the line after the colon. 
			#print line[74:85]; Again, sanity check
			Kiwi_0.append(int(line[73:85])); #Put this into a list
			#print Kiwi_0;
			total = sum(Kiwi_0,0.0); #Can do this to avoid problems when dividing sum by length. 
			length = len(Kiwi_0);
			#print total/(length);	
print min(Kiwi_0);
print max(Kiwi_0);
print total/length;		
#BY SAI NARAM

One.close();
Two.close();
Zero.close();
Three.close();
Four.close();
Out.close();
#Please find test cases in excel sheet