import matplotlib.pyplot as plt


def deferment_plot(dic):
	plt.close()
	fig, ax = plt.subplots(1, 1, figsize=(10, 10))

	facility = df['Facilitykey'].unique()[0]

	ax.plot(df['time'], df['oil_rate'])

	plt.title('Liquid Rates for Facility {}'.format(facility))
	plt.xlabel('Date')
	plt.ylabel('bbl/day')

	cnt = 0
	if len(ax.xaxis.get_ticklabels()) > 12:
		for label in ax.xaxis.get_ticklabels():
			if cnt % 7 == 0:
				label.set_visible(True)
			else:
				label.set_visible(False)
			cnt += 1

	plt.xticks(rotation='vertical')

	plt.savefig('images/rates/total/tot_rate_{}.png'.format(facility))
