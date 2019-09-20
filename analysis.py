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
                    print('Quartile')
                    print('----------')
                    print(data[column].quantile([0, .25, .5, .75, 1]))
                    print('Minimum  --->  ', data[column].min())
                    print('Maximum  --->  ', data[column].max())
                    print('Mean     --->  ', data[column].mean())

                    q1_series = data[column].quantile([.25])
                    # q2 = data[column].quantile([.5])

                    for i, v in q1_series.items():
                        q1 = v

                    q3_series = data[column].quantile([.75])
                    for i,v in q3_series.items():
                        q3 = v

                    iqr = q3 - q1
                    lower_whisker = q1 - 1.5 * iqr
                    upper_whisker = q3 + 1.5 * iqr
                    print('Inter Quartile Range ---> ', iqr)
                    print('Lower Whisker ---> ', lower_whisker)
                    print('Upper Whisker ---> ', upper_whisker)
                    outliers = 0
                    for i in data[column]:
                        if i < lower_whisker or i > upper_whisker:
                            outliers = outliers + 1

                    print('Outliers Detected ---> ', outliers)



                    print('Skewness --->', data[column].skew(axis=0, skipna=True))
                    print('**********' + column.upper() + '**********')

                    print('Explainability for the data')
                    print('To find the quartile of the data, lets sort it first')

                    print("""Quartiles in statistics are values that divide your data into quarters.
                        They divide your data into four segments according to where the numbers fall on the number line. 
                        The four quarters that divide a data set into quartiles are:
                        The lowest 25% of numbers.
                        The next lowest 25% of numbers (up to the median).
                        The second highest 25% of numbers (above the median).
                        The highest 25% of numbers.""")
                    print('***************************************')
                    box_plot = data.boxplot(return_type='axes', column=column)
                    plt.show()
                    if data[column].skew(axis=0, skipna=True) > -0.5:
                        print("It's negatively skewed.")
                    if data[column].skew(axis=0, skipna=True) > 0.5:
                        print("It's positively skewed.")
                else:
                    print('Given column name is not present in the csv file.')