import os
import sys

# Lecture des hachages depuis des variables d'environnement (GitHub Actions)
BAD = os.environ.get("BADHASH", "c1a4be04b972b6c17db242fc37752ad517c29402")
GOOD = os.environ.get("GOODHASH", "e4cfc6f77ebbe2e23550ddab682316ab4ce1c03c")

print(f"[bisect] starting with BAD={BAD}  GOOD={GOOD}")

# Démarre git bisect
os.system(f"git bisect start {BAD} {GOOD}")

# Lance automatiquement les tests à chaque commit
os.system("git bisect run python manage.py test")

# Revient à l'état initial à la fin du bisect
os.system("git bisect reset")
