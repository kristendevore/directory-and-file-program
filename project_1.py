### Cheyenne Chavez 92973249 and Kristen DeVore 76958230 Project 1 Section 10

from pathlib import Path
import os
import shutil

###RUNNING THE PROGRAM###
            
def user_interface():
    '''Runs program'''
    while True:
        inPut = input()
        user_input_one = Path(inPut)
        
        if user_input_one.is_dir() == True:
            break
        else:
            print("ERROR")

    while True:  
        user_input_two = str(input()) #Valid inputs would be: [N, E, S]
        split_input_two = user_input_two.split()
        essential_second_input = " ".join(split_input_two[1:])
        "".join(essential_second_input[-1:-4])

#Second User Input#

        if split_input_two[0] == "N":
            search_for_name_of_file(user_input_one, essential_second_input)
            files_list = search_for_name_of_file(user_input_one, essential_second_input)
            break

        elif split_input_two[0] == "E":
            search_for_extension(user_input_one, essential_second_input)
            files_list = search_for_extension(user_input_one, essential_second_input)
            break
        
        elif split_input_two[0] == "S":
            try:
                search_by_file_size(user_input_one, int(essential_second_input))
                files_list = search_by_file_size(user_input_one, int(essential_second_input))
                break
            except:
                print("ERROR")

#Third User Input#

    while True:
        user_input_three = str(input()) #Valid inputs would be: [P, F, D, T]
        
        if user_input_three == "P":
            print_path_file(files_list)
            break
        
        elif user_input_three == "F":
            read_first_line_of_file(files_list)
            break
        
        elif user_input_three == "D":
            duplicate_file(files_list)
            break
        
        elif user_input_three == "T":
            touch_file(files_list)
            break
        
        else:
            print("ERROR")     

###Functions###

def search_for_name_of_file(path_input: Path, name_search: str):
    '''N function: allows the user to search for specific file names'''
    name_list = []
    for element in path_input.iterdir():
        if element.is_dir():
            name_list.extend(search_for_name_of_file(element, name_search))
        elif element.is_file():
            if element.name == name_search:
                name_list.append(element)
    return name_list
                             

def search_for_extension(path_input: Path, ext_input: str):
    '''E function: allows the user to search for files by extension only'''
    ext_list = []
    for element in path_input.iterdir():
            if element.is_dir():
                ext_list.extend(search_for_extension(element, ext_input))
            elif element.is_file():
                if element.suffix == ext_input:
                    ext_list.append(element)
                elif element.suffix[1:] == ext_input:
                    ext_list.append(element)
    return ext_list

def search_by_file_size(path_input: Path, size_input: int) -> None:
    '''S function: allows the user to search for files based on size (in bytes)
    that is greater than the input given by the user'''
    files_over_size_input = []
    for element in path_input.iterdir():
        if element.is_dir():
                files_over_size_input.extend(search_by_file_size(element, size_input))
        elif element.is_file():
            if element.stat().st_size > size_input:
                files_over_size_input.append(element)
    return files_over_size_input

def print_path_file(files: list) -> str:
    '''P function: allows user to print directory path of the file chosen in
    previous input answer'''
    for file in files:
        print(file)

def read_first_line_of_file(files: list) -> str:
    '''F function: allows user to print and read first line of the file chosen
    in previous input answer'''
    for file in files:
        print(file)
        f = open(file, 'r')
        print(f.readline())
        

def duplicate_file(files: list) -> None:
    '''D function: allows user to duplicate file, chosen in second input,
    and adds ".dup" to the end of the copy'''
    for file in files:
        shutil.copyfile(str(file), str(file) + ".dup")
    
    
def touch_file(files: list)-> None:
    '''T function: "touches" file and updates time stamp'''
    for file in files:
        file.touch()
            
if __name__ == "__main__":
    user_interface()
