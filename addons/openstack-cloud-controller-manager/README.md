# Openstack Cloud Controller Manager Addon

### Prerequisites
- Openstack w/ Octavia
- Microk8s on an Openstack Instance

### Usage
1. Add the this repository to microk8s
```bash
microk8s addons repo add openstack https://github.com/canonical/microk8s-openstack-addons.git
```

2. Create a `values.yaml` file to match the configuration of your Openstack.  Configuration options can be found [here](https://github.com/kubernetes/cloud-provider-openstack/blob/master/docs/openstack-cloud-controller-manager/using-openstack-cloud-controller-manager.md).  The `openstack-cloud-controller-manager` addon utilizes Helm and supports any config option that the Helm chart supports.

Below is an example of a valid `values.yaml`:

```yaml
cloudConfig:
  global:
    auth-url: <keystone-url>
    application-credential-id: <cred-id>
    application-credential-secret: <cred-secret>
    region: <region>
    tenant-name: <user-id>
    ca-cert: /path/to/rootCA.crt
  loadBalancer:
    enabled: true
    lb-provider: <provider>
    lb-method: SOURCE_IP_PORT
    manage-security-groups: true
  networking:
    public-network-name: <external-net-name>
    internal-network-name: <internal-net-name>
tolerations:
  - key: node.cloudprovider.kubernetes.io/uninitialized
    value: "true"
    effect: NoSchedule
```

 3. Enable the addon
```bash
microk8s enable openstack-cloud-controller-manager --values ./path/to/values.yaml
```

#### Additional options
- **rbac-addon:** Override the RBAC addon 
- **helm3-addon:** Override the Helm3 addon
- **skip-taint-nodes:** Skips tainting the K8s nodes on enable.  Use for granual control over tainting nodes.  Will require manually tainting the appropriate nodes.
