n = int(input().strip())
print(len(max(bin(n).strip()[2:].split('0'))))

# Q: what does [2:] do here?
# A: it is used for slicing the first two elements of the string.
# for example if word = 'helloguys' word[2:] will return 'lloguys'
# so bin function returns a binary value as 0b..., so to remove it i have used the function



# another way for Python3:

n = int(input().strip())

# create an empty list to hold our binary numbers
binary = []

# fill the list with 1s and 0s from left to right using Base-Conversion Method (remainders of dividing by 2)

while n > 0:
    remainder = n%2
    binary.append(remainder)
    n = n//2
consec = 0
maximum = 0

# iterate through our list of 1s and 0s to find our max consecutive set of 1s
for i in binary:
    if i == 1:
        consec += 1
        if maximum <= consec:
            maximum = consec
        else:
            pass
    elif i == 0:
        consec = 0

print(maximum)
