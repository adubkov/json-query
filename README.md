# json-query
JSON query is a simple tool to query json input by key.

### Installation
```bash
pip install json-query
```

### Examples
```bash
$ curl -s http://127.0.0.1:9200/_cluster/health | json-query
{
    "active_primary_shards":11111,
    "active_shards":222222,
    "cluster_name":"ClusterName",
    "initializing_shards":0,
    "number_of_data_nodes":33,
    "number_of_nodes":11,
    "relocating_shards":0,
    "status":"green",
    "timed_out":false,
    "unassigned_shards":0
}

$ curl -s http://127.0.0.1:9200/_cluster/health | json-query .
status
number_of_nodes
unassigned_shards
timed_out
active_primary_shards
cluster_name
relocating_shards
active_shards
initializing_shards
number_of_data_nodes

$ curl -s http://127.0.0.1:9200/_cluster/health | json-query status
green
```

```bash
$ curl -s http://127.0.0.1:5050/master/state.json | json-query .
id
hostname
deactivated_slaves
flags
slaves

$ curl -s http://127.0.0.1:5050/master/state.json | json-query .slaves.5.used_resources
{
    "cpus":0.95,
    "disk":0,
    "mem":1792,
    "ports":"[31640-31640, 31978-31978, 31644-31644]"
}

$ curl -s http://127.0.0.1:5050/master/state.json | json-query .slaves.5.used_resources.mem
1792
```
