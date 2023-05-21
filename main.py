import laspy
import numpy as np

inp = "wanaka.las"
tile_x_size = 100
tile_y_size = 100
tile_z_size = 100

print("processing...")
las = laspy.read(inp)
print(las)
print("converting...")
las = laspy.convert(las,point_format_id=3,file_version="1.2")
print("converted to LAS1.2 PointFormat3!")
x = np.array(las.x)
y = np.array(las.y)
z = np.array(las.z)
intensity = np.array(las.intensity)
classification = np.array(las.classification)
return_number = np.array(las.return_number)
number_of_returns = np.array(las.number_of_returns)
scan_direction_flag = np.array(las.scan_direction_flag)
edge_of_flight_line = np.array(las.edge_of_flight_line)
synthetic = np.array(las.synthetic)
key_point = np.array(las.key_point)
withheld = np.array(las.withheld)
scan_angle_rank = np.array(las.scan_angle_rank)
user_data = np.array(las.user_data)
point_source_id = np.array(las.point_source_id)
gps_time = np.array(las.gps_time)
red = np.array(las.red)
green = np.array(las.green)
blue = np.array(las.blue)
idx = np.arange(len(x))
tile_x = np.int_((x-x.min())//tile_x_size)
tile_y = np.int_((y-y.min())//tile_y_size)
tile_z = np.int_((z-z.min())//tile_z_size)
print("tiling...")
for i in range(tile_x.max()+1):
    for j in range(tile_y.max()+1):
        for k in range(tile_z.max()+1):
            query = idx[(tile_x == i) & (tile_y == j) & (tile_z == k)]
            header = laspy.LasHeader()
            new = laspy.LasData(header)
            new.x = x[query]
            new.y = y[query]
            new.z = z[query]
            new.intensity = intensity[query]
            new.classification = classification[query]
            new.return_number = return_number[query]
            new.number_of_returns = number_of_returns[query]
            new.scan_direction_flag = scan_direction_flag[query]
            new.edge_of_flight_line = edge_of_flight_line[query]
            new.synthetic = synthetic[query]
            new.key_point = key_point[query]
            new.withheld = withheld[query]
            new.scan_angle_rank = scan_angle_rank[query]
            new.user_data = user_data[query]
            new.point_source_id = point_source_id[query]
            new.gps_time = gps_time[query]
            new.red = red[query]
            new.green = green[query]
            new.blue = blue[query]
            new.write(inp[:-4]+"_"+str(i)+"_"+str(j)+"_"+str(k)+".las")
print("finished!")
