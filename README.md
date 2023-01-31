# PHSX 815: Week 2
## Categorical Distributions - Coins, Cookies, and Dice!

This repository includes a few different projects, each of which are detailed below.

---

### Coin Toss Generation and Analysis

To simulate a coin toss, run the **CoinToss.py** file with Python [^1] . In Linux, this means opening the containing folder in the terminal and simply running, 
> $ python3 CoinToss.py

The default seed in the file is a fixed value, however you can change this value by including the argument `-seed ####` which will provide a different output from the algorithm.

Similarly, you can change the number of tosses with the `-Ntoss ####` argument, and change the number of experiments with the `-Nexp ####` argument. The number of tosses detailes how many times the algorithm will return an output, while the number of experiments details the number of times the algorithm is run. This means unless the seed is changed, the outputs for each run will be the same.

The output of the **CoinToss.py** file can be fed into a text file by using simple Unix commands, such as, 
> $ python3 CoinToss.py > outputfile.txt 

where it feeds it into a text file called **outputfile.txt**. Then, this file can be used as the input file for the **CoinAnalysis.py** file [^1] . This is done with the argument: 
> $ python3 CoinAnalysis.py -input0 outputfile.txt

This takes the output file from **CoinToss.py** and creates a graph from its contents. A picture of this graph is saved in the repo as **Graph_CoinAnaylsis.png**.

![Graph_CoinAnalysis.png](https://user-images.githubusercontent.com/76142511/215650136-61e40222-1fbc-47fe-83fa-cbb7b49621b5.png)

*Note: I do not understand what this graph means nor do I understand if it correct. But it does run, and that is all that matters. Dr. Rogan showed us in class what it was supposed to look like, but I do not recall what that was.*

---

### Categorical Distribution - 6-Sided Die

A categorical distribution has been added to the **Random.py** file. It generates a roll of a 6-sided die. By including this class in our previous **rng.py** file. we can generate a text file that contains any amount of permutations of our Random algorithm. The textfile for this is named **dicerolls.txt** and is created by,
> $ python3 rng.py

By then running,
> $ python3 plot_rng.py

we can create a histogram of the rolls. These are discrete values, as can be seen in the **dicerolls.txt** file. The output graph is included in the folder as **Graph_plot_rng.py**.

![Graph_plot_rng.py](https://user-images.githubusercontent.com/76142511/215650195-cb703a08-aa43-435c-90ae-4fd4cd93a314.png)

*Note: The histogram is a little wonky, I am so sorry. I spend a long time trying to fix it and it only got worse.*

---

### Cookie Analysis - Calculating and Visualizing Quantiles

In this portion of the assignment, the great cookie mystery continues and it is up to us to graph probability distributions to help determine the culprit of the stolen cookies. Through use of familiar random number generators, we can use the **CookieTimer.py** file to generate a spread of times for a particular situation of cookie thievery. We do this by running the code in our terminal with,

> $ python3 CookieTimer.py

where we can also use the arguments `-Nexp ####`, `-Nmeas ####`, and `-seed ####` same as before. We can output this directly to a text file by adding,

> $ python3 CookieTimer.py > cookie_output.py

which can then be used as the input file for the aptly named analyizng script, **CookieAnalysis.py**. We run this by entering,

> $ python3 CookieAnalysis.py cookie_output.py

which will then sort the data, find the mean value, find quartile values, make a histogram, and add the quartiles to the plot as dashed lines. Pretty neat!

![fig3](https://user-images.githubusercontent.com/76142511/215650365-43616cbd-8a3f-4a4e-9089-f35f11698e10.png)

[^1] The code for the file is provided by [Dr. Chris Rogan (crogan) on github](https://github.com/crogan/PHSX815_Week2.git).
