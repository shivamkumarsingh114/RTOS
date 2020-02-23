# Assignment 1
A Muli-client chat Application with test bed to analyse performance

## Setup:
```
>make all
```

## Chat instruction
```
bin\server port
bin\client ip port name group_number

```

## Example
```
bin\server 6666
bin\client 17.0.0.1 6666 Shivam 1
bin\client 17.0.0.1 6666 Satyam 1
```
## Test run
```
python3 ./test/stats.py
use -d or --dev flag to generate log files.
 ```

## performance:

### Only One group

|Number of Clients| Time(micro sec)|
|----------------- | -----|
|10| |[240.385714]|
|20| |[228.330000]|
|30| |[221.181818]|
|40| |[291.465333]|
|50| ||[203.793636]|
|60| |[194.106000]|
|70| |[207.119474]|
|80| |[198.786875]|
|90| |[339.205600]|
|100| |[200.555263]|
