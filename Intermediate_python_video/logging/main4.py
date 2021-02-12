import logging

try:
    a = [1,2,3]
    val = a[4]
except IndexError as e:
    logging.error(e,  exc_info=True)

# we can do the following thing by importing
# traceback and using logging.error("the error is %s", traceback.format_exc())
