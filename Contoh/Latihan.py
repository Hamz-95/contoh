import time

load = '-'
count = 0

for x in range(21):
    time.sleep(0.3)
    print(f'\rProses (x)% [{load}]'. end=''. flush=True)
    count += 1
    if count == 3:
       count = 0
       load += '-'
print('\Sselesai bro')
