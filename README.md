# Stock Checker

I'm sure quite a few people hae had trouble getting the latest computer parts as bots buy up all the stock near instantly. 
I decided to fight fire with fire, almost. 
This program will check the stock of a certain item and refresh at specified intervals (defined in seconds). 

## Usage
When launching the program, you will be prompted to enter the url of your item, your budget, and the refresh interval.
Once entered, the program will start printing alerts on the terminal.
There are three different alerts, all of which print the time of said alert.

### Out of Stock
This will probably be the alert you see the most. 
It prints "Sold Out" or "Out of Stock" (depending on the site used) in red text

### In Stock
When the item is in stock, the text "In Stock" or "Add to Cart" (again depending on the site) will be printed in green.
Along with the message, the link to the site is printed in the terminal in case your terminal supports clickable links.

## In Stock but out of price range
This alert is the same as the In Stock alert, but if the price of your item is above your budget variable, it is printed in yellow instead of green.
This Budget variable is defined at the beginning of the program.

## Supported Stores
- Amazon
- Best Buy
- Newegg
