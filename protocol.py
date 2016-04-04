class Node:
    def __init__(self, identifier, neighbors=[]):
        self.identifiers = []
        self.neighbors = {}
        self.seen = []
        self.identifier = identifier
        [neighbor.connect(self) for neighbor in neighbors]
        self.identifiers += [(identifier, self)]
        self.neighbors.update(dict([(neighbor.identifier, neighbor) for neighbor in neighbors]))
        import uuid
        announce_uuid = str(uuid.uuid4())
        for _, neighbor in self.neighbors.items():
            neighbor.announce((self.identifier, self, announce_uuid))

    def connect(self, connector):
        self.neighbors[connector.identifier] = connector
        #print("Node %s just got new neighbor %s, new list is %s" % (self.identifier, connector.identifier, str(self.neighbors.keys())))

    def announce(self, announcer):
        if announcer[2] in self.seen:
            return
        self.seen += [announcer[2]]
        neighbor_identifiers = list(self.neighbors.items())
        neighbor_identifiers += [announcer, (self.identifier, self)]
        neighbor_identifiers.sort()
        #print("Node %s just got new announce %s, new list is %s" % (self.identifier, announcer[0], dict(self.identifiers).keys()))
        id_neighbor_idx = neighbor_identifiers.index(announcer)
        id_neighbors = (neighbor_identifiers[(id_neighbor_idx + 1) % len(neighbor_identifiers)], neighbor_identifiers[(id_neighbor_idx - 1) % len(neighbor_identifiers)])
        print("At %s, %s id_n: %s" % (self.identifier, announcer[0], str(id_neighbors)))
        if self in id_neighbors:
            self.identifiers += [announcer]
        for id_neighbor in id_neighbors:
            if not id_neighbor[0] in (self.identifier, announcer[0]):
                id_neighbor[1].announce(announcer)
        


       
b = Node("Hello")
c = Node("There", [b])
d = Node("Now", [b,c])
e = Node("Is", [d])
f = Node("The", [b])
g = Node("Time", [f,e])
h = Node("For", [g])

for node in [b,c,d,e,f,g,h]:
    print("%s : %s " % (node.identifier, node.neighbors.keys()))
