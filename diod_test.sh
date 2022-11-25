status1=0
status2=1
status3=0
while [ 1 ]; do
    echo $status1 > /sys/class/gpio/gpio11/value
    sleep 0.1
    echo $status2 > /sys/class/gpio/gpio12/value
    sleep 0.1
    echo $status3 > /sys/class/gpio/gpio13/value
    sleep 0.1

    if [ $status1 -eq 1 ]; then
        status1=0
    else
        status1=1
    fi

    if [ $status2 -eq 1 ]; then
        status2=0
    else
        status2=1
    fi

    if [ $status3 -eq 1 ]; then
        status3=0
    else
        status3=1
    fi
    sleep 0.1
done