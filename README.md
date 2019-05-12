Given a **time-frame/window** parameter and **file** containing the events, the tool computes and logs (in a time series of configurable bucket-size) the rolling average delivery time for given events falling in the time frame.

Invoke the python tool as,

`$ python unbabel_cli.py -h`

`usage: unbabel_cli.py [-h] --input-file INPUT-FILE [--window-size N]`

`unbabel_cli.py: error: argument --input-file is required`

Note: Default value for `--window-size` is 10 minutes

Given following input file:  

