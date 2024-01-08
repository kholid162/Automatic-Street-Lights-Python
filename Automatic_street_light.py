import machine

class LampuJalan:
    def __init__(self, pin_led):
        self.pin_led = machine.Pin(pin_led, machine.Pin.OUT)
        self.status = False

    def nyalakan_lampu(self):
        print("Lampu Jalan Dinyalakan")
        print("Mengubah nilai pin LED menjadi HIGH")
        self.pin_led.value(1)  

    def matikan_lampu(self):
        print("Lampu Jalan Dimatikan")
        print("Mengubah nilai pin LED menjadi LOW")
        self.pin_led.value(0)  

class SensorCahaya:
    def __init__(self, pin_ldr):
        self.pin_ldr = machine.ADC(machine.Pin(pin_ldr))

    def baca_nilai(self):
        nilai = self.pin_ldr.read()
        return nilai < 100  
