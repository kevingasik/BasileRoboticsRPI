from threading import Timer
import os
import time

class RepeatedTimer(object):
    
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False
        
    def do_every(self,period,f,*args):
		def g_tick():
			t = time.time()
			count = 0
			while True:
				count += 1
				yield max(t + count*period - time.time(),0)
		g = g_tick()
		while True:
			time.sleep(next(g))
			f(*args)
    
    def send_thread(self,f): 
		timerThread = threading.Thread(target=lambda: self.do_every(freq,f,*args))
		timerThread.daemon = True
		timerThread.start()

if __name__ == "__main__": 
    print ("starting...")
    rt = RepeatedTimer(1, hello, "World") # it auto-starts, no need of rt.start()
    while count < 100000: 
        count = count + 1
        print(count) 
    try:
        time.sleep(5) # your long-running job goes here...
    finally:
        rt.stop() # better in a try/finally block to make sure the program ends!
    
