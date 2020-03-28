from pytube import YouTube

def main():
    while True:
        video = input("Enter link: ")
        try:
            yt = YouTube(video)
            stream = yt.streams.filter(file_extension='mp4', progressive=True).order_by("resolution").desc().first()
            print('Downloading...')
            stream.download()
            print("Done.")
        except:
            break

if __name__ == "__main__":
    main()