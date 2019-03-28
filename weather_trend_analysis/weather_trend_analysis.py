import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def computeMovingAverage(data, step):
    '''
    @description: 计算移动平均值
    @param {type} data- 输入数据, step- 单次计算移动平均值的数目
    @return: res- 移动平均值结果
    '''
    res = np.array([])
    for i in range(step, len(data)):
        res = np.append(res, np.average(data[i-step:i]))
    return res


# read data
fname_weather_global = 'data/weather_global.csv'
fname_weather_shanghai = 'data/weather_shanghai.csv'

weather_global = pd.read_csv(fname_weather_global)
weather_shanghai = pd.read_csv(fname_weather_shanghai)

# compute moving average of temperature
step = 10
weather_shanghai_avg = computeMovingAverage(weather_shanghai.avg_temp, step)
weather_global_avg = computeMovingAverage(weather_global.avg_temp, step)
diff_avg = weather_shanghai_avg - \
    weather_global_avg[-len(weather_shanghai_avg):]

# plot
plt.title("Moving average temperature for weather trend")
plt.xlabel("year")
plt.ylabel("Temperature")
plt.plot(weather_shanghai.year[step:], weather_shanghai_avg, color='red')
plt.plot(weather_global.year[step:], weather_global_avg, color='blue')
plt.plot(weather_shanghai.year[step:], diff_avg, color='green')
plt.legend(['Shanghai', 'global', 'diff'])
plt.savefig('plots/weather_trend.png')
plt.show()
