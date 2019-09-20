import pandas
import numpy
import matplotlib.pyplot as plt
import seaborn as sns

class Analysis:
    instance =None

    @staticmethod
    def boxplot(data):
        column_name_list = data.columns.values
        for column in column_name_list:
            if column in data.columns:
                data_type = str(data[column].dtype)
                if data_type in ['int64', 'float64', 'int32', 'float32']:
                    # box_plot_columns.append(column)
                    print('**********' + column.upper() + '**********')
                    print('Quantile')
                    print('----------')
                    print(data[column].quantile([.25, .5, .75]))
                    print('Minimun  --->  ', data[column].min())
                    print('Maximum  --->  ', data[column].max())
                    print('Mean     --->  ', data[column].mean())
                    print('Skewness --->', data[column].skew(axis=0, skipna=True))
                    print('**********' + column.upper() + '**********')
                    box_plot = data.boxplot(return_type='axes', column=column)
                    plt.show()
                    if data[column].skew(axis=0, skipna=True) > -0.5:
                        print("It's negatively skewed.")
                    if data[column].skew(axis=0, skipna=True) > 0.5:
                        print("It's positively skewed.")
                else:
                    print('Given column name is not present in the csv file.')