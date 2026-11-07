import logging

logging.basicConfig(level=logging.DEBUG,
                    filename="logs_p81.log",
                    filemode="w",
                    format="We have logging massage: %(asctime)s: %(name)s: %(levelname)s: %(message)s")

logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")
