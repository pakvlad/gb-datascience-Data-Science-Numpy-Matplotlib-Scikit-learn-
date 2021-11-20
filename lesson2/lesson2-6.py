authors_price = pd.merge(authors, book, on = 'author_id', how = 'outer')
print(authors_price)