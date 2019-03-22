from rediscluster import StrictRedisCluster


startup_nodes = [
        {"host":"172.16.255.43", "port":8801},
        {"host":"172.16.255.43", "port":8802},
        {"host":"172.16.255.43", "port":8803},
        {"host":"172.16.255.43", "port":8804},
        {"host":"172.16.255.43", "port":8805},
        {"host":"172.16.255.43", "port":8806},
    ]

rc = StrictRedisCluster(startup_nodes=startup_nodes)
rc.set("name","wangyang")
rc.set("eclipse","111")
print rc.get("name")
print rc.get("eclipse")