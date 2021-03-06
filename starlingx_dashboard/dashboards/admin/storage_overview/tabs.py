#
# Copyright (c) 2016-2019 Wind River Systems, Inc.
#
# SPDX-License-Identifier: Apache-2.0
#

import logging

from django.utils.translation import ugettext_lazy as _

from horizon import exceptions
from horizon import tabs

from starlingx_dashboard.api import base as stx_base
from starlingx_dashboard.api import ceph
from starlingx_dashboard.dashboards.admin.storage_overview import constants
from starlingx_dashboard.dashboards.admin.storage_overview import tables

LOG = logging.getLogger(__name__)


class StorageServicesTab(tabs.TableTab):
    table_classes = (tables.MonitorsTable, tables.OSDsTable,)
    name = _("Services")
    slug = "storage_services"
    template_name = constants.STORAGE_SERVICE_DETAIL_TEMPLATE_NAME

    def get_monitors_data(self):
        try:
            return ceph.monitor_list()
        except Exception as e:
            LOG.error(e)
            return

    def get_osds_data(self):
        try:
            return ceph.osd_list()
        except Exception as e:
            LOG.error(e)
            return

    def get_cluster_data(self):
        try:
            return ceph.cluster_get()
        except Exception as e:
            LOG.error(e)
            return

    def get_storage_data(self):
        try:
            return ceph.storage_get()
        except Exception as e:
            LOG.error(e)
            return

    def get_context_data(self, request):
        try:
            context = super(StorageServicesTab, self).get_context_data(request)
            context['monitors'] = self.get_monitors_data()
            context['osds'] = self.get_osds_data()
            context['cluster'] = self.get_cluster_data()
            context['storage'] = self.get_storage_data()
            return context
        except Exception as e:
            LOG.error(e)
            msg = _('Unable to get storage services list.')
            exceptions.check_message(["Connection", "refused"], msg)
            return

    def allowed(self, request):
        return stx_base.is_stx_region(request)


class StorageOverviewTabs(tabs.TabGroup):
    slug = "storage_overview"
    tabs = (StorageServicesTab, )
    sticky = True
