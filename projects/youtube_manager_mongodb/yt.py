from pymongo import MongoClient
from bson import ObjectId
client = MongoClient('mongodb+srv://youtubepy:youtubepy@webdev.asdepyf.mongodb.net/', tlsAllowInvalidCertificates = True)
db = client["youtubepy"]
videos_collection = db["videos"]

def list_videos():
    for vid in videos_collection.find():
        print(f"ID: {vid['_id']}, name: {vid['name']}, time: {vid['time']} ")

def add_videos(name, time):
    videos_collection.insert_one({'name': name, 'time': time})

def update_videos(video_id, new_name, new_time):
    videos_collection.update_one({'_id': ObjectId(video_id)}, {"$set": {'name': new_name, 'time': new_time}})
     

def del_videos(video_id):
    videos_collection.delete_one({'_id': ObjectId(video_id)})
    


def main():
    while True:
        print("Youtube manager via mongodb")
        print("1. list videos")
        print("2. add videos")
        print("3. update videos")
        print("4. del videos")
        print("5. Exit")
        choice = input("Enter the choice: ")

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input("Enter the new video name: ")
            time = input("Enter the new video duration: ")
            add_videos(name, time)
        elif choice == '3':
            video_id = input('Enter the video index to be updated: ')
            name = input("Enter the new video name: ")
            time = input("Enter the new video duration: ")
            update_videos(video_id, name, time)
        elif choice == '4':
            video_id = input('Enter the video index to be deleted: ')
            del_videos(video_id)
        elif choice == '5':
            break
        else:
            print('Invalid choice')

if __name__ == "__main__":
    main()