# file = open('file.py', 'w')
# print(file)
# try:
#     file.write('hello from sai')
# finally:
#     file.close()
import json
def load_video():
    try:
        with open('youtube.txt', 'r') as file:
            test = json.load(file)
            return test
    except FileNotFoundError:
        return []
    

def save_video(video):
    with open('youtube.txt', 'w') as file:
        return json.dump(video, file)


def list_all_videos(video):
    print('\n')
    print("*" * 50)
    for index, vid in enumerate(video, start= 1):
        print(f"{index}. {vid['name']}, 'Duration': {vid['time']}")
    # print('\n')
    print("*" * 50)

def add_new_video(video):
    name = input('enter the video name: ')
    time = input('enter the video duration: ')
    video.append({'name':name, 'time':time})
    save_video(video)


def update_video(videos):
    pass
def del_video(videos):
    pass


def main():
    video = load_video()
    while True:
        print("Youtube Manager | choose an option")
        print("1. List all videos")
        print("2. Add a new video")
        print("3. Update a video")
        print("4. del a video")
        choice = input('enter the choice: ')

        match choice:
            case '1':
                list_all_videos(video)
            case '2':
                add_new_video(video)
            case '3':
                update_video(video)
            case '4':
                del_video(video)

        
if __name__ == "__main__":
    main()