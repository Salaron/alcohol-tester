import OPi.GPIO as GPIO
import time
import serial

# Инициализируем номера пинов, к которым подключены светодиоды
LED_1_PIN = 11 # green
LED_2_PIN = 12 # yellow
LED_3_PIN = 7 # red

# Инициализируем пины как выходы
GPIO.setboard(GPIO.PC2)
GPIO.setmode(GPIO.SOC)
GPIO.setup(LED_1_PIN, GPIO.OUT)
GPIO.setup(LED_2_PIN, GPIO.OUT)
GPIO.setup(LED_3_PIN, GPIO.OUT)

GPIO.output(LED_1_PIN, True)

ser = serial.Serial('/dev/ttyUSB0', 9600)

maxPpl = 0
lastTime = 0
def control_leds(ppml):
    GPIO.output(LED_1_PIN, False)
    GPIO.output(LED_2_PIN, False)
    GPIO.output(LED_3_PIN, False)

    if ppml >= 0.01 and ppml <= 0.02:
        GPIO.output(LED_2_PIN, True)
    elif ppml > 0.02:
        GPIO.output(LED_3_PIN, True)
    else:
        GPIO.output(LED_1_PIN, True)


if __name__ == "__main__":
    while True:
        try:
            sensor_signal = ser.readline().strip()
            sensor_signal = float(sensor_signal)
            print(sensor_signal)

            # Управляем светодиодами
            control_leds(sensor_signal)
            time.sleep(1)
        except ValueError as ex:
            print(ex)
            pass