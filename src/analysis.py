import pandas as pd
import matplotlib.pyplot as plt
import sys

def load_data(path):
    return pd.read_csv(path)

def average_scores(df):
    return df[['math', 'science', 'english']].mean()

def top_performer(df):
    df['total'] = df[['math', 'science', 'english']].sum(axis=1)
    return df.loc[df['total'].idxmax()]['name']

def pass_percentage(df):
    passed = df[(df['math'] >= 40) & (df['science'] >= 40) & (df['english'] >= 40)]
    return (len(passed) / len(df)) * 100

def plot_average_scores(df):
    avg = average_scores(df)
    avg.plot(kind='bar', title='Average Scores')
    plt.ylabel('Marks')
    plt.savefig('average_scores.png')

if __name__ == "__main__":
    df = load_data("data/students.csv")

    if len(sys.argv) > 1 and sys.argv[1] == "plot":
        plot_average_scores(df)
        print("Graph generated")
    else:
        print("Average Scores:\n", average_scores(df))
        print("Top Performer:", top_performer(df))
        print("Pass Percentage:", pass_percentage(df))