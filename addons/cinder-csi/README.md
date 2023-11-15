# Cinder CSI Addon

### Prerequisites
- Openstack w/ Cinder
- Microk8s on an Openstack Instance

### Usage
1. Add the this repository to microk8s
```bash
microk8s addons repo add openstack https://github.com/canonical/microk8s-openstack-addons.git
```

2. Create a `values.yaml` file to match the configuration of your Openstack.  Configuration options can be found [here](https://github.com/kubernetes/cloud-provider-openstack/blob/master/docs/cinder-csi-plugin/using-cinder-csi-plugin.md).  The `cinder-csi` addon utilizes Helm and supports any config option that the Helm chart supports.

Below is an example of a valid `values.yaml`:

```yaml
secret:
  enabled: true
  name: cinder-csi-cloud-config
  metadata:
    namespace: ccsi
  data:
    cloud.conf:
      global:
        auth-url: http://keystone-url
        application-credential-id: <cred-id>
        application-credential-secret: <cred-secret>
        region: <region>
        tenant-name: <user-id>
        ca-cert: /path/to/rootCA.crt
      blockstorage:
        bs-version: v3
csi:
  plugin:
    nodePlugin:
      kubeletDir: /var/snap/microk8s/common/var/lib/kubelet
```

 3. Enable the addon
```bash
microk8s enable cinder-csi --values ./path/to/values.yaml
```
