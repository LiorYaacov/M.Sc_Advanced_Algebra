    #################
    ##  Addition   ##
    #################
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
    

        #######################
        ##  Multiplication   ##
        #######################
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


    def show_field_orders(self):
        try:
            p = int(self.Fp_E.get())
        except ValueError:
            messagebox.showerror("Values Error", "Please enter valid integers")
            return

        add_group_order,mul_group_order = Fp.group_orders(Fp(1,int(self.Fp_E.get())))
        
        self.results_TB.insert(tk.END, f"(|F{p}|,+) = {add_group_order}\n")
        self.results_TB.insert(tk.END, f"(|F{p}|,*) = {mul_group_order}\n")