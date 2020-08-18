![CI](https://github.com/Brucknem/workstation-monitor/workflows/CI/badge.svg)
![Docker Image CI](https://github.com/Brucknem/workstation-monitor/workflows/Docker%20Image%20CI/badge.svg)

# workstation-monitor
These scripts monitor the most common sensor interfaces of a Ubuntu system.

## For additional ASUS specific sensors
https://github.com/electrified/asus-wmi-sensors

```
git clone https://github.com/electrified/asus-wmi-sensors.git
sudo make dkms
sudo modprobe asus-wmi-sensors
```
