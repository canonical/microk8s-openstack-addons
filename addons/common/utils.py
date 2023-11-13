import subprocess
import click
import os
import sys

KUBECTL = os.path.expandvars("$SNAP/microk8s-kubectl.wrapper")
HELM = os.path.expandvars("$SNAP/microk8s-helm3.wrapper")
MICROK8S_STATUS = os.path.expandvars("$SNAP/microk8s-status.wrapper")
MICROK8S_ENABLE = os.path.expandvars("$SNAP/microk8s-enable.wrapper")


def ensure_addon(addon_name: str):
    click.echo("Checking for addon {}...".format(addon_name))
    output = subprocess.check_output([MICROK8S_STATUS, "-a", addon_name]).decode()
    if "enabled" not in output:
        p = subprocess.run([MICROK8S_ENABLE, addon_name])
        if p.returncode != 0:
            click.echo("Failed to enable addon {}".format(addon_name), err=True)
            sys.exit(1)

    click.echo("Checking for addon {}... OK".format(addon_name))
