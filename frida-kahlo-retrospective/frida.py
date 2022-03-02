
# 1
paintings = ["The Two Fridas", "My Dress Hangs Here", "Tree of Hope", "Self Portrait With Monkeys"]

# 2
dates = [1939, 1933, 1946, 1940]

# 3
paintings = list(zip(paintings, dates))

# 4
paintings.append(('The Broken Column', 1944))
paintings.append(('The Wouneded Deer', 1946))
paintings.append(('Me and My Doll', 1937))

# 5
print(len(paintings))
print(paintings)

# 6
audio_tour_number = range(1, 8)
print(audio_tour_number)

# 7
master_list = list(zip(audio_tour_number, paintings))

# 8
print(master_list)
