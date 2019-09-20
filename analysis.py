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
                    print(data[column].quantile([.25, .5, .75]))
                    print('Minimum  --->  ', data[column].min())
                    print('The maximum value of all points in the dataset.')
                    print('Maximum  --->  ', data[column].max())
                    print('The maximum value of all points in the dataset.')
                    print('Mean     --->  ', data[column].mean())
                    print('The mean is derived by summing all the data points and dividing by the number of points.')
                    print('Skewness --->', data[column].skew(axis=0, skipna=True))
                    print('**********' + column.upper() + '**********')
                    print('***************************************')
                    print('Explainability for the data')
                    print('To find the quartile of the data, lets sort it first')
                    print("""Formula for quartile: 
                        Order the data from least to greatest.
                        Find the median of the data set and divide the data set into halves.
                        Find the median of the two halves.""")
                    sorted_column = data[column].sort_values()
                    print('sorted column is:', sorted_column)
                    column_length = data[column].count()
                    print('Column length is: ', column_length)
                    median_column = int(column_length/2)
                    print('Median length is: ', median_column)

                    quartile1 = data[column].iloc[0:median_column]
                    print('quartile1 is:', quartile1, quartile1.count())
                    quartile2 = data[column].iloc[median_column:]
                    print('quartile2 is:', quartile2, quartile2.count())
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