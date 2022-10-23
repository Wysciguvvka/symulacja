import matplotlib.pyplot as plt
import scipy.stats as stats


def chi2(observed: list, expected: list | float, a: float = 0.05, *, df: int = None) -> dict:
    df = len(observed) - 1 if df is None else df
    expected = expected if isinstance(expected, list) else [expected for _ in range(len(observed))]
    values = [(obs - exp) ** 2 / exp for obs, exp in zip(observed, expected)]
    crit = stats.chi2.ppf(q=1 - a, df=df)
    p_val = 1 - stats.chi2.cdf(sum(values), df=df)
    return {'chisq': sum(values), 'crit': crit, 'p-value': p_val}


def rps(n: int = 100) -> dict:
    from lista1 import RandGen
    results_map = [
        # r p s (p1)
        [0, 1, -1],  # r (p2)
        [-1, 0, 1],  # p (p2)
        [1, -1, 0]  # s (p2)
    ]
    p1_data = {'wygrane': 0, 'remisy': 0, 'przegrane': 0}
    p1_choices = [RandGen.randint(0, 2) for _ in range(n)]
    p2_choices = [RandGen.randint(0, 2) for _ in range(n)]
    for p1_choice, p2_choice in zip(p1_choices, p2_choices):
        _result = results_map[p1_choice][p2_choice]
        p1_data['wygrane'] += 1 if _result == 1 else 0
        p1_data['remisy'] += 1 if _result == 0 else 0
        p1_data['przegrane'] += 1 if _result == -1 else 0
    return p1_data


if __name__ == '__main__':
    results = rps()
    prepared_results = list(results.values())
    print(prepared_results)
    print(chi2(prepared_results, 100 / 3))
    plt.bar(results.keys(), results.values())
    plt.show()
