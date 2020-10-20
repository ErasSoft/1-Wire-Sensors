#!/usr/bin/env python2.7
# Hochschule Neubrandenburg
# VMGG07 - Anwenderprojekte
# Verfasser: Tino Schuldt, Mathias Krueger
# Datum: 20.01.2016

configuration = {
	"sensoren" : ("t-probe", "ow-env"),	#Liste der angeschlossenen Sensoren, Einträge in Gänsefüßchen getrennt durch Komma, kleingeschrieben, bisher :t-probe, ow-env und ow-temp
	"mountPfad" : "./1wire",			#Mountpfad der Sensoren, Standard ist der Pfad in unserer Ordnerstruktur
	"speicherort" : "./data"			#Speicherpfad der Sensoren, Standard ist der Pfad in unserer Ordnerstruktur
	"messungen" : 200					#Anzahl der Messungen, die getätigt werden sollen
}

plotting = ""							#Pfad und Name der Datei die geplottet werden soll, z.B. "../data/t-probe-2016-01-20.csv"

if __name__ =="__main__":
	print(configuration)
	print("OK!")
