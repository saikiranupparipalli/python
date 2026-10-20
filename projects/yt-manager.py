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


def update_video(video):
    list_all_videos(video)
    index = int(input('enter the index to be updated: '))
    name = input("enter the new video name: ")
    time = input("enter the new video duration: ")
    video[index -1 ] = {'name': name, 'time': time}
    save_video(video)


def del_video(video):
    list_all_videos(video)
    index = int(input('enter the index to be deleted: '))
    del video[index -1 ]
    save_video(video)

def main():
    videos = load_video()
    while True:
        print("Youtube Manager | choose an option")
        print("1. List all videos")
        print("2. Add a new video")
        print("3. Update a video")
        print("4. del a video")
        choice = input('enter the choice: ')

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_new_video(videos)
            case '3':
                update_video(videos)
            case '4':
                del_video(videos)
            case '5':
                break
            case _:
                print('invalid index ')
            

        
if __name__ == "__main__":
    main()
    #  index = int(input("enter the index to update: "))
    #  name = input("enter the new video name")
    #  time = input("enter the new video duration")
    #  for vid in index-1:
    #     video.append({'name': name}, {'time': time})
    #     save_video(video)
    #     print('New video info updated successfully.')