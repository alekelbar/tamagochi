# How to install this project...

- python3 required
- package required for this project

  `pip install SpeechRecognition`

  `pip install pyttsx3`

  `pip install pyaudio`

  `pip install flask`

  `pip install flask-socketio`

  `pip install simple-websocket`

## Common problems with this installation

some linux distributions has problems with this, if you watch something like this:

```
      Traceback (most recent call last):

  File "/home/alekelbar/.local/lib/python3.10/site-packages/pyttsx3/**init**.py", line 20, in init
  eng = \_activeEngines[driverName]
  File "/usr/lib/python3.10/weakref.py", line 137, in **getitem**
  o = self.data[key]()
  KeyError: None

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
File "/home/alekelbar/projects/tamagochi-main/main.py", line 7, in <module>
engine = pyttsx3.init()
File "/home/alekelbar/.local/lib/python3.10/site-packages/pyttsx3/**init**.py", line 22, in init
eng = Engine(driverName, debug)
File "/home/alekelbar/.local/lib/python3.10/site-packages/pyttsx3/engine.py", line 30, in **init**
self.proxy = driver.DriverProxy(weakref.proxy(self), driverName, debug)
File "/home/alekelbar/.local/lib/python3.10/site-packages/pyttsx3/driver.py", line 50, in **init**
self.\_module = importlib.import_module(name)
File "/usr/lib/python3.10/importlib/**init**.py", line 126, in import_module
return \_bootstrap.\_gcd_import(name[level:], package, level)
File "<frozen importlib._bootstrap>", line 1050, in \_gcd_import
File "<frozen importlib._bootstrap>", line 1027, in \_find_and_load
File "<frozen importlib._bootstrap>", line 1006, in \_find_and_load_unlocked
File "<frozen importlib._bootstrap>", line 688, in \_load_unlocked
File "<frozen importlib._bootstrap_external>", line 883, in exec_module
File "<frozen importlib._bootstrap>", line 241, in \_call_with_frames_removed
File "/home/alekelbar/.local/lib/python3.10/site-packages/pyttsx3/drivers/espeak.py", line 9, in <module>
from . import \_espeak, toUtf8, fromUtf8
File "/home/alekelbar/.local/lib/python3.10/site-packages/pyttsx3/drivers/\_espeak.py", line 18, in <module>
dll = cdll.LoadLibrary('libespeak.so.1')
File "/usr/lib/python3.10/ctypes/**init**.py", line 452, in LoadLibrary
return self.\_dlltype(name)
File "/usr/lib/python3.10/ctypes/**init**.py", line 374, in **init**
self.\_handle = \_dlopen(self.\_name, mode)
OSError: libespeak.so.1: cannot open shared object file: No such file or directory
```

Please, try with the following command line:

```
sudo apt-get update
sudo apt-get install espeak
```

Do not remenber to install pyaudio library
`pip install pyaudio`

if you get an error like this:

```
pip install pyaudio

  Defaulting to user installation because normal site-packages is not writeable
  Collecting pyaudio
  Using cached PyAudio-0.2.13.tar.gz (46 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Preparing metadata (pyproject.toml) ... done
  Building wheels for collected packages: pyaudio
  Building wheel for pyaudio (pyproject.toml) ... error
  error: subprocess-exited-with-error

  × Building wheel for pyaudio (pyproject.toml) did not run successfully.
  │ exit code: 1
  ╰─> [17 lines of output]
  running bdist_wheel
  running build
  running build_py
  creating build
  creating build/lib.linux-x86_64-3.10
  creating build/lib.linux-x86_64-3.10/pyaudio
  copying src/pyaudio/**init**.py -> build/lib.linux-x86_64-3.10/pyaudio
  running build_ext
  creating build/temp.linux-x86_64-3.10
  creating build/temp.linux-x86_64-3.10/src
  creating build/temp.linux-x86_64-3.10/src/pyaudio
  x86_64-linux-gnu-gcc -Wno-unused-result -Wsign-compare -DNDEBUG -g -fwrapv -O2 -Wall -g -fstack-protector-strong -Wformat -Werror=format-security -g -fwrapv -O2 -fPIC -I/usr/local/include -I/usr/include -I/usr/include/python3.10 -c src/pyaudio/device_api.c -o build/temp.linux-x86_64-3.10/src/pyaudio/device_api.o
  src/pyaudio/device_api.c:9:10: fatal error: portaudio.h: No such file or directory
  9 | #include "portaudio.h"
  | ^~~~~~~~~~~~~
  compilation terminated.
  error: command '/usr/bin/x86_64-linux-gnu-gcc' failed with exit code 1
  [end of output]

  note: This error originates from a subprocess, and is likely not a problem with pip.
  ERROR: Failed building wheel for pyaudio
  Failed to build pyaudio
  ERROR: Could not build wheels for pyaudio, which is required to install pyproject.toml-based projects

```

try with this: `sudo apt-get install portaudio19-dev`
