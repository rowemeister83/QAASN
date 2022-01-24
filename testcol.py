books = {"The Handmaid's Tale":"Margaret Atwood", "The Hobbit":"J.R.R. Tolkien", "Charlie and the Chocolate Factory":"Roald Dahl"}
print(books["The Handmaid's Tale"])

books.update({"The Left Hand of Darkness": "Ursula K Le Guin", "Dune": "Frank Herbert"})
print(books)

print(books["The Left Hand of Darkness"])

books.update({"The Waste lands": "Stephen King", "The Adjacent": "Christopher Priest"})
print(books)

print(books["The Adjacent"])

books.pop("Charlie and the Chocolate Factory")
print(books)