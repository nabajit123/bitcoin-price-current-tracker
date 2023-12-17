"""
The Observer pattern is a behavioral design pattern that allows objects to establish a 
one-to-many dependency, so that when one object changes its state, all its dependents are 
notified and updated automatically. This pattern is useful when you have a set of objects 
that need to be notified when a particular subject or event occurs.
"""

class WeatherData:
    def __init__(self):
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self.temperature, self.humidity, self.pressure)

    def set_measurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.notify()


class User:
    def __init__(self, name):
        self.name = name

    def update(self, temperature, humidity, pressure):
        print(f"Hello {self.name}! Current weather conditions: Temperature={temperature}°C, Humidity={humidity}%, Pressure={pressure}hPa")


# Usage example
weather_data = WeatherData()

user1 = User("John")
weather_data.attach(user1)

user2 = User("Jane")
weather_data.attach(user2)

# Simulating weather updates
weather_data.set_measurements(25, 60, 1013)
weather_data.set_measurements(28, 55, 1008)

weather_data.detach(user1)

weather_data.set_measurements(30, 50, 1015)
