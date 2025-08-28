# Python Keylogger — Educational Project

A minimal keylogger written in Python for **educational and research** purposes.
It demonstrates how global key events can be captured and logged locally.

> ⚠️ **Ethics & Disclaimer**  
> This project is for learning and defensive security research only.  
> Do **not** use it on any system you don’t own or lack explicit permission to test.

## Features
- Logs keystrokes with timestamps
- Stops safely when `ESC` is pressed
- Saves to `keystrokes.log` (ignored by git)

## How it works (high level)
- Uses the `keyboard` library to hook global key events
- Appends events with a timestamp to a local log file

## Setup (Linux)
```bash
python3 -m venv ~/keylogger_env
source ~/keylogger_env/bin/activate
pip install -r requirements.txt
