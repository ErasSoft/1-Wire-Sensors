#!/bin/bash
# Hochschule Neubrandenburg
# VMGG07 - Anwenderprojekte
# Verfasser: Tino Schuldt, Mathias Krueger
# Datum: 12.01.2016

# Hier die Sensoren definieren
sensor[0]="28.DBF5BD030000=t-probe"		# Sensor T-Probe (Temperatur Sensor)
sensor[1]="7E.782600001000=ow-env-thpl"		# Sensor OW-ENV-THPL (Mess Sensor)
sensor[2]="10.DCA98C020800=ow-temp-s3-12r"	# Sensor OW-TEMP-S3-12R (Temperatur Sensor)

# Zusätzliche Namen und Pfade
aliasname="sensoren_name.txt"			# Datei für die Sensor Namen
mountpfad=$(pwd ~)"/1wire"			# Pfad zum mounten der Sensoren

# Benötigte Pakete für die Installation
pkg_python="python"
pkg_owfs="owfs"
pkg_matplotlib="python-matplotlib"
