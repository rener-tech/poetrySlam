Irene Lunt
CSCI 3725
M6-PoetrySlam
Date Due: 11/10/2020

SYSTEM TITLE: Don't Get Too Spooked! 

PROJECT DESCRIPTION: 
This system utilizes an n-gram construction to write poems based on an inspiring set. I first scraped seasonal poems from a website to create my inspiring set. From that set, I constructed a bi-gram using a dictionary data structure. The keys of the dictionary are tuples containing 2-word sequences. Each key maps to a list of words, each of which appears directly after that 2-word sequence somewhere in the inpsiring set. To write each poem, a random key from the bi-gram is selected, and then the subsequent word is randomly selected from the associated dictionary value (the list of words following the 2-word sequence). This process continues either for a finite number of iterations or until the current sequence is not found in the dictionary. The system uses this process to construct 10 poems, evaluating the fitness of each and printing and reading aloud the poem with the highest fitness. The poem with the highest fitness is the one deemed the "spookiest" (meaning it has the most spooky words in it). 

SET UP:
Since I have already performed the webscrape to build my inspiring set, all one needs to do is run the program. It will generate 10 poems and print and read aloud the spookiest one, using the fitness evaluation described in the project description section. Please view my video for an example! 

HOW WAS I CHALLENGED: 
This was a big project of growth for me, though perhaps in mostly technical ways. One of my biggest goals at the outset of this project was to learn how to perform a basic webscrape, which I managed to do successfully, after much difficulty. That was incredibly exciting for me because it is applicable and it also allowed me to make a slightly larger inspiring set than would have been convenient had I hand-entered each poem. Another technical challenge I faced was installing packages. I didn't end up using the package I had trouble installing, but I was actually able to install it eventually, and through that process I better understood my conda environment and more about common package installation errors. It was also a great exercise for me to take my many big ideas and have to pare them down to create small, manageable tasks given the timeframe and expected deliverable. That was important for me because I have a tendency to get overwhelmed when I don't break projects down into smaller chunks. I also tried hard to make good stylistic choices and make use of helper methods. 

SCHOLARLY PAPERS: 
Raymond Kurzweil and John A. Keklak. "Basic Poetry Generation". U.S. Patent 7,184,949 B2 
- This patent discussed poetry generation on a computer, and it discussed the use of ngrams, which I ended up using as the basis for my system's generation.
Marjan Ghazvininejad, Xing Shi†, Yejin Choi, and Kevin Knight. "Generating Topical Poetry".
- I had planned to use this article for its discussion on evaluating rhyme, but I decided not to use rhyme after all. 
Pablo Gervás. "Computational Modelling of Poetry Generation".
- This article talked more about the purpose of poetry and its relation to computational modelling, which I thought was interesting as I thought about what I was hoping to accomplish with the poems my system generated. 

OTHER CREDITS: 
Peers/Mentors: Nell Fusco, Cara Nunley, Sarah Harmon

Poems:
https://www.poetryfoundation.org/collections/142010/halloween-poems

N-grams: 
https://stackabuse.com/python-for-nlp-developing-an-automatic-text-filler-using-n-grams/

Learning to webscrape: 
https://www.freecodecamp.org/news/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe/

https://www.crummy.com/software/BeautifulSoup/bs4/doc/

https://www.freecodecamp.org/news/how-to-scrape-websites-with-python-and-beautifulsoup-5946935d93fe/

https://docs.python.org/3/library/urllib.request.html#module-urllib.request

https://stackoverflow.com/questions/13055208/httperror-http-error-403-forbidden

https://towardsdatascience.com/an-introduction-to-web-scraping-with-python-a2601e8619e5


Other: 
https://www.geeksforgeeks.org/python-check-substring-present-given-string/

https://docs.python.org/3/library/textwrap.html

https://www.guru99.com/reading-and-writing-files-in-python.html

https://stackoverflow.com/questions/32193856/how-to-create-a-txt-file-in-python-pycharm

https://stackoverflow.com/questions/20021457/playing-mp3-song-on-python

https://stackoverflow.com/questions/1614059/how-to-make-python-speak



