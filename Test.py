
from collections import deque


graph = {}

graph["1"] = ["2"]
graph["2"] = ["1" , "3" , "4"]
graph["3"] = ["2" , "4"]
graph["4"] = ["2" , "3" , "4"]
graph["5"] = ["4"]


def search(name):
    search_queue = deque()

    search_queue += graph[name]

    searched = []

    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if person_is_seller(person):
                print person + " is a mango seller"
                return True
            else:
                print person + " skip"
                search_queue += graph[person]
                searched.append(person)
    return False

def person_is_seller(name):
    return name[-1] == '5'

search("1")
