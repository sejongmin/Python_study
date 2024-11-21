import sys
import heapq
input = sys.stdin.readline

def solution(N, cards):
    answer = 0
    heapq.heapify(cards)

    while len(cards) > 1:
        card1 = heapq.heappop(cards)
        card2 = heapq.heappop(cards)
        new_card = card1 + card2
        answer += new_card
        heapq.heappush(cards, new_card)
    
    print(answer)

N = int(input())
cards = [int(input()) for _ in range(N)]
solution(N, cards)