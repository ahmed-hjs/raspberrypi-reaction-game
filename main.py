import time
import random
from lcd import LCD
import RPi.GPIO as GPIO


lcd = LCD(2, 0x27, True)
BUTTON_PIN = 17
GPIO.setmode(GPIO.BCM)


GPIO.setup(BUTTON_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
last_frame = time.time()
time_block = 0.7
cooldown = 0.2
last_button_press = 0

ph1 = '  Reaction Game'
ph2 = 'Press button to start'

ph2 = ph2 + "      "
ch1 = ph1[:16]
ch2 = ph2[:16]
ph1_cp = ph1[16:]
ph2_cp = ph2[16:]

while True:
    
    if GPIO.input(BUTTON_PIN) == GPIO.LOW and (time.time() - last_button_press) > cooldown :
            last_button_press = time.time()
            lcd.clear()
            break
            
    
    if (time.time() - last_frame) > time_block:
            last_frame = time.time() 
            
            lcd.message(ch1, 1)
            lcd.message(ch2, 2)

            ph2_cp = ph2_cp + ch2[0]
            ch2 = ch2[1:] + ph2_cp[0]
            ph2_cp = ph2_cp[1:]


time.sleep(1)
lcd.message("     Ready?", 1)
time.sleep(1)
lcd.message("    Let's go!", 2)
time.sleep(1)
lcd.clear()
lcd.message("        3", 2)
time.sleep(0.7)
lcd.clear()
lcd.message("        2", 2)
time.sleep(0.7)
lcd.clear()
lcd.message("        1", 2)
time.sleep(0.7)
lcd.clear()
lcd.message("       GO!", 2)
time.sleep(0.3)
lcd.clear()


    
start_time = time.time() +1
finish_time = start_time + 10 
print(start_time,finish_time)
time_to_guess = random.uniform(start_time,finish_time)
print(time_to_guess)

occ = 0
valid = False
while (finish_time > time.time()) :
    if time.time() >= time_to_guess and occ == 0:
        occ = 1
        lcd.message("     CLICK!", 1)
        
    if GPIO.input(BUTTON_PIN) == GPIO.LOW:
        time_pressed = time.time()
        valid = True
        break

lcd.clear()
time.sleep(0.5)

if valid:
    if time_to_guess > time_pressed:
        lcd.message("  You clicked", 1)
        lcd.message("   TOO EARLY", 2)
        
    else:
        last_frame = time.time()
        ch = "     " + str(time_pressed - time_to_guess)
        ch = ch[:12]
            
        ph3 = "Your reaction time was:                 "
        ch3 = ph3[:16]
        lcd.message(ch3, 1)
        ph3_cp = ph3[16:]
        while True:
            if (time.time() - last_frame) > time_block:
                last_frame = time.time() 
                
                ph3_cp = ph3_cp + ch3[0]
                ch3 = ch3[1:] + ph3_cp[0]
                ph3_cp = ph3_cp[1:]
                lcd.message(ch3, 1)

            lcd.message(ch, 2)
else:
    lcd.message("    Hello?", 1)
    lcd.message("You didnt CLICK", 2)
