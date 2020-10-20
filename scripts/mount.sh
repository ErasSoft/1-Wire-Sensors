#!/bin/bash
# Hochschule Neubrandenburg
# VMGG07 - Anwenderprojekte
# Verfasser: Tino Schuldt, Mathias Krueger
# Datum: 12.01.2016


# Konfigurationsdatei laden
source config/config.sh

(
#  Sensoren in eine Text-Datei schreiben
date +"LOG: %H:%M:%S Write Sensorlist in File <config/$aliasname>."
echo -n > config/$aliasname;
for i in ${sensor[@]}
do
	echo $i >> config/$aliasname;
done
if ! [ $? -eq 0 ] ; then			# Fehlerbehandlung
	date +"ERR: %H:%M:%S Can not write in File <$mountpfad>."
fi

# Mount Ordner erstellen
date +"LOG: %H:%M:%S Mount path in <$mountpfad>."
if ! [ -d "$mountpfad" ] ; then 		# Wenn noch kein Ordner vorhanden ist
	mkdir $mountpfad
	if ! [ $? -eq 0 ] ; then		# Fehlerbehandlung
		date +"ERR: %H:%M:%S Can not create path in <$mountpfad>."
	fi
fi

# Dateipfad mounten
ls /dev/ | grep ttyUSB* > /dev/null 2>&1	# Alle ttyUSB auslesen
if [ $? == 0 ]; then				# Überprüfen, ob mind. ttyUSB0 vorhanden ist
	usb_devices=(`ls /dev/ttyUSB*`)		# Alle ttyUSB auslesen und speichern
	available_usbdevices=""
	for i in ${usb_devices[@]}		# Alle ttyUSB durchgehen
	do
		date +"LOG: %H:%M:%S Found Sensor in USB-Device <${i:5}>."
		available_usbdevices+="$i "
	done
fi

# USB-Device mounten
if [ -n "$available_usbdevices" ]; then
	date +"LOG: %H:%M:%S Mount USB-Devices <$available_usbdevices>."
	owfs -a config/$aliasname -d $available_usbdevices -m $mountpfad
else
	date +"ERR: %H:%M:%S No USB-Devices found!"
	#owfs -a config/$aliasname -m $mountpfad
fi

#  Sensoren Namen auslesen
sensor_devices=(`ls $mountpfad`)
for i in ${sensor_devices[@]}
do
	if [ $i != "05.4AEC29CDBAAB" ] && [ $i != "10.67C6697351FF" ] && [ $i != "alarm" ] && [ ${i:0:4} != "bus." ] && [ $i != "settings" ] && [ $i != "simultaneous" ] && [ $i != "statistics" ] && [ $i != "structure" ] && [ $i != "system" ] && [ $i != "uncached" ] ; then
		date +"LOG: %H:%M:%S Sensor available <$i>."
	fi
done

) 2>&1 | tee -a "logfiles/"$(date +"%Y%m%d")"_mount.log"			# logfile erstellen
