# -*-  coding: utf-8 -*-
"""
"""

# Copyright (C) 2015 ZetaOps Inc.
#
# This file is licensed under the GNU General Public License v3
# (GPLv3).  See LICENSE.txt for details.
import pytest
from pyoko.conf import settings
from pyoko.db.adapter.db_riak import BlockSave
from zengine.lib.exceptions import HTTPError
from zengine.lib.test_utils import BaseTestCase
from zengine.models import User
from zengine.notifications.model import NotificationMessage
from zengine.signals import lane_user_change


class TestCase(BaseTestCase):
    def test_call_activity(self):
        self.prepare_client('/call_activity/', username='test_user')
        resp = self.client.post()
        resp.raw()

