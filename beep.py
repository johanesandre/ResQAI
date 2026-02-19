import time
import threading
import winsound

_last_beep = 0

def beep():
    global _last_beep
    now = time.time()

    if now - _last_beep < 2:
        return

    _last_beep = now

    threading.Thread(
        target=lambda: winsound.Beep(1200, 400),
        daemon=True
    ).start()
