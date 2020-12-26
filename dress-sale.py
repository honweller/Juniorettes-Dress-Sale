import csv
import os.path

images = []

with open('dress sale.csv', 'r') as dress_file:
    reader = csv.reader(dress_file)
    for row in reader:
        img, id, price, size = row
        assert(os.path.isfile(f"images/{img}"))
        images.append(
            '\n'.join(["<div class='dress-entry'>",
            f"<img src='images/{img}'/>",
            "<div class='dress-description'>",
            f"<p class='id'>Dress Number: {id}</p>",
            f"<p class='price'>Price: {price}</p>",
            f"<p class='size'>Size: {size}</p>",
            "</div>",
            "</div>"]))

print(f"""<!doctype html>

<html lang="en">
    <head>
        <link rel="preconnect" href="https://fonts.gstatic.com">
        <link href="https://fonts.googleapis.com/css2?family=Lora:wght@500;700&display=swap" rel="stylesheet">
        <meta charset="utf-8">
        <title>Juniorettes Prom Dress Sale</title>
        <link rel="stylesheet" href="css/styles.css">
    </head>
    <body>
        <header>
            <h1>2021 Juniorettes Dress Sale</h1>
            <p>
                Thank you for for you're interest in our 2021 dress sale.
                Listed below is a selection of our dresses with ID number,
                price, and size (please note that these dresses may run small).
                If you are interested in a dress, please contact Sally Doris at
                <a href="mailto: sdoris@chubb.com">
                    sdoris@chubb.com
                </a>
                and Hailey Onweller at
                <a href="mailto: hailey9614@icloud.com">
                    hailey9614@icloud.com 
                </a>
                with the dress ID number. 
                Proceeds from the sale will be reallocated into the community. 
            </p>
        </header>
        <div id=dress-grid>
        {''.join(images)}
        </div>
    </body>
</html>
""")

