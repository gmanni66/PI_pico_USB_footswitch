# PI_pico_USB_footswitch
Rasbberry PI Pico USB midi footswitch 

a simple foot switch for sending midi ControlChange to Midi enabled Apps

It uses 8 switches and 8 LED
simple send ControlChanges to whatever value is specified in the code
it will Turn ON the LED if the ControlChange is set from 64 to 127 which is the ON value
it will turn Off the LED if the value is from 0 to 63 

The MIDI value or channel canbe customized but it will work with any app that can receive MIDI input from a USB source 

I've used it with Raspberry PI MODEP and with Tonelib GFX on PC 

Hope someone finds it usefull 

The code is ery rudimental and needs of cleaning up 
I'm sure there is a better way to do just the same but is the only way I could make it work 
anyone care to improve it please go ahead and thank you in advance :) 
