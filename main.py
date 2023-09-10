from pmk import PMK
from pmk.platform.rgbkeypadbase import RGBKeypadBase as Hardware
import usb_midi
import adafruit_midi
from adafruit_midi.note_off import NoteOff
from adafruit_midi.note_on import NoteOn
import time
import random

keypico = PMK(Hardware())
keys = keypico.keys

midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[1], 
                          out_channel=0)

# Colour selection
snow = (0, 0, 0)
blue = (0, 0, 255)
cyan = 0
red = (255, 0, 0)
green = (0, 255, 0)
purple = (255, 0, 255)
orange = (255, 100, 0)
white = (255, 255, 255)

# Set key colours for all keys
keypico.set_all(*snow)

# Orientation
# keypico.set_led(0, *red)
# keypico.set_led(3, *green)
# keypico.set_led(12, *blue)
# keypico.set_led(15, *purple)

# Set sleep time
keypico.led_sleep_enabled = True
keypico.led_sleep_time = 10

# Midi
spawn = 0
start_note = 68
velocity = 127

# preset keys 

for key in keys:
    @keypico.on_press(key)
    def press_handler(key):
        if key.number == 0 or key.number == 4 or key.number == 8 or key.number == 12:
            print("Key {} pressed".format(key.number))
            key.set_led(*orange)
            note = start_note + key.number
            midi.send(NoteOn(note, velocity))

    @keypico.on_release(key)
    def release_handler(key):
        if key.number == 0 or key.number == 4 or key.number == 8 or key.number == 12:
            print("Key {} released".format(key.number))
            key.set_led(*snow)
            note = start_note + key.number
            midi.send(NoteOff(note, 0))

    @keypico.on_hold(key)
    def hold_handler(key):
        if key.number == 0 or key.number == 4 or key.number == 8 or key.number == 12:
            print("Key {} held".format(key.number))
            key.set_led(*purple)

    keypico.update()







# Loop


for key in keys:
    spawn = random.randint(1,4)
    if spawn == 1:
        spawn = 3
        keypico.set_led(3, *red)
    elif spawn == 2:
        spawn = 7
        keypico.set_led(7, *red)        
    elif spawn == 3:
        spawn = 11
        keypico.set_led(11, *red)
    else:
        spawn = 15
        keypico.set_led(15, *red)
    for x in range(30):
        @keypico.on_press(key)
        def press_handler(key):
            if key.number == 0 or key.number == 4 or key.number == 8 or key.number == 12:
                print("Key {} pressed".format(key.number))
                if (key.number + 3) == spawn:
                    key.set_led(*orange)
                    note = start_note + key.number
                    midi.send(NoteOn(75, 127))

        @keypico.on_hold(key)
        def hold_handler(key):
            if key.number == 0 or key.number == 4 or key.number == 8 or key.number == 12:
                print("Key {} held".format(key.number))
                key.set_led(*purple)
        keypico.update()  

    keypico.set_led(spawn, *snow)
    keypico.set_led((int(spawn)-1), *red)

    for x in range(30):
        @keypico.on_press(key)
        def press_handler(key):
            if key.number == 0 or key.number == 4 or key.number == 8 or key.number == 12:
                print("Key {} pressed".format(key.number))
                if (key.number + 3) == spawn:
                    key.set_led(*orange)
                    note = start_note + key.number
                    midi.send(NoteOn(75, 127))

        @keypico.on_hold(key)
        def hold_handler(key):
            if key.number == 0 or key.number == 4 or key.number == 8 or key.number == 12:
                print("Key {} held".format(key.number))
                key.set_led(*purple)
        keypico.update()




    keypico.set_led((int(spawn)-1), *snow)
    keypico.set_led((int(spawn)-2), *red)


    for x in range(30):
        @keypico.on_press(key)
        def press_handler(key):
            if key.number == 0 or key.number == 4 or key.number == 8 or key.number == 12:
                print("Key {} pressed".format(key.number))
                if (key.number + 3) == spawn:
                    key.set_led(*orange)
                    note = start_note + key.number
                    midi.send(NoteOn(75, 127))

        @keypico.on_hold(key)
        def hold_handler(key):
            if key.number == 0 or key.number == 4 or key.number == 8 or key.number == 12:
                print("Key {} held".format(key.number))
                key.set_led(*purple)
        keypico.update()


    keypico.set_led((int(spawn)-2), *snow)

keypico.set_all(*snow)