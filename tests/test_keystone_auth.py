import pytest
import time

from utils import (
    microk8s_enable,
    addon_enabled,
)


class TestKeystoneAuth(object):
    @pytest.mark.order("first")
    def test_enable_keystone_auth(self):
        """
        Sets up and validates keystone-auth.
        """
        print("Enabling k8s-keystone-auth")
        microk8s_enable(
            "k8s-keystone-auth",
            optional_args="--keystone-url http://keystone.url --cert=tests/templates/k8s-keystone-auth/tls.crt --key=tests/templates/k8s-keystone-auth/tls.key",
        )
        print("Validating k8s-keystone-auth")
        time.sleep(30)
        addon_enabled("k8s-keystone-auth")

    def test_rbac_enabled(self):
        """
        Checks that rbac addon is enabled
        """
        assert addon_enabled("rbac")
