#!/usr/bin/env python2.7
# Hochschule Neubrandenburg
# VMGG07 - Anwenderprojekte
# Verfasser: Tino Schuldt, Mathias Krueger
# Datum: 20.01.2016

"""
In diesem Script sind die Klassen zum Auslesen der Sensoren erstellt.
"""

import threading
from sys import stdout
from sys import exit
from time import sleep
import datetime
import observable

class read_t_probe(observable.Observable):
	def __init__(self, pfad, messungen):
		super(read_t_probe, self).__init__()
		self.pfad = pfad
		self.__data = None
		self.date = str(datetime.datetime.today()).split()
		self.messungen = messungen

	def run(self):
		for i in range(messungen):
			
			# Temperature = Temperatur in [Grad Celsius]
            temp = open(self.pfad+"/t-probe/temperature", "r")
            t_raw = temp.read()
            temp.close()
            t = float(t_raw)

			# Zeitstempel (2012-12-15 01:21:05 oder nur 01:21:05)
			z = datetime.datetime.today()

			# Zeitstempel|Temperatur|
            self.data = (str(z) + '|' + str(t) + '\n')
			print(self.data)
			
			# Optimaler Wert 15 Sekunden zwischen jeden Wert!
            sleep(15.0)

			# Leert den Ausgabepuffer
            stdout.flush()
		exit()
	
	"""
	Die Funktionen sind für die Observer-Pattern
	"""
	@property
	def data(self):
		value = self.__data
		return value

	@data.setter
	def data(self, value):
		self.__data = value
		self.notify()

class read_ow_env(observable.Observable):
	def __init__(self, pfad, messungen):
		super(read_ow_env, self).__init__()
		self.pfad = pfad
		self.__data = None
		self.date = str(datetime.datetime.today()).split()
		self.messungen = messungen

	def run(self):
		for i in range(messungen):
        		
			# Temperature = Temperatur in [Grad Celsius]
            temp = open(self.pfad+"/ow-env-thpl/EDS0068/temperature", "r")
            t_raw = temp.read()
            temp.close()
            t = float(t_raw)
			
			# Luftfeuchtigkeit = Luftfeuchtigkeit in [Prozent]
            humidity = open(self.pfad+"/ow-env-thpl/EDS0068/humidity", "r")
            h_raw = humidity.read()
            humidity.close()
            h = float(h_raw)
			
			# Dewpoint = Taupunkt in [Grad]
            dewpoint = open(self.pfad+"/ow-env-thpl/EDS0068/dew_point", "r")
            d_raw = dewpoint.read()
            dewpoint.close()
            d = float(d_raw)
			
			# Pressure = Luftdruck in [hp]
            pressure = open(self.pfad+"/ow-env-thpl/EDS0068/pressure", "r")
            p_raw = pressure.read()
            pressure.close()
            p = float(p_raw)
			
			# Light = Helligkeit in [Lux]
            light = open(self.pfad+"/ow-env-thpl/EDS0068/light", "r")
            l_raw = light.read()
            light.close()
            l = float(l_raw)

			# Zeitstempel (2012-12-15 01:21:05 oder nur 01:21:05)
			z = datetime.datetime.today()

			# Zeitstempel|Temperatur|Luftfeutigkeit|Taupunkt|Luftdruck|Helligkeit
			self.data = (str(z) + '|' + str(t) + '|' + str(h) + '|' + str(d) + '|' + str(p) + '|' + str(l) + '\n')
			print(self.data)
			
			# Optimaler Wert 15 Sekunden zwischen jeden Wert!
            sleep(15.0)

			# Leert den Ausgabepuffer
            stdout.flush()
		exit()

	"""
	Die Funktionen sind für die Observer-Pattern
	"""
	@property
	def data(self):
		value = self.__data
		return value

	@data.setter
	def data(self, value):
		self.__data = value
		self.notify()

class read_ow_temp(observable.Observable):
	def __init__(self, pfad, messungen):
		super(read_t_probe, self).__init__()
		self.pfad = pfad
		self.__data = None
		self.date = str(datetime.datetime.today()).split()
		self.messungen = messungen

	def run(self):
		for i in range(messungen):
			
			# Temperature = Temperatur in [Grad Celsius]
            temp = open(self.pfad+"/ow-temp/temperature", "r")
            t_raw = temp.read()
            temp.close()
            t = float(t_raw)

			# Zeitstempel (2012-12-15 01:21:05 oder nur 01:21:05)
			z = datetime.datetime.today()

			# Zeitstempel|Temperatur|
            self.data = (str(z) + '|' + str(t) + '\n')
			print(self.data)
			
			# Optimaler Wert 15 Sekunden zwischen jeden Wert!
            sleep(15.0)

			# Leert den Ausgabepuffer
            stdout.flush()
		exit()

	"""
	Die Funktionen sind für die Observer-Pattern
	"""
	@property
	def data(self):
		value = self.__data
		return value

	@data.setter
	def data(self, value):
		self.__data = value
		self.notify()
