#!/usr/bin/env python3
"""
Ce module contient une coroutine qui génère dix
nombres flottants aléatoires avec une pause d'une
seconde entre chaque génération.
"""
import asyncio
import random
import typing

"""
Fonction asynchrone qui génère 10 nombres aléatoires.
À chaque itération, elle attend 1 seconde avant de produire
un nombre flottant compris entre 0 et 10.
"""


async def async_generator():
    for _ in range(10):
        await asyncio.sleep(1)
        result = random.uniform(0, 10)
        yield result
