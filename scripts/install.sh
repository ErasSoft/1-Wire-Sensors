#!/bin/bash
# Hochschule Neubrandenburg
# VMGG07 - Anwenderprojekte
# Verfasser: Tino Schuldt, Mathias Krueger
# Datum: 12.01.2016


# Skript als root starten!
if [ $(id -u) -ne 0 ]; then
  echo "ERR: This script must be run as root."
  exit 1
fi

# Konfigurationsdatei laden
source config/config.sh

# Installations Routine
(
dpkg -l $pkg_python > /dev/null 2>&1
if [ $? != 0 ]; then
	apt-get -y install $pkg_python 2>&1
	python_version=`python -c "import sys;t='{v[0]}.{v[1]}.{v[2]}'.format(v=list(sys.version_info[:3]));sys.stdout.write(t)";`
	date +"LOG: %H:%M:%S Install Package <$pkg_python>. Python Version: $python_version"
else
	python_version=`python -c "import sys;t='{v[0]}.{v[1]}.{v[2]}'.format(v=list(sys.version_info[:3]));sys.stdout.write(t)";`
	date +"LOG: %H:%M:%S Package <$pkg_python> is installed. Python Version: $python_version"
fi

dpkg -l $pkg_owfs > /dev/null 2>&1
if [ $? != 0 ]; then
	date +"LOG: %H:%M:%S Install Package <$pkg_owfs>."
	apt-get -y install $pkg_owfs 2>&1
else
	date +"LOG: %H:%M:%S Package <$pkg_owfs> is installed."
fi

# Matplotlib
dpkg -l $pkg_matplotlib > /dev/null 2>&1
if [ $? != 0 ]; then
	date +"LOG: %H:%M:%S Install Package <$pkg_matplotlib>."
	apt-get -y install $pkg_matplotlib 2>&1
else
	date +"LOG: %H:%M:%S Package <$pkg_matplotlib> is installed."
fi


) 2>&1 | tee -a "logfiles/"$(date +"%Y%m%d")"_install.log"			# logfile erstellen


