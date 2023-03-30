import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class DownloadHandler(FileSystemEventHandler):
    def __init__(self):
        self.events = []

    def on_created(self, event):
        if not event.is_directory and "Downloads" in event.src_path:
            self.events.append({"type": "created", "path": event.src_path, "time": time.time()})

    def on_modified(self, event):
        if not event.is_directory and "Downloads" in event.src_path:
            self.events.append({"type": "modified", "path": event.src_path, "time": time.time()})

    def on_deleted(self, event):
        if not event.is_directory and "Downloads" in event.src_path:
            self.events.append({"type": "deleted", "path": event.src_path, "time": time.time()})

    def on_moved(self, event):
        if not event.is_directory and "Downloads" in event.src_path:
            self.events.append({"type": "moved", "src_path": event.src_path, "dest_path": event.dest_path, "time": time.time()})

if __name__ == "__main__":
    download_path = os.path.expanduser("~") + "/Downloads"
    event_handler = DownloadHandler()
    observer = Observer()
    observer.schedule(event_handler, download_path, recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(5)
            if event_handler.events:
                print("Eventos:")
                for event in event_handler.events:
                    print(f"{event['type']} - {event['path']} - {time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(event['time']))}")
                event_handler.events = []
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
import keyboard

def on_key_press(event):
    if event.name == 'e':
        print("A tecla 'E' foi pressionada!")

if __name__ == '__main__':
    keyboard.on_press(on_key_press)
    keyboard.wait()
