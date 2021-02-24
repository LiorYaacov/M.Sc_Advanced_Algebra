import tkinter as tk


class test_gui:

    def __init__(self,main):

        self.main = main

        self.build_GUI()
    

    def build_GUI(self):

        # Title Frame
        self.title_frame = tk.Frame(self.main,width=600,height=50, \
                                    highlightthickness=1, highlightbackground="#FFFFFF")
        self.title_frame.grid(row=0,column=0)

        # Middle Frame
        self.middle_frame = tk.Frame(self.main, width=600,height=250, \
                                     highlightthickness=1,highlightbackground="#FFFFFF")
        self.middle_frame.grid()
            # Left-Middle Frame
        self.left_middle_frame = tk.Frame(self.middle_frame,width=300,height=250, \
                                          highlightthickness=1, highlightbackground="#FFFFFF")
        self.left_middle_frame.grid(row=1,column=0,sticky=tk.E)
            # Right-Middle Frame
        self.right_middle_frame = tk.Frame(self.middle_frame,width=300,height=250, \
                                           highlightthickness=1, highlightbackground="#FFFFFF")
        self.right_middle_frame.grid(row=1,column=1,sticky=tk.E)

            # Left-Middle Frames:
                # Top Frame
        self.left_middle_title_frame = tk.Frame(self.left_middle_frame,width=300,height=50, \
                                                highlightthickness=1, highlightbackground="#FFFFFF")
        self.left_middle_title_frame.grid(row=0,column=0)
                # Field and Numbers Frame
        self.field_frame = tk.Frame(self.left_middle_frame,width=300,height=50, \
                                                highlightthickness=1, highlightbackground="#FFFFFF")
        self.field_frame.grid(row=1,column=0)
                    # P1
        # self.p1_L = tk.Label(self.field_frame, text="p1:")
        # self.p1_L.grid(row=0,column=0)
        self.p1_frame = tk.Frame(self.field_frame,width=90,height=50, \
                                                highlightthickness=1, highlightbackground="#FFFFFF")
        self.p1_frame.grid(row=0,column=0)

        self.p1_L = tk.Label(self.p1_frame, text="p1:")
        self.p1_L.grid(row=0,column=0)
        self.p1_B = tk.Entry(self.p1_frame)
        self.p1_B.grid(row=0,column=1)
        #self.p1_B.grid_columnconfigure(0, weight=1)
        


                    # Fp
        self.Fp_frame = tk.Frame(self.field_frame,width=120,height=50, \
                                                highlightthickness=1, highlightbackground="#FFFFFF")
        self.Fp_frame.grid(row=0,column=1)
                    # P2
        self.p2_frame = tk.Frame(self.field_frame,width=90,height=50, \
                                                highlightthickness=1, highlightbackground="#FFFFFF")
        self.p2_frame.grid(row=0,column=2)

                # Calculator Frame
        self.calc_frame = tk.Frame(self.left_middle_frame,width=300,height=50, bg='blue', \
                                                highlightthickness=1, highlightbackground="#FFFFFF")
        self.calc_frame.grid(row=2,column=0)


            # Right-Middle Frames:
                # Top Frame
        self.right_middle_title_frame = tk.Frame(self.right_middle_frame,width=300,height=50, \
                                                highlightthickness=1, highlightbackground="#FFFFFF")
        self.right_middle_title_frame.grid(row=0,column=0)
                # Smooth Curve Frame
        self.smooth_curve_frame = tk.Frame(self.right_middle_frame,width=300,height=50, \
                                                highlightthickness=1, highlightbackground="#FFFFFF")
        self.smooth_curve_frame.grid(row=2,column=0)
                    # Smooth Curve - a
        self.smooth_a_frame = tk.Frame(self.smooth_curve_frame,width=150,height=50, \
                                                highlightthickness=1, highlightbackground="#FFFFFF")
        self.smooth_a_frame.grid(row=0,column=0)
                    # Smooth Curve - b
        self.smooth_b_frame = tk.Frame(self.smooth_curve_frame,width=150,height=50, \
                                                highlightthickness=1, highlightbackground="#FFFFFF")
        self.smooth_b_frame.grid(row=0,column=1)


        # Results Frame
        self.results_frame = tk.Frame(self.main, width=600,height=300,\
                                      highlightthickness=1, highlightbackground="white")
        self.results_frame.grid(row=2)

        self.results_TB = tk.Text(self.results_frame)
        self.results_TB.grid(row=0,column=0)
        self.results_clear_B = tk.Button(self.results_frame, text="Clear")#, command=self.clear_TB)
        self.results_clear_B.grid(row=1, column=0)


        # Bottom Frame
        self.bottom_frame = tk.Frame(self.main,width=600,height=50, \
                                     highlightthickness=1,highlightbackground="purple")
        self.bottom_frame.grid(row=3,columnspan=2)


        ''' ----- Buttons ----- '''
        self.ele_add_order = tk.Button(self.calc_frame, text="o(p),+")
        self.ele_add_order.grid(row=0,column=0)
        self.add_B = tk.Button(self.calc_frame, text="+", bg="yellow")
        self.add_B.grid(row=0, column=1)
        self.sub_B = tk.Button(self.calc_frame, text="-", bg="yellow")
        self.sub_B.grid(row=0, column=2)
        self.mul_B = tk.Button(self.calc_frame, text="*", bg="yellow")
        self.mul_B.grid(row=0, column=3)
        self.div_B = tk.Button(self.calc_frame, text="/", bg="yellow")
        self.div_B.grid(row=0, column=4)
        self.ele_mul_order = tk.Button(self.calc_frame, text="o(p),*")
        self.ele_mul_order.grid(row=0,column=5)


root = tk.Tk()
test_gui(root)
root.mainloop()

# Switching to windows