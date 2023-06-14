# python_logger
a log.py which logs logs...

How to import and use in an application

Uses a rotatingfilehandler i.e. will only keep 2 files, 5mb max, before deleting. Up to user to archive / set rule.

Directory will need to be set in the `log.py` file

```python
import log

logger = log.setup('root') # use in each file you wish to log.

if __name__ == '__main__':
  logger.error('error here')
  logger.warning('warning here')
  logger.info('info here')
  logger.critical('critical here')
```
