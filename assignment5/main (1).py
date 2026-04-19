import sys
from profiles import ProfileManager
from network_graph import FriendshipNetwork
from algorithms import bfs_shortest_path, dfs_depth_limited, suggest_friends

def demo_mode(pm, fn):
    print("\n" + "="*40)
    print("   LOADING DEMO DATA...   ")
    users = [
        ("u1", "Aditya", 19, ["AI", "Robotics"]),
        ("u2", "Sneha", 22, ["Law"]),
        ("u3", "Rahul", 20, ["Gaming"]),
        ("u4", "Priya", 19, ["AI"]),
        ("u5", "Vikram", 22, ["Robotics"])
    ]
    for uid, n, a, i in users: 
        pm.add_user(uid, n, a, i)
        fn.add_user_node(uid)
    conns = [("u1","u3"), ("u3","u2"), ("u1","u5"), ("u4","u5")]
    for u1, u2 in conns: fn.add_friendship(u1, u2)
    print("Demo Data Ready.")
    print("="*40)

def main():
    pm = ProfileManager()
    fn = FriendshipNetwork()
    demo_mode(pm, fn)

    while True:
        print("\n--- SOCIAL NETWORK EXPLORER ---")
        print("1: Add | 2: View | 3: Update | 4: Friend | 5: BFS | 6: DFS | 7: Recs | 8: Exit")
        
        choice = input("\nSelect a number: ").strip()

        # Handle Exit immediately
        if choice == '8':
            print("Goodbye!")
            break

        # Logic for each choice
        try:
            if choice == '1':
                uid = input("ID: ").strip()
                name = input("Name: ").strip()
                age = int(input("Age: "))
                ints = input("Interests (comma): ").split(",")
                pm.add_user(uid, name, age, [i.strip() for i in ints])
                fn.add_user_node(uid)
                print(">> Added.")

            elif choice == '2':
                uid = input("Enter ID to View: ").strip()
                user = pm.get_user(uid)
                if user:
                    print(f"\nFOUND: {user.name}, Age: {user.age}, Interests: {user.interests}")
                else:
                    print(">> Not found.")

            elif choice == '3':
                uid = input("ID to Update: ").strip()
                name = input("New Name: ").strip()
                if pm.update_user(uid, name if name else None):
                    print(">> Updated.")

            elif choice == '4':
                u1 = input("ID 1: ").strip()
                u2 = input("ID 2: ").strip()
                if fn.add_friendship(u1, u2):
                    print(">> Connected.")

            elif choice == '5':
                u1 = input("Start ID: ").strip()
                u2 = input("End ID: ").strip()
                print(f">> Path: {bfs_shortest_path(fn.graph, u1, u2)}")

            elif choice == '6':
                uid = input("ID: ").strip()
                d = int(input("Depth: "))
                print(f">> Reachable: {dfs_depth_limited(fn.graph, uid, d)}")

            elif choice == '7':
                uid = input("User ID: ").strip()
                results = suggest_friends(uid, pm, fn)
                print(f">> Recommendations: {results}")
            
            else:
                print(f"Option {choice} not recognized. Try again.")

        except Exception as e:
            print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()