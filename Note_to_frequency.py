c4_freq = 261.63
d4_freq = 293.66
e4_freq = 329.63
f4_freq = 349.23
g4_freq = 392.00
a4_freq = 440.00
b4_freq = 493.88

name = input("Enter the two character note name, such as C4 : ")
note = name[0]
octave = int(name[1])
if note == "c":
    freq = c4_freq
elif note == "d":
    freq = d4_freq
elif note == "e":
    freq = e4_freq
elif note == "f":
    freq = f4_freq
elif note == "g":
    freq = g4_freq
elif note == "a":
    freq = a4_freq
elif note == "b":
    freq = b4_freq

freq = (freq / 2) ** (4 - octave)
print("The Frequency of ", name, "is", freq)
