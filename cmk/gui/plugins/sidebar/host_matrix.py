#!/usr/bin/env python
# -*- encoding: utf-8; py-indent-offset: 4 -*-
# +------------------------------------------------------------------+
# |             ____ _               _        __  __ _  __           |
# |            / ___| |__   ___  ___| | __   |  \/  | |/ /           |
# |           | |   | '_ \ / _ \/ __| |/ /   | |\/| | ' /            |
# |           | |___| | | |  __/ (__|   <    | |  | | . \            |
# |            \____|_| |_|\___|\___|_|\_\___|_|  |_|_|\_\           |
# |                                                                  |
# | Copyright Mathias Kettner 2014             mk@mathias-kettner.de |
# +------------------------------------------------------------------+
#
# This file is part of Check_MK.
# The official homepage is at http://mathias-kettner.de/check_mk.
#
# check_mk is free software;  you can redistribute it and/or modify it
# under the  terms of the  GNU General Public License  as published by
# the Free Software Foundation in version 2.  check_mk is  distributed
# in the hope that it will be useful, but WITHOUT ANY WARRANTY;  with-
# out even the implied warranty of  MERCHANTABILITY  or  FITNESS FOR A
# PARTICULAR PURPOSE. See the  GNU General Public License for more de-
# tails. You should have  received  a copy of the  GNU  General Public
# License along with GNU Make; see the file  COPYING.  If  not,  write
# to the Free Software Foundation, Inc., 51 Franklin St,  Fifth Floor,
# Boston, MA 02110-1301 USA.

import cmk.gui.sites as sites
import cmk.gui.visuals as visuals
from cmk.gui.i18n import _
from cmk.gui.globals import html
from . import (
    CustomizableSidebarSnapin,
    snapin_registry,
    snapin_width,
)


@snapin_registry.register
class HostMatrixSnapin(CustomizableSidebarSnapin):
    @staticmethod
    def type_name():
        return "hostmatrix"

    @classmethod
    def title(cls):
        return _("Host Matrix")

    @classmethod
    def description(cls):
        return _("A matrix showing a colored square for each host")

    @classmethod
    def refresh_regularly(cls):
        return True

    @classmethod
    def vs_parameters(cls):
        return [
            ("context", visuals.VisualFilterList(
                title=_("Filters"),
                info_list=["host"],
            )),
        ]

    @classmethod
    def parameters(cls):
        return {
            "context": {},
        }

    def show(self):
        hosts = self._get_hosts()
        num_hosts = len(hosts)

        if num_hosts > 900:
            html.write_text(_("Sorry, I will not display more than 900 hosts."))
            return

        # Choose smallest square number large enough
        # to show all hosts
        n = 1
        while n * n < num_hosts:
            n += 1

        rows = num_hosts / n
        lastcols = num_hosts % n
        if lastcols > 0:
            rows += 1

        # Calculate cell size (Automatic sizing with 100% does not work here)
        # - Get cell spacing: 1px between each cell
        # - Substract the cell spacing for each column from the total width
        # - Then divide the total width through the number of columns
        # - Then get the full-digit width of the cell and summarize the rest
        #   to be substracted from the cell width
        # This is not a 100% solution but way better than having no links
        cell_spacing = 1
        cell_size = ((snapin_width - cell_spacing * (n + 1)) / n)
        cell_size, cell_size_rest = divmod(cell_size, 1)
        style = 'width:%spx' % (snapin_width - n * cell_size_rest)

        html.open_table(
            class_=["content_center", "hostmatrix"],
            cellspacing=0,
            style=["border-collapse:collapse;", style])
        col = 1
        row = 1
        for site, host, state, has_been_checked, worstsvc, downtimedepth in sorted(hosts):
            if col == 1:
                html.open_tr()
            if downtimedepth > 0:
                s = "d"
            elif not has_been_checked:
                s = "p"
            elif worstsvc == 2 or state == 1:
                s = 2
            elif worstsvc == 3 or state == 2:
                s = 3
            elif worstsvc == 1:
                s = 1
            else:
                s = 0
            url = "view.py?view_name=host&site=%s&host=%s" % (html.urlencode(site),
                                                              html.urlencode(host))
            html.open_td(class_=["state", "state%s" % s])
            html.a(
                '',
                href=url,
                title=host,
                target="main",
                style=["width:%spx;" % cell_size,
                       "height:%spx;" % cell_size])
            html.close_td()

            if col == n or (row == rows and n == lastcols):
                html.open_tr()
                col = 1
                row += 1
            else:
                col += 1
        html.close_table()

    def _get_hosts(self):
        context_filters, only_sites = visuals.get_filter_headers(
            table="hosts", infos=["host"], context=self.parameters()["context"])

        return self._execute_host_query(self._get_host_query(context_filters), only_sites)

    def _get_host_query(self, context_filters):
        query = (
            "GET hosts\n"
            "Columns: name state has_been_checked worst_service_state scheduled_downtime_depth\n"
            "Limit: 901\n") + context_filters

        return query

    def _execute_host_query(self, query, only_sites):
        try:
            sites.live().set_prepend_site(True)
            if only_sites:
                sites.live().set_only_sites(only_sites)

            return sites.live().query(query)
        finally:
            sites.live().set_only_sites(None)
            sites.live().set_prepend_site(False)

    @classmethod
    def allowed_roles(cls):
        return ["user", "admin", "guest"]

    def styles(self):
        return """
table.hostmatrix { border-spacing: 0;  }
table.hostmatrix tr { padding: 0; border-spacing: 0; }
table.hostmatrix a { display: block; width: 100%; height: 100%; line-height: 100%; }
table.hostmatrix td { border: 1px solid #123a4a; padding: 0; border-spacing: 0; }
    """
