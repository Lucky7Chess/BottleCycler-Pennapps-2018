# BottleCycler-Pennapps-2018
BottleCycler:  Automate $0.05 bottle recycle refunds though image processing

## Inspiration:
* Americans waste about 425 beverage containers per capita per year 
	in landfill, litter, etc. Bottles are usually replaced with cans and 
	bottles made from virgin materials which are more energy-intensive 
	than recycled materials. This causes emissions of a host of toxics 
* The US recycling rate is about 33% while that in stats what have 
	container deposit laws have a 70% average rate of beverage 
	recycling rate. This is a significant change in the amount of harm 
	we do to the planet. 
	to the air and water and increases greenhouse gas emissions. 
* Inspired by these state beverage container deposit laws, we looked to put a refreshing spin by automating the depositing process.
* While some states already have a program for exchanging cans for 
	cash, EarthCent brings incentives to states to make this a 
	program and something available. Eventually when this software 
	gets accurate enough, there will not be as much labor needed to 
	make this happen.
## What it does
* The EarthCents image recognizes your bottles and dispenses physical change, encouraging a larger audience of people to be eco-friendly.
## How we built it
* Convolutional Neural Networks scan the image to recognize cans and bottles.
* Frontend and Flask presents a UI as well as processes user data.
* The Arduino is connected upto the Flask backend and responds with a pair of angle controlled servos to spit out coins.
## Challenges we ran into
* Streaming image files from the html page to the flask backend.
* Processing flask backend into the image classifier that was adapted.
* Creating new connectors for the pair of servos
## Accomplishments that we're proud of
* With very little tools, we could
## What we learned
* We learned about Arduino/hardware hacking.
* We learned about the pros/cons of Flask vs. using something like Node.js
* Learned how to better work together and manage our time effectively though the weekend to achieve as much as possible without being too overly ambitious.
## What's next for BottleCycler-Pennapps-2018
* The BottleCycler could deposit Cryptocurrency/venmo etc and hold more coins.
