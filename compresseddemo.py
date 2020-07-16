import zipfile
import gzip
myzip = zipfile.ZipFile("d:/kara-0.1.15.jar.src.zip")
print(myzip.filelist)