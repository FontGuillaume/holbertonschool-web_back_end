#!/usr/bin/env python3
"""
Ce module définit une coroutine qui collecte les
valeurs générées par async_generator dans une liste.
"""
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """
    Utilise une compréhension de liste pour collecter
    les valeurs générées par async_generator.
    Retourne une liste de 10 nombres flottants.
    """
    return [i async for i in async_generator()]
