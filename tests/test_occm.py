import pytest
import time

from utils import (
    microk8s_enable,
    addon_enabled,
)


class TestOCCM(object):
    @pytest.mark.order("first")
    def test_enable_occm(self):
        """
        Sets up and validates OCCM.
        """
        print("Enabling OCCM")
        microk8s_enable(
            "openstack-cloud-controller-manager",
            optional_args="--values tests/templates/occm.yaml",
        )
        print("Validating OCCM")
        time.sleep(30)
        addon_enabled("openstack-cloud-controller-manager")

    def test_rbac_enabled(self):
        """
        Checks that rbac addon is enabled
        """
        assert addon_enabled("rbac")

    def test_helm3_enabled(self):
        """
        Checks that helm3 addon is enabled
        """
        assert addon_enabled("helm3")
