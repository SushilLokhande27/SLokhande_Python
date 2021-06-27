"""
@Class name  :    Book
@Description :    Get the book name, verify data types, print book data
@Author      :    Sushilkumar Lokhande
@Date        :    June 27, 2021
Version      :    0.1
"""

import datetime

class Book:
    def __init__(self, book_name, writer_name, edition, pages, publisher_name, publish_date):
        self.book_name = book_name
        self.writer_name = writer_name
        self.edition = edition
        self.pages = pages
        self.publisher_name = publisher_name
        self.publish_date = publish_date

    def PrintBook(self):
        print("Book Name: ", self.book_name)
        print("Writer Name: ", self.writer_name)
        print("Edition: ", self.edition)
        print("Number of Pages: ", self.pages)
        print("Publisher: ", self.publisher_name)
        print("Publish Date: ", self.publish_date)

p1 = Book("Python", "Sushilkumar Lokhande", 0.1, 100, "Publisher", datetime.datetime(2021, 6, 27))
p1.PrintBook()
    
    
        
                
        
