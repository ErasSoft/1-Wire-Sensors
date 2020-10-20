#!/usr/bin/env python2.7
# Hochschule Neubrandenburg
# VMGG07 - Anwenderprojekte
# Verfasser: Tino Schuldt, Mathias Krueger
# Datum: 20.01.2016

import matplotlib.pyplot as plt
sys.path.append('config')
import config_python
import csv

#Einlesen von Pfad und Namen der Datei die geplottet werden soll
file = config_python.plotting

#Unterschieden wird in Ow-Env, der mehrere Werte ausliest und T-Probe und Ow-Temp, die nur einen Wert einlesen
if "ow-env" in file:
	temperatur = []
	time = []
	luftdruck = []
	luftfeuchtigkeit = []
	taupunkt = []
	helligkeit = []
	
	with open(file) as f:
		#Auslesen der csv-Datei
		reader = csv.reader(f)
		for row in reader:
			#Speichern der Werte in die dazugehörenden Dictionaries
			time.append(row[0])
			temperatur.append(row[1])
			luftdruck.append(row[2])
			luftfeuchtigkeit.append(row[3])
			taupunkt.append(row[4])
			helligkeit.append(row[5])
	
	#Plotten der Werte
	#Für jeden wert wird dafür ein Subplot angelegt
	fig, axes = plt.subplots(3, 2)
	axes[0, 0].plot(temperatur)
	axes[0, 0].set_title("Temperatur")
	axes[1, 0].plot(luftdruck)
	axes[1, 0].set_title("Luftdruck")
	axes[0, 1].plot(luftfeuchtigkeit)
	axes[0, 1].set_title("Luftfeuchtigkeit")
	axes[1, 1].plot(taupunkt)
	axes[1, 1].set_title("Taupunkt")
	axes[2, 0].plot(helligkeit)
	axes[2, 0].set_title("Helligkeit")
	plt.show()
else:
	temperatur = []
	time = []
	
	with open(file) as f:
		#Auslesen der csv-Datei
		reader = csv.reader(f)
		for row in reader:
			#Speichern der Werte in die dazugehörenden Dictionaries
			time.append(row[0])
			temperatur.append(row[1])
	
	#Plotten der Werte
	plt.figure()
	plt.plot(temperatur)
	plt.show()