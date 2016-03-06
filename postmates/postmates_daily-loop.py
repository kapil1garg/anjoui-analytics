


import postmates as pm
api = pm.PostmatesAPI("API_KEY", "API_KEY")

address = ['2145 Sheridan Road, Evanston, IL', # Tech
	'1870 Campus Dr, Evanston, IL', # McCormick Foundation Center (Medill Building)
	'1915 Maple Ave, Evanston, IL', # Engelhart hall
	'639 Library Place, Evanston, IL', # Alejandro's house
	'1725 Orrington Ave, Evanston, IL', # McManus Hall
	'2157 Ridge Avenue, Evanston, IL', # Kapil's cribb
	'1501 Central St, Evanston, IL', # Ryan Field
	'635 Chicago Ave, Evanston, IL', # Walgreens in Main
	'299 Hamilton St,  Evanston, IL' # Same street as Jewel Osco, but closer to the Lake
	]

import sched, time
s = sched.scheduler(time.time, time.sleep)

# Create a maxtrix that will get everything
import numpy
save = numpy.empty([1,5], dtype = str)

def get_quotes():
	
	temp = numpy.empty([81,5], dtype = str) # There are 81 combinations of pick ups and drop offs.

	for iterating_pickUp in range(len(address)):
		#print 'pick up: ', address[0]
		#print 'drop off: ', address[iterating_pickUp]
		pickup = pm.Location('N/A', address[iterating_pickUp], 'xxx-xxx-xxxx')
		for iterating_dropOff in range(len(address)):
			dropoff = pm.Location('N/A', address[iterating_dropOff], 'xxx-xxx-xxxx')
			quote = pm.DeliveryQuote(api, pickup.address, dropoff.address)
			
			temp[iterating_pickUp][0] = address[iterating_pickUp] # pick up
			temp[iterating_dropOff][1] = address[iterating_dropOff] # drop off
			#temp[0][2] = date # date
			#temp[0][3] = time # time
			#temp[0][4] = fee # fee

	save = numpy.vstack((save, test))

# For a day
count = 0
while (count <= 24):
	s.enter(3600, 1, get_quotes, ()) #Every hour
	s.run()
	count = count + 1




# For a day: 24 runs. Have a counter in a while loop

