# raspberrypi-reaction-game
Embedded reaction time game built with Python, Raspberry Pi GPIO, and an I²C LCD interface.

# Raspberry Pi Reaction Time Game

## Overview

This project is an interactive reaction time game built using a Raspberry Pi. The user must press a button as quickly as possible after a random delay. The reaction time is measured in milliseconds and displayed on a 16x2 I²C LCD screen.

The project was built as an introduction to embedded systems programming, GPIO handling, and I²C communication.

---

## Objectives

- Learn Raspberry Pi GPIO input handling
- Understand I²C communication with an LCD display
- Implement real-time timing in Python
- Build a simple embedded interactive system

---

## Hardware Used

- Raspberry Pi (any model with GPIO support)
- 16x2 LCD display with I²C backpack (PCF8574)
- Push button
- Breadboard and jumper wires

---

## How It Works

1. The system waits for a random delay (to avoid prediction).
2. After the delay, the LCD shows "CLICK!".
3. The user presses the button as fast as possible.
4. The reaction time is calculated using Python timing functions.
5. The result is displayed on the LCD.

---

## Concepts Used

- GPIO digital input
- Event timing using Python (`time` module)
- I²C communication protocol
- LCD control using a PCF8574 I/O expander
- State-based program logic

---

## Project Structure
reaction-game/
│
├── main.py # Main game logic
├── lcd.py # LCD driver (I2C communication)
├── README.md # Project documentation


---

## Possible Improvements

- Add high score memory storage
- Add difficulty levels (shorter reaction windows)
- Add sound feedback (buzzer)
- Add multiple rounds with average score

---

## Demo


<img width="4032" height="3024" alt="IMG_3534 (1)" src="https://github.com/user-attachments/assets/2e5514d7-200b-4ed1-b3b1-b5d6868f9e6d" />


https://github.com/user-attachments/assets/1d49973a-1e2d-4a8a-8803-e40f2047069b




---

## What I Learned

This project helped me understand how software interacts with hardware in embedded systems. It strengthened my understanding of GPIO, timing accuracy, and I²C-based device communication.
My main objective was to understand the I2C protocol for future projects and working with a 16x2 LCD using this protocol via an I/O expander (PCF8574) helped me understand how multiple hardware devices can share a single communication bus using addressing.

I also learned that:

data is transmitted in structured frames
devices are selected using addresses
and communication relies on a master-slave architecture

---

## Notes

- LCD address may vary (commonly `0x27` or `0x3F`)
- Requires I2C to be enabled on Raspberry Pi (`raspi-config`)
