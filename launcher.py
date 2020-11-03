import glob
import os
from datetime import datetime

##################################
#      Variables Setup           #
##################################
avidemux="e:/batch/avidemux_64/avidemux_cli.exe"
videocodec="x264"
audiocodec="Copy"
count=1

##################################
#        Main Program            #
##################################
print(datetime.now().strftime("[%d/%m/%Y %H:%M:%S] : ") + "Launching RGB-Pi Encoding Video Script")
print(datetime.now().strftime("[%d/%m/%Y %H:%M:%S] : ") + "--------------------------------------")
print(datetime.now().strftime("[%d/%m/%Y %H:%M:%S] : ") + "")
print(datetime.now().strftime("[%d/%m/%Y %H:%M:%S] : ") + "Initialing variables and settings")
print(datetime.now().strftime("[%d/%m/%Y %H:%M:%S] : ") + "Preparing the list of videos to encode and create subtitles")
print(datetime.now().strftime("[%d/%m/%Y %H:%M:%S] : ") + "")
number_vid = len(glob.glob('*.mp4'))
print(datetime.now().strftime("[%d/%m/%Y %H:%M:%S] : ") + "Nº Videos found to use: " + str(number_vid))
print(datetime.now().strftime("[%d/%m/%Y %H:%M:%S] : ") + "")

for val in glob.glob('*.mp4'):

	print(datetime.now().strftime("[%d/%m/%Y %H:%M:%S] : ") + "Video Position " + str(count) + "/" + str(number_vid) + " to encode")
	
	gamename = os.path.splitext(val)[0] 
	
	print(datetime.now().strftime("[%d/%m/%Y %H:%M:%S] : ") + "[VIDEO] Launch Encoding for " + gamename)
	os.system(avidemux + " --video-codec " + videocodec + " --audio-codec " + audiocodec + " --load " + (f'"{val}"') + " --run videos.py --save e:/batch/salida/" + (f'"{val}"') + " --quit")
	count=count+1
		
	print(datetime.now().strftime("[%d/%m/%Y %H:%M:%S] : ") + "[SUBS] Generating Subtitle for " + gamename)
	path = r"e:/batch/salida/"
	ruta = path	+ gamename + ".srt"

	if len(gamename) < 26:
		text_file = open(ruta, "w")
		text_file.write("1\n")
		text_file.write("00:00:00,000 --> 00:00:20,000\n")
		text_file.write(gamename)
		text_file.close()
		print("")	
	else:
		gamename_split = gamename.split(" ");
		text_file = open(ruta, "w")
		text_file.write("1\n")
		text_file.write("00:00:00,000 --> 00:00:20,000\n")
		split = len(gamename_split);
		mid = len(gamename_split)/2

		def dos_elementos():
			text_file.write(gamename_split[0] + "\n");
			text_file.write(gamename_split[1]);
			text_file.close()			

		def tres_elementos():
			text_file.write(gamename_split[0] + "\n");
			text_file.write(gamename_split[1] + " " + gamename_split[2]);
			text_file.close()		

		def cuatro_elementos():
			text_file.write(gamename_split[0] + " " + gamename_split[1] + "\n");
			text_file.write(gamename_split[2] + " " + gamename_split[3]);
			text_file.close()		

		def cinco_elementos():
			text_file.write(gamename_split[0] + " " + gamename_split[1] + " " + gamename_split[2] + "\n");
			text_file.write(gamename_split[3] + " " + gamename_split[4]);
			text_file.close()		

		def seis_elementos():
			text_file.write(gamename_split[0] + " " + gamename_split[1] + " " + gamename_split[2] + "\n");
			text_file.write(gamename_split[3] + " " + gamename_split[4] + " " + gamename_split[5]);
			text_file.close()		

		def siete_elementos():
			text_file.write(gamename_split[0] + " " + gamename_split[1] + " " + gamename_split[2] + "\n");
			text_file.write(gamename_split[3] + " " + gamename_split[4] + " " + gamename_split[5] + " " + gamename_split[6]);
			text_file.close()		

		def ocho_elementos():
			text_file.write(gamename_split[0] + " " + gamename_split[1] + " " + gamename_split[2] + " " + gamename_split[3] + "\n");
			text_file.write(gamename_split[4] + " " + gamename_split[5] + " " + gamename_split[6] + " " + gamename_split[7]);
			text_file.close()		
			
		def nueve_elementos():
			text_file.write(gamename_split[0] + " " + gamename_split[1] + " " + gamename_split[2] + " " + gamename_split[3] + "\n");
			text_file.write(gamename_split[4] + " " + gamename_split[5] + " " + gamename_split[6] + " " + gamename_split[7] + " " + gamename_split[8]);
			text_file.close()		
			
		def diez_elementos():
			text_file.write(gamename_split[0] + " " + gamename_split[1] + " " + gamename_split[2] + " " + gamename_split[3] + gamename_split[4] +"\n");
			text_file.write(gamename_split[5] + " " + gamename_split[6] + " " + gamename_split[7] + " " + gamename_split[8] + " " + gamename_split[9]);
			text_file.close()		
			
		def once_elementos():
			text_file.write(gamename_split[0] + " " + gamename_split[1] + " " + gamename_split[2] + " " + gamename_split[3] + " " + gamename_split[4] + " " + gamename_split[5] + "\n");
			text_file.write(gamename_split[6] + " " + gamename_split[7] + " " + gamename_split[8] + " " + gamename_split[9] + " " + gamename_split[10]);
			text_file.close()					

		def doce_elementos():
			text_file.write(gamename_split[0] + " " + gamename_split[1] + " " + gamename_split[2] + " " + gamename_split[3] + " " + gamename_split[4] + " " + gamename_split[5] + "\n");
			text_file.write(gamename_split[6] + " " + gamename_split[7] + " " + gamename_split[8] + " " + gamename_split[9] + " " + gamename_split[10] + " " + gamename_split[11]);
			text_file.close()		

		def trece_elementos():
			text_file.write(gamename_split[0] + " " + gamename_split[1] + " " + gamename_split[2] + " " + gamename_split[3] + " " + gamename_split[4] + " " + gamename_split[5] + " " + gamename_split[6] + "\n");
			text_file.write(gamename_split[7] + " " + gamename_split[8] + " " + gamename_split[9] + " " + gamename_split[10] + " " + gamename_split[11] + " " + gamename_split[12]);
			text_file.close()	
			
		def catorce_elementos():
			text_file.write(gamename_split[0] + " " + gamename_split[1] + " " + gamename_split[2] + " " + gamename_split[3] + " " + gamename_split[4] + " " + gamename_split[5] + " " + gamename_split[6] + "\n");
			text_file.write(gamename_split[7] + " " + gamename_split[8] + " " + gamename_split[9] + " " + gamename_split[10] + " " + gamename_split[11] + " " + gamename_split[12] + " " + gamename_split[13]);
			text_file.close()					

		def quince_elementos():
			text_file.write(gamename_split[0] + " " + gamename_split[1] + " " + gamename_split[2] + " " + gamename_split[3] + " " + gamename_split[4] + " " + gamename_split[5] + " " + gamename_split[6] + "\n");
			text_file.write(gamename_split[7] + " " + gamename_split[8] + " " + gamename_split[9] + " " + gamename_split[10] + " " + gamename_split[11] + " " + gamename_split[12] + " " + gamename_split[13] + " " + gamename_split[14]);
			text_file.close()		

		def diecesiete_elementos():
			text_file.write(gamename_split[0] + " " + gamename_split[1] + " " + gamename_split[2] + " " + gamename_split[3] + " " + gamename_split[4] + " " + gamename_split[5] + " " + gamename_split[6] + "\n");
			text_file.write(gamename_split[7] + " " + gamename_split[8] + " " + gamename_split[9] + " " + gamename_split[10] + " " + gamename_split[11] + " " + gamename_split[12] + " " + gamename_split[13] + "\n");
			text_file.write(gamename_split[14] + " " + gamename_split[15] + " " + gamename_split[16]);
			text_file.close()			
			
		switch_mid = {
			1.0: dos_elementos,
			1.5: tres_elementos,
			2.0: cuatro_elementos,
			2.5: cinco_elementos,
			3.0: seis_elementos,
			3.5: siete_elementos,
			4.0: ocho_elementos,
			4.5: nueve_elementos,
			5.0: diez_elementos,
			5.5: once_elementos,
			6.0: doce_elementos,
			6.5: trece_elementos,
			7.0: catorce_elementos,
			7.5: quince_elementos,
			8.5: diecesiete_elementos,
			
		}

		switch_mid.get(mid)()
		print("")	