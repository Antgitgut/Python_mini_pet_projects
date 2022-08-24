"""

The program works if you have Pyhon version 3.10 or higher.

"""

print("Put all '.webp' files in a separate empty folder before enter a link to that folder.\n")

import os
import sys


def reformat(link_address):
    for filename in os.listdir(link_address):                                       # List all fiels in the directory from the provided link.
        old_filename = os.path.join(link_address,filename)                          # Joined file path & names to avoid "FileNotFoundError: [WinError 2]" error.
        if ".webp" in filename:
            new_filename = old_filename.replace(".webp", ".jpg")
            os.rename(old_filename, new_filename)                                   # By this string, the system rename old files & old extension with new ones. Didn't use 'os.replace' to avoid file corruption.
                               
        else:
            print("This directory has no files with the extension '.webp'")         # This print + input leaves 1 message when there are no files with '.webp' extension.
            input()
            
    print("Your files with the extension '.webp' were successfuly converted")       # This print + input leaves 1 message when the files with '.webp' extension were successfuly converted.
    input()
    

    


inp = input('Enter the link to files: ')
reformat(inp)






