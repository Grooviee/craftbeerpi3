import time
from thread import start_new_thread
from modules import cbpi

try:
    import RPi.GPIO as GPIO
except Exception as e:
    pass

class Buzzer(object):

    sound = ["H", 0.1, "L", 0.1, "H", 0.1, "L", 0.1, "H", 0.1, "L"]
    melodie1 = ["H", 0.1, "L", 0.1, "H", 0.1, "L", 0.1, "H", 0.1, "L", 0.1, "H", 0.1, "L", 0.1, "H", 0.1, "L"]
    melodie2 = ["H", 0.1, "L", 0.1, "H", 0.1, "L", 0.1, "H", 0.1, "L"]
    melodie3 = ["H", 0.4, "L", 0.1, "H", 0.4, "L", 0.1, "H", 0.4, "L"]
    melodie4 = ["H", 0.4, "L", 0.1, "H", 0.1, "L", 0.1, "H", 0.4, "L", 0.1, "H", 0.1, "L", 0.1, "H", 0.4, "L"]
    melodie5 = ["H", 0.6, "L", 0.3, "H", 0.6, "L", 0.3, "H", 0.6, "L"]
    melodie6 = ["H", 0.2, "L", 0.4, "H", 0.2, "L", 0.3, "H", 0.2, "L", 0.2, "H", 0.2, "L", 0.1, "H", 0.2, "L", 0.1, "H", 0.2, "L"]
    melodie7 = ["H", 0.3, "L", 0.3, "H", 0.3, "L", 0.3, "H", 0.3, "L", 0.3, "H", 0.3, "L"]

    def __init__(self, gpio, beep_level):
        try:
            cbpi.app.logger.info("INIT BUZZER NOW GPIO%s" % gpio)
            self.gpio = int(gpio)
            self.beep_level = beep_level
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(self.gpio, GPIO.OUT)
            self.state = True
            cbpi.app.logger.info("BUZZER SETUP OK")
        except Exception as e:
            cbpi.app.logger.info("BUZZER EXCEPTION %s" % str(e))
            self.state = False

    def beep(self):
        if self.state is False:
            cbpi.app.logger.error("BUZZER not working")
            return

        def play(sound):
            try:
                for i in sound:
                    if (isinstance(i, str)):
                        if i == "H" and self.beep_level == "HIGH":
                            GPIO.output(int(self.gpio), GPIO.HIGH)
                        elif i == "H" and self.beep_level != "HIGH":
                            GPIO.output(int(self.gpio), GPIO.LOW)
                        elif i == "L" and self.beep_level == "HIGH":
                            GPIO.output(int(self.gpio), GPIO.LOW)
                        else:
                            GPIO.output(int(self.gpio), GPIO.HIGH)
                    else:
                        time.sleep(i)
            except Exception as e:
                pass

        start_new_thread(play, (self.sound,))
    
    def MashStepEndBeep(self):   # beeps at end of step
        if self.state is False:
            cbpi.app.logger.error("BUZZER not working")
            return

        def play(sound):
            try:
                for i in sound:
                    if (isinstance(i, str)):
                        if i == "H":
                            GPIO.output(int(self.gpio), GPIO.HIGH)
                        else:
                            GPIO.output(int(self.gpio), GPIO.LOW)
                    else:
                        time.sleep(i)
            except Exception as e:
                pass

        start_new_thread(play, (self.melodie1,))



    def MashInStepEndBeep(self):   # beeps at end of step
        if self.state is False:
            cbpi.app.logger.error("BUZZER not working")
            return

        def play(sound):
            try:
                for i in sound:
                    if (isinstance(i, str)):
                        if i == "H":
                            GPIO.output(int(self.gpio), GPIO.HIGH)
                        else:
                            GPIO.output(int(self.gpio), GPIO.LOW)
                    else:
                        time.sleep(i)
            except Exception as e:
                pass

        start_new_thread(play, (self.melodie3,))


    def ChilStepEndBeep(self):   # beeps at end of step
        if self.state is False:
            cbpi.app.logger.error("BUZZER not working")
            return

        def play(sound):
            try:
                for i in sound:
                    if (isinstance(i, str)):
                        if i == "H":
                            GPIO.output(int(self.gpio), GPIO.HIGH)
                        else:
                            GPIO.output(int(self.gpio), GPIO.LOW)
                    else:
                        time.sleep(i)
            except Exception as e:
                pass

        start_new_thread(play, (self.melodie4,))        


    def PumpStepEndBeep(self):   # beeps at end of step
        if self.state is False:
            cbpi.app.logger.error("BUZZER not working")
            return

        def play(sound):
            try:
                for i in sound:
                    if (isinstance(i, str)):
                        if i == "H":
                            GPIO.output(int(self.gpio), GPIO.HIGH)
                        else:
                            GPIO.output(int(self.gpio), GPIO.LOW)
                    else:
                        time.sleep(i)
            except Exception as e:
                pass

        start_new_thread(play, (self.melodie5,))        


    def BoilStepEndBeep(self):   # beeps at end of step
        if self.state is False:
            cbpi.app.logger.error("BUZZER not working")
            return

        def play(sound):
            try:
                for i in sound:
                    if (isinstance(i, str)):
                        if i == "H":
                            GPIO.output(int(self.gpio), GPIO.HIGH)
                        else:
                            GPIO.output(int(self.gpio), GPIO.LOW)
                    else:
                        time.sleep(i)
            except Exception as e:
                pass

        start_new_thread(play, (self.melodie6,))

    def HopAddBeep(self):   # beeps at end of step
        if self.state is False:
            cbpi.app.logger.error("BUZZER not working")
            return

        def play(sound):
            try:
                for i in sound:
                    if (isinstance(i, str)):
                        if i == "H":
                            GPIO.output(int(self.gpio), GPIO.HIGH)
                        else:
                            GPIO.output(int(self.gpio), GPIO.LOW)
                    else:
                        time.sleep(i)
            except Exception as e:
                pass

        start_new_thread(play, (self.melodie7,))

@cbpi.initalizer(order=1)
def init(cbpi):
    gpio = cbpi.get_config_parameter("buzzer", 22)
    beep_level = cbpi.get_config_parameter("buzzer_beep_level", "HIGH")

    cbpi.buzzer = Buzzer(gpio, beep_level)
    cbpi.beep()
    cbpi.MashStepEndBeep()
    cbpi.MashInStepEndBeep()
    cbpi.ChilStepEndBeep()
    cbpi.PumpStepEndBeep()
    cbpi.BoilStepEndBeep()
    cbpi.HopAddBeep()
    cbpi.app.logger.info("INIT OK")
