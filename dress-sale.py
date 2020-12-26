import csv 

with open('dress sale.csv', 'r') as dress_file:
    reader = csv.reader(dress_file)
    for row in reader:
        img, id, price, size = row
        print(
            "<div class='dress-entry'>",
            f"<img src='images/{img}'/>",
            "<div class='dress-description'>",
            f"<p class='id'>Dress Number: {id}</p>",
            f"<p class='price'>Price: {price}</p>",
            f"<p class='size'>Size: {size}</p>",
            "</div>",
            "</div>",
            sep='\n')
