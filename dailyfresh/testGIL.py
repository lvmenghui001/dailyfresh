import threading

def f():
    while True:
        pass

if __name__ == "__main__":
    t = threading.Thread(target=f)
    t.start()

    while True:
        pass