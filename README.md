# batterMon
Because of weird charging behavior of my 40.- CHF flea market laptop with chinese knock off battery, I was in need of a battery monitor.

## install
```
# m h  dom mon dow   command

*/5 *  *   *   *     date -Iseconds | cat /dev/stdin /sys/class/power_supply/BAT0/uevent >> /home/marco/repos/batterMon/batter_log.txt && python /home/marco/repos/batterMon/batParse.py /home/marco/repos/batterMon/batter_log.txt > /home/marco/repos/batterMon/data.csv 
```


## use
No need for a local webserver. Just use `'file:///`-urls.
```
firefox file:///home/marco/repos/batterMon/index.html
```
