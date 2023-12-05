# K8s-Keystone-Auth

### Overview

The k8s-keystone-auth addon enables integration between Microk8s and Openstack Keystone. Information on the upstream project can be found [here](https://github.com/kubernetes/cloud-provider-openstack/blob/master/docs/keystone-auth/using-keystone-webhook-authenticator-and-authorizer.md).

### Prerequisites
- Openstack w/ Keystone
- Microk8s on an Openstack Instance

### Usage
1. Add the this repository to microk8s
```bash
microk8s addons repo add openstack https://github.com/canonical/microk8s-openstack-addons.git
```

2. Create authorization policy as outlined [here](https://github.com/kubernetes/cloud-provider-openstack/blob/master/docs/keystone-auth/using-keystone-webhook-authenticator-and-authorizer.md#authorization-policy-definitionversion-2)(optional)

3. Enable the addon
```bash
sudo microk8s enable k8s-keystone-auth --auth-policy path/to/policy.yaml --keystone-url <keystone-url> --cert path/to/cert --key path/to/key
```

#### CLI Options
- **rbac-addon:** Override the RBAC addon 
- **auth-policy:** Specify path to non-default auth policy
- **keystone-url:** HTTP(S) url to Keystone service
- **cert:** Cert for use with the keystone-auth service
- **key:** Cert key for use with the keystone-auth service
- **username:** User to configure client-keystone-auth
- **skip-config-authorization:** Skip configuring kube-apiserver for authorization
- **keystone-ca:** Provide CA for authorizing Keystone TLS