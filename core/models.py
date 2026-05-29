from django.db import models

# Create your models here.

class Book:
    title:str
    author:str
    status:str

    def __init__(self, title, author, status):
        self.title = title
        self.author = author
        self.status = status

    def __str__(self):
        return f"""
Title: {self.title}
Author: {self.author}
Status: {self.status}
"""

