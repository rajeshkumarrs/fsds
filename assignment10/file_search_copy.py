import os,shutil

base_path= "../../python"
source_folder_name='source_folder'
target_folder_name='target_folder'

def search_move_files(source,target,file_extension):
    for root,dirs,files in os.walk(source):
        for file in files:
            if file.endswith('.'+file_extension):
                source_file = os.path.join(root,file)
                shutil.copy(source_file,target)

source_path = os.path.join(base_path,source_folder_name)
target_path = os.path.join(base_path,target_folder_name)

search_move_files(source_path,target_path,"jpg")