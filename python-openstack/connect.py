import openstack

# Automatically uses OS_* env variables
conn = openstack.connect()

# Test: list servers
for server in conn.compute.servers():
    print(server.name, server.status)