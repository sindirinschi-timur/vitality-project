from filefifo import Filefifo

FILE_NAME = 'capture_250Hz_03.txt' # Change capture_250Hz_XX.txt from 01 up to 03

data = Filefifo(10, name=FILE_NAME) 

prev = data.get()
curr = data.get()
next = data.get()
count = 2
peaks = []
i = 0

while len(peaks) < 3: # Increase to find more peaks
    if next < curr > prev:
        peaks.append(count)
        i += 1 
        print(f"Peak {i}: sample nr. {count}")
    prev, curr = curr, next
    next = data.get()
    count += 1

intervals = [peaks[i + 1] - peaks[i] for i in range(len(peaks) - 1)]
frequency = 250 / (sum(intervals) / len(intervals))
print(f"Peak sample intervals: {intervals}")
print(f"Frequency: {frequency:.2f} Hz")