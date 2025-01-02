import keyboard as kbd  # Importing keyboard module
import time
import threading
import random

# Define the string to type
string = """
lorem ipsum dolor sit amet consectetur adipiscing elit donec mollis dolor et euismod dictum enim mauris aliquam arcu at pretium justo mi ut lacus fusce leo risus dictum sed est ac auctor feugiat metus ut a tortor in nulla mattis dictum ut in ante aliquam erat volutpat in in ex ante aenean scelerisque risus ut neque dapibus a sollicitudin odio elementum donec a egestas ante nunc non laoreet nisi sed quis odio nec ipsum sagittis rutrum at ut augue pellentesque at dui iaculis malesuada lorem fringilla gravida orci in ut tincidunt nibh
"""

def random_enter_keypress():
    """Function to randomly press Enter every ~10 seconds"""
    while True:
        delay = 10 + random.uniform(-2, 2)
        time.sleep(delay)
        kbd.press_and_release('enter')  # Simulate Enter keypress
        print(f"[INFO] Pressed Enter after {delay:.2f} seconds")

# Main function
if __name__ == "__main__":
    # Start the Enter keypress logic in a separate thread
    enter_thread = threading.Thread(target=random_enter_keypress, daemon=True)
    enter_thread.start()

    print("Starting typing in 3 seconds...")
    time.sleep(3)  # Short delay to avoid unwanted actions
    print("Typing started. Press Ctrl+C to stop.")

    # Continuously type the string with a delay between characters
    try:
        while True:
            kbd.write(string, delay=2.5)
            print("[INFO] Finished typing the string, starting over...")
    except KeyboardInterrupt:
        print("\n[INFO] Program stopped by user.")
