#with out using abstraction 
class laptop:
    def hdmiport(self):
        pass
    def cport(self):
        pass
    def usbport(self):
        pass
class dell(laptop):
    def hdmiport(self):
        print("dell has hdmi port")
    def cport(self):
        print("dell has c port")
class asus(laptop):
      def hdmiport(self):
        print("asus has hdmi port")
      def usbport(self):
        print("asus has usb port")
obj1=dell()
obj1.cport()
obj1.hdmiport()
obj2=asus()
obj2.hdmiport()
obj2.usbport()