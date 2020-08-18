#!/bin/bash

/bin/bash ${BASH_SOURCE%/*}/query-cpu.sh $1
/bin/bash ${BASH_SOURCE%/*}/query-ram.sh $1
/bin/bash ${BASH_SOURCE%/*}/query-gpu.sh $1
/bin/bash ${BASH_SOURCE%/*}/query-sensors.sh $1