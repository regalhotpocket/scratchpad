from stats import bino_dist

print("fair majority: ", bino_dist(100, 1/2, 51, 100))
print("fair super majority: ", bino_dist(100, 1/2, 60, 100))
print("unfair super majority with 5.95: ", bino_dist(100, 0.595, 60, 100))
