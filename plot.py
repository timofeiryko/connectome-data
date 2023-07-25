import pandas as pd
import statsmodels.api as sm

import matplotlib.pyplot as plt
import seaborn as sns

from typing import Optional, Tuple


def despine_all(ax: Optional[plt.Axes] = None) -> None:
    """Remove spines, ticks etc."""

    if ax is None:
        ax = plt.gca()

    ax.get_yaxis().set_visible(False)
    # remove x ticks:
    ax.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=True)
    sns.despine(ax=ax, left=True, bottom=True)


def kde_boxen_qq(
    dataframe: pd.DataFrame, col_name: str,
    title: str,
    figsize: Optional[Tuple[str, str]] = None
    # It's not good practice to "inherit" figsize without actual inheritance or composition
) -> None:

    fig, axes = plt.subplot_mosaic([['up', 'right'],['down', 'right']],
                                    constrained_layout=True, figsize=(10,6),
                                    gridspec_kw={
                                        'height_ratios': (0.3, 0.7),
                                        'width_ratios': (0.6, 0.4)
                                    })
    
    fig.suptitle(title, fontsize='xx-large')

    sns.histplot(data=dataframe, x=col_name, ax=axes['down'], kde=True)

    sns.boxenplot(data=dataframe, x=col_name, ax=axes['up'])
    axes['up'].set_xlabel('')
    axes['up'].set_xticklabels('')

    sm.qqplot(dataframe[col_name], fit=True, line='45', alpha=0.2, ax=axes['right'])
    axes['right'].set_title('QQ plot')

    if figsize:
        x, y = figsize
        fig.set_figwidth(x)
        fig.set_figheight(y)

    sns.despine()
    plt.show()