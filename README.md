## cali
```
colcon build --cmake-args -DCMAKE_BUILD_TYPE=Release
source install/setup.bash

ros2 run hiwin_libmodbus hiwinlibmodbus_server

python3 calib.py
```
