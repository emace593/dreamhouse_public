# dreamhouse_public
COMS 4995 - Applied Deep Learning Final Project

data_gathering: scraping dataset using BeautifulSoup, redfin-houses package, and Google Street View API

public_data_urls.txt: location of dataset available for download from Google Cloud

part1.ipynb: numerical vs. visual regression models for housing costs (run this notebook first; it downloads data necessary for part 2)

part2.ipynb: DC-GAN to generate images of homes (based on https://www.tensorflow.org/tutorials/generative/dcgan)

part2B.ipynb: c-GAN to generate homes at a specific price point (https://arxiv.org/pdf/1411.1784.pdf)

example_cgan.ipynb: same model as part2B but following implementation of https://machinelearningmastery.com/how-to-develop-a-conditional-generative-adversarial-network-from-scratch/

emm2314_dreamhouse.pptx: final presentation

video_url.txt: youtube link for presentation

--------------------------------------------------------------------------------

ORIGINAL PROPOSAL:
My husband and I have been house hunting; the real estate market in our area (northern VA) is a bit crazy right now, and I was wondering how I could turn this into a computer vision problem for this class. I have already begun doing a little investigation as to whether this could turn into a feasible project (N.B. I know I am not the first person to think of this; see this article for example, but I promise I came up with the idea before I searched arXiv). I built a little web scraper using Python’s BeautifulSoup to read a list of the zip codes in the state of Virginia and sort the ones that are in counties considered part of Northern VA. Then, I used the Python API for the website Redfin to retrieve a list of active listings for single family homes within those zipcodes. This gave me not only the street address of the houses for sale, but also data such as the year each home was built, the number of bedrooms and bathrooms in each, and each home’s latitude and longitude. Using the (lat,lon) information, along with the Google StreetView Python API, to retrieve 600 by 600 images of the houses located at each address. Please note that this process is not perfect, because some houses are blocked by trees or are not captured completely by the StreetView image. I am very curious whether this noisy dataset will prove useful for cost prediction. Here are my proposed project goals:

Minimal goal: Build a computer vision regression model with a CNN to predict the cost of a house for sale based on its StreetView appearance. I will compare this to a DNN regression model based on a combination of the homes’ numbers of bedrooms, numbers of bathrooms, and years built. For good measure, I can also see if I can build CNN’s to predict the other data points from appearance (I hypothesize that year built might be possible to predict from outward appearance).

Expected goal: To be honest, I have worked with CNN’s and images before (though not for regression – that’s new! But relatively similar to classification/detection work I have done in the past). Therefore, to stretch myself, I’d like to try working with GANs. My goal is to input a desired cost and have a network generate your “Dream House” – right on budget! 
