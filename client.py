from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

# Create a new InfluxDB client instance
client = InfluxDBClient(url="http://localhost:8086", token="EwuseQsoYKLIxjtslj-1kSHptKi6TUFnz9WRUFMuPK2CI8fJprWA6FzLTELgOpTvv-z30npmWOBTBydt15qxig==", org="BrigadeFantome")

# Create a write API instance
write_api = client.write_api(write_options=SYNCHRONOUS)

# Write data using the write API
data = Point("measurement").tag("tag_key", "tag_value").field("field_key", "field_value")
write_api.write(bucket="BrigadeFantome", record=data)

# Close the InfluxDB client
client.close()
