import tkinter as tk
from finite_fields import Fp

class final_project:

    def __init__(self,main):
        self.main = main
        main.title("Advanced Algebra - Final Project")
        #main.geometry('700x700')
        #main.config(bg="white")

        # Top Frame
        self.top_frame = tk.Frame(main, width=500, height=200, bg="white")
        self.top_frame.grid(row=0, column=0, padx=10, pady=5)

        # Advanced Algebra - Final Project (Label)
        tk.Label(self.top_frame, text="Advanced Algebra - Final Project", font=("Arial Bold",20)).grid(row=1,column=0, padx=5, pady=5)

        # Middle Frame
        self.middle_frame = tk.Frame(main,width=500, height=400)
        self.middle_frame.grid(row=1,column=0,padx=10,pady=5)
        # Calculator Frame (inside Middle Frame)
        self.calc_frame = tk.Frame(self.middle_frame,width=100,height=100)
        self.calc_frame.grid(row=3,column=2,pady=15)

        self.Fp_L = tk.Label(self.middle_frame, text="Fp: ")
        self.Fp_L.grid(row=0,column=0)

        self.Fp_E = tk.Entry(self.middle_frame, width=5)
        self.Fp_E.grid(row=0,column=1)

        self.Fp_B = tk.Button(self.middle_frame, text="Select", command=self.select_Fp)
        self.Fp_B.grid(row=0,column=2)
        #self.Fp_add_group_order_L = tk.Label(self.middle_frame, text="(Fp,+) Group Order: ").grid(row=1,column=0)
        #self.Fp_add_group_order = tk.Label(self.middle_frame, text="g")
        #self.Fp_add_group_order.grid(row=1,column=1)

        # Element
        self.p1_L = tk.Label(self.middle_frame, text="p1: ").grid(row=2,column=0)
        self.p1_E = tk.Entry(self.middle_frame, width=5)
        self.p1_E.grid(row=2,column=1)
        self.p2_L = tk.Label(self.middle_frame, text="p2: ").grid(row=2,column=2)
        self.p2_E = tk.Entry(self.middle_frame, width=5)
        self.p2_E.grid(row=2,column=3)

        # Addition, Subtraction, Multiplication and Division
        self.element_addition_B = tk.Button(self.calc_frame, text="+", command=self.addition)
        self.element_addition_B.grid(row=0,column=0)

        self.element_subtraction_B = tk.Button(self.calc_frame, text="-", command=self.subtraction)
        self.element_subtraction_B.grid(row=0,column=1)

        self.element_multiplication_B = tk.Button(self.calc_frame, text="*", command=self.multiplication)
        self.element_multiplication_B.grid(row=1,column=0)

        self.element_division_B = tk.Button(self.calc_frame, text="/", command=self.division)
        self.element_division_B.grid(row=1,column=1)

        # Results
        self.result_L = tk.Label(self.calc_frame)
        self.result_L.grid(row=2,column=1)


    
    def select_Fp(self):
        add_group_order = finite_fields.add_group_order
        self.Fp_add_group_order.config(text=add_group_order)
        
    def addition(self):
        
        try:
            p1 = int(self.p1_E.get())
            p2 = int(self.p2_E.get())
            p = int(self.Fp_E.get())
        except ValueError:
            # TBD
            print("Please enter valid integers")
        
        self.p1 = Fp(p1,p)
        self.p2 = Fp(p2,p)

        result = self.p1+self.p2

        # Print to GUI
        self.result_L.config(text=f"{p1} + {p2} = {result} (mod {p})")
    
    def subtraction(self):
        try:
            p1 = int(self.p1_E.get())
            p2 = int(self.p2_E.get())
            p = int(self.Fp_E.get())
        except ValueError:
            # TBD
            print("Please enter valid integers")
        
        self.p1 = Fp(p1,p)
        self.p2 = Fp(p2,p)

        result = self.p1-self.p2

        # Print to GUI
        self.result_L.config(text=f"{p1} - {p2} = {result} (mod {p})")
    
    def multiplication(self):
        try:
            p1 = int(self.p1_E.get())
            p2 = int(self.p2_E.get())
            p = int(self.Fp_E.get())
        except ValueError:
            # TBD
            print("Please enter valid integers")
        
        self.p1 = Fp(p1,p)
        self.p2 = Fp(p2,p)

        result = self.p1*self.p2

        # Print to GUI
        self.result_L.config(text=f"{p1} * {p2} = {result} (mod {p})")
    
    def division(self):
        try:
            p1 = int(self.p1_E.get())
            p2 = int(self.p2_E.get())
            p = int(self.Fp_E.get())
        except ValueError:
            # TBD
            print("Please enter valid integers")
        
        self.p1 = Fp(p1,p)
        self.p2 = Fp(p2,p)

        result = self.p1/self.p2

        # Print to GUI
        self.result_L.config(text=f"{p1} / {p2} = {result} (mod {p})")
'''
        self.title_L = tk.Label(main, text="Advanced Algebra - Final Project", font = ("Arial Bold", 20))
        self.title_L.pack()

        self.Fp_L1 = tk.Label(main, text="Fp:").pack(side=tk.LEFT)
        self.Fp_E1 = tk.Entry(main, bd=2).pack(side=tk.LEFT)
        self.Fp_B1 = tk.Button(main, text="Select", command=lambda: self.select_Fp).pack(side=tk.RIGHT)

        self.Fp_add_order_L = tk.Label(main, text="(Fp, +) Order: ").pack(side=tk.LEFT)
        self.Fp_add_order = tk.Label(main).pack()
        self.Fp_mul_order = tk.Label(main).pack(side=tk.RIGHT)

        # Layout
        #self.selected_prime_L = tk.IntVar()
        #self.selected_prime_L.pack()
 '''   

    



root = tk.Tk()
main = final_project(root)
root.mainloop()