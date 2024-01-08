import time
from Automatic_street_light import LampuJalan, SensorCahaya

def main():
    pin_led = 15  
    pin_ldr = 34  

    lampu_jalan = LampuJalan(pin_led)
    sensor_cahaya = SensorCahaya(pin_ldr)

    while True:
        nilai_cahaya = sensor_cahaya.baca_nilai()

        if nilai_cahaya:
            lampu_jalan.matikan_lampu()
        else:
            lampu_jalan.nyalakan_lampu()

        time.sleep(1)  

if __name__ == "__main__":
    main()
