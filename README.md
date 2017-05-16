# QGIS_redirect_stdout
Redirect standard output (print) from scripts to QGIS's progress console

## Use case

You wrap a third-party Python script or library into a QGIS processing toolbox interface.

The script is using print for information output but that is not forwarded to QGIS progress console.

Yet.


## Usage

It is as easy as this:

```python

## Your QGIS script

from redirect_stdout import redirect_stdout

with redirect_stdout(progress):
    pass  # your third-party script call goes here
```
