# yadrp 
Yet Another Distributed Routing Protocol

This is a learning project!

The goal of this project is to build a distributed routing protocol where the
nodes are relatively static, and the graph formed by the nodes is manually
configured and permissive.  Initial goals are as follows:

* Any node may join the network by connecting to another node. A single node
  can be connected to as many other nodes as desired. Nodes choose their own
  identifiers, and are then reachable based on addressing that identifier.
* All routed information transits the links between the nodes.
* If a piece of information can traverse the graph to reach a node, it should
  do so. The initial goal is at least once delivery.
* Nodes should store some information about their neighbors, and paths that
  traverse them.
* If it is possible to optimize transit by selecting another node, maybe we
  will try that.

The hope is that the design will be both trivial to experiment with, and
deployment will be achievable via a few simple commands. The idea is to be like
hyperboria but with encryption managed outside of this level. Applications
sending traffic across the network are responsible for encrypting (or not)
their traffic.

To Not Do:
* Do not edit config files. Initially, there will be a few cli parameters.
  Next, the node will implement a simple control api.
  * If necessary, eventually there will be a mechanism to request a
    configuration from a running node. Only then will a configuration file
    format be implemented.
* Do not encrypt the traffic. Let the application do that if it desires.
* Do not attempt to conceal the paths of traffic a node is utilizing.
* Do not force reliability at to early of a stage. Get it somewhat working with
  datagrams first.
* Do not store data at the node level. All retry attempts should be driven by the
  applications.
* Do not try to be too efficient. Let datagrams start out big, allow for
  inefficient paths. Soon, _do_ build some type of a test system!

The initial implementation will be as follows. Values of _m_ and _n_ to be
determined.

* Each packet comes with a UUID. If a node has already seen a UUID, it throws it away.

* A node announces its presence on the network. In this case it has a node ID,
  and dispatches the announcement with a uuid to the neighbors where it is
  connected. If the node has already announced this uuid, the node ignores the
  announcement. Otherwise, the node adds itself to the list of nodes this
  announcement has traversed to get here (call it a transit route) on the
  announcement, and forwards the announcement to _m_ of its neighbors, where
  those neighbors have the closest id lexically to the announced id. If a node
  has no neighbors closer lexically, then it stores the announcement and the
  list.  Each node must announce itself periodically.

* A node dispatches information to another node on the network. It puts the
  information in a datagram, with the destination node's ID, and hands it to
  the connected node with an id closes to the destination node.  That node
  checks if it has an announcement for that node on record. If not, it forwards
  the datagram to its neighbor node that has the next closest ID to the
  destination node. If it does have an announcement for the destination node,
  it takes that announcement, with the list that the announcement traversed to
  get to the storage node, adds that metadata to the datagram (call the result a
  routing request), gives it a new UUID, and sends it to the last node on the
  list (presumably connected to the storage node), if it is still connected.
  If that node is not connected, it wraps the datagram in a routing request,
  and sends that routing request to the _n_ neighbors that have the closest ids
  to the last nodes in the routing request.




