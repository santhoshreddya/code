#now we going with abstraction That’s abstraction → you see what is available, but the details are hidden 
#implementation is hidden
from abc import ABC,abstractmethod
class laptop(ABC):
    @abstractmethod           #It forces all subclasses to implement the three methods (hdmiport, cport, usbport).
    def hdmiport(self):
        pass
    @abstractmethod
    def cport(self):
        pass
    @abstractmethod
    def usbport(self):
        pass
class dell(laptop):    #for abstract method all functionalities must be called in sub class all must be inherit from parent class
    def hdmiport(self):
        print("dell has hdmi port")
    def cport(self):
        print("dell has c port")
    def usbport(self):
        print("dell has usb port")
class asus(laptop):
      def hdmiport(self):
        print("asus has hdmi port")
      def usbport(self):
        print("asus has usb port")
      def cport(self):
        print("asus has c port")
obj1=dell()
obj1.cport()
obj1.hdmiport()
obj1.usbport()
obj2=asus()
obj2.hdmiport()
obj2.usbport()
obj2.cport()