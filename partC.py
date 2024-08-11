import matplotlib.pyplot as plt


def graph_plotting(high_temp,low_temp):
    print(f"The highest Temprature is {high_temp} and The lowest Temprature is {low_temp}")
    categories = ['Highest', 'Lowest']
    value1 = high_temp
    value2 = low_temp
    values = [value1, value2]
    colors = ['red', 'blue']
    plt.barh(categories, values, color=colors)
    plt.title("Horizontal Bar Chart with Highest and Lowest Values")
    plt.xlabel("Values")
    plt.ylabel("Categories")
    plt.show()
    plt.show()
