# jetson-nano-led-pwm
- Use this wiring setup.
[Wiring Diagram](https://github.com/quicktwit/jetson-nano-led-pwm/blob/master/images/Jetson-Nano-LED-GPIO-3.png)
- For BJT transistor, Collector is connected to LED(short wire -ve terminal) and 330ohm is connected to LED(long wire +ve terminal)
- Emitter is connected to GND
- Base is connected to 10kohm resistance
- Testing with PWM pins (32 or 33) which will be connected to Jetson Nano GPIO

References for the image: 
[Jetson Nano GPIO](https://www.jetsonhacks.com/2019/06/07/jetson-nano-gpio/)
