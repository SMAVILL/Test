# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 11:54:33 2024

@author: SMAVILL
"""
import os
from datetime import datetime
import shutil
import calendar
import re

folder_path_input=r"D:\Hema"

folder_path_output=r"D:\Hemaphone\photo"


def extract_dates_from_filenames(folder_path,filetype):
    #filetype="ram"
    try:
       for dir1, subdir, files  in os.walk(folder_path):
           for filename in files:
               if(filetype in filename or filetype.lower() in filename):
                 
                  if(filename.startswith("IMG-")):
                      creation_year = filename[4:8]
                      month_number = filename[8:10] 
                      creation_mon = str(calendar.month_abbr[int(month_number)]).upper()
                      
                  elif(filename.startswith("IMG_")):
                      creation_year = filename[4:8]
                      month_number = filename[8:10] 
                      creation_mon = str(calendar.month_abbr[int(month_number)]).upper()    
                      
                  elif(filename.startswith("IMG")):
                      creation_year = filename[3:7]
                      month_number = filename[7:9]
                      creation_mon = str(calendar.month_abbr[int(month_number)]).upper()
                  else:
                      pattern = r'^\d{4}(0[1-9]|1[0-2])([0-2][0-9]|3[0-1])'
                      match = re.match(pattern, filename)
                      if match:
                        #filename=filename.trim()
                        creation_year = filename[:4]
                        month_number = filename[4:6]
                        creation_mon = str(calendar.month_abbr[int(month_number)]).upper()
                      else:
                        month_number ="_"
                        creation_year="others"
                        creation_mon="ok"
                        print("No match")
                    
                  
                  
                  
                  creation_mon=month_number+"_"+creation_mon
                  file_path=os.path.join(dir1,filename)
                  
                 
                  
                  print(creation_mon,creation_year)
                  print(file_path)
                  destination_folder=os.path.join(folder_path_output,creation_year,creation_mon)
                  destination_file=os.path.join(destination_folder,filename)
                  
                  if not (os.path.isdir(destination_folder)):
                          os.makedirs(destination_folder)
                          
                  if not os.path.exists(destination_file):        
                     shutil.move(file_path,destination_folder)        
                  else:
                     os.remove(file_path)
                     
                     
               elif(".mp4" in filename):
                    src_file=os.path.join(dir1,filename)
                    
                    destination =os.path.join(folder_path_output,"Videos")
                    
                    if not (os.path.isdir(destination)):
                            os.makedirs(destination)
                    
                    destination_file=os.path.join(destination,filename)
                    
                    
                    if not os.path.exists(destination_file):        
                       shutil.move(src_file,destination) 
                       print("COPIED FILE",destination + "\\" + filename)
                    else:
                       os.remove(src_file)
                       print("REMOVED FILE",destination + "\\" + filename)
                    
                    
                    
                    
    except Exception as e:
            print(os.path.join(dir1,filename))
            print(f"Error extracting dates from filenames: {e}")
       


if __name__ == "__main__":
    #extract_dates_from_filenames(folder_path_input,".JPG")
    filetype=".JPG"
    for dir1, subdir, files  in os.walk(folder_path_input):
        for file in files:
            if((filetype in file) or (filetype.lower() in file)):
                filename=file
                file_name=os.path.join(dir1,file)
                print(file_name)
                file_modified_time = os.path.getmtime(file_name)
                readable_time = datetime.fromtimestamp(file_modified_time).strftime('%Y-%m-%d %H:%M:%S')
                creation_year = readable_time[0:4]
                month_number = readable_time[5:7] 
                creation_mon = str(calendar.month_abbr[int(month_number)]).upper()
                print(creation_mon,creation_year)
                print(readable_time)
                
                creation_mon=month_number+"_"+creation_mon
                destination_folder=os.path.join(folder_path_output,creation_year,creation_mon)
                
                destination_file=os.path.join(destination_folder,filename)
                
                
        
                if not (os.path.isdir(destination_folder)):
                        os.makedirs(destination_folder)
                        
                if not os.path.exists(destination_file):        
                   shutil.move(file_name,destination_folder)        
                else:
                   os.remove(file_name)
                   print("REMOVED FILE",destination_folder + "\\" + file_name) 
                   
                   
                   
            elif(".mp4" in file):
                src_file=os.path.join(dir1,file)
                
                destination =os.path.join(folder_path_output,"Videos")
                
                if not (os.path.isdir(destination)):
                        os.makedirs(destination)
                
                destination_file=os.path.join(destination,file)
                
                
                if not os.path.exists(destination_file):        
                   shutil.move(src_file,destination) 
                   print("COPIED FILE",destination + "\\" + file)
                else:
                   os.remove(src_file)
                   print("REMOVED FILE",destination + "\\" + file) 
            
            else:
               print(file)
         
        
         
        
        
         
        
            
   
    print("done")
    
    
    
    