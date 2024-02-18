import os
import shutil


class MovementOpr:
    
    def __init__(self):
        pass
        
    def extract_files(self, inPath: str) -> str:
        fileNames = os.listdir(inPath)
        for fileName in fileNames:
            #print('File Name: ' + fileName)
            #print('Forlder Path: ' + os.path.abspath(os.path.join(dir, fileName)), sep='\n')
            allFiles += fileName
        return allFiles
    
    def move_file(self, inPath: str, OutPath: str, fileName: str):
        shutil.move( inPath + '/' + fileName, OutPath + '/' + fileName)
        