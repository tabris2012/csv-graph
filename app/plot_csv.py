import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import japanize_matplotlib

data_csv = 'resources/data.csv'

data_frame = pd.read_csv(data_csv)
data_column = ['食費','交際費','日用品費','光熱費', '備考']
sum_field = '計'
data_frame[sum_field] = data_frame[data_column].sum(axis=1)
subtract_field = '貯金'
data_frame[subtract_field] = data_frame['収入'] - data_frame['計']
print(data_frame)

with PdfPages('resources/data.pdf') as pdf:
    fig = plt.figure()
    plt.subplot(1,1,1)
    ylabel = ['食費','交際費','日用品費','光熱費', '計', '貯金']
    plt.plot(range(data_frame.shape[0]), data_frame[ylabel], marker="o", linewidth=3.0)
    plt.xticks(range(data_frame.shape[0]), data_frame['日付'],
        rotation=15, ha='right')
    plt.xlabel("日付")
    plt.ylabel("円")
    plt.ylim((0,300000))
    plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
    plt.gca().grid(axis="y")
    plt.legend(ylabel, loc="upper left", bbox_to_anchor=(1,1))
    fig.tight_layout() #ラベルが重ならないように
    pdf.savefig()
    plt.close()
