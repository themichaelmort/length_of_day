import suntime
import numpy as np
import datetime
import matplotlib.pyplot as plt 

# Latitudes
latitudes = np.arange(66)

logitude = 0

sun_times = []
for latitude in latitudes:
    sun_times.append(suntime.Sun(latitude, logitude))

# Solstice day lengths
summer_day_lengths = []
winter_day_lengths = []
summer_solstice = datetime.date(2024, 6, 20)
winter_solstice = datetime.date(2023, 12, 21)
for sun in sun_times:
    summer_day_lengths.append((sun.get_local_sunset_time(summer_solstice) - sun.get_local_sunrise_time(summer_solstice)).total_seconds()/3600)
    winter_day_lengths.append((sun.get_local_sunset_time(winter_solstice) - sun.get_local_sunrise_time(winter_solstice)).total_seconds()/3600)

fig, ax = plt.subplots(nrows=2, figsize=(8,5))
ax[0].grid(True)
ax[1].grid(True)
ax[0].plot(latitudes, summer_day_lengths, 'r', label='Summer Soltice')
ax[1].plot(latitudes, winter_day_lengths, label='Winter Solstice')
ax[0].set_xlabel('Degrees Latitude')
ax[1].set_xlabel('Degrees Latitude')
ax[0].set_ylabel('Length of Daylight (hours)')
ax[1].set_ylabel('Length of Daylight (hours)')
ax[0].legend()
ax[1].legend()
plt.tight_layout()
plt.show()



