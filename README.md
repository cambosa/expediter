### Features
- Quickly organize an evaluator's notes into the appropriate "Eval Worksheet Area Grade" categories within Patriot Excalibur, a unit-level software automation tool that coordinates Qualification/Continuation training.
- Automatic copy and paste functionality
- Adaptive SimpleHTTPServer
- Integration with a free, open source pastebin for quick access to notes
  (For more information on psty.io, visit https://github.com/psty-io/psty-api)

### Getting Started
First, clone this github repository:
```
git clone https://github.com/cambosa/expediter
```

Then, you will need to install the Python modules required:
```
pip install -r requirements.txt
```
Install the appropriate WebDriver to communicate with Mozilla Firefox.
The Windows and Linux .zip files containing geckodriver v0.29.0 are included in this repo.

You can find the latest Gecko browser web driver releases at https://github.com/mozilla/geckodriver/releases

### Usage   
Verify this script is placed in the same directory where your notes are located.

Run the command:
```
python3 expediter.py
```
