with open('123.txt') as file:
    data = file.readlines()

# initialize counts for each interval to 0
count_0 = 0
count_1_10 = 0
count_11_20 = 0
count_21_30 = 0
count_31_40 = 0
count_41_50 = 0
count_51_100 = 0
count_101_500 = 0
count_501_1000 = 0
count_1000_plus = 0

# iterate through the list and count numbers in each interval
for number in data:
    number = int(number.strip())  # remove any whitespace and convert to integer
    if number == 0:
        count_0 += 1
    elif number >= 1 and number <= 10:
        count_1_10 += 1
    elif number >= 11 and number <= 20:
        count_11_20 += 1
    elif number >= 21 and number <= 30:
        count_21_30 += 1
    elif number >= 31 and number <= 40:
        count_31_40 += 1
    elif number >= 41 and number <= 50:
        count_41_50 += 1
    elif number >= 51 and number <= 100:
        count_51_100 += 1
    elif number >= 101 and number <= 500:
        count_101_500 += 1
    elif number >= 501 and number <= 1000:
        count_501_1000 += 1
    elif number > 1000:
        count_1000_plus += 1

# print the counts
print("Count of numbers in the list:")
print(f"0: {count_0}")
print(f"1-10: {count_1_10}")
print(f"11-20: {count_11_20}")
print(f"21-30: {count_21_30}")
print(f"31-40: {count_31_40}")
print(f"41-50: {count_41_50}")
print(f"51-100: {count_51_100}")
print(f"101-500: {count_101_500}")
print(f"501-1000: {count_501_1000}")
print(f"1000+: {count_1000_plus}")

