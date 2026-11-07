import logging

logging.basicConfig(level=logging.DEBUG,
                    filename="logs_p82.log",
                    filemode="w",
                    format="We have logging massage: %(asctime)s: %(name)s: %(levelname)s: %(message)s"
                    )

try:
    print(10/0)
except Exception:
    logging.exception("Exception")