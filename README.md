# ClapActivatedLightSwitch - RaspberryPI

Welcome to the documentation for the Clap Sensor Project. This project aims to create a clap sensor system that allows you to control the lights by simply clapping your hands twice. The system utilizes a microphone to capture the sound of the claps, and the analog signal is transmitted via the ADS sensor over an I2C bus to the Raspberry Pi. On the Raspberry Pi we using cross-correlation, a signal processing technique, to detect the clapping sounds. By analyzing the similarity between captured audio signals and a reference clap signal, the system can accurately identify claps and trigger corresponding actions, such as turning lights on or off. 

In addition to the clap sensor functionality, the lights can also be controlled remotely using your phone or computer through the Apache web server. This adds convenience and flexibility to the system, allowing you to manage the lights from anywhere within your network.

This documentation will guide you through the setup and configuration of the clap sensor system, including the necessary hardware components, wiring instructions, and software installation. Follow the provided steps carefully to successfully implement and enjoy the functionality of the clap sensor system.


## Hardware List

- Raspberry Pi 4 (Wifi needed)
- Grove - Loudness Sensor (LM2904)
- Adc Amplifier Board (ADCS1115)
- 433 MHz RX/TX Modul (DEBO 433 RX/TX)
- 433MHz Wireless Power Outlets


## Wiring Diagram
Input - Microphone:
|Raspberry Pi|<------I2C------|ADCS1115|<--------|LM2904|

Output - Wireless Power Outlets:
|Raspberry Pi|--------->| 433 MHz TX Modul|----Wireless---->|433MHz Wireless Power Outlets|------230V------>|Light|

## Getting Started
To start using the system, follow these steps:
- Wire the components as shown wiring diagram. To find the correct pins please check the datasheet of the components
- Set up and install the Raspberry Pi according to the manufacturer's instructions.
- Download the necessary libraries and drivers for the ADCS1115 and the DEBO 433 RX/TX Module.
- Install Apache by running the command: $sudo apt-get install apache2.
- Save the "home_system.py" file on your Raspberry Pi's desktop and configure it to run automatically upon boot..
- Save the home_automation.php file in your default web root directory "/var/www/html" on the Raspberry Pi.
- Discover the IP address of your Raspberry Pi and enter it on your device, which is connected to the same Wi-Fi network as your Raspberry Pi. This will enable you to control the lights using your mobile device or computer.

Troubleshooting:
- Depending on your 433MHz Wireless Power Outlets you might have to change the code for the 433 MHz TX Modul in the home_system.py script. Therefor use the 433 MHz RX Module and sniff the signal sended by the remote of the 433MHz Wireless Power Outlets with the raspberry pi.

## Demo & Pictures
