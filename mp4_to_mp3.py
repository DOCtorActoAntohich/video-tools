import moviepy.editor as mp
import os


class Mode:
    """Enumeration of modes in which the program can work."""
    SINGLE = "SINGLE"
    FOLDER = "FOLDER"



def str_compare(first : str, second : str) -> bool:
    """Compares uppercase variants of given strings."""
    
    return first.upper() == second.upper()



def say_hello() -> None:
    """Prints messages to welcome the user."""
    
    messages = [
        "Welcome to MP4 -> MP3 converter!",
        "Choose mode:",
        f"'{Mode.SINGLE}' - Convert single file",
        f"'{Mode.FOLDER}' - Convert all video files in current folder. Program closes automatically."
    ]
    
    for message in messages:
        print(message)



def create_folder(folder : str) -> None:
    """Creates a folder for converted files.
    Has no effect if folder already exists.
    """
    
    try:
        os.mkdir(folder)
    except:
        ...



def convert_listed_files() -> None:
    """Converts files one by one as user inputs their names."""
    
    folder = "Converted audio\\"
    
    MP4 = ".mp4"
    MP3 = ".mp3"
    
    stop_string = "NULL"
    
    while True:
        print(f"Enter mp4-video file name (without format). Send '{stop_string.upper()}' to stop.")
        name = input()
        if str_compare(name, stop_string):
            break
        try:
            clip = mp.VideoFileClip(name + MP4)
            create_folder(folder)
            clip.audio.write_audiofile(folder + name + MP3)
        except:
            print("Something went wrong. Probably format is incorrect or file not found.")
        finally:
            print()



def convert_files_in_folder() -> None:
    """Converts every MP4 file to MP3 in current folder."""
    
    MP4 = ".mp4"
    MP3 = ".mp3"
    
    current_directory = os.getcwd() + "\\"
    videos = os.listdir(current_directory)
    videos = list(filter(lambda string: string.endswith(MP4), videos))
    
    folder = "Converted audio\\"
    
    fileNumber = 1
    for video in videos:
        try:
            print(f"Processing file {fileNumber}/{len(videos)}")
            clip = mp.VideoFileClip(video)
            create_folder(folder)
            file_name = video[:len(video) - len(MP4)] + MP3     # Replace only file format.
            clip.audio.write_audiofile(folder + file_name)
            fileNumber += 1
        except:
            print(f"Something went wrong with file '{video}'")
        finally:
            print()



def get_mode() -> str:
    """Returns the current mode read from console."""
    
    stop_string = "NULL"
    
    mode = ""
    while not (str_compare(mode, Mode.SINGLE) or str_compare(mode, Mode.FOLDER)):
        mode = input()
        if str_compare(mode, stop_string):
            break
    print()
    return mode



def main() -> None:
    say_hello();
    
    mode = get_mode()
    if str_compare(mode, Mode.SINGLE):
        convert_listed_files()
    elif str_compare(mode, Mode.FOLDER):
        convert_files_in_folder()    



if __name__ == "__main__":
    main()

