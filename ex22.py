import pandas as pd
import matplotlib.pyplot as plt
def main():
	data = pd.read_csv('./olympics.csv', skiprows=4)
	
	p = data[data.Edition==1896].Sport.value_counts().plot(kind='barh')
	plt.show()

if __name__ == '__main__':
	main()