import re
import os
fo =open('running_config.txt', "r+")
#print ("Name of the file: ", fo.name)
lines=fo.readlines()
#print(type(lines))
int2 = "_"
desc = "_"
mtu="_"
vrf="_"

section = []
each_line=[]
all_line=[['intname','des','mtu','vrf','ip','subnet']]

for i in lines :
	if "!" not in i: # secifing the sections
		section.append(i)
	else :
		for k in section:
			if 'interface' in k :  ## concerned only about sections with interface in it 
				#print(section)
				section_selected=section 
				#print(section_selected)
				each_line=['-','-','-','-','-','-']
				for l in section_selected:
					
					if re.search("^interface\s\S+", l) :
						int1 = re.search("^interface\s\S+", l).group(0)
						int =int1.split('interface')
						int2=str(int[1])
						#print(int)
						each_line[0]=int2
						if 'preconfigure' in int2 :
							special_int=re.search("^interface\s\S+\s\S+", l).group(0)
							#print(special_int)
							int =special_int.split('interface')
							int2=str(int[1])
							each_line[0]=int2
							#each_line[0] = str(int[1]) + str(int[2]) + str(int[3])
				
					if  'description' in l:
					    desc1 = re.search("^\sdes.*", l).group(0)
					    desc2=desc1.split("description")
					    desc=desc2[1]
					    #print (desc)
					    #each_line.append(des)
					    each_line[1]=desc


					
					if re.search("^\smtu\s.*", l):
					   mtu1 = re.search("^\smtu\s.*", l).group(0)
					   mtu2=mtu1.split("mtu")
					   mtu=str(mtu2[1])
					   #print(mtu[1])
					   #f.write(mtu)
					   #each_line.append(mtu)
					   each_line[2]=mtu

					
					
					
					if re.search("^\svrf\s.*",l):
					    vrf1=re.search("^\svrf\s.*",l).group(0)
					    #print vrf1
					    vrf=vrf1.split("vrf")
					    #print(vrf[1])
					    #f.write(vrf[1])
					    #each_line.append(vrf[1])
					    each_line[3]=vrf[1]

					if re.search(r"^\sipv4\saddress\s\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", l):
						ip1= re.search(r"^\sipv4\saddress\s\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",l).group(0)
						ip2=ip1.split("ipv4 address")
						#print ip2
						ip3=ip2[1]
						ip=ip3.split()
						#print (ip[0])
						#print (ip[1])
						each_line[4]=ip[0]
						each_line[5]=ip[1]
        				#f.write(ip[0])
					#	f.write("\n")
					all_line.append(each_line)
		#print(section)
		section = []
    
        #f.write(" ")
#print(all_line)
'''
    if re.search(r"^\s\ipv4\saddress\s\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", k):
        ip1= re.search(r"^\sipv4\saddress\s\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",
                      k).group(0)
        ip2=ip1.split("ipv4 address")
        #print ip2
        ip3=ip2[1]
        ip=ip3.split()
        print (ip[0])
        print (ip[1])
        f.write(ip[0])

    '''    #f.write(" ")

    #f.write(int2)

    #f.write(desc)

    #f.write(mtu)

    #f.write(ip[0])


    #f.write(ip[1])

    

    #f.write(int)

    #f.write("\n")

    #f.write(desc + "\n")

    #f.write(mtu + "\n")


        #elif re.search("description.*",k):
                #desc=re.search("description.*",k).group(0)
                #f.write(desc+"")

                #f.write("\n")

        #else:
            #desc="_"
        #else:
            #desc="_"
            #f.write(desc)

            #f.write("\n")

    #f.write("\n")

    #f.write(desc)

    #f.write("\n")

#save config 

f = open("Config_new.csv", "w+")


for each_line in all_line :

	if each_line[0] is not '-' : 

		for item in each_line :


			f.write(item+',')
			#f.write(',')
	f.write('\n')	

f.close()
fo.close()
