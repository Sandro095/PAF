import kolokvij1 as kol
import matplotlib.pyplot as plt
a = kol.Vertikalnihitac(10,10)
b = kol.Vertikalnihitac(20,30)
print("nova visina je: " + str(a.promjeni_visinu(20)))
print("nova pozicija je: "+ str(b.promjeni_brzinu(20)))

a.maximalna_visina_i_vrjeme_leta()
a.graph()

c = a.promjeni_brzinu(10)
d = a.promjeni_brzinu(10)
a.otpor(c,d)
