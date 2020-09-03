# Logging Example
Sample code to show how logging works for a package. 
There is a package called logging_example inside the project that you can import and see how logging works.

## How to use

```
$ git clone git@github.com/leela/logging-example.git

$ cd logging-example   # Get into the project directory
$ python
...
>>> import logging_example
>>> logging_example.addition(1, 2)  # This adds record to debug.log with logger name as `logging_example.add`
3
>>> logging_example.division(4, 0) # This adds record to debug.log & error.log with logger name as `logging_example.div`
```