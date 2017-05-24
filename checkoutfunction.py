import networkx as nx
import matplotlib.pyplot as plt
import networkx.drawing
import os
import json
counter=0
from stop_words import get_stop_words
from collections import Counter
def checkout(st):
	global counter
	counter=0
	g=nx.DiGraph()
	nodelabeldict={0:"root"}

	
	g.add_node(0,value="null")
	n=1
	f=0
	f1=0
	temp=""
	do=0
	listop=["have","do","no","yes"]
	list21=[]
	list22=[]
	list23=[]
	list44=[]
	dict={}
	stop_words = get_stop_words('english')
	with open("/home/aayushman/Desktop/Checkout.json") as data_file:    
	    data_reply = json.load(data_file)    

	print("hola hola")
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
	#print(list1)

	abl=[]

	#print(g.node)
	#print(g.edge)
	for j in list1:
		for i in j:
		
			if i==j[0]:
			
				for k,l in g.node.items():
					for q,p in l.items():
						if p==i:
							#print(p)
					#if l['value']==i:
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
							#print(p)
					#if l['value']==i:
							f1=1
							for k1,l1 in g.node.items():
								for q1,p1 in l1.items():
									if p1==temp:
								#if l1['value']==temp:
										g.add_edge(k1,k)
				if f1==0:
					for k1,l1 in g.node.items():
						for q,p in l1.items():
							if p==temp:
						#if l['value']==temp:
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

	#print(g.node)
	#print(g.edge)
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
		#print(newli)
		x=newli[-1]
		#print(x)
		g.add_node(n,value=txt2,check=newli)
		g.add_edge(x,n)
		n=int(n)+1

	n1=0
	newli=[]
	#st=input()

	lir2=st.split()
	
	
	def function2(n1):
		global counter				
		for i in lir2:
		
			dictn1=g.successors(n1)
			for m in dictn1:
				#print(m)
				if g.node[m]['value']==i and m not in newli:
					counter=int(counter)+1					
					newli.append(m)	
					function2(m)			
			if i==lir2[-1]:
				return newli
			
			
			

	send=[]
	newli=function2(0)
	#print(newli)
	if len(newli)!=0:
		dictn2=g.successors(newli[-1])
		#print("expected answers")
		for mk in dictn2:
			if g.node[mk]['check']==newli:
				send.append(g.node[mk]['value'])
				
	#print(send)

	#print(g.node)
	#print(g.edge)
	print("\n")
	#dic=g.successors(5)
	#for m in dic:
		#print(m)
	#pos=nx.circular_layout(g)
	#nx.draw_networkx_labels(g,pos,labels,font_size=16)
	#nx.draw(g,pos,font_size=30)
	#nx.draw_circular(g)
	#pos = nx.spring_layout(g,scale=10)
	#nx.draw(g,pos)
	#nx.draw_networkx_labels(g, pos, labels=nodelabeldict, font_size=16,
		      # font_family='sans-serif')
	
	return counter,send
