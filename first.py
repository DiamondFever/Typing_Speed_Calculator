import time
import accuracy
import calculation

sample_text = 'My purpose on this visit was to work out a developmental programme in the area of herbs, forest products'
print(sample_text)

print("Write the above text to calculate your speed ")
start_time = time.time()
input_text = input()
end_time = time.time()
Total_time = end_time-start_time

correct = accuracy.accu(sample_text, input_text)
calculation.speed_cal(correct, Total_time)








