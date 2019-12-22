# PageRank


In this practice we will implement the PageRank algorithm in order to sort the webs given in the file "gr0.California.txt.
In the file we will find a graph of the webs, where we will find the different "links" of the nodes of each web.

To solve the problem, we needed to complete the file "processPageRank.py", implementing the way PageRank will crawl the websites and make links between the different websites.

The approach I have taken to solve the problem has been:
First, go through all the links (j) in a loop, and within this, make a second loop which for each in-link, I am accumulating the result of Rj while dividing it between its own out-degree.
This result is stored in a variable that has the total dimension of links in the input file.

Once we have iterated through all the links, I do the Beta multiplication out of the loop so that I can optimize the calculation a bit, since it doesn't run every time.

The next step is to calculate the "s". To do this, I simply sum up the results obtained above. I set the variable "t" to 0, so I can iterate again for the last inlinks.

In this last step, we recalculate the end result with the variable "s" just calculated.

At the time of running the program, I tested with different betas, and we can see that the lower the value of the beta, the faster the program runs.
This is because depending on beta, it does more or less iterations as it takes more / less time to converge. The higher the beta, the more iterations the program will perform.

Once the practice was over, I realized that at first it wasn't quite clear how PageRank worked, but thanks to playing around with different values ​​and different ways of solving it.
The problem is, I understand that this is a very powerful tool for data extraction. Not least, I've learned the basics of Python, a very important language for AI technologies, machine learning, and more.
