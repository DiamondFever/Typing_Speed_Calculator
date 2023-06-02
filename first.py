import time
import accuracy
import calculation
import fact_api
# sample_text = 'My purpose on this visit was to work out a developmental programme in the area of herbs, forest products'
a_json = fact_api.facts()
sample_text = a_json[0]['fact']
print(sample_text)

print("Write the above text to calculate your speed ")
start_time = time.time()
input_text = input()
input_text_count = len(input_text.split())
end_time = time.time()
Total_time = end_time-start_time

correct = accuracy.accu(sample_text, input_text)
calculation.speed_cal(input_text_count, Total_time)








