# lol_health_rgb
League of legends Health statistics integrated with RGB lamp


### libraries
- bleak
- requests
- btledstrip

### Usage
```
setx RGB_ADDRESS YOUR_RGB_BLUETOOTH_MAC_ADDRESS
python -m pip install -r requirements.txt
python main.py
```

### PSEUDOCODE

- Loop:
  - Checks if localhost has the port 2999 open
  - if yes:
    - get the updated champion stats
    - send the value of the percentage of health to the Lamp.set_health module
        - this module converts the percentage of health in a rgb color from gren to red.
    - waits 0.5 seconds
  - else:
    - wait 10 sec