import os                   #imports OS module. OS module allows for file searching and editing.
import subprocess           #imports subprocess module. Subprocess module allows for external executables (like the Exiftool) to be run.


def convert(): 
    #The convert function completes two objectives.
        #(1) ask the user to imput a file path to the files that will be edited.
        #(2) allow the user to convert .bmp files to .jpg files so that files can be modified in the Exiftool.
    loop = 1   
    # Makes sure a valid file path is entered.
    while loop == 1:
        file_directory = input("Where are the files you want to work with? Enter file directory: ")
        if os.path.exists(file_directory):
            print(f"The file path '{file_directory} exists. Navigating now.","\n")
            loop = 0
        else:
            print(f"The file path '{file_directory} does not exist. Please enter a valid file path.")
    
    loop1 = 0  
    # Makes sure user input is YES or NO
    while loop1 ==0:
        convert =input("The Exif Tool is not compatible with .bmp files. Do you need to convert .bmp to .jpg? (YES or NO ): ")
        if convert == "YES":
            #converts bmp to jpg and runs the Elif_Tool_overview funtion.
            bmp_to_jpg(file_directory)
            Elif_Tool_overview(file_directory)
            loop1 =1
            print()
        elif convert == "NO":
            # does not #converts bmp to jpg but runs the Elif_Tool_overview funtion.
            Elif_Tool_overview(file_directory)
            loop1 =1
            print()
        else:
            print("Input needs to be YES or NO")
            loop1 =0
            #loops back to top of the funtion if an invalid input is entered.
            print()
            
    


def Elif_Tool_overview(file_directory):
    #The Elif_Tool_overview function allow the user to choose the metadata modifications they want to perform
    # User can change the file name based on an associated txt document, add a metadata comment or both.
    loop2 = 1
    #Handles invalid user input
    while loop2 == 1:
        selection = input("What do you want to do? 1 = change file name 2 = add metadata comment 3 = both: ")
        if selection == "1":
            change_name(file_directory)
            #calls the change_name function based on user input
            loop2 = 0
        elif selection == "2":
            add_metadata(file_directory)
            #calls the add_metatdata function based on user input
            loop2 = 0
        elif selection == "3":
            change_name(file_directory)
            add_metadata(file_directory)
            # calls the change_name function and then the add_metadata function based on user input
            loop2 = 0
        else:
            print("Input needs to be 1, 2, or 3. Try again")
            loop2 = 1
            #loops back to top of the funtion if an invalid input is entered.

def bmp_to_jpg(file_directory):
    # converts .bmp files to .jpg
    from PIL import Image
    #imports PIL library
    input_directory = file_directory
    output_directory = file_directory

    file_list = os.listdir(input_directory)

    for file_name in file_list:
        if file_name.lower().endswith('.bmp'):
            input_file_path = os.path.join(input_directory, file_name)
            output_file_name = os.path.splitext(file_name)[0] + '.jpg'
            output_file_path = os.path.join(output_directory, output_file_name)
            #finds all bmp files and creates an output file path that uses the bmp name but chages the file type to jpg

            with Image.open(input_file_path) as img:
                img.save(output_file_path, 'JPEG')
            #convets .bmp to .jpg
    print("conversion succesful", "\n")

def change_name(file_directory ):
    files = os.listdir(file_directory)
    print("\n", "List of files in the directory:","\n", files, "\n")
    #lists files in given file path
    txt_files = [file for file in files if file.endswith(".txt")]
    #extracts txt files from list
    print("List of.txt files:","\n", txt_files,"\n")
    if txt_files:
        first_txt_file =txt_files[0]
        with open(os.path.join(file_directory, first_txt_file), 'r') as txt_file:
                first_line = txt_file.readline().strip()
        first_line = first_line.replace('"','')
        first_line = first_line.replace(',','')
        first_line = first_line.replace('_','')
        first_line = first_line.replace(' ','_')
        print("First line of the .txt file:","\n", first_line,"\n")
    # Pull first line of .txt and assign it to a variable
    jpg_files = [file for file in files if file.endswith(".jpg")]
    print("List of .jpg files:","\n", jpg_files,"\n")
    # Takes all .jpg from  the file directory and adds them to a list.
    for jpg_file in jpg_files:
        base_name, extension = os.path.splitext(jpg_file)
        new_name = first_line + base_name + extension
        print(jpg_file, "renamed to", new_name, "\n")
        old_path = os.path.join(file_directory, jpg_file)
        new_path = os.path.join(file_directory, new_name)
    # Create new name field that combines first_Line of .txt and name of .jpg
        os.rename(old_path, new_path)
    #renames .jpg
    

    
def add_metadata(file_directory):
    # adds comment field to metadata of .jpgs using the exiftool
    #exifTool = r"/Users/dvitale/exiftool.exe"
    loop3 = 0
    #handles invalid user input
    while loop3 ==0:
        exifTool = input("Enter the path to your exiftool: ")
    # has user input the file path to their Exiftool.exe. Example: C:\Users\dvitale\exiftool.exe
        if os.path.exists(exifTool):
            print("Valid file path entered.")
            loop3 = 1
        else:
            print("invalid file path entered")
    def add_comment_to_jpg(file_directory, comment):
    #uses Exiftool to add comment to metadata
        command = [exifTool, "-comment="+comment, file_directory]
        subprocess.run(command)

    for filename in os.listdir(file_directory):
    # Allows user to pick comment from a list of preset comments or create their own.
    #iterates through all .jpg files in the previously definced file path.
        if filename.lower().endswith(".jpg"):
            file_path = os.path.join(file_directory, filename)
            preset_1 = "Plot of Horizontal to Vertical Spectral Ratio that plots frequency in Hertz on the x-axis and amplitude (a dimensionless value) on the y-axis.  The resonance frequency is indicated at the top of the plot."
            preset_2 = "Single component spectra plot frequency in Hertz are shown on the x axis and acceleration in mm/s per Hertz are plotted on the y-axis.   The north-south component is green; the east-west component is blue; and up-down (vertical) is pink."
            print(f"\n","Choose a preset comment to add to your image or enter a new comment","\n","1 =", preset_1,"\n","2 =", preset_2, "\n","3= input your own comment: ", "\n" )
            choose_comment =input(f"What comment to you want to add to {filename}? Choose 1,2, or 3 from the above text: ")
            print()

            if choose_comment == '1':
                comment = preset_1
            elif choose_comment == '2':
                comment = preset_2
            elif choose_comment =='3':
                comment = input(f"What comment to you want to add to {filename} ")
                
            
            add_comment_to_jpg(file_path, comment)
            print(f"comment added to {file_path}: {comment}")

convert()


# learn how to export code so others can use it
# Create visual workflow





