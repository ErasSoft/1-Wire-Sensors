#!/usr/bin/python
# Hochschule Neubrandenburg
# VMGG07 - Anwenderprojekte
# Verfasser: Tino Schuldt, Mathias Krueger
# Datum: 12.01.2016


# Bibliotheken einbinden
import subprocess

### FUNKTIONEN ###
def mountOWFS():
	# OWFS ins Filesystem mounten
	subprocess.call("./scripts/mount.sh")

def read():
	# Auslesen mehrerer Sensoren und speichern
	subprocess.call(["python", "./scripts/synchronized_all.py"])



### MAIN ###
mountOWFS()
read()
