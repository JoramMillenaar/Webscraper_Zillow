# Webscraper: Zillow

### Purpose:
To scrape all the houses that are for sale on Zillow to detect commonalities between areas/ prices/ floor size etc. 

### Current Progress
The scraper is outdated. It has worked to a point where I could scrape the first page and create some Objects from them so I could do some test with a small amount of data. This project ended by getting sidetracked by trying to make a custom database using Pickle files, Hashes and Mapping (which ended up being pretty cool, but not better than what is availble today). 

### Future Features
* Updating so it works with the current new weblayout
* Tailor the scraper to Safari (Chrome has not been reliable)
* Multipage features: being able to scrape the whole website, not this the front page
* Hook up a DataBase instead of a CSV builder
* Start to make some sense out of the data

## Result
See the CSV file for all the info:

| Data                                  | Meta-Data         |
| ---------------------------------------|----------------:|
|"6967 Reflection St, Redding, CA 96001 House for sale $339,000 4 bds2 ba1,936 sqft 1 hour ago HOUSE OF REALTY"                        | 'A lot of metadata the code makes sense of'|

|"5517 Mill Pond Ln, Redding, CA 96001  House for sale $265,000 3 bds2 ba1,389 sqft 3 hours ago REAL LIVING REAL ESTATE PROFESSIONALS" | 'A lot of metadata the code makes sense of'|

|"2393 Shining Star Way, Redding, CA 96003 For sale by owner $285,000 3 bds3 ba1,540 sqft 4 hours ago"                            | 'A lot of metadata the code makes sense of'|