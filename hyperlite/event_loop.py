""" Event Loop The Heart Of HyperLite DB """

class EventLoop:
    def __init__(self):
        self.events = []
        self.callbacks = []
        self.system_process = []

    def execute_event(self):
        self.events.clear()
        pass

    def execute_callbacks(self):
        self.callbacks.clear()
        pass

    def execute_system_process(self):
        self.callbacks.clear()
        pass


class LoopRunner:
    def __init__(self):
        self.loop = EventLoop()

    def run(self):
        print(self.shouldContinue())
        while(self.shouldContinue()):
            self.loop.execute_event()
            self.loop.execute_callbacks()
            self.loop.execute_system_process()

    def shouldContinue(self):
        return (self.loop.events.__len__() != 0) or (self.loop.callbacks.__len__() != 0) or (self.loop.system_process.__len__() != 0)