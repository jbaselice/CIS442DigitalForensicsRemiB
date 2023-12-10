# CIS442DigitalForensicsRemiB
CIS442 Project for University of Massachusetts Dartmouth, Remi (Jeremiah) Baselice
This is the default project for Digital Forensics CIS 442 at University of Massachusetts Dartmouth, submitted by Remi (Jeremiah) Baselice.
It is a program written in python that takes as input a folder path, and then will check if there are any masqueraded files in it, and output the paths of each of those that it finds. It uses the "magic" library in python in order to get the file signature from each of the files it finds in the folder, it then compares it with the extension found in the files name, to see if they match. If they do not, it will output the path of the file, and if it finds no masquaraded files it will output that it could not find any. The code relies on knowing the signatures of file types prior, as seen in the beginning. If there are other file types that you want to check that are not available, you can simply add them to the list at the beginning of the code (shown with comments) It currently supports the following file types: jpeg, png, gif, txt, html, pdf, doc, docx, ppt, pptx, xls, xlsx, csv, mp3, wav, mp4, mov, and avi. 
This is a link to a short demo showing it working: https://youtu.be/vdU8S52l5K0    This can also be found in the github under "VideoLink.txt"
