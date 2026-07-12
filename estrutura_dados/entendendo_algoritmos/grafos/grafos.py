#!/usr/bin/env python
"""
-----------------------------------------------------
Program    : grafos.py
Description:
Version    : 0.1
Author     : Luca Gorayeb <lucagorayeb@gmail.com>
Date       : 10/07/2026
Licence   : GNU/GPL v3.0
-----------------------------------------------------
Use:
-----------------------------------------------------
"""
from collections import deque

graph = {'Luca': ['Larissa', 'Luana', 'Pedro'],
         'Larissa': ['Leandro'],
         'Leandro': ['Martim']}
# print(graph)
# print(graph['Larissa'])



def person_sailor(name):
    return name[-1] == 'm'

def init(name: str) -> str:
    return 'The smallest path is ' +  name + ' -> ' + search(name)

def search(name: str) -> str:
    queue = deque()
    # for name in names:
    queue += graph[name]
    verified = []
    while queue:
        person = queue.popleft()
        if not person in verified:
            if person_sailor(person):
                return person
            else:
                # print(person)
                if person in queue:
                    queue += graph[person]
                    verified.append(person)
                    if person in graph:
                        queue += graph[person]
                return person + ' -> ' + search(person)
    return 'The path does not exists'

print(init('Luca'))