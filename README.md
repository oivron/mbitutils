# mbitutils (micro:bit Utilities)

A Python module for the 4tronix Bit:bot XL and stubs for the BBC micro:bit.

The intention is to use this package with the Visual Studio Code extension found at [https://github.com/oivron/microbit-extension-vscode](https://github.com/oivron/microbit-extension-vscode). This extension is also available from [Visual Studio Code Marketplace](https://marketplace.visualstudio.com/).

The stubs for micro:bit complements the following: [https://github.com/PhonicCanine/microbit](https://github.com/PhonicCanine/microbit).

## Installation
```pip install mbitutils```

## Usage
See [micro:bit Micropython API](https://microbit-micropython.readthedocs.io/en/latest/microbit_micropython_api.html) for a complete documentation/API on how to use the micro:bit.

### Import
```
from bitbot import *
from music import *
from speech import *
```

### Bit:bot XL API
```
bias(direction, percent)
# Set left/right bias to match motors.
# Direction: LEFT or RIGHT.
# Bias in %.
```

```
go(direction, speed)
# Move robot forwards or backwards at speed.
# Direction: FORWARD or REVERSE.
# Speed in %.
```

```
goms(direction, speed, duration)
# Move robot forwards or backwards at speed for milliseconds.
# Direction: FORWARD or REVERSE.
# Speed in %.
# Duration in milliseconds.
```

```
spin(direction, speed)
# Rotate robot in direction at speed.
# Direction: LEFT or RIGHT.
# Speed in %.
```

```
spinms(direction, speed, duration)
# Rotate robot in direction at speed for milliseconds.
# Direction: LEFT or RIGHT.
# Speed in %.
# Duration in milliseconds.
```

```
buzz(duration)
# Sound a buzz for milliseconds.
# Duration in milliseconds.
```

```
linesensor(direction)
# Read line sensor.
# Directon: LEFT or RIGHT.
```

```
stop()
# Stops the Bit:bot.
```
