import time
import pyperclip

def main():
    print("Watching clipboard...")
    recent_value = ""
    try:
        while True:
            tmp_value = pyperclip.paste()
            if tmp_value != recent_value and tmp_value.strip():
                recent_value = tmp_value
                print(f"\n[NEW COPY]: {recent_value}")
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\nStopped.")

if __name__ == "__main__":
    main()