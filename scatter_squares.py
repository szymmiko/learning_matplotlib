import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x ** 2 for x in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
# Wyświetlanie serii punktów dzięki funkcji scatter()
# s określa wielkość punktu
# c / cmap - wykorzystanie mapy kolorów
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# Zdefiniowanie tytułu wykresu i etykiet osi
ax.set_title("Kwadraty liczb", fontsize=24)
ax.set_xlabel("Wartość", fontsize=14)
ax.set_ylabel("Kwadraty wartości", fontsize=14)

# Zdefiniowanie wielkości etykiet
# which='major' Zmiana dotyczy podziałek głównych
ax.tick_params(axis='both', which='major', labelsize=14)

# Zdefiniowanie zakresu dla każdej osi
ax.axis([0, 1100, 0, 1100000])

# bbox_inches='tight' Matplotlib automatycznie dostosowuje marginesy,
# aby obejmowały tylko elementy wykresu.
plt.savefig('squares_plot.png', bbox_inches='tight')

# Istotne jest, aby pierwsze zapisać wykres do pliku, ponieważ funkcja
# plt.show() renderuje wykres w oknie interaktywnym, ale równocześnie
# czyści bieżący stan wykresu (w domyślnym trybie działania Matplotlib).
plt.show()
