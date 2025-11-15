#Ejercicio 4

class Nobel:
    def __init__(self, category, year, winner):
        self.category = category
        self.year = year
        self.winner = winner

np2025 = Nobel("Peace", 2025, "Muhammad Yunus")

print(np2025.category, np2025.year, np2025.winner)

