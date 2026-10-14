# Laboratory work 3

class TemperatureSensor:
    def __init__(self, value):
        self.value = value

    def read_value(self):
        return self.value


class HumiditySensor:
    def __init__(self, value):
        self.value = value

    def read_value(self):
        return self.value


class MotionSensor:
    def __init__(self, motion):
        self.motion = motion

    def read_value(self):
        return self.motion


class Device:
    def __init__(self, name):
        self.name = name
        self.is_on = False

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def show_state(self):
        if self.is_on:
            print(self.name, "is on")
        else:
            print(self.name, "is off")


class BuildingController:
    def __init__(self, temp, humidity, motion):
        self.temp = TemperatureSensor(temp)
        self.humidity = HumiditySensor(humidity)
        self.motion = MotionSensor(motion)
        self.heating = Device("Heating")
        self.ventilation = Device("Ventilation")
        self.light = Device("Light")

    def check_building(self):
        if self.temp.read_value() < 21:
            self.heating.turn_on()
        else:
            self.heating.turn_off()

        if self.humidity.read_value() > 60:
            self.ventilation.turn_on()
        else:
            self.ventilation.turn_off()

        if self.motion.read_value():
            self.light.turn_on()
        else:
            self.light.turn_off()

        self.heating.show_state()
        self.ventilation.show_state()
        self.light.show_state()


if __name__ == "__main__":
    print("Example 1: 19.5 C, humidity 67%, motion detected")
    room = BuildingController(19.5, 67, True)
    room.check_building()

    print("\nExample 2: 23 C, humidity 50%, no motion")
    room.temp.value = 23
    room.humidity.value = 50
    room.motion.motion = False
    room.check_building()

    print("\nExample 3: 21 C, humidity 60%, no motion")
    room.temp.value = 21
    room.humidity.value = 60
    room.check_building()
