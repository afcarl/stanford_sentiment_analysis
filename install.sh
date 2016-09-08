#!/bin/sh
#Directory name where the stanford file will be copied
DIRECTORY=".stanford_sentiment_library"
FILENAME="stanford-corenlp-full-2015-12-09.zip"
#Checking if there directory exist
if [ ! -d "$HOME/$DIRECTORY" ]
then
    mkdir $HOME/$DIRECTORY
fi	


#Checking the existence of the file
if [ ! -f "$HOME/$DIRECTORY/$FILENAME" ]
then
    echo 'Please wait I need to download around 400 MB. of file'
    wget -O $HOME/$DIRECTORY/stanford-corenlp-full-2015-12-09.zip http://nlp.stanford.edu/software/stanford-corenlp-full-2015-12-09.zip
else
	#Checking the file size
	FILESIZE=$(wc -c <"$HOME/$DIRECTORY/$FILENAME")
	
	if [ $FILESIZE -lt 403157240 ]; then
		echo 'Last time the download was interrupted so downloading the rest of 400 MB. '
    	        wget -O $HOME/$DIRECTORY/stanford-corenlp-full-2015-12-09.zip http://nlp.stanford.edu/software/stanford-corenlp-full-2015-12-09.zip
	fi
fi
 # Checking if the extracted folder exist otherwise extract it
if [ ! -d "$HOME/$DIRECTORY/stanford-corenlp-full-2015-12-09" ]
then 
    unzip $HOME/$DIRECTORY/$FILENAME -d $HOME/$DIRECTORY/
fi

cd stanford_sentiment
sudo python setup.py install
echo "Awesome! Please enjoy the package"
