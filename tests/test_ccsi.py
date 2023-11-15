import pytest
import time

from utils import (
    microk8s_enable,
    addon_enabled,
)


class TestCCSI(object):
    @pytest.mark.order("first")
    def test_enable_ccsi(self):
        """
        Sets up and validates CCSI.
        """
        print("Enabling CCSI")
        microk8s_enable(
            "cinder-csi",
            optional_args="--values tests/templates/ccsi.yaml",
        )
        print("Validating CCSI")
        time.sleep(30)
        addon_enabled("cinder-csi")

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
