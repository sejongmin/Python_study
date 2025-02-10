import sys
input = sys.stdin.readline

N = input().strip()
a = {
    "NLCS": "North London Collegiate School",
    "BHA": "Branksome Hall Asia",
    "KIS": "Korea International School",
    "SJA": "St. Johnsbury Academy"
}
print(a[N])