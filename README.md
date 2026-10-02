# Python Software Engineering & Computer Science Fundamentals

[![Language](https://img.shields.io/badge/Language-Python%203.x-blue.svg)](https://www.python.org/)
[![Focus](https://img.shields.io/badge/Focus-OOP%20%7C%20Design%20Patterns%20%7C%20DSA-success.svg)]()
[![Author](https://img.shields.io/badge/Author-Ahmed%20Hamaydi-orange.svg)](https://github.com/ahmedhamaydi)

A modular, production-focused repository demonstrating **Object-Oriented Design (OOD)**, **Software Architecture Patterns**, and **Data Structures & Algorithms (DSA)** in Python. Built with clean code practices, type annotations, and Big-O computational efficiency analysis.

---

## 📁 Repository Architecture

```text
python-software-engineering/
├── oop_and_design_patterns/       # Clean architecture, design patterns, and OOP systems
│   ├── discount_strategy_pattern.py     # Strategy Pattern using ABCs and runtime polymorphism
│   ├── media_catalogue_polymorphism.py  # Inheritance hierarchy & custom exception handling
│   ├── budget_app.py                    # Multi-category ledger with balance & transfer mechanics
│   ├── polygon_area_calculator.py       # Geometric modeling with OOP class hierarchies
│   ├── email_simulator.py               # State management and message dispatch simulation
│   ├── isbn_validator.py                # Checksum validation and input sanitization
│   └── salary_tracker.py                # Payroll calculations and record tracking
│
├── algorithms/                    # Core algorithms with computational complexity analysis
│   ├── shortest_path_dijkstra.py        # Dijkstra's shortest path algorithm for weighted graphs
│   ├── merge_sort.py                    # Divide-and-conquer stable sorting (O(n log n))
│   ├── quicksort.py                     # In-place pivot partitioning sort
│   ├── selection_sort.py                # Comparison sort implementation
│   ├── bisection_method.py              # Numerical root-finding algorithm
│   ├── luhn_algorithm.py                # Checksum formula for credit card / identity numbers
│   └── tower_of_hanoi.py                # Recursive state-space puzzle solver
│
├── data_structures_and_graphs/    # Graph traversals and constraint satisfaction
│   ├── breadth_first_search.py          # Level-order traversal & shortest hop discovery
│   ├── depth_first_search.py            # Exhaustive path exploration & cycle detection
│   ├── n_queens.py                      # Backtracking constraint satisfaction algorithm
│   ├── adjacency_matrix_converter.py    # Graph representation transformation (List ⇄ Matrix)
│   └── fibonacci_memoization.py         # Dynamic programming & recursion optimization
│
├── .gitignore                     # Python bytecode, environment, and cache exclusion
└── README.md                      # Comprehensive technical documentation
```

---

## 🏗️ 1. Object-Oriented Design & Architectural Patterns

### Strategy Design Pattern (`discount_strategy_pattern.py`)
* **Concept:** Utilizes Python's `abc` module (`ABC`, `@abstractmethod`) to define interchangeable discount algorithms decoupled from the client context.
* **Key Components:**
  * `DiscountStrategy` (Abstract Base Class): Enforces contract definitions via `is_applicable()` and `apply_discount()`.
  * Concrete Strategies: `PercentageDiscount`, `FixedAmountDiscount`, and tiered customer pricing.
  * Adheres to the **Open/Closed Principle (OCP)**: New pricing strategies can be introduced without modifying existing client code.

### Inheritance, Polymorphism & Custom Exceptions (`media_catalogue_polymorphism.py`)
* **Concept:** Multi-level class hierarchies modeling media items (`Movie`, `TVSeries`, etc.).
* **Key Components:**
  * Defines specialized `MediaError(Exception)` for structured error propagation.
  * Overrides `__str__()` for polymorphic string representation across derived classes.
  * Enforces strict parameter boundary checks (durations, episode counts, release dates).

### Encapsulation & Ledger Management (`budget_app.py`)
* **Concept:** Encapsulated state management tracking financial ledgers across multiple categories (`Food`, `Clothing`, `Entertainment`).
* **Key Components:**
  * Robust deposit, withdrawal, and inter-category transfer pipelines with fund verification.
  * Formatted output rendering with custom ASCII expense-percentage charting.

---

## ⚡ 2. Computational Complexity & Algorithm Analysis

| Algorithm | Category | Time (Best) | Time (Average) | Time (Worst) | Space Complexity |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Merge Sort** | Sorting (Divide & Conquer) | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n)$ |
| **Quicksort** | Sorting (Partitioning) | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n \log n)$ | $\mathcal{O}(n^2)$ | $\mathcal{O}(\log n)$ |
| **Selection Sort** | Sorting (In-place) | $\mathcal{O}(n^2)$ | $\mathcal{O}(n^2)$ | $\mathcal{O}(n^2)$ | $\mathcal{O}(1)$ |
| **Dijkstra's Algorithm** | Shortest Path (Greedy) | $\mathcal{O}((V + E) \log V)$ | $\mathcal{O}((V + E) \log V)$ | $\mathcal{O}(V^2)$ | $\mathcal{O}(V)$ |
| **Breadth-First Search (BFS)** | Graph Traversal | $\mathcal{O}(V + E)$ | $\mathcal{O}(V + E)$ | $\mathcal{O}(V + E)$ | $\mathcal{O}(V)$ |
| **Depth-First Search (DFS)** | Graph Traversal | $\mathcal{O}(V + E)$ | $\mathcal{O}(V + E)$ | $\mathcal{O}(V + E)$ | $\mathcal{O}(V)$ |
| **N-Queens Problem** | Backtracking | $\mathcal{O}(N)$ | $\mathcal{O}(N!)$ | $\mathcal{O}(N!)$ | $\mathcal{O}(N)$ |
| **Bisection Method** | Numerical Root Finding | $\mathcal{O}(1)$ | $\mathcal{O}(\log(\frac{b-a}{\epsilon}))$ | $\mathcal{O}(\log(\frac{b-a}{\epsilon}))$ | $\mathcal{O}(1)$ |
| **Luhn Algorithm** | Validation / Checksum | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | $\mathcal{O}(n)$ | $\mathcal{O}(1)$ |

---

## 🚀 3. Getting Started

### Prerequisites
* Python 3.8 or higher installed on your system.

### Running Any Module
Clone the repository and run any module directly:

```bash
# Clone the repository
git clone https://github.com/ahmedhamaydi/python-software-engineering.git

# Move into directory
cd python-software-engineering

# Run the Strategy Pattern module
python oop_and_design_patterns/discount_strategy_pattern.py

# Run Dijkstra's Shortest Path Algorithm
python algorithms/shortest_path_dijkstra.py

# Run the N-Queens Backtracking Solver
python data_structures_and_graphs/n_queens.py
```

---

## 👨‍💻 Author

**Ahmed Hamaydi**  
*Aspiring Computer Engineer*  
* University of Huddersfield — BEng (Hons) Electronic Engineering & Computer Systems *(Predicted 1st Class)*  
* **GitHub:** [@ahmedhamaydi](https://github.com/ahmedhamaydi)  
* **Email:** [ahmedhamaydi1914@gmail.com](mailto:ahmedhamaydi1914@gmail.com)
