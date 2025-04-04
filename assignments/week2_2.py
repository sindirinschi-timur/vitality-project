from filefifo import Filefifo
FILE_NAME = 'capture_250Hz_02.txt'

def scale():
    data = Filefifo(10, name=FILE_NAME)

    min_val = float('inf')
    max_val = float('-inf')
    test = 500  # 2 sec
    
    for _ in range(test):
        val = data.get()
        if val < min_val:
            min_val = val
        if val > max_val:
            max_val = val

    # Reset
    data = Filefifo(10, name=FILE_NAME)
    samples = 2500  # 10 sec
    
    for _ in range(samples):
        val = data.get()
        scaled = ((val - min_val) / (max_val - min_val)) * 100 # scale 0 to 100
        print(scaled)

scale()
    