# jetson-nano-led-pwm
- Use this wiring setup.

- For BJT transistor, Collector is connected to LED(short wire -ve terminal) and 330ohm is connected to LED(long wire +ve terminal)
- Emitter is connected to GND
- Base is connected to 10kohm resistance
- Testing with PWM pins (32 or 33) which will be connected to Jetson Nano GPIO

References: 
![alt Jetson Nano GPIO](https://www.jetsonhacks.com/2019/06/07/jetson-nano-gpio/)