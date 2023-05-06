# The Factory Method is a creational design pattern in object-oriented programming 
# that provides an interface for creating objects in a superclass, but allows subclasses 
# to alter the type of objects that will be created. It defines an abstract method that 
# should be implemented by each subclass, which is responsible for creating a specific instance of a class.
# Python Code for factory method
# it comes under the creational
# Design Pattern
 
class FrenchLocalizer:
 
    """ it simply returns the french version """
 
    def __init__(self):
 
        self.translations = {"car": "voiture", "bike": "bicyclette",
                             "cycle":"cyclette"}
 
    def localize(self, msg):
 
        """change the message using translations"""
        return self.translations.get(msg, msg)
 
class SpanishLocalizer:
    """it simply returns the spanish version"""
 
    def __init__(self):
        self.translations = {"car": "coche", "bike": "bicicleta",
                             "cycle":"ciclo"}
 
    def localize(self, msg):
 
        """change the message using translations"""
        return self.translations.get(msg, msg)
 
class EnglishLocalizer:
    """Simply return the same message"""
 
    def localize(self, msg):
        return msg
 
def Factory(language ="English"):
 
    """Factory Method"""
    localizers = {
        "French": FrenchLocalizer,
        "English": EnglishLocalizer,
        "Spanish": SpanishLocalizer,
    }
 
    return localizers[language]()
 
if __name__ == "__main__":
 
    f = Factory("French")
    e = Factory("English")
    s = Factory("Spanish")
 
    message = ["car", "bike", "cycle"]
 
    for msg in message:
        print(f.localize(msg))
        print(e.localize(msg))
        print(s.localize(msg))



# Benifits :
# for lang in ['French', 'English']:
#     for msg in  ["car", "bike", "cycle"]:
#         dyn_obj = Factory(lang)
#         print(dyn_obj.localize(msg))
    