from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from builtins import *  # NOQA
from future import standard_library
standard_library.install_aliases()

from abc import abstractmethod
from logging import getLogger
logger = getLogger(__name__)


class Policy(object):
    """Abstract policy."""

    @abstractmethod
    def __call__(self, state, test=False):
        """Evaluate a policy.

        Returns:
            Distribution of actions
        """
        raise NotImplementedError()


from chainerrl.policies.softmax_policy import *  # NOQA
from chainerrl.policies.gaussian_policy import *  # NOQA
from chainerrl.policies.deterministic_policy import *  # NOQA
