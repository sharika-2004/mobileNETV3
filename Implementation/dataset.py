!wget -q https://download.microsoft.com/download/3/E/1/3E1C3F21-ECDB-4869-8368-6DEBA77B919F/kagglecatsanddogs_5340.zip
!unzip -q kagglecatsanddogs_5340.zip -d cats_dogs
!rm kagglecatsanddogs_5340.zip
!find cats_dogs -type f -size 0 -delete
