import networkx as nx
import matplotlib.pyplot as plt
import networkx.drawing
import os
import json
from stop_words import get_stop_words
from collections import Counter
from  mywork1 import order
g=nx.DiGraph()
nodelabeldict={0:"root"}


g.add_node(0,value="null")
n=1
f=0
f1=0
temp=""
do=0
listop=["have","do"]
list44=[]
dict={}
stop_words = get_stop_words('english')
with open("/home/aayushman/Desktop/demo1.json") as data_file:    
    data_reply = json.load(data_file)    


list1=[]
kl=[]
list2=[]
for x in data_reply["dialogs"]:
	list44.append(str(x["cust"]).lower())
for j in list44:
	kl=j.split()
	
	for l in range(0,len(kl)):
		if kl[l] not in stop_words:
			list2.append(kl[l])
		if kl[l] in listop:
			list2.append(kl[l])
	list1.append(list2)
	list2=[]


abl=[]


for j in list1:
	for i in j:
		
		if i==j[0]:
			
			for k,l in g.node.items():
				for q,p in l.items():
					if p==i:
						
						g.add_edge(0,k)
						f=1
			if f==0:
				g.add_node(n,value=i,check=abl)
				nodelabeldict[n]=i
				g.add_edge(0,n)
				n=int(n)+1
			f=0
		else:
			for k,l in g.node.items():
				for q,p in l.items():
					if p==i:
						
						f1=1
						for k1,l1 in g.node.items():
							for q1,p1 in l1.items():
								if p1==temp:
							
									g.add_edge(k1,k)
			if f1==0:
				for k1,l1 in g.node.items():
					for q,p in l1.items():
						if p==temp:
					
							do=1
							temp2=k1
							
				if do==1:
					g.add_node(n,value=i,check=abl)
					nodelabeldict[n]=i
					g.add_edge(temp2,n)
					n=int(n)+1
					do=0
			f1=0

		temp=i
newli=[]


def function1(nod,n,txt2,lir=[],newli=[]):
	for i in lir:
		dictn=g.successors(nod)
		for m in dictn:
			if g.node[m]['value']==i and m not in newli:
				newli.append(m)
				m1=m	
				#print(m1)	
				if i==lir[-1]:
					break		
				function1(m,n,txt2,lir,newli)
	
					
			
	

for x in data_reply["dialogs"]:
	txt1=str(x["cust"]).lower()
	txt2=x["sales"]
	newli=[]
	lir=txt1.split()
	function1(0,n,txt2,lir,newli)            
	
	x=newli[-1]
	
	g.add_node(n,value=txt2,check=newli)
	g.add_edge(x,n)
	n=int(n)+1

n1=0
var=0
while(var<1):
	var=var+1
	print(var)
	newli=[]
	st=input()

	lir2=st.split()
	counter_intro=0
	def function2(n1):
		global counter_intro				
		for i in lir2:
		
			dictn1=g.successors(n1)
			for m in dictn1:
				
				if g.node[m]['value']==i and m not in newli:
					counter_intro=int(counter_intro)+1
								
					newli.append(m)	
					function2(m)			
			if i==lir2[-1]:
				return newli
		
			
			
	imsend=[]

	send1=[]
	newli=function2(0)
	
	if len(newli)!=0:
		dictn2=g.successors(newli[-1])

		for mk in dictn2:
			if g.node[mk]['check']==newli:
				send1.append(g.node[mk]['value'])



	con,imsend=order(st)
	print ("expected answers")
	if con>counter_intro:
		for i in imsend:
			print(i)
	else:
		for i in send1:	
			print(i)
				

pos=nx.spring_layout(g)

nx.draw(g, pos)
nx.draw_networkx_labels(g, pos, labels=nodelabeldict, font_size=24,
               font_family='sans-serif')

plt.show()
