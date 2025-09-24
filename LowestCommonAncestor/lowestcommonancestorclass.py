# Lowest Common Ancestor in Organization Chart (Frequency: 3 / 5)
# Problem: Find the lowest common manager in a company org chart.
# Concepts: N-ary tree traversal, recursive DFS

class Employee:
    def __init__(self, name):
        self.name = name
        self.subordinates = []

    def add_subordinate(self, emp):
        self.subordinates.append(emp)

def find_lca(root, emp1, emp2):
    if root is None or root == emp1 or root == emp2:
        return root

    count = 0
    temp = None

    for sub in root.subordinates:
        res = find_lca(sub, emp1, emp2)
        if res:
            count += 1
            temp = res
        if count == 2:
            return root

    return temp

# Example usage
if __name__ == "__main__":
    # Create organization structure
    ceo = Employee("CEO")
    vp_eng = Employee("VP Engineering")
    vp_sales = Employee("VP Sales")

    # CEO has two VPs reporting to them
    ceo.add_subordinate(vp_eng)
    ceo.add_subordinate(vp_sales)

    # Engineering team
    eng_manager1 = Employee("Engineering Manager 1")
    eng_manager2 = Employee("Engineering Manager 2")
    vp_eng.add_subordinate(eng_manager1)
    vp_eng.add_subordinate(eng_manager2)

    # Engineers under manager 1
    engineer1 = Employee("Engineer 1")
    engineer2 = Employee("Engineer 2")
    eng_manager1.add_subordinate(engineer1)
    eng_manager1.add_subordinate(engineer2)

    # Engineers under manager 2
    engineer3 = Employee("Engineer 3")
    engineer4 = Employee("Engineer 4")
    eng_manager2.add_subordinate(engineer3)
    eng_manager2.add_subordinate(engineer4)

    # Sales team
    sales_manager = Employee("Sales Manager")
    vp_sales.add_subordinate(sales_manager)

    salesperson1 = Employee("Salesperson 1")
    salesperson2 = Employee("Salesperson 2")
    sales_manager.add_subordinate(salesperson1)
    sales_manager.add_subordinate(salesperson2)

    # Test cases
    print("Finding LCA of Engineer 1 and Engineer 2:")
    lca = find_lca(ceo, engineer1, engineer2)
    print(f"LCA: {lca.name if lca else 'None'}")  # Should be Engineering Manager 1

    print("\nFinding LCA of Engineer 1 and Engineer 3:")
    lca = find_lca(ceo, engineer1, engineer3)
    print(f"LCA: {lca.name if lca else 'None'}")  # Should be VP Engineering

    print("\nFinding LCA of Engineer 1 and Salesperson 1:")
    lca = find_lca(ceo, engineer1, salesperson1)
    print(f"LCA: {lca.name if lca else 'None'}")  # Should be CEO