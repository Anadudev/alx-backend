#!/usr/bin/env python3
from functools import lru_cache

@lru_cache(maxsize=3)  # Cache will store up to 3 unique results
def square(number):
    print(f"Calculating square of {number}")
    return number * number

# Example usage:
result1 = square(2)  # Function is called and result is calculated
result2 = square(3)  # Function is called and result is calculated
result3 = square(4)  # Function is called and result is calculated

# Now, let's reuse some values
result1_cached = square(2)  # Cached result is returned without recalculating
result2_cached = square(3)  # Cached result is returned without recalculating

# Evicting the least recently used result by introducing a new value
result4 = square(5)  # Function is called, and the least recently used result (square(2)) is evicted from the cache

# Cached results are still available
result3_cached_again = square(4)  # Cached result is returned without recalculating

# Checking cache statistics
cache_info = square.cache_info()
print(f"Cache hits: {cache_info.hits}")
print(f"Cache misses: {cache_info.misses}")
print(f"Cache size: {cache_info.currsize}")

