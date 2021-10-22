# Text2BMP
convert a long text (novel, diary, press article collection) to a BMP image to spot hidden images in the dot patterns
The app reads content from a sound file and converts it to a BMP image. The image is in 240x640 RGB format 16 bit.
You must have Python installed or it will not work.
The sound file must be named sound.wav and placed in the same directory as the program or the program will crash.
The sound file must be in the following format:
	- uncompressed WAV
	- 11025Hz
	- 8 bit
	- at least 1,6MB or the program won't work (use a whole song or edit the sound to repeat it until you reach the right file size)
The program still works with different bitrates but size is crucial, a file too small will result in an unusable picture.
You can convert an mp3 file to this format with Audacity, a free open source program you can find at https://www.audacityteam.org/
If you are converting a typical file format recorded with a cellphone you will probably need the FFmpeg plugin. You can download it at https://manual.audacityteam.org/man/installing_ffmpeg_for_windows.html
I included a demo sound file, containing the prelude to Marc Antoine Charpentier's "Te Deum", which everyone in Europe knows as the opening theme of Eurovision, the satellite TV shows aired all over Europe. I also included the resulting image.
Once you have the sound file, just double click the script and you will get an image file named soundimage.bmp. You can open the file with any image viewer supporting the BMP format, but it will be in color and difficult to "decode". In order to be able to spot recognizable shapes you will have to convert it to grayscale. You can use the free open source program GIMP. Download it at www.gimp.org
