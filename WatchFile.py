import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import ntpath
import shutil
import time
import os

from ImageReader import ImageReader
from FileMove    import MovementOpr
from OpenAIApi   import OpenAIAPI

# create event handler object
if __name__ == "__main__":
    patterns = "*"
    ignore_patterns = ""
    fileName = ""
    text = ""
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
    ir = ImageReader()
    fm = MovementOpr()
    api = OpenAIAPI()

    # create our functions to alert when something happens
    def on_created(event):
        print(f"created f'{event.src_path}'")
        time.sleep(5)
        fileFullPath = f'{event.src_path}'
        if os.path.exists(fileFullPath):
            fileName = ntpath.basename(fileFullPath)
            print(f"Image {fileName} has been found. Reading now...")
            text = ir.extract_text(fileFullPath, 'eng')
            #print("output image extract " + text)
            reqDone = False
            if text != "" or text != False:
                text = text.strip()
                print(text)
                #print("Asif")
                reqDone = True
                resp = api.getApiResp(text)
                print(resp)
            
            if reqDone:
                fm.move_file('G:\Learning\Python\Workspace\ScrumAnswers\Images',
                             'G:\Learning\Python\Workspace\ScrumAnswers\Done', 
                             fileName)

    def on_deleted(event):
        print(f"Removed {event.src_path}")

    def on_modified(event):
        print(f"modified f'{event.src_path}'")
        """time.sleep(5)
        fileFullPath = f'{event.src_path}'
        fileName = ntpath.basename(fileFullPath)
        #newFile = f"G:\\Learning\\Python\\Workspace\\ScrumAnswers\\WIP\\" + fileName
        #shutil.move(fileFullPath, newFile)
        print(f"Image {fileName} has been found. Reading now...")
        text = ir.extract_text(fileFullPath, 'eng')
        text = text.strip()
        print(text)
        #print("Asif")
        reqDone = False
        if text != "" or text != False:
            reqDone = True
            resp = api.getApiResp(text)
            print(resp)
        
        if reqDone:
            fm.move_file('G:\Learning\Python\Workspace\ScrumAnswers\Images',
                         'G:\Learning\Python\Workspace\ScrumAnswers\Done', 
                         fileName)"""

    def on_moved(event):
        print(f"The document {event.src_path} has been moved to the location: {event.dest_path}")

# call functions 
    my_event_handler.on_created = on_created
    my_event_handler.on_deleted = on_deleted
    my_event_handler.on_modified = on_modified
    my_event_handler.on_moved = on_moved

    # set up the 'observer' to watch  
    # Set the variable "path" the path to monitor  
    path = r"G:\Learning\Python\Workspace\ScrumAnswers\Images"
    go_recursively = True
    my_observer = Observer()
    my_observer.schedule(my_event_handler, path, recursive=go_recursively)

    # start the observer
    my_observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        my_observer.stop()
        my_observer.join()
        