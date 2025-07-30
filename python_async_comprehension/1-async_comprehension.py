#!/usr/bin/env python3
async_generator = __import__('0-async_generator').async_generator

"""
Fonction asynchrone qui utilise une compréhension de liste
pour collecter les valeurs générées par async_generator.
Retourne une liste de 10 nombres flottants.
"""


async def async_comprehension():
    return [i async for i in async_generator()]
