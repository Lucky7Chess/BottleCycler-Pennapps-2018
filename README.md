# EarthCents
EarthCents: Automate bottle recycle refunds through image processing

## Inspiration
Americans waste about 425 beverage containers per capita per year in landfill, litter, etc. Bottles are usually replaced with cans and bottles made from virgin materials which are more energy-intensive than recycled materials. This causes emissions of a host of toxics to the air and water and increases greenhouse gas emissions. 

The US recycling rate is about 33% while that in stats what have container deposit laws have a 70% average rate of beverage recycling rate. This is a significant change in the amount of harm we do to the planet. 
	
While some states already have a program for exchanging cans for cash, EarthCent brings some incentive to states to make this a program and something available. Eventually when this software gets accurate enough, there will not be as much labor needed to make this happen. 

## What it does
The webapp allows a GUI for the user to capture an image of their item in real time. The EarthCents image recognizer recognizes the users bottles and dispenses physical change through our change dispenser. The webapp then prints a success or failure message to the user. 

## How we built it
Convolutional Neural Networks were used to scan the image to recognize cans and bottles.
Frontend and Flask presents a UI as well as processes user data. 
The Arduino is connected up to the Flask backend and responds with a pair of angle controlled servos to spit out coins. 
Change dispenser: The change dispenser is built from a cardboard box with multiple structural layers to keep the Servos in place. The Arduino board is attached to the back and is connected to the Servos by a hole in the cardboard box. 

## Challenges we ran into
Software: Our biggest challenge was connect the image file from the HTML page to the Flask backend for processing through a TensoFlow model. Flask was also a challenge since complex use of it was new to us. 
Hardware: Building the cardboard box for the coin dispenser was quite difficult. We also had to adapt the Servos with the Arduino so that the coins can be successfully spit out. 

## Accomplishments that we're proud of
With very little tools, we could build with hardware a container for coins, a web app, and artificial intelligence all within 36 hours. This project is also very well rounded (hardware, software, design, web development) and let us learn a lot about connecting everything together. 

## What we learned
We learned about Arduino/hardware hacking. We learned about the pros/cons of Flask vs. using something like Node.js. In general, there was a lot of light shed on the connectivity of all the elements in this project. We both had skills here and there, but this project brought it all together. Learned how to better work together and manage our time effectively through the weekend to achieve as much as possible without being too overly ambitious.

## What's next for EarthCents
EarthCents could deposit Cryptocurrency/venmo etc and hold more coins. If this will be used, we would want to connect it to a weight to ensure that the user exchanged their can/bottle. More precise recognition. 
