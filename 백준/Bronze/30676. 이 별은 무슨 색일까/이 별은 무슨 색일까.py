import sys
input = sys.stdin.readline

answer = ""
gamma = int(input())
if 620 <= gamma <= 780:
    answer = "Red"
elif 590 <= gamma < 620:
    answer = "Orange"
elif 570 <= gamma < 590:
    answer = "Yellow"
elif 495 <= gamma < 570:
    answer = "Green"
elif 450 <= gamma < 495:
    answer = "Blue"
elif 425 <= gamma < 450:
    answer = "Indigo"
elif 380 <= gamma < 425:
    answer = "Violet"

print(answer)