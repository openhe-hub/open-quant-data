from datetime import datetime
from open_quant_data.dataset.thirdparty.jointquant.JointQuantDataset import JointQuantDataset
from open_quant_data.utils.Configuration import Configuration

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

if __name__ == '__main__':
    config = Configuration.load('../config/config.toml')
    jq_dataset = JointQuantDataset(config)
    dataset_2311 = jq_dataset.get_price('RB2311.XSGE', begin=datetime(2023, 2, 1), end=datetime(2023, 7, 1),
                                        frequency="1d")
    dataset_2309 = jq_dataset.get_price('RB2309.XSGE', begin=datetime(2023, 2, 1), end=datetime(2023, 7, 1),
                                        frequency="1d")
    dataset_2310 = jq_dataset.get_price('RB2310.XSGE', begin=datetime(2023, 2, 1), end=datetime(2023, 7, 1),
                                        frequency="1d")
    dataset_2312 = jq_dataset.get_price('RB2312.XSGE', begin=datetime(2023, 2, 1), end=datetime(2023, 7, 1),
                                        frequency="1d")
    dataset_2401 = jq_dataset.get_price('RB2401.XSGE', begin=datetime(2023, 2, 1), end=datetime(2023, 7, 1),
                                        frequency="1d")

    dataset = pd.DataFrame({
        '2309': dataset_2309['close'],
        '2310': dataset_2310['close'],
        '2311': dataset_2311['close'],
        '2312': dataset_2312['close'],
        '2401': dataset_2401['close'],
    })

    sns.heatmap(dataset.corr(), linewidths=0.1, vmin=0.998, vmax=1.0, square=True, linecolor='white', annot=True)
    plt.show()
