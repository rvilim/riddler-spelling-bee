import pandas as pd
from string import ascii_lowercase
import tqdm


def filterword(x, centerletter):

    if len(x) < 4:
        return False

    if len(set(x)) > 7:
        return False

    if centerletter not in x:
        return False

    if "s" in x:
        return False
    return True


def scoreword(x):
    if len(x) == 4:
        return 1
    if len(set(x)) == 7:
        return 14
    return len(x)


def main():
    bestscore = 0
    bestboard = {}

    df = pd.read_csv("enable1.txt", names=["word"])
    df["word"] = df["word"].astype(str)

    for centerletter in tqdm.tqdm(ascii_lowercase):
        df_subset = df[df["word"].apply(lambda x: filterword(x, centerletter))]
        df_subset["score"] = df_subset["word"].apply(scoreword)
        df_subset["letters"] = df_subset["word"].apply(frozenset)

        pangram_subset = [i for i in df_subset["letters"].unique() if len(i) == 7]

        for pangram in tqdm.tqdm(pangram_subset):
            df_score = df_subset[df_subset["letters"].apply(lambda x: pangram.issuperset(x))]
            df_score = df_score.drop_duplicates(subset="word")

            s = sum(df_score["score"])
            if s >= bestscore:
                bestboard = (centerletter, pangram)
                bestscore = s
    print(bestscore)
    print(bestboard)


if __name__ == "__main__":
    main()
