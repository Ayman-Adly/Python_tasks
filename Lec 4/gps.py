import pynmea2

f1 = open("gps_data.tet","r")
out = pynmea2.parse(f1.read(), check=True)
f1.close()

f2 = open("decryption","w+")
f1.write(out.latitude)
f2.close()