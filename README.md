# exifTool_metadata_edit
The purpose of this script is to use the Exiftool to edit the metadata of images and make them 508 compliant
This script specifically is meant for files generated as output of HVSR analysis.
This script will pull text information from the associated .txt file and use this text to rename output images.
Additonally this script will add a user defined comment to the metadata of each output image.

To properly run this script, the Exiftool executable must be installed and the Pillow Image library must be installed in your active virtual environment.

Tutorial on how to create a virtual environment:
https://www.youtube.com/watch?v=KxvKCSwlUv8

Exiftool installation:
https://exiftool.org/index.html
