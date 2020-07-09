import sys
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import japanize_matplotlib

csv_path = sys.argv[1]
csv_dir = os.path.dirname(csv_path)
csv_filename = os.path.splitext(os.path.basename(csv_path))[0]

data_frame = pd.read_csv(csv_path)
print(data_frame)

with PdfPages(csv_dir + '/' + csv_filename + '.pdf') as pdf:
    fig = plt.figure()
    num_x = 31
    fig.set_size_inches(num_x/3,4)
    plt.subplot(1,1,1)
    plt.plot(np.arange(num_x)+1, data_frame.iloc[:,1], marker="o", linewidth=2, markerfacecolor="none")
    plt.xlabel("日付")
    plt.ylabel("℃")
    plt.title(data_frame.columns[1])
    plt.xlim((1,31))
    plt.ylim((35,39))
    #plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
    plt.gca().grid(axis="y")

    fig.tight_layout() #ラベルが重ならないように
    pdf.savefig()
    plt.close()
