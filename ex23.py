import pandas as pd
import matplotlib.pyplot as plt


def main():
	data = pd.read_csv('olympics.csv', skiprows=4)
	data.City.value_counts().plot(kind='barh', color='red')
	plt.show()

if __name__ == '__main__':
	main()