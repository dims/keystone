# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import fixtures
from oslo_policy import opts

from keystone.policy.backends import rules


class Policy(fixtures.Fixture):
    """A fixture for working with policy configuration."""

    def __init__(self, policy_file, config_fixture):
        self._policy_file = policy_file
        self._config_fixture = config_fixture

    def setUp(self):
        super(Policy, self).setUp()
        opts.set_defaults(self._config_fixture.conf)
        self._config_fixture.config(group='oslo_policy',
                                    policy_file=self._policy_file)
        rules.init()
        self.addCleanup(rules.reset)
