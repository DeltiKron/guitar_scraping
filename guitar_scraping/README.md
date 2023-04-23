# guitar_scraping
I was interested on how prices for acoustic guitars vary between different brands and different sets of parameters like age of the model, wood type or guitar shape. Also an especially interesting question for me was how prices for the same instrument or similar categories change over time.

As a first step towards getting a feel for the acoustic-steel string guitar market, I wrote a set of scripts to scrape data on different guitars from one of europes largest online merchants for musical instruments: [Thomann](http://www.thomann.de).

I use cron to run the scraper on a daily basis which then generates the data for me. I might eventually make the dataset public.

Data Cleaning:
1. define features and clean data accordingly. Features are:
    * Manufacturer
    * Body Shape
    * Number of frets
    * Woods used:
        * Body
        * Sides
        * Fretboard
    * Finish? How difficult is it to get this info?
    * Pickups Yes/No
    * Cutaway Yes/No
    * Comes with case Yes/No
    * Thomann sale rank
    * Time on market   
    

Data Exploration:
* What does the distribution of guitar prices look like?
* How are market shares divided between manufacturers?
* How are prices from different Manufacturers priced?
   * Can manufacturers be classified according to their price ranges?
* What types of woods are used and how often?
* Which shapes are there and what is their market share?
* Which features are the most useful in predicting prices?


* which are the inherent groups and classes of guitars according to key parameters. These key parameters would be: 
    * Price
    * Manufacturer
    * Types of wood used for manufacturing the guitar
    * sales rank
    
 It would also be interesting to make a visualization of the best selling guitars over time (similar to the nice videos that pop up all the time on facebook and such)
 
 It would also be interesting to see which parameters are most dominating when predicting the price of individual guitars. The possible predictors are the same as the predictors above used for dataset segmentation. If I'm able to sucessfully model the pricing of a guitar, it could also be possible to check where the discrepancies between the model output and the given price are most favorable and then get the best deal there when buying a new guitar.
 
 