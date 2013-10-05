#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import datetime
import dateutil.parser
import lxml.etree


class GpxParseError(Exception):
    """DOCUMENT ME"""

    pass


class GpxRecord(object):
    """DOCUMENT ME"""

    def __init__(self, latitude=0, longitude=0, elevation=0, speed=0, timestamp=None):
        self.latitude = latitude
        self.longitude = longitude
        self.elevation = elevation
        self.speed = speed
        self.timestamp = timestamp

    @property
    def has_timestamp(self):
        return self.timestamp is not None


def parse_gpx(file_obj):
    """DOCUMENT ME"""

    #
    try:
        gpx = lxml.etree.parse(file_obj)
        nss = {'ns': gpx.getroot().nsmap[None]}
    except Exception, ex:
        raise GpxParseError('Failed to parse the GPX file.')

    #
    trkpt_records = []

    for trkpt in gpx.xpath('//ns:trkpt', namespaces=nss):
        try:
            lat = _convert_attribute(trkpt, 'lat', float)
            lon = _convert_attribute(trkpt, 'lon', float)
            ele = _convert_node(trkpt, './ns:ele/text()', nss, float, -1)
            speed = _convert_node(trkpt, './ns:speed/text()', nss, float, -1)
            time = _convert_node(trkpt, './ns:time/text()', nss, dateutil.parser.parse, None)

        except (KeyError, ValueError):
            raise GpxParseError('Failed to parse the GPX file.')

        trkpt_records.append(
            GpxRecord(latitude=lat, longitude=lon, elevation=ele, speed=speed, timestamp=time))

    #
    return trkpt_records


def validate_gpx(file_obj):
    try:
        parse_gpx(file_obj)
        return True

    except GpxParseError:
        return False


def _convert_attribute(node, name, convert_func):
    """DOCUMENT ME"""

    text = node.attrib.get(name)
    if text is None:
        raise KeyError(name)

    return convert_func(text)


def _convert_node(root_node, xpath, nss, convert_func, default_value):
    """DOCUMENT ME"""

    nodes = root_node.xpath(xpath, namespaces=nss)

    if len(nodes) < 1:
        return default_value

    return convert_func(nodes[0])
