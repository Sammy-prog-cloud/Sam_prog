noise_decibel_level = int(input("Enter in the sound level >>> "))
if noise_decibel_level == 130:
    print("Noise is Jack - Hammer")
elif noise_decibel_level == 106:
    print("Noise is Gas LawnMower")
elif noise_decibel_level == 70:
    print("Noise is Alarm - Clock")
elif noise_decibel_level == 40:
    print('Noise is Quiet-Room')
elif noise_decibel_level >= 40 and noise_decibel_level <= 70:
    print("Noise is between Alarm-Clock and Quiet-Room")
elif noise_decibel_level <= 130 and noise_decibel_level > 106:
    print("Noise is between Jack-Hammer and Gas LawnMower")
elif noise_decibel_level <= 106 and noise_decibel_level > 70:
    print("Noise is between Alarm-Clock and Gas LawnMower")
elif noise_decibel_level < 40:
    print("Noise : Extremely Quiet")
elif noise_decibel_level > 130:
    print("Noise: Rambunctious")
else:
    print('Invalid Input..... Try again later !!!')
