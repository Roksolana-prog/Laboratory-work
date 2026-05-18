class Node:
    """Вузол AVL-дерева для пріоритетної черги."""
    def __init__(self, value, priority):
        """Ініціалізація вузла з значенням та пріоритетом."""
        self.value = value       
        self.priority = priority  
        self.left = None          
        self.right = None         
        self.height = 1          

class AVLPriorityQueue:
    """Пріоритетна черга на основі AVL-дерева."""
    def __init__(self):
        """Ініціалізація порожньої пріоритетної черги."""
        self.root = None  
        self.size = 0     


    def height(self, node):
        """Повертає висоту вузла або 0, якщо вузол None."""
        return node.height if node else 0

    def balance_factor(self, node):
        """Обчислює фактор балансу вузла."""
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def update_height(self, node):
        """Оновлює висоту вузла на основі висот його дітей."""
        if node:
            node.height = 1 + max(self.height(node.left), self.height(node.right))


    def rotate_right(self, y):
        """Виконує праву ротацію навколо вузла y."""
        x = y.left
        t = x.right
        x.right = y
        y.left = t
        self.update_height(y)
        self.update_height(x)
        return x

    def rotate_left(self, x):
        """Виконує ліву ротацію навколо вузла x."""
        y = x.right
        t = y.left
        y.left = x
        x.right = t
        self.update_height(x)
        self.update_height(y)
        return y

    def rebalance(self, node):
        """Перебалансовує вузол після вставки або видалення."""
        self.update_height(node)
        bf = self.balance_factor(node)

       
        if bf > 1:
            if self.balance_factor(node.left) < 0:
                node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

    
        if bf < -1:
            if self.balance_factor(node.right) > 0:
                node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node


    def insert(self, node, value, priority):
        """Рекурсивно вставляє новий вузол у дерево."""
        if node is None:
            return Node(value, priority)

        if priority < node.priority:
            node.right = self.insert(node.right, value, priority)
        else:
            node.left = self.insert(node.left, value, priority)

        return self.rebalance(node)

    def enqueue(self, value, priority):
        """1. Вставка елемента до черги."""
        self.root = self.insert(self.root, value, priority)
        self.size += 1

    def delete_rightmost(self, node):
        """Видаляє та повертає найправіший вузол піддерева."""
        if node.right is None:
            return node.left, node

        node.right, removed = self.delete_rightmost(node.right)
        return self.rebalance(node), removed

    def dequeue(self):
        """2. Видалення та повернення елемента з найвищим пріоритетом."""
        if self.root is None:
            raise IndexError("Черга порожня")

        self.root, removed = self.delete_rightmost(self.root)
        self.size -= 1
        return removed.value, removed.priority

    def peek(self):
        """3. Перегляд елемента з найвищим пріоритетом без видалення."""
        if self.root is None:
            raise IndexError("Черга порожня")

        node = self.root
        while node.right:
            node = node.right
        return node.value, node.priority

    def inorder_traversal(self, node, result):
        if node:
            self.inorder_traversal(node.left, result)
            result.append((node.value, node.priority))
            self.inorder_traversal(node.right, result)

    def view(self):
        """Повертає список всіх елементів від найвищого пріоритету до найнижчого."""
        result = []
        self.inorder_traversal(self.root, result)
        result.reverse()
        return result

    def is_empty(self):
        return self.size == 0

    def print_tree_structure(self, node, prefix="", is_left=False):
        if node:
            connector = "├── " if is_left else "└── "
            print(prefix + connector + f"[P:{node.priority}] {node.value}")
            extension = "│   " if is_left else "    "
            self.print_tree_structure(node.left, prefix + extension, True)
            self.print_tree_structure(node.right, prefix + extension, False)

if __name__ == "__main__":
    pq = AVLPriorityQueue()

    pq.enqueue("Сходити в магазин", 3)
    pq.enqueue("Здати лабу", 1)
    pq.enqueue("Прийти додому", 5)
    pq.enqueue("Випити кави", 2)

    print("Структура AVL-дерева:")
    pq.print_tree_structure(pq.root)

    print("\nВміст черги (від найважливішого):")
    for v, p in pq.view():
        print(f"  Пріоритет {p}: {v}")

    print(f"\nЗараз у черзі елементів: {pq.size}")
    print(f"Найвищий пріоритет (peek): {pq.peek()}")

    print("\nВидалення елементів (dequeue):")
    while not pq.is_empty():
        val, prio = pq.dequeue()
        print(f"  Вилучено: {val} (пріоритет {prio})")
