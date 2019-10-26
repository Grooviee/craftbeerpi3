# -*- coding: utf-8 -*-
import time


from modules.core.step import StepBase
from modules import cbpi

@cbpi.step
class WaitStep(StepBase):

    
    def init(self):
        self.notify("Wait Step reached!", "Please press the next button to continue", timeout=None)
        # if you dont want a beep sound comment out like :  # cbpi.MashInStepEndBeep()
        cbpi.MashStepEndBeep()