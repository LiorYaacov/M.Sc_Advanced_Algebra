# Switching to windows DONE

import tkinter as tk
from tkinter import messagebox
from finite_fields import Fp

class final_project:

    def __init__(self,main):
        self.main = main
        main.title("Advanced Algebra - Final Project")

        ''' Frames '''
        # Top Frame
        self.top_frame = tk.Frame(main, width=500, height=500, highlightthickness=1, highlightbackground="#FFFFFF")
        self.top_frame.grid()#row=0, column=0, padx=10, pady=5,columnspan=2)
        # Advanced Algebra - Final Project (Label)
        tk.Label(self.top_frame, text="Advanced Algebra - Final Project", font=("Arial Bold",20)).grid(row=1,column=0, padx=5, pady=5)

        # Middle Frame
        self.middle_frame = tk.Frame(main,width=250, height=400,highlightthickness=1, highlightbackground="#FFFFFF")
        self.middle_frame.grid(row=1,column=0,padx=10,pady=5,columnspan=1)
        
        # Projective Curves Frame
        self.elliptic_curve_frame = tk.Frame(main,width=250,height=300,highlightthickness=1,highlightbackground="#FFFF00")
        self.elliptic_curve_frame.grid(row=1,column=1,columnspan=1)
            # Title Frame
        self.EC_title_frame = tk.Frame(self.elliptic_curve_frame,width=250,height=50,highlightbackground="#FFFFFF")
        self.EC_title_frame.grid(row=0,column=0)

        tk.Label(self.EC_title_frame, text="Elliptic Curve").grid(row=0,column=0)
        # EC_title_canvas = tk.Canvas(self.EC_title_frame, width=250)
        # EC_title_canvas.grid(row=2,column=0)
        # img = tk.PhotoImage(file="Projective Curve Equation.gif")
        # EC_title_canvas.create_image(200,200,image=img)
        
        # path = "Projective Curve Equation.gif"
        # img = ImageTk.PhotoImage(Image.open(path))
        # panel = tk.Label(root, image = img)


        # Calculator Frame (inside Middle Frame)
        self.calc_frame = tk.Frame(self.middle_frame,width=400,height=100,highlightthickness=1, highlightbackground="#FFFFFF")
        self.calc_frame.grid(row=4,column=2,pady=15)
        # Exponentiation by Squaring Frame
        self.ebs_frame = tk.Frame(self.middle_frame, width=400,height=500,highlightthickness=1, highlightbackground="#FFFFFF")
        self.ebs_frame.grid(row=5,column=2,pady=15)

        # Results Frame
        self.results_frame = tk.Frame(main,width=500,height=200)
        self.results_frame.grid(row=2, column=0)


        self.Fp_L = tk.Label(self.middle_frame, text="Fp: ")
        self.Fp_L.grid(row=0,column=0, sticky=tk.W)

        self.Fp_E = tk.Entry(self.middle_frame, width=5)
        self.Fp_E.grid(row=0,column=1, sticky=tk.W)

        self.Fp_B = tk.Button(self.middle_frame, text="Show Field Orders", command=self.select_Fp)
        self.Fp_B.grid(row=0,column=2, sticky=tk.W)

        # Element
        self.p1_L = tk.Label(self.middle_frame, text="p1:").grid(row=2,column=0)
        self.p1_E = tk.Entry(self.middle_frame, width=5)
        self.p1_E.grid(row=2,column=1)
        self.p2_L = tk.Label(self.middle_frame, text="p2:").grid(row=3,column=0)
        self.p2_E = tk.Entry(self.middle_frame, width=5)
        self.p2_E.grid(row=3,column=1)

        # Addition, Subtraction, Multiplication and Division
        # Addition
        self.element_addition_B = tk.Button(self.calc_frame, text="+", command=self.addition)
        self.element_addition_B.grid(row=0,column=0)
        # Subtraction
        self.element_subtraction_B = tk.Button(self.calc_frame, text="-", command=self.subtraction)
        self.element_subtraction_B.grid(row=0,column=1)
        # Multiplication
        self.element_multiplication_B = tk.Button(self.calc_frame, text="*", command=self.multiplication)
        self.element_multiplication_B.grid(row=1,column=0)
        # Division
        self.element_division_B = tk.Button(self.calc_frame, text="/", command=self.division)
        self.element_division_B.grid(row=1,column=1)
        # Inverse
        self.element_add_inverse_B = tk.Button(self.calc_frame, text="inv (+)", command=lambda: self.inverse('add'))
        self.element_add_inverse_B.grid(row=2,column=0)
        self.element_mul_inverse_B = tk.Button(self.calc_frame, text="inv (*)", command=lambda: self.inverse('mul'))
        self.element_mul_inverse_B.grid(row=2,column=1)
        # Element's Order
        self.element_add_order_B = tk.Button(self.calc_frame, text="o(p),+", command=lambda: self.element_order('add'))
        self.element_add_order_B.grid(row=3,column=0)
        self.element_mul_order_B = tk.Button(self.calc_frame, text="o(p),*", command=lambda: self.element_order('mul'))
        self.element_mul_order_B.grid(row=3,column=1)
        # Exponentiation by Squaring
        self.base_L = tk.Label(self.ebs_frame, text="Base:").grid(row=5,column=0, sticky=tk.W)
        self.exp_L = tk.Label(self.ebs_frame, text="Exp:").grid(row=5,column=1, sticky=tk.W)
        self.modulo_L = tk.Label(self.ebs_frame, text="Modulo:").grid(row=5,column=2, sticky=tk.W)
        self.base_E = tk.Entry(self.ebs_frame, width=5)
        self.base_E.grid(row=6,column=0, sticky=tk.W)
        self.exp_E = tk.Entry(self.ebs_frame, width=5)
        self.exp_E.grid(row=6,column=1, sticky=tk.W)
        self.modulo_E = tk.Entry(self.ebs_frame, width=5)
        self.modulo_E.grid(row=6,column=2, sticky=tk.W)

        self.ebs_B = tk.Button(self.ebs_frame, text="Exponentiation by Squaring", command=self.ebs)
        self.ebs_B.grid(row=7,column=0, pady=10, columnspan=3)

        # Results
        self.results_TB = tk.Text(self.results_frame)
        self.results_TB.grid(row=0,column=0)
        self.results_clear_B = tk.Button(self.results_frame, text="Clear", command=self.clear_TB)
        self.results_clear_B.grid(row=1, column=0)


    
    def select_Fp(self):
        try:
            p = int(self.Fp_E.get())
        except ValueError:
            messagebox.showerror("Values Error", "Please enter valid integers")
            return

        add_group_order,mul_group_order = Fp.group_orders(Fp(1,int(self.Fp_E.get())))
        
        self.results_TB.insert(tk.END, f"(|F{p}|,+) = {add_group_order}\n")
        self.results_TB.insert(tk.END, f"(|F{p}|,*) = {mul_group_order}\n")
        
    def addition(self):
        
        try:
            p1 = int(self.p1_E.get())
            p2 = int(self.p2_E.get())
            p = int(self.Fp_E.get())
        except ValueError:
            messagebox.showerror("Values Error", "Please enter valid integers")
            return
        
        self.p1 = Fp(p1,p)
        self.p2 = Fp(p2,p)

        result = self.p1+self.p2

        # Print to GUI
        self.results_TB.insert(tk.END, f"{p1}+{p2} = {result} (mod {p})\n")
    
    def subtraction(self):
        try:
            p1 = int(self.p1_E.get())
            p2 = int(self.p2_E.get())
            p = int(self.Fp_E.get())
        except ValueError:
            messagebox.showerror("Values Error", "Please enter valid integers")
            return
        
        self.p1 = Fp(p1,p)
        self.p2 = Fp(p2,p)

        result = self.p1-self.p2

        # Print to GUI
        self.results_TB.insert(tk.END, f"{p1}-{p2} = {result} (mod {p})\n")
    
    def multiplication(self):
        try:
            p1 = int(self.p1_E.get())
            p2 = int(self.p2_E.get())
            p = int(self.Fp_E.get())
        except ValueError:
            messagebox.showerror("Values Error", "Please enter valid integers")
            return
        
        self.p1 = Fp(p1,p)
        self.p2 = Fp(p2,p)

        result = self.p1*self.p2

        # Print to GUI
        self.results_TB.insert(tk.END, f"{p1}*{p2} = {result} (mod {p})\n")
    
    def division(self):
        try:
            p1 = int(self.p1_E.get())
            p2 = int(self.p2_E.get())
            p = int(self.Fp_E.get())
        except ValueError:
            messagebox.showerror("Values Error", "Please enter valid integers")
            return

        self.p1 = Fp(p1,p)
        self.p2 = Fp(p2,p)

        result = self.p1/self.p2

        # Print to GUI
        if type(result) is not int:
            self.results_TB.insert(tk.END, f"{p1}/{p2} = {result}\n")
        else:
            self.results_TB.insert(tk.END, f"{p1}/{p2} = {result} (mod {p})\n")
    
    def inverse(self, method='mul'):

        try:
            p1 = int(self.p1_E.get())
            p = int(self.Fp_E.get())
        except ValueError:
            messagebox.showerror("Values Error", "Please enter valid integers")
            return
        
        self.p1 = Fp(p1,p)

        if method=='add':
            result = -self.p1.p
            # Print to GUI
            self.results_TB.insert(tk.END, f"inv({p1}),+ = {result} (mod {p})\n")
        elif method=='mul':
            result = self.p1.inverse()
            # Print to GUI
            self.results_TB.insert(tk.END, f"inv({p1}),* = {result} (mod {p})\n")
        # else:
        #     (-self.p1.p,self.p1.inverse)

    def element_order(self, method='add'):

        try:
            p1 = int(self.p1_E.get())
            p = int(self.Fp_E.get())
        except ValueError:
            messagebox.showerror("Values Error", "Please enter valid integers")
            return
        
        if method=='add':
            result = Fp.add_element_order(Fp(p1,p))
            # Print to GUI
            self.results_TB.insert(tk.END, f"o({p1}),+ = {result}\n")
        
        elif method=='mul':
            result = Fp.mul_element_order(Fp(p1,p))
            # Print to GUI
            self.results_TB.insert(tk.END, f"o({p1}),* = {result}\n")

    def ebs(self):

        try:
            base = int(self.base_E.get())
            exp = int(self.exp_E.get())
            mod = int(self.modulo_E.get())
        except ValueError:
            messagebox.showerror("Values Error", "Please enter valid integers")
            return

        p = Fp(base,mod)

        print(base,exp,mod)
        result = p.exp_by_square(base,exp,mod)

        # Print to GUI
        self.results_TB.insert(tk.END, f"{base}^{exp} = {result} (mod {mod})\n")

    def clear_TB(self):
        self.results_TB.delete("1.0", "end")
        
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