from functools import wraps
from pydantic import BaseModel
from .table_data import TableData, Updater


class Feature(BaseModel):
    data: TableData
    updater: Updater


# def update_state(method):
#     """Update the table state if plugin state changes"""
#     @wraps(method)
#     def _impl(self: Plugin, *args, **kwargs):
#         old = self.copy()
#         result = method(self, *args, **kwargs)
#         new = self.copy()
#         if old != new:
#             self.updater()
#         return result
#     return _impl

def update_state(method):
    """Update the table state if plugin state changes"""
    @wraps(method)
    def _impl(self: Feature, *args, **kwargs):
        result = method(self, *args, **kwargs)
        self.updater()
        return result
    return _impl
