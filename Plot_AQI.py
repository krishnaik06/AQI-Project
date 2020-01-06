import pandas as pd
import matplotlib.pyplot as plt


def yearly_avg_data(year):
    temp_i=0
    average=[]
    for rows in pd.read_csv('Data/AQI/aqi{}.csv'.format(year),chunksize=24):
        add_var=0
        avg=0.0
        data=[]
        df=pd.DataFrame(data=rows)
        for index,row in df.iterrows():
            data.append(row['PM2.5'])
        for i in data:
            if type(i) is float or type(i) is int:
                add_var=add_var+i
            elif type(i) is str:
                if i!='NoData' and i!='PwrFail' and i!='---' and i!='InVld':
                    temp=float(i)
                    add_var=add_var+temp
        avg=add_var/24
        temp_i=temp_i+1
        
        average.append(avg)
    return average
    

if __name__=="__main__":
    lst2013=yearly_avg_data(2013)
    lst2014=yearly_avg_data(2014)
    lst2015=yearly_avg_data(2015)
    lst2016=yearly_avg_data(2016)
    lst2017=yearly_avg_data(2017)
    lst2018=yearly_avg_data(2018)
    
    for year in range(2013, 2019):
        #Dynamically creating variable name like lst2013, lst2014 etc
        varName=globals()['lst{}'.format(str(year))]
        plt.plot(range(0,len(varName)),varName, label='{} Data'.format(str(year)))
    plt.xlabel('Day')
    plt.ylabel('PM 2.5')
    plt.legend(loc='upper right')
    plt.show()




