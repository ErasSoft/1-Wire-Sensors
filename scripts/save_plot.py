#!/usr/bin/env python2.7
# Hochschule Neubrandenburg
# VMGG07 - Anwenderprojekte
# Verfasser: Tino Schuldt, Mathias Krueger
# Datum: 20.01.2016

import csv
import datetime

class csv_dumper(object):
	def __init__(self, filename):
		self.file = filename

	def update(self, fromObservable):
		"""
		Aufbau des Namens der csv-Datei
		Hinzufügens des Datums und der Dateiendung zum Sensornamen
		"""
		date = str(datetime.datetime.today()).split()
		newfile = self.file + date[0] + ".csv"
		
		"""
		Öffnen des csv-Files
		Umwandeln der Messwerte in eine Liste
		Speichern der Werte in die Datei
		"""
		f = open(self.file, 'a')
		try:
			datalist = []
			datalist = fromObservable.data.strip().split('|')
			
			writer = csv.writer(f)
			writer.writerow(datalist)
		finally:
			f.close()