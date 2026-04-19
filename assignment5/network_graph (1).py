# network_graph.py
class FriendshipNetwork:
    def __init__(self):
        self.graph = {} 

    def add_user_node(self, user_id):
        if user_id not in self.graph:
            self.graph[user_id] = []

    def add_friendship(self, u1, u2):
        if u1 in self.graph and u2 in self.graph:
            if u2 not in self.graph[u1]:
                self.graph[u1].append(u2)
                self.graph[u2].append(u1)
                return True
        return False
    def get_friends(self, user_id):
        return self.graph.get(user_id, [])