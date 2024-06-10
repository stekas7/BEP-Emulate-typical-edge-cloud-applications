from prometheus_api_client import PrometheusConnect
from datetime import datetime
import pytz
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

prom = PrometheusConnect(url="http://10.12.0.149:30994", disable_ssl=True)

# Parse the timestamps
start_time = datetime.strptime('2024-05-03 13:41:55', '%Y-%m-%d %H:%M:%S')
end_time = datetime.strptime('2024-05-03 13:45:30', '%Y-%m-%d %H:%M:%S')

# Convert to UTC
start_time = pytz.timezone('UTC').localize(start_time)
end_time = pytz.timezone('UTC').localize(end_time)

# Fetch the raw metrics from Prometheus
offset_metric_data = prom.get_metric_range_data(
    'kafka_topic_partition_current_offset{topic="transactions",partition="1"}', 
    start_time=start_time,
    end_time=end_time,
)

# Extract the offset values and calculate their rates per second
offset_values = np.array([float(sample[1]) for sample in offset_metric_data[0]['values']])
time_values = [float(value[0]) for data in offset_metric_data for value in data['values']]
# Convert the offset values and timestamps to numpy arrays
offset_values = np.array(offset_values, dtype=float)
time_values = np.array(time_values, dtype=float)

# Calculate the differences between consecutive offset values and timestamps
offset_diff = np.diff(offset_values)
time_diff = np.diff(time_values)

# Calculate the rate per second
rate_per_second = offset_diff / time_diff

# Print the maximum rate
print(f"Maximum rate: {max(rate_per_second)} records/sec")

# Fetch the lag metric data from Prometheus
lag_metric_data = prom.get_metric_range_data(
    'kafka_consumergroup_lag{partition="1"}',
    start_time=start_time,
    end_time=end_time,
)

# Extract the lag values
lag_values = np.array([float(sample[1]) for sample in lag_metric_data[0]['values']])[1:]  # Exclude the first value to match the length of offset_values_rate_rounded

# Plot the rate per second and lag values against time
plt.figure()
plt.subplot(2, 1, 1)
plt.plot(time_values[1:], rate_per_second)
#plt.title('')
#plt.xlabel('Time')
plt.ylabel('Records generated per Second')
plt.xticks([])  # Remove x-axis values
plt.yticks(range(0, 19, 2))  # Set y-axis values from 0 to 20 with step 2
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(time_values[1:], lag_values)
#plt.title('Kafka Lag')
plt.xlabel('Time')
plt.ylabel('Lag')
plt.xticks([])  # Remove x-axis values
plt.yticks(range(0, 501, 50))  # Set y-axis values from 0 to 20 with step 2
plt.grid(True)

plt.suptitle('Records generated and Kafka Lag over time')
plt.tight_layout()
plt.show()



