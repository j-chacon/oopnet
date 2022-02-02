import datetime
from typing import Optional, Union, Type
import logging

from xarray import DataArray, Dataset

from oopnet.report.binaryfile_reader import BinaryFileReader
from oopnet.report.reportfile_reader import ReportFileReader


# todo: add documentation
class Report:
    """ """
    def __new__(cls, filename: str, startdatetime: Optional[datetime.datetime] = None, reader: Union[Type[BinaryFileReader], Type[ReportFileReader]] = ReportFileReader) -> tuple[Union[DataArray, Dataset, None], Union[DataArray, Dataset, None]]:
        logging.debug('Creating report')
        return reader(filename, startdatetime)