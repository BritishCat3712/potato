# Just Finger Mini

# Description
Just Finger Mini is a musical game inspired by Just Dance.
<br>This game is meant to be played on a Pico RGB Keypad.

# Navigator
1. [Requirements](https://github.com/BritishCat3712/potato#requirements)
2. [Setup](https://github.com/BritishCat3712/potato#setup)
<br>   2.1 [Hardware](https://github.com/BritishCat3712/potato#hardware)
<br>   2.2 [CircuitPython](https://github.com/BritishCat3712/potato#circuitpython)
<br>   2.3 [CircuitPython Libraries](https://github.com/BritishCat3712/potato#circuitpython-libraries)
<br>   2.4 [Pimoroni Libraries](https://github.com/BritishCat3712/potato#pimoroni-libraries)
<br>   2.5 [Installing Libraries](https://github.com/BritishCat3712/potato#installing-libraries)
<br>   2.6 [Visual Studio](https://github.com/BritishCat3712/potato#visual-studio)
<br>   2.7 [Python Code](https://github.com/BritishCat3712/potato#python-code)
<br>   2.8 [LMMS](https://github.com/BritishCat3712/potato#lmms)
3. [The Game](https://github.com/BritishCat3712/potato#the-game)

# Requirements
1. Pico RGB Keypad
2. USB
3. PC
4. A brain

# Setup

## Hardware
Use the graphical guides printed on the Pimoroni RGB Keypad's PCB to align the Raspberry Pi Pico's pins to the board.
<br>Make sure the Raspberry Pi Pico's GPIO pins are firmly pushed into the keypad.
<br>Connect the keypad via USB to your computer.

## CircuitPython
Download the latest version of CircuitPython from for the Raspberry Pi Pico [here](https://circuitpython.org/board/raspberry_pi_pico/).
<br>Mount the Pico and drag and drop the downloaded UF2 file into the Pico. The Pico will restart and remount with the label CIRCUITPY.
<br>If this step doesn't work, hold down the BOOTSEL button on the Pico before plugging in the USB cable.

## CircuitPython Libraries
Open the [following site](https://circuitpython.org/libraries) and choose the CircuitPython Bundle appropriate for your system. In this instance, if CircuitPython 8.x is installed, select the bundle for Version 8.x. We will be using the `/lib/adafruit_midi` folder, and `/lib/adafruit_dotstar.mpy` driver. Documentation for both libraries can be found [here](https://docs.circuitpython.org/projects/midi/en/latest/) and [here](https://docs.circuitpython.org/projects/dotstar/en/latest/) respectively.

## Pimoroni Libraries
Next, download [the following git repository](https://github.com/pimoroni/pmk-circuitpython). We will be using the `/lib/pmk` folder. Documentation for this library is available in the README.md file.

## Installing Libraries
In the mounted Pico drive, select (or create if it's absent) a top level `lib` folder. Copy and paste the mentioned libraries into the `lib` folder.

## Visual Studio
Download [Visual Studio Code](https://code.visualstudio.com/download) and download extension python.

## Python Code
Create a python folder and paste the codes from the code tab into the python project

## LMMS
Last but not least, download [LMMS](https://lmms.io/). This is essential for the sound effects of the game.

# The Game
If you played Friday Night Funkin, this should look familiar to you. 16 blocks will drop and you have to press tile 8, 9, A and B to catch them. React fast as faster reaction time lead to longer music. Red blocks are those you need to catch. Yellow light will light up at where you press. Yellow will eventually turn purple if you press it for too long. Music will play to confirm you pressing. 
