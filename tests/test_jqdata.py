from datetime import datetime
from open_quant_data.dataset.thirdparty.jointquant.JointQuantDataset import JointQuantDataset
from open_quant_data.utils.Configuration import Configuration

import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':
    config = Configuration.load('../config/config.toml')
    jq_dataset = JointQuantDataset(config)
    dataset_near = jq_dataset.get_price('RB2311.XSGE', begin=datetime(2023, 2, 1), end=datetime(2023, 7, 1),
                                        frequency="1d")
    dataset_far = jq_dataset.get_price('RB2401.XSGE', begin=datetime(2023, 2, 1), end=datetime(2023, 7, 1),
                                       frequency="1d")
    diff = dataset_far['close'] - dataset_near['close']
    thres_90 = diff.quantile(0.9)
    thres_65 = diff.quantile(0.65)
    thres_10 = diff.quantile(0.1)
    thres_35 = diff.quantile(0.35)

    plt.figure(figsize=(10, 12))
    plt.subplot(4, 1, 1)
    plt.plot(dataset_near['close'])
    plt.plot(dataset_far['close'])
    plt.title('price')

    plt.subplot(4, 1, 2)
    plt.plot(diff)
    plt.axhline(thres_90, color='g', linestyle='--')
    plt.axhline(thres_65, color='g', linestyle='--')
    plt.axhline(thres_35, color='r', linestyle='--')
    plt.axhline(thres_10, color='r', linestyle='--')
    plt.title('diff')

    plt.subplot(4, 1, 3)
    entry_long = diff.index[np.where(diff >= thres_90)[0]]
    exit_long = diff.index[np.where((thres_65 - 1 <= diff) & (diff <= thres_65 + 1))[0]]
    entry_short = diff.index[np.where(diff <= thres_10)[0]]
    exit_short = diff.index[np.where((thres_35 - 1 <= diff) & (diff <= thres_35 + 1))[0]]
    plt.plot(dataset_near['close'])
    plt.scatter(entry_long, dataset_near['close'].loc[entry_long], color='red',
                label='Long Entry')
    plt.scatter(exit_long, dataset_near['close'].loc[exit_long], color='gray',
                label='Long Exit')
    plt.scatter(entry_short, dataset_near['close'].loc[entry_short], color='green',
                label='Short Entry')
    plt.scatter(exit_short, dataset_near['close'].loc[exit_short], color='gray',
                label='Short Exit')
    plt.title('near(RB.2311)')

    plt.subplot(4, 1, 4)
    entry_short = diff.index[np.where(diff >= thres_90)[0]]
    exit_short = diff.index[np.where((thres_65 - 1 <= diff) & (diff <= thres_65 + 1))[0]]
    entry_long = diff.index[np.where(diff <= thres_10)[0]]
    exit_long = diff.index[np.where((thres_35 - 1 <= diff) & (diff <= thres_35 + 1))[0]]
    plt.plot(dataset_far['close'])
    plt.scatter(entry_long, dataset_far['close'].loc[entry_long], color='red',
                label='Long Entry')
    plt.scatter(exit_long, dataset_far['close'].loc[exit_long], color='gray',
                label='Long Exit')
    plt.scatter(entry_short, dataset_far['close'].loc[entry_short], color='green',
                label='Short Entry')
    plt.scatter(exit_short, dataset_far['close'].loc[exit_short], color='gray',
                label='Short Exit')
    plt.title('far(RB.2401)')

    plt.tight_layout()
    plt.show()

    correlation = dataset_near['close'].corr(dataset_far['close'])
    print(correlation)
