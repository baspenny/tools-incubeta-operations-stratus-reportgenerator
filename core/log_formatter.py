import json
import logging


class GCPJsonFormatter(logging.Formatter):
    """
    Custom formatter to format logs as JSON for Google Cloud Logging.
    """

    def format(self, record):
        log_record = {
            "message": record.getMessage(),
            "severity": record.levelname,
            "filename": record.pathname,
            "lineno": record.lineno,
            "funcName": record.funcName,
            "timestamp": self.formatTime(record),
        }
        if record.exc_info:
            log_record["exception"] = self.formatException(record.exc_info)
        return json.dumps(log_record)