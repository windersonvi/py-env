import matplotlib.pyplot as plt

def generate_chart_pie():
    labels = ['A', 'B', 'C']
    values = [1, 2, 3]

    fig, ax = plt.subplots()
    ax.pie(values,labels=labels)
    plt.savefig('.pie.png')
    plt.close()

