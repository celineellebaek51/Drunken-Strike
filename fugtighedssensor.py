import smbus
import time

class MCP3021:
    def __init__(self,address=0x4B):
        self.bus = smbus.SMBus(1)
        self.address = address
   # bus = smbus.SMBus(1)

    #def __init__(self, address = 0x4B):
     #   self.address = address

    def read_raw(self):
        # reads word (16bits) as int
        rd = self.bus.read_word_data(self.address, 0)
        # exchanges upper and lower bytes
        data = ((rd & 0xFF) << 8) | ((rd & 0xFF00) >> 8)
        # ignores two least significant bits
        return data >> 2
    
adc = MCP3021()

DRY=779
WET=130

while True:
    raw = adc.read_raw()

    percent = (779-raw)*100/(779-130)
    #(DRY - raw) * 100 / (DRY - WET)
    percent = max(0, min(100, percent))

    #status tekst
    if percent >= 60:
        status = "Jorden er fugtig"
    elif percent < 60:
        status = "Jorden er tør"
    print(f"Fugtighed: {percent:5.1f}% | {status}")
   # print(f"Raw: {raw:4d} | Fugtighed: {percent:5.1f}% | {status}")

    time.sleep(1)

   # def read_prct(self):
    #    rd = self.bus.read_word_data(self.address, 0)
     #   data = ((rd & 0xFF) << 8) | ((rd & 0xFF00) >> 8)
      #  raw = data >> 2
       # wet = (779-raw)*100/(779-300)
        #return wet

adc = MCP3021()

while True:
    raw = adc.read_raw()
    prct = adc.read_prct()
    print("Raw :", raw)
    print("wet: ", prct)
    time.sleep(1)