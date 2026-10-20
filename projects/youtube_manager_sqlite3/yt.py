import sqlite3

conn = sqlite3.connect("youtube.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos(
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                time TEXT NOT NULL
    )
''')

def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_videos(name, time):
    # cursor.execute("SELECT FROM videos WHERE name = ?, time = ?", (name, time))
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()


def update_videos(video_id, name, time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (name, time, video_id))
    conn.commit()
def del_videos(video_id):
    cursor.execute("DELETE FROM videos WHERE id = ?", (video_id))
    conn.commit()

def main():
    while True:
        print('\n youtube manager with DB')
        print('1. list videos')
        print('2. add videos')
        print('3. update videos')
        print('4. del videos')
        print('5. Exit')
        choice = input('Enter the choice: ')

        if choice == '1':
            list_videos()
        elif choice == '2':
            name = input('enter the video name: ')
            time = input('enter the video duration: ')
            add_videos(name, time)

        elif choice == '3':
            video_id = input('enter the video to be updated: ')
            name = input('enter the video name: ')
            time = input('enter the video duration: ')
            update_videos(video_id, name, time)

        elif choice == '4':
            video_id = input('enter the video to be updated: ')
            del_videos(video_id)
        elif choice == '5':
            break
        else:
            print('Invalid index')

if __name__ == "__main__":
    main()