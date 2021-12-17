import RPi.GPIO as GPIO
import time

pwm_pin = 33 # change to 32 when trying different pwm
frequency_value = 100 # change this value to 1000 if you want
pwm_speed_1 = 20
pwm_speed_2 = 30
pwm_speed_3 = 40
duty_cycle = 50 # max it can go to 100


def main():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pwm_pin, GPIO.OUT, initial=GPIO.HIGH)
    p = GPIO.PWM(pwm_pin, frequency_value)
    print("PWM running on pin: {}!".format(pwm_pin))
    try:
        while True:
            # GPIO.setup(pwm_pin, GPIO.OUT
            p.start(pwm_speed_1)
            time.sleep(0.5)
            p.start(pwm_speed_2)
            time.sleep(0.5)
            p.start(pwm_speed_3)
            time.sleep(0.5)
            p.start(pwm_speed_2)
            time.sleep(0.5)
            p.start(pwm_speed_1)
            time.sleep(0.5)
            pass
    finally:
        p.stop()
        GPIO.cleanup()

if __name__ == '__main__':
    main()
