#!/usr/bin/python
# Hochschule Neubrandenburg
# VMGG07 - Anwenderprojekte
# Verfasser: Tino Schuldt, Mathias Krueger
# Datum: 12.01.2016


# Bibliotheken einbinden
import subprocess

### FUNKTIONEN ###
def installOWFS():
	# Installiere OWFS
	subprocess.call("./scripts/install.sh")


### MAIN ###
installOWFS()
