### Misc
![Docker Image](https://github.com/Brucknem/workstation-monitor/workflows/Docker%20Image/badge.svg)

### Backend
![flake8](https://github.com/Brucknem/workstation-monitor/workflows/flake8%20(Backend)/badge.svg)
![pytest](https://github.com/Brucknem/workstation-monitor/workflows/pytest%20(Backend)/badge.svg)

# workstation-monitor
These scripts monitor the most common sensor interfaces of a **Ubuntu** system.

***

# Requirements
- python3 - Has to be accessible as `python`
- pip3 - Has to be accessible as `pip`
- [virtualenv](https://wiki.ubuntuusers.de/virtualenv/)
- [systemd](https://pypi.org/project/systemd/)

## For additional ASUS specific sensors
https://github.com/electrified/asus-wmi-sensors

```
git clone https://github.com/electrified/asus-wmi-sensors.git
sudo make dkms
sudo modprobe asus-wmi-sensors
```

***

# Setup
```
bash install_venv.sh
source source_venv.sh
```

## Setup service
Edit `src/backend/workstation-monitor.service` and adjust 
```
ExecStart=/bin/bash /home/brucknem/Repositories/workstation-monitor/src/backend/workstation-monitor-service.sh
```
to point at your local clone of the `workstation-monitor-service.sh` script.


***

# Running tests
```
source source_venv.sh
bazel test //... --test_output=all
```
