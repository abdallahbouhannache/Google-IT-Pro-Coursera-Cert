#!/usr/bin/env python3



import os
import csv

fp=open('data.csv')
cvs_f=csv.reader(fp)

for row in csv_f:
	name,lastname,age=row
	print(f'{name}{lastname}{age}')

fp.close()

hosts=[['www.google.fr','10.22.54.83'],['localhost','127.0.0.1']]

with open('hosts.csv','w') as host_csv:
	csv_wr=csv.writer(host_csv)
	csv_wr.writerows(hosts)


#dictionnaries with csv:
with open('softwares.csv') as software:
	csv_dict_reader=csv.DictReader(software)
	for row in csv_dict_reader:
		print(f'{row["name"]} has {row["users"]}')

users=[{"name":"abdo","surname":"dodling","departement":"computing"},{"name":"kouki","surname":"latour","departement":"cool"},{"name":"david","surname":"touti","departement":"nothingness"}]
keys=["name","surname","departement"]

with open('by_departement.csv') as dept:
	csv_dict_writer=csv.DictWriter(dept,fieldnames=keys)
	csv_dict_writer.writeheader()
	csv_dict_writer.writeusers(users)








