from heapq import heappush, heappop
from collections import defaultdict
class FoodRatings:
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_to_rating = {}
        self.food_to_cuisine = {}
        self.cuisine_to_heap = defaultdict(list)
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            rating = -rating
            self.food_to_rating[food] = rating
            self.food_to_cuisine[food] = cuisine
            heappush(self.cuisine_to_heap[cuisine], (rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        newRating = -newRating
        self.food_to_rating[food] = newRating
        heappush(self.cuisine_to_heap[self.food_to_cuisine[food]], (newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisine_to_heap[cuisine]
        while heap:
            rating, food = heap[0]
            if self.food_to_rating[food] == rating:
                return food
            heappop(heap)
        