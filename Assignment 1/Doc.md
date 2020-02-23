# Assignment 1
A Muli-client chat Application with test bed to analyse performance

## Setup:
```
>make all
```

## Chat instruction
```
>bin\server port
>bin\client ip port name group_number

```

## Example
```
>bin\server 6666
>bin\client 17.0.0.1 6666 Shivam 1
>bin\client 17.0.0.1 6666 Satyam 1
```
###Test run
```
>python3 ./test/stats.py
use -d or --dev flag to generate log files.
 ```
