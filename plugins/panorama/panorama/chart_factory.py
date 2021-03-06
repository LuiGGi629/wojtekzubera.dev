# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from functools import partial

from pandas import Series, DataFrame
# !! Import required to instantiate charts, do not remove
from nvd3 import *
import numpy


# A dict used for chart configuration.
# DEFAULT settings can be overwritten and/or completed by chart specific settings.
# In this case, the chart class is used as key.
DEFAULT_CONF = {
    'DEFAULT': {'name': None, 'display_container': False, 'height': 300, 'width': 700},
    'stackedAreaChart': {'use_interactive_guideline': True, 'x_axis_format': ''},
    'multiBarChart': {'x_axis_format': ''},
    'lineChart': {'x_is_date': True, 'x_axis_format': '%m-%Y'}
}

CLASS_ALLOWED = ('discreteBarChart', 'pieChart', 'multiBarChart', 'stackedAreaChart', 'lineChart')


class ChartFactory(object):
    def __init__(self):
        # TODO extra series conf ?
        self.extra_series = {'tooltip': {'y_start': '', 'y_end': ' posts'}}
        self.chart_conf = DEFAULT_CONF

    def render(self, data, renderer):
        """ Create a chart by using the renderer, add data, render and return it.

        :param data: the chart input data. Can be a Series or a DataFrame.
        :param renderer: the renderer to use to create the chart.
        :return: the produced chart.
        """
        chart = renderer()
        if isinstance(data, Series):
            self._add_series(series=data, chart=chart)
        elif isinstance(data, DataFrame):
            for column in data.columns.values:
                series = data[column]
                self._add_series(series=series, chart=chart)
        chart.buildcontent()
        return chart

    def _add_series(self, series, chart):
        # Converting values for Python 3.x compatibility, because numpy numbers are not supported by the JSON encoder
        # TODO fix it in a better way
        y = _list_convert(l=series.tolist())
        x = _list_convert(l=series.index.get_values())
        chart.add_serie(name=series.name, y=y, x=x, extra=self.extra_series)

    def get_renderer(self, class_name):
        """ Return a method responsible to create a chart corresponding to the given class_name.
        Raises an exception if the class is not allowed.

        :param class_name: the class of the chart to create.
        :return: the method permitting to create the chart.
        """
        if class_name not in CLASS_ALLOWED:
            raise ValueError('Class [%s] not allowed for a renderer' % class_name)
        return partial(self._create_chart, class_name=class_name)

    def _create_chart(self, class_name, name):
        """ Initialize a chart, with defaults values and its name.

        :param class_name: the class of the chart to create.
        :param name: its name.
        :return: the chart.
        """
        chart = eval(class_name)
        # Initializing with default values
        conf = self.chart_conf['DEFAULT'].copy()
        if class_name in self.chart_conf:
            # Overriding with specific chart values if defined
            conf.update(self.chart_conf[class_name])
        # Setting the chart name
        conf['name'] = name
        # Passing the dictionary as keywords
        return chart(**conf)


def _list_convert(l):
    """ Convert list containing potential numpy objects in order to transform them in Python standard types.
    Other objects remain the same.
    This method is a workaround to the behavior of the JSON encoder that does not handle numpy numbers.

    :param l: the list to convert
    :return: a new list with numpy objects converted and other objects remaining the same
    """
    return list(map(_numpy_convert, l))


def _numpy_convert(obj):
    """ Convert numpy numbers to standard numbers

    :param obj: the object to convert
    :return: the new object or the same object if it does not need to be converted
    """
    if isinstance(obj, numpy.int_):
        return int(obj)
    elif isinstance(obj, numpy.float_):
        return float(obj)
    elif isinstance(obj, numpy.datetime64):
        epoch_delta = obj - numpy.datetime64('1970-01-01T00:00:00Z')
        return epoch_delta / numpy.timedelta64(1, 'ms')
    # TODO correct this hack from https://github.com/bokeh/bokeh/blob/master/bokeh/protocol.py
    return obj


