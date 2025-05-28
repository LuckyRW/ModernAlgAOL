import tkinter as tk
from tkinter import messagebox

class frame:
    def __init__(self, master):
        self.root = master
        self.root.geometry("1200x800") 
        self.root.title("Ring checker")

        self.entries = []
        self.entries_add = []
        self.entries_mul = []

        input_frame = tk.Frame(self.root)
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Enter size of multiplication table (n x n):").pack()
        self.n_entry = tk.Entry(input_frame, width=5)
        self.n_entry.pack(side=tk.LEFT, padx=5)
        tk.Button(input_frame, text="Generate Table", command=self.generate_tables).pack(side=tk.LEFT)

        instructions_frame1= tk.Frame(self.root)
        instructions_frame1.pack(pady=1)
        instructions_frame2= tk.Frame(self.root)
        instructions_frame2.pack(pady=1)
        instructions_frame3= tk.Frame(self.root)
        instructions_frame3.pack(pady=1)
        tk.Label(instructions_frame1, text="Insert your addition and multiplicative tables! Please make sure your input is indeed at least a ring").pack(side=tk.LEFT)
        tk.Label(instructions_frame2, text="The program will check if it is a ring based on additive group being abelian, multiplicative associativity, and distributive property, and then checks what properties it has").pack(side=tk.LEFT)
        tk.Label(instructions_frame3, text="please keep in mind i havent implemented caps check yet, use all caps!").pack(side=tk.LEFT)


        main_frame = tk.Frame(root)
        main_frame.pack(fill=tk.BOTH, expand=True)
 
        canvas_container = tk.Frame(main_frame)
        canvas_container.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(200, 0))  

        canvas = tk.Canvas(canvas_container, width=800, height=600)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        v_scrollbar = tk.Scrollbar(canvas_container, orient=tk.VERTICAL, command=canvas.yview)
        v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        h_scrollbar = tk.Scrollbar(root, orient=tk.HORIZONTAL, command=canvas.xview)
        h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X, padx=50) 
        
        canvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

        content_frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=content_frame, anchor="nw")

        content_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        
        self.canvas = canvas

        self.button_frame = tk.Frame(content_frame)
        self.button_frame.pack(pady=10)

        self.sample_frame = tk.Frame(content_frame)
        self.sample_frame.pack(pady=5)
        tk.Label(self.sample_frame, text="Sample Tables:").pack()
        
        sample_frame_row1 = tk.Frame(self.sample_frame)
        sample_frame_row1.pack()
        tk.Button(sample_frame_row1, text="Commutative ring (Zero ring)", 
                 command=self.generate_sample_no_identity).pack(side=tk.LEFT, padx=5)
        tk.Button(sample_frame_row1, text="Field ring", 
                command=self.generate_field_sample).pack(side=tk.LEFT, padx=5)
        tk.Button(sample_frame_row1, text="Commutative ring with unity",
                command=self.generate_commutative_ring_with_unity_sample).pack(side=tk.LEFT, padx=5)
        
        # Second row of sample buttons
        sample_frame_row2 = tk.Frame(self.sample_frame)
        sample_frame_row2.pack()
        tk.Button(sample_frame_row2, text="Non-distributive multiplication", 
                command=self.generate_non_distributive_sample).pack(side=tk.LEFT, padx=5)
        tk.Button(sample_frame_row2, text="Boolean Ring", 
                command=self.generate_boolean_ring_sample).pack(side=tk.LEFT, padx=5)
        tk.Button(sample_frame_row2, text="Ring",   
                command=self.generate_ring_sample).pack(side=tk.LEFT, padx=5)
        
        # Third row of sample buttons
        sample_frame_row3 = tk.Frame(self.sample_frame)
        sample_frame_row3.pack()
        tk.Button(sample_frame_row3, text="Non-abelian addition", 
                 command=self.generate_non_abelian_addition).pack(side=tk.LEFT, padx=5)
        tk.Button(sample_frame_row3, text="Non-associative multiplication", 
                command=self.generate_non_associative_sample).pack(side=tk.LEFT, padx=5)
        

        self.parent_frame = tk.Frame(content_frame)
        self.parent_frame.pack(fill=tk.BOTH, expand=True)

        self.left_frame = tk.Frame(self.parent_frame)
        self.left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        self.right_frame = tk.Frame(self.parent_frame)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.button_frame = tk.Frame(content_frame)
        self.button_frame.pack(side=tk.BOTTOM,pady=10)

        self.check_frame = tk.Frame(content_frame)
        self.check_frame.pack(pady=10)
        
        self.results_text = tk.Text(content_frame, height=20, width=60)
        self.results_text.pack(pady=10)
    
    def generate_sample_no_identity(self):
        self.n_entry.delete(0, tk.END)
        self.n_entry.insert(0, "3")
        self.generate_tables()
        add_table = [
            ['A', 'B', 'C'],
            ['B', 'C', 'A'],
            ['C', 'A', 'B']
        ]

        mul_table = [
            ['A', 'A', 'A'],
            ['A', 'A', 'A'],
            ['A', 'A', 'A']
        ]
        self.fill_table(add_table,mul_table)
    
    def generate_field_sample(self):
        self.n_entry.delete(0, tk.END)
        self.n_entry.insert(0, "3")
        self.generate_tables()
        add_table = [
            ['A', 'B', 'C'],
            ['B', 'C', 'A'],
            ['C', 'A', 'B']
        ]
        mul_table = [
            ['A', 'A', 'A'],
            ['A', 'B', 'C'],
            ['A', 'C', 'B']
        ]
        self.fill_table(add_table, mul_table)
    
    def generate_non_distributive_sample(self):
        self.n_entry.delete(0, tk.END)
        self.n_entry.insert(0, "3")
        self.generate_tables()
        add_table = [
            ['A', 'B', 'C'],
            ['B', 'C', 'A'],
            ['C', 'A', 'B']
        ]
        mul_table = [
            ['A', 'A', 'A'],
            ['A', 'B', 'B'],
            ['A', 'B', 'C']
        ]
        self.fill_table(add_table, mul_table)
    
    def generate_boolean_ring_sample(self):
        self.n_entry.delete(0, tk.END)
        self.n_entry.insert(0, "2")
        self.generate_tables()
        add_table = [
            ['A', 'B'],
            ['B', 'A']
        ]
        mul_table = [
            ['A', 'A'],
            ['A', 'B']
        ]
        self.fill_table(add_table, mul_table)
    
    def generate_non_abelian_addition(self):
        self.n_entry.delete(0, tk.END)
        self.n_entry.insert(0, "6")
        self.generate_tables()
        add_table = [
            ['A', 'B', 'C', 'D', 'E', 'F'],
            ['B', 'A', 'E', 'F', 'C', 'D'],
            ['C', 'F', 'A', 'E', 'D', 'B'],
            ['D', 'E', 'F', 'A', 'B', 'C'],
            ['E', 'D', 'B', 'C', 'F', 'A'],
            ['F', 'C', 'D', 'B', 'A', 'E']
        ]
        mul_table = [
            ['A', 'B', 'C', 'D', 'E', 'F'],
            ['B', 'A', 'C', 'D', 'E', 'F'],
            ['C', 'B', 'A', 'D', 'E', 'F'],
            ['D', 'C', 'B', 'A', 'E', 'F'],
            ['E', 'D', 'C', 'B', 'A', 'F'],
            ['F', 'E', 'D', 'C', 'B', 'A']
        ]
        self.fill_table(add_table, mul_table)
    
    def generate_non_associative_sample(self):
        self.n_entry.delete(0, tk.END)
        self.n_entry.insert(0, "3")
        self.generate_tables()
        add_table = [
            ['A', 'B', 'C'],
            ['B', 'C', 'A'],
            ['C', 'A', 'B']
        ]
        mul_table = [
            ['A', 'C', 'C'],
            ['C', 'B', 'B'],
            ['C', 'B', 'A']
        ]
        self.fill_table(add_table, mul_table)
    
    def generate_commutative_ring_with_unity_sample(self):
        self.n_entry.delete(0, tk.END)
        self.n_entry.insert(0, "4")
        self.generate_tables()
        add_table = [
            ['A', 'B', 'C', 'D'],
            ['B', 'C', 'D', 'A'],
            ['C', 'D', 'A', 'B'],
            ['D', 'A', 'B', 'C']
        ]
        mul_table = [
            ['A', 'A', 'A', 'A'],  
            ['A', 'B', 'C', 'D'],  
            ['A', 'C', 'A', 'C'],  
            ['A', 'D', 'C', 'B']  
        ]
        self.fill_table(add_table, mul_table)
        
    def generate_ring_sample(self):
        self.n_entry.delete(0, tk.END)
        self.n_entry.insert(0, "4")
        self.generate_tables()
        add_table = [
            ['A', 'B', 'C', 'D'],
            ['B', 'A', 'D', 'C'],
            ['C', 'D', 'A', 'B'],
            ['D', 'C', 'B', 'A']
        ]
        mul_table = [
            ['A', 'A', 'A', 'A'],
            ['A', 'B', 'C', 'D'],
            ['A', 'A', 'A', 'A'],
            ['A', 'B', 'C', 'D']
        ]
        self.fill_table(add_table, mul_table)

    def fill_table(self,add_table,mul_table):
        for i in range(len(add_table)):
            for j in range(len(add_table[i])):
                self.entries_add[i][j].delete(0, tk.END)
                self.entries_add[i][j].insert(0, add_table[i][j])

        for i in range(len(mul_table)):
            for j in range(len(mul_table[i])):
                self.entries_mul[i][j].delete(0, tk.END)
                self.entries_mul[i][j].insert(0, mul_table[i][j])
        
    def generate_tables(self):
        self.generate_table_additive()
        self.generate_table_multiplicative()
        self.put_buttons()

        self.right_frame.update_idletasks()
        self.right_frame.master.update_idletasks()
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        self.resize_window()
    def resize_window(self):
        width = self.right_frame.winfo_width()
        height = self.right_frame.winfo_height()

        self.root.geometry(f"{width + 800}x{height + 800}")
        self.root.update_idletasks()
        
        

    
    def put_buttons(self):
        for widget in self.button_frame.winfo_children():
            widget.destroy()
        for widget in self.check_frame.winfo_children():
            widget.destroy()
        tk.Button(self.check_frame, text="Check Ring", 
                 command=self.check_ring).pack(side=tk.LEFT, padx=5)
    
    def check_ring(self):
        self.print_tables()
        results = []

        if not self.check_valid_tables() or not self.add_check_valid_tables():
            messagebox.showerror("Invalid Tables", "The tables entries are not closed under the defined set. Please check again!")
            return
        if not self.add_check_abelian()[0]:
            messagebox.showerror("Non-Abelian Addition", "The addition group is not abelian: " + self.add_check_abelian()[1])
            return
        if not self.check_associative()[0]:
            messagebox.showerror("Non-Associative Multiplication", "The multiplication table is not associative: " + self.check_associative()[1])
            return
        if not self.check_distributive()[0]:
            messagebox.showerror("Non-Distributive Multiplication", "The multiplication table does not satisfy the distributive law: " + self.check_distributive()[1])
            return
        if self.check_commutative()[0]:
            results.append("Commutative: Yes |" + self.check_commutative()[1])
        else:
            results.append("Commutative: No")
        if self.check_identity()[0]:
            results.append("Unity element: Yes |" + self.check_identity()[1])
        else:
            results.append("Unity: No")
        if self.check_zero_divisor()[0]:
            results.append("Exists zero divisor? : Yes |" + self.check_zero_divisor()[1])
        else:
            results.append("Exists zero divisor? : No")
        if self.check_inverse()[0]:
            results.append("All non-zero elements are units: Yes |" + self.check_inverse()[1])
        else:
            results.append("All non-zero elements are units: No")
        if self.check_inverse()[0] and self.check_identity()[0]: #by Wedderburn's little theorem, this is enough to check if it is a field
            results.append("Analysis: \nThis is a field! the multiplicative group is commutative, \ndoesnt have zero divisors, has a unity element, and all non-zero elements are units. \n It is known that fields are also both integral domains and division rings! \n A known example of a field is Z/pZ, where p is a prime \nnumber.")
        elif self.check_commutative()[0] and self.check_identity()[0]:
            results.append("Analysis: \nThis is a commutative ring with unity! It is neither a \ndivision ring nor an integral domain as it has zero divisors and does not have inverses for all non-zero elements.\n A known example of a ring of this type is Z/nZ, where n is a composite number.")
        elif self.check_commutative()[0] and self.check_identity()[0] == False:
            results.append("Analysis: \nThis is a commutative ring! The multiplicative group is \ncommutative, but has no unity element. \n It is neither division ring or integral domain \nas both integral domains and division rings requires \nAT LEAST a unity element.\n A known example of a ring of this type is the zero ring, \nwhere all elements are equal to zero.")
        elif self.check_identity()[0] and self.check_commutative()[0] == False:
            results.append("Analysis: \nThis is a ring with unity! It is associative, has an unity element, but is not commutative. \n It isn't a division ring as there doesnt exist finite strictly skew fields by Wedderburn's little theorem, and it is not an integral domain as it has to be commutative.")
        elif self.check_identity()[0] == False and self.check_commutative()[0] == False:
            results.append("Analysis: \nThis is a ring! \nDoesnt have a unity element, is not commutative, and has zero divisors. \n It is neither a division ring nor an integral domain as it has no unity element.\n A known example of a ring of this type is the ring of even square matrices.")
        self.results_text.delete(1.0, tk.END)
        self.results_text.insert(tk.END, "\n".join(results))
        print("\n".join(results)) 

    def generate_table_additive(self):
        for widget in self.left_frame.winfo_children():
            widget.destroy()
        self.entries_add.clear()

        n = int(self.n_entry.get())

        labels = [self.number_to_letters(i) for i in range(n)]
        for i in range(n + 1):
            row_entries = []
            for j in range(n + 1):
                if i == 0 and j == 0:
                    tk.Label(self.left_frame, text="+", width=4).grid(row=0, column=0)
                elif i == 0:
                    tk.Label(self.left_frame, text=labels[j - 1], width=4).grid(row=0, column=j)
                elif j == 0:
                    tk.Label(self.left_frame, text=labels[i - 1], width=4).grid(row=i, column=0)
                else:
                    entry = tk.Entry(self.left_frame, width=4, justify='center')
                    entry.grid(row=i, column=j)
                    row_entries.append(entry)
            if row_entries:
                self.entries_add.append(row_entries)
    def generate_table_multiplicative(self):
        for widget in self.right_frame.winfo_children():
            widget.destroy()
        self.entries_mul.clear()

        n = int(self.n_entry.get())

        labels = [self.number_to_letters(i) for i in range(n)]
        for i in range(n + 1):
            row_entries = []
            for j in range(n + 1):
                if i == 0 and j == 0:
                    tk.Label(self.right_frame, text="×", width=4).grid(row=0, column=0)
                elif i == 0:
                    tk.Label(self.right_frame, text=labels[j - 1], width=4).grid(row=0, column=j)
                elif j == 0:
                    tk.Label(self.right_frame, text=labels[i - 1], width=4).grid(row=i, column=0)
                else:
                    entry = tk.Entry(self.right_frame, width=4, justify='center')
                    entry.grid(row=i, column=j)
                    row_entries.append(entry)
            if row_entries:
                self.entries_mul.append(row_entries)
    def check_valid_tables(self):
        n = int(self.n_entry.get())
        labels_mul = [self.number_to_letters(i) for i in range(n)]
        for row in self.entries_mul:
            for entry in row:
                if entry.get() not in labels_mul:
                    return False
        return True
    def multiply(self, a, b):
        n = int(self.n_entry.get())
        labels = [self.number_to_letters(i) for i in range(n)]
        if a == self.add_check_identity()[2] or b == self.add_check_identity()[2]:
            return self.add_check_identity()[2]
        a_index = labels.index(a)
        b_index = labels.index(b)
        return self.entries_mul[a_index][b_index].get()
    def add(self, a, b):
        n = int(self.n_entry.get())
        labels = [self.number_to_letters(i) for i in range(n)]
        a_index = labels.index(a)
        b_index = labels.index(b)
        return self.entries_add[a_index][b_index].get()
    def check_associative(self):
        n = int(self.n_entry.get())
        labels = [self.number_to_letters(i) for i in range(n)]
        for a in labels:
            for b in labels:
                for c in labels:
                    print(f"Checking associativity for: {a}, {b}, {c}")
                    left = self.multiply(a, self.multiply(b, c))
                    right = self.multiply(self.multiply(a, b), c)
                    print(f"Left: {left}, Right: {right}")
                    if left != right:
                        reason = f"Not associative for: {a}, {b}, {c} -> {left} != {right}"
                        print(reason)
                        return False, reason
        reason = "All combinations are associative"
        print(reason)
        return True, reason
    def add_check_associative(self):
        n = int(self.n_entry.get())
        labels = [self.number_to_letters(i) for i in range(n)]
        for a in labels:
            for b in labels:
                for c in labels:
                    print(f"Checking additive associativity for: {a}, {b}, {c}")
                    left = self.add(a, self.add(b, c))
                    right = self.add(self.add(a, b), c)
                    print(f"Left: {left}, Right: {right}")
                    if left != right:
                        reason = f"Not additive associative for: {a}, {b}, {c} -> {left} != {right}"
                        print(reason)
                        return False, reason
        reason = "All combinations are additive associative"
        print(reason)
        return True, reason
    def check_commutative(self):
        n = int(self.n_entry.get())
        labels = [self.number_to_letters(i) for i in range(n)]
        for a in labels:
            for b in labels:
                print(f"Checking commutativity for: {a}, {b}")
                if self.multiply(a, b) != self.multiply(b, a):
                    reason = f"Not commutative for: {a}, {b} -> {self.multiply(a, b)} != {self.multiply(b, a)}"
                    print(reason)
                    return False, reason
        reason = "All combinations are commutative"
        print(reason)
        return True, reason
    def add_check_commutative(self):
        n = int(self.n_entry.get())
        labels = [self.number_to_letters(i) for i in range(n)]
        for a in labels:
            for b in labels:
                print(f"Checking additive commutativity for: {a}, {b}")
                if self.add(a, b) != self.add(b, a):
                    reason = f"Not additive commutative for: {a}, {b} -> {self.add(a, b)} != {self.add(b, a)}"
                    print(reason)
                    return False, reason
        reason = "All combinations are additive commutative"
        print(reason)
        return True, reason
    def check_identity(self):
        n = int(self.n_entry.get())
        labels = [self.number_to_letters(i) for i in range(n)]
        for a in labels:
            found_identity = True
            for b in labels:
                if self.multiply(a, b) != b or self.multiply(b, a) != b:
                    found_identity = False
                    break
            if found_identity:
                reason = f"Identity found: {a}"
                print(reason)
                return True, reason, a
        reason = "No identity found"
        print(reason)
        return False, reason
    def add_check_identity(self):
        n = int(self.n_entry.get())
        labels = [self.number_to_letters(i) for i in range(n)]
        for a in labels:
            found_identity = True
            for b in labels:
                if self.entries_add[labels.index(a)][labels.index(b)].get() != b:
                    found_identity = False
                    break
            if found_identity:
                reason = f"Additive identity found: {a}"
                return True, reason, a
        reason = "No additive identity found"
        print(reason)
        return False, reason
    def check_zero_divisor(self):
        n = int(self.n_entry.get())
        labels = [self.number_to_letters(i) for i in range(n)]

        add_id_result = self.add_check_identity()
        if not add_id_result[0]:
            reason = "No additive identity found, cannot check zero divisors."
            print(reason)
            return False, reason
        add_id = add_id_result[2]

        for i, a in enumerate(labels):
            for j, b in enumerate(labels):
                if a == add_id or b == add_id:
                    continue
                prod = self.multiply(a, b)
                if prod == add_id:
                    reason = f"Zero divisor found: {a} * {b} = {add_id}"
                    print(reason)
                    return True, reason
        reason = "No zero divisors found"
        print(reason)
        return False, reason
    def check_inverse(self):
        n = int(self.n_entry.get())
        labels = [self.number_to_letters(i) for i in range(n)]
        
        if self.check_identity()[0] is False:
            reason = "No identity element, so no inverses."
            print(reason)
            return False, reason
        identity = self.check_identity()[2]
        for a in labels:
            if a == self.add_check_identity()[2]:
                print(f"Skipping additive identity: {a}")
                continue
            print(f"Checking inverse for: {a}")
            has_inverse = False
            for b in labels:
                print(f"Checking if {a} has an inverse with {b} -> {self.multiply(a, b)} vs {identity}")
                if self.multiply(a, b) == identity and self.multiply(b, a) == identity:
                    has_inverse = True
                    break
            if not has_inverse:
                reason = f"No inverse for element: {a}"
                print(reason)
                return False, reason

        reason = "All nonzero elements have inverses."
        print(reason)
        return True, reason
    def add_check_inverse(self):
        n = int(self.n_entry.get())
        labels = [self.number_to_letters(i) for i in range(n)]
        
        if self.add_check_identity()[0] is False:
            reason = "No additive identity, so no inverses."
            print(reason)
            return False, reason
        identity = self.add_check_identity()[2]
        for a in labels:
            if a == self.add_check_identity()[2]:
                print(f"Skipping additive identity: {a}")
                continue
            print(f"Checking additive inverse for: {a}")
            has_inverse = False
            for b in labels:
                print(f"Checking if {a} has an additive inverse with {b} -> {self.add(a, b)} vs {identity}")
                if self.add(a, b) == identity and self.add(b, a) == identity:
                    has_inverse = True
                    break
            if not has_inverse:
                reason = f"No additive inverse for element: {a}"
                print(reason)
                return False, reason

        reason = "All elements have additive inverses."
        print(reason)
        return True, reason
    def add_check_valid_tables(self):
        n = int(self.n_entry.get())
        labels_add = [self.number_to_letters(i) for i in range(n)]
        for row in self.entries_add:
            for entry in row:
                if entry.get() not in labels_add:
                    return False
        return True
    def add_check_abelian(self):
        if self.add_check_associative()[0] and self.add_check_identity()[0] and self.add_check_inverse()[0] and self.add_check_commutative()[0]:
            return True, "Addition is abelian."
        else:
            if not self.add_check_associative()[0]:
                reason = "Addition is not associative." + self.add_check_associative()[1]
                return False, reason
            if not self.add_check_identity()[0]:
                reason = "No additive identity found." + self.add_check_identity()[1]
                return False, reason
            if not self.add_check_inverse()[0]:
                reason = "Not all elements have additive inverses." + self.add_check_inverse()[1]
                return False, reason
            if not self.add_check_commutative()[0]:
                reason = "Addition is not commutative." + self.add_check_commutative()[1]
                return False, reason
    def check_distributive(self):
        n = int(self.n_entry.get())
        labels = [self.number_to_letters(i) for i in range(n)]
        for a in labels:
            for b in labels:
                for c in labels:
                    print(f"Checking distributive law for: {a}, {b}, {c}")
                    print(f"Multiplying {a} with {self.add(b, c)} and comparing with {self.multiply(a, b)} + {self.multiply(a, c)}")
                    left = self.multiply(a, self.add(b, c))
                    right = self.add(self.multiply(a, b), self.multiply(a, c))
                    print(f"Left: {left}, Right: {right}")
                    if left != right:
                        reason = f"Distributive law fails for: {a}, {b}, {c} -> {left} != {right}"
                        print(reason)
                        return False, reason
        reason = "Distributive law holds for all combinations"
        print(reason)
        return True, reason
    def print_tables(self):
        print("Additive Table:")
        for row in self.entries_add:
            print([entry.get() for entry in row])
        print("\nMultiplicative Table:")
        for row in self.entries_mul:
            print([entry.get() for entry in row])
    
    def number_to_letters(self, n):
        result = ""
        n = int(n)
        while True:
            result = chr(65 + n % 26) + result
            n = n // 26 - 1
            if n < 0:
                break
        return result

if __name__ == "__main__":
    root = tk.Tk()
    app = frame(root)
    root.mainloop()