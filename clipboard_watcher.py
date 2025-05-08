import time
import pyperclip
import os

def watch_clipboard_and_save():
    last_text = ""
    log_file = "clipboard_log.txt"

    print("Watching clipboard...")
    try:
        while True:
            text = pyperclip.paste()
            if text != last_text and text.strip() != "":
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                entry = f"[{timestamp}] {text}\n"
                print(entry.strip())

                # Yeni Özelliğimiz! Artık bir .txt dosyasına kaydediyoruz.
                with open(log_file, "a", encoding="utf-8") as file:
                    file.write(entry)

                last_text = text
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopped.")

if __name__ == "__main__":
    watch_clipboard_and_save()