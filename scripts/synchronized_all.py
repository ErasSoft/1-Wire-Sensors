#!/usr/bin/env python2.7
# Hochschule Neubrandenburg
# VMGG07 - Anwenderprojekte
# Verfasser: Tino Schuldt, Mathias Krueger
# Datum: 20.01.2016

import save_plot
import read_all
import threading
import datetime
import sys
sys.path.append('config')
import config_python

class start_read(threading.Thread):
	def __init__(self, obj):
		threading.Thread.__init__(self)
		self.obj = obj

	def run(self):
		#Start des Sensorobjektes
		self.obj.run()

def main():
	while True:
		#Einbinden der Konfigurations-Datei
		configuration = config_python.configuration

		# Mount Pfad der Sensoren		
		pfad = configuration["mountPfad"]
		messungen = configuration["messungen"]
		
		if "t-probe" in configuration["sensoren"]:
			r1 = read_all.read_t_probe(pfad, messungen)				#Legt Objekt der Klasse für T-Probe an
			file1 = configuration["speicherort"] + "/t-probe-"		#Aufbau des Filenamens zum Speichern
			r1p1 = save_plot.csv_dumper(file1)						#Legt Objekt der Speicherklasse an
			r1.attach(r1p1)											#Ankoppeln der Speicherklasse an die Sensorklasse mittels Observer-Pattern
			thread1 = start_read(r1)								#Erstellen eines Threads für den Sensor und übergeben der dazugehörenden Sensorklasse
			thread1.run()

		if "ow_env" in configuration["sensoren"]:
			r2 = read_all.read_ow_env(pfad, messungen)				#Legt Objekt der Klasse für Ow-Env an
			file2 = configuration["speicherort"] + "/ow-env-"		#Aufbau des Filenamens zum Speichern
			r2p1 = save_plot.csv_dumper(file2)						#Legt Objekt der Speicherklasse an
			r2.attach(r2p1)											#Ankoppeln der Speicherklasse an die Sensorklasse mittels Observer-Pattern
			thread2 = start_read(r2)								#Erstellen eines Threads für den Sensor und übergeben der dazugehörenden Sensorklasse
			thread2.run()

		if "ow-temp" in configuration["sensoren"]:
			r3 = read_all.read_ow_temp(pfad, messungen)				#Legt Objekt der Klasse für Ow-Temp an
			file3 = configuration["speicherort"] + "/ow-temp-"		#Aufbau des Filenamens zum Speichern
			r3p1 = save_plot.csv_dumper(file3)						#Legt Objekt der Speicherklasse an
			r3.attach(r3p1)											#Ankoppeln der Speicherklasse an die Sensorklasse mittels Observer-Pattern
			thread3 = start_read(r3)								#Erstellen eines Threads für den Sensor und übergeben der dazugehörenden Sensorklasse
			thread3.run()

if __name__ == "__main__":
	main()
