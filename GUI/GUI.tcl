#############################################################################
# Generated by PAGE version 6.0.1
#  in conjunction with Tcl version 8.6
#  Feb 28, 2021 05:49:05 AM +0200  platform: Windows NT
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    tk_messageBox -title Error -message  "You must open project files from within PAGE."
    exit}


if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_font_dft_desc)  TkDefaultFont
set vTcl(actual_gui_font_dft_name)  TkDefaultFont
set vTcl(actual_gui_font_text_desc)  TkTextFont
set vTcl(actual_gui_font_text_name)  TkTextFont
set vTcl(actual_gui_font_fixed_desc)  TkFixedFont
set vTcl(actual_gui_font_fixed_name)  TkFixedFont
set vTcl(actual_gui_font_menu_desc)  TkMenuFont
set vTcl(actual_gui_font_menu_name)  TkMenuFont
set vTcl(actual_gui_font_tooltip_desc)  TkDefaultFont
set vTcl(actual_gui_font_tooltip_name)  TkDefaultFont
set vTcl(actual_gui_font_treeview_desc)  TkDefaultFont
set vTcl(actual_gui_font_treeview_name)  TkDefaultFont
set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(actual_gui_menu_active_fg)  #000000
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Relative
}




proc vTclWindow.top44 {base} {
    global vTcl
    if {$base == ""} {
        set base .top44
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -background $vTcl(actual_gui_bg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 777x696+443+0
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1916 1053
    wm minsize $top 120 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "Advanced Algebra - Final Project"
    vTcl:DefineAlias "$top" "Toplevel1" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    frame $top.fra45 \
        -borderwidth 2 -relief groove -background $vTcl(actual_gui_bg) \
        -height 376 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -width 365 
    vTcl:DefineAlias "$top.fra45" "Finite_Fields" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.fra45
    label $site_3_0.lab47 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 20 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {Finite Fields} 
    vTcl:DefineAlias "$site_3_0.lab47" "Label1" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab48 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text P1 
    vTcl:DefineAlias "$site_3_0.lab48" "Label2" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab49 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text P2 
    vTcl:DefineAlias "$site_3_0.lab49" "Label2_1" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab50 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Fp 
    vTcl:DefineAlias "$site_3_0.lab50" "Label2_2" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent51 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 34 
    vTcl:DefineAlias "$site_3_0.ent51" "p1_E" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent53 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 34 
    vTcl:DefineAlias "$site_3_0.ent53" "p2_E" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent54 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 34 
    vTcl:DefineAlias "$site_3_0.ent54" "Fp_E" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but45 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -command show_field_orders \
        -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {Show Field Orders} 
    vTcl:DefineAlias "$site_3_0.but45" "field_orders_B" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but46 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -command addition_2 \
        -disabledforeground #a3a3a3 -font TkDefaultFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text + 
    vTcl:DefineAlias "$site_3_0.but46" "add_B" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but47 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text - 
    vTcl:DefineAlias "$site_3_0.but47" "sub_B" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but48 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text x 
    vTcl:DefineAlias "$site_3_0.but48" "mul_B" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but49 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text / 
    vTcl:DefineAlias "$site_3_0.but49" "div_B" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but50 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {inv (+)} 
    vTcl:DefineAlias "$site_3_0.but50" "Button2" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but51 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {inv (*)} 
    vTcl:DefineAlias "$site_3_0.but51" "Button2_1" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but52 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {o(p), +} 
    vTcl:DefineAlias "$site_3_0.but52" "Button2_1_1" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but53 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {o(p), *} 
    vTcl:DefineAlias "$site_3_0.but53" "Button2_1_1_1" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab54 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 14 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {Exponentiation by Squaring} 
    vTcl:DefineAlias "$site_3_0.lab54" "Label1_1" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab55 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Base 
    vTcl:DefineAlias "$site_3_0.lab55" "Label2_3" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab56 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Exp 
    vTcl:DefineAlias "$site_3_0.lab56" "Label2_3_1" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab57 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Modulo 
    vTcl:DefineAlias "$site_3_0.lab57" "Label2_3_1_1" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent58 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 34 
    vTcl:DefineAlias "$site_3_0.ent58" "base_E" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent59 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 34 
    vTcl:DefineAlias "$site_3_0.ent59" "exp_E" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent60 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 34 
    vTcl:DefineAlias "$site_3_0.ent60" "modulo_E" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but61 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Calculate 
    vTcl:DefineAlias "$site_3_0.but61" "Button3" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.lab47 \
        -in $site_3_0 -x 0 -relx 0.247 -y 0 -rely 0.028 -width 0 \
        -relwidth 0.477 -height 0 -relheight 0.115 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab48 \
        -in $site_3_0 -x 0 -relx 0.137 -y 0 -rely 0.17 -width 0 \
        -relwidth 0.093 -height 0 -relheight 0.059 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab49 \
        -in $site_3_0 -x 0 -relx 0.247 -y 0 -rely 0.169 -width 0 \
        -relwidth 0.093 -height 0 -relheight 0.059 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab50 \
        -in $site_3_0 -x 0 -relx 0.384 -y 0 -rely 0.169 -width 0 \
        -relwidth 0.093 -height 0 -relheight 0.059 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent51 \
        -in $site_3_0 -x 0 -relx 0.137 -y 0 -rely 0.225 -width 34 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.ent53 \
        -in $site_3_0 -x 0 -relx 0.247 -y 0 -rely 0.225 -width 34 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.ent54 \
        -in $site_3_0 -x 0 -relx 0.384 -y 0 -rely 0.225 -width 34 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but45 \
        -in $site_3_0 -x 0 -relx 0.521 -y 0 -rely 0.22 -width 107 -relwidth 0 \
        -height 24 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but46 \
        -in $site_3_0 -x 0 -relx 0.137 -y 0 -rely 0.338 -width 37 -relwidth 0 \
        -height 34 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but47 \
        -in $site_3_0 -x 0 -relx 0.329 -y 0 -rely 0.338 -width 37 -relwidth 0 \
        -height 34 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but48 \
        -in $site_3_0 -x 0 -relx 0.521 -y 0 -rely 0.338 -width 37 -relwidth 0 \
        -height 34 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but49 \
        -in $site_3_0 -x 0 -relx 0.712 -y 0 -rely 0.346 -width 37 -relwidth 0 \
        -height 34 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but50 \
        -in $site_3_0 -x 0 -relx 0.11 -y 0 -rely 0.479 -width 57 -relwidth 0 \
        -height 34 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but51 \
        -in $site_3_0 -x 0 -relx 0.301 -y 0 -rely 0.479 -width 57 -relwidth 0 \
        -height 34 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but52 \
        -in $site_3_0 -x 0 -relx 0.493 -y 0 -rely 0.479 -width 57 -relwidth 0 \
        -height 34 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but53 \
        -in $site_3_0 -x 0 -relx 0.685 -y 0 -rely 0.479 -width 57 -relwidth 0 \
        -height 34 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab54 \
        -in $site_3_0 -x 0 -relx 0.164 -y 0 -rely 0.62 -width 0 \
        -relwidth 0.641 -height 0 -relheight 0.115 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab55 \
        -in $site_3_0 -x 0 -relx 0.356 -y 0 -rely 0.732 -width 0 \
        -relwidth 0.093 -height 0 -relheight 0.059 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab56 \
        -in $site_3_0 -x 0 -relx 0.466 -y 0 -rely 0.732 -width 0 \
        -relwidth 0.093 -height 0 -relheight 0.059 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab57 \
        -in $site_3_0 -x 0 -relx 0.575 -y 0 -rely 0.732 -width 0 \
        -relwidth 0.121 -height 0 -relheight 0.059 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent58 \
        -in $site_3_0 -x 0 -relx 0.356 -y 0 -rely 0.789 -width 34 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.ent59 \
        -in $site_3_0 -x 0 -relx 0.466 -y 0 -rely 0.789 -width 34 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.ent60 \
        -in $site_3_0 -x 0 -relx 0.603 -y 0 -rely 0.798 -width 34 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but61 \
        -in $site_3_0 -x 0 -relx 0.438 -y 0 -rely 0.873 -width 57 -relwidth 0 \
        -height 24 -relheight 0 -anchor nw -bordermode ignore 
    frame $top.fra62 \
        -borderwidth 2 -relief groove -background $vTcl(actual_gui_bg) \
        -height 374 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -width 365 
    vTcl:DefineAlias "$top.fra62" "Elliptic_Curves" vTcl:WidgetProc "Toplevel1" 1
    set site_3_0 $top.fra62
    label $site_3_0.lab45 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 20 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {Elliptic Curves} 
    vTcl:DefineAlias "$site_3_0.lab45" "Label1_2" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab48 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text a 
    vTcl:DefineAlias "$site_3_0.lab48" "Label2_4" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent51 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 34 
    vTcl:DefineAlias "$site_3_0.ent51" "ec_a_E" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab52 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text b 
    vTcl:DefineAlias "$site_3_0.lab52" "Label2_4_1" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab53 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text p 
    vTcl:DefineAlias "$site_3_0.lab53" "Label2_4_1_1" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent54 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 34 
    vTcl:DefineAlias "$site_3_0.ent54" "ec_p_E" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab55 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 14 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Projective 
    vTcl:DefineAlias "$site_3_0.lab55" "Label3" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but56 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {Group Order} 
    vTcl:DefineAlias "$site_3_0.but56" "ec_group_order_B" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but57 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Identity 
    vTcl:DefineAlias "$site_3_0.but57" "ec_identity_B" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab58 \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 14 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Affine 
    vTcl:DefineAlias "$site_3_0.lab58" "Label3_1" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but59 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {Show Points} 
    vTcl:DefineAlias "$site_3_0.but59" "ec_show_points_B" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but60 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {Hasse's Bound} 
    vTcl:DefineAlias "$site_3_0.but60" "hasses_B" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab61 \
        -activebackground #f9f9f9 -activeforeground black -anchor w \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 14 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Points 
    vTcl:DefineAlias "$site_3_0.lab61" "Label3_1_1" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab62 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 12 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text P 
    vTcl:DefineAlias "$site_3_0.lab62" "Label4" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab63 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 12 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Q 
    vTcl:DefineAlias "$site_3_0.lab63" "Label4_1" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent64 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 34 
    vTcl:DefineAlias "$site_3_0.ent64" "ec_p_x_E" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent65 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 34 
    vTcl:DefineAlias "$site_3_0.ent65" "ec_p_y_E" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent66 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 34 
    vTcl:DefineAlias "$site_3_0.ent66" "ec_q_x_E" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent67 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 34 
    vTcl:DefineAlias "$site_3_0.ent67" "ec_q_y_E" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but68 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text -P 
    vTcl:DefineAlias "$site_3_0.but68" "ec_p_inverse_B" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but69 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text o(P) 
    vTcl:DefineAlias "$site_3_0.but69" "ec_p_order_B" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but70 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text <P> 
    vTcl:DefineAlias "$site_3_0.but70" "ec_p_generate_B" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but71 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text nP 
    vTcl:DefineAlias "$site_3_0.but71" "ec_p_nP_B" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but72 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text P+Q 
    vTcl:DefineAlias "$site_3_0.but72" "ec_p_q_addition_B_1" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent73 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 34 
    vTcl:DefineAlias "$site_3_0.ent73" "ec_p_n_E" vTcl:WidgetProc "Toplevel1" 1
    label $site_3_0.lab74 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font {-family {Segoe UI} -size 12 -weight normal -slant roman -underline 0 -overstrike 0} \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text n 
    vTcl:DefineAlias "$site_3_0.lab74" "Label4_1_1" vTcl:WidgetProc "Toplevel1" 1
    entry $site_3_0.ent75 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 34 
    vTcl:DefineAlias "$site_3_0.ent75" "ec_b_E" vTcl:WidgetProc "Toplevel1" 1
    button $site_3_0.but77 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text {Print Points} 
    vTcl:DefineAlias "$site_3_0.but77" "ec_print_points_B" vTcl:WidgetProc "Toplevel1" 1
    place $site_3_0.lab45 \
        -in $site_3_0 -x 0 -relx 0.274 -y 0 -rely 0.027 -width 0 \
        -relwidth 0.477 -height 0 -relheight 0.115 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab48 \
        -in $site_3_0 -x 0 -relx 0.329 -y 0 -rely 0.16 -width 0 \
        -relwidth 0.093 -height 0 -relheight 0.059 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent51 \
        -in $site_3_0 -x 0 -relx 0.329 -y 0 -rely 0.214 -width 34 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab52 \
        -in $site_3_0 -x 0 -relx 0.466 -y 0 -rely 0.16 -width 0 \
        -relwidth 0.093 -height 0 -relheight 0.059 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab53 \
        -in $site_3_0 -x 0 -relx 0.63 -y 0 -rely 0.16 -width 0 \
        -relwidth 0.093 -height 0 -relheight 0.059 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent54 \
        -in $site_3_0 -x 0 -relx 0.63 -y 0 -rely 0.214 -width 34 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab55 \
        -in $site_3_0 -x 0 -relx 0.055 -y 0 -rely 0.348 -width 0 \
        -relwidth 0.258 -height 0 -relheight 0.083 -anchor nw \
        -bordermode ignore 
    place $site_3_0.but56 \
        -in $site_3_0 -x 0 -relx 0.384 -y 0 -rely 0.358 -width 77 -relwidth 0 \
        -height 24 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but57 \
        -in $site_3_0 -x 0 -relx 0.644 -y 0 -rely 0.358 -width 47 -relwidth 0 \
        -height 24 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab58 \
        -in $site_3_0 -x 0 -relx 0.055 -y 0 -rely 0.481 -width 0 \
        -relwidth 0.258 -height 0 -relheight 0.083 -anchor nw \
        -bordermode ignore 
    place $site_3_0.but59 \
        -in $site_3_0 -x 0 -relx 0.384 -y 0 -rely 0.481 -width 77 -relwidth 0 \
        -height 24 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but60 \
        -in $site_3_0 -x 0 -relx 0.493 -y 0 -rely 0.556 -width 97 -relwidth 0 \
        -height 24 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab61 \
        -in $site_3_0 -x 0 -relx 0.055 -y 0 -rely 0.615 -width 0 \
        -relwidth 0.258 -height 0 -relheight 0.083 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab62 \
        -in $site_3_0 -x 0 -relx 0.384 -y 0 -rely 0.634 -width 0 \
        -relwidth 0.093 -height 0 -relheight 0.056 -anchor nw \
        -bordermode ignore 
    place $site_3_0.lab63 \
        -in $site_3_0 -x 0 -relx 0.575 -y 0 -rely 0.634 -width 0 \
        -relwidth 0.093 -height 0 -relheight 0.056 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent64 \
        -in $site_3_0 -x 0 -relx 0.384 -y 0 -rely 0.695 -width 34 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.ent65 \
        -in $site_3_0 -x 0 -relx 0.384 -y 0 -rely 0.775 -width 34 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.ent66 \
        -in $site_3_0 -x 0 -relx 0.575 -y 0 -rely 0.695 -width 34 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.ent67 \
        -in $site_3_0 -x 0 -relx 0.575 -y 0 -rely 0.775 -width 34 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but68 \
        -in $site_3_0 -x 0 -relx 0.11 -y 0 -rely 0.882 -width 47 -relwidth 0 \
        -height 24 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but69 \
        -in $site_3_0 -x 0 -relx 0.274 -y 0 -rely 0.882 -width 47 -relwidth 0 \
        -height 24 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but70 \
        -in $site_3_0 -x 0 -relx 0.438 -y 0 -rely 0.882 -width 47 -relwidth 0 \
        -height 24 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but71 \
        -in $site_3_0 -x 0 -relx 0.767 -y 0 -rely 0.882 -width 47 -relwidth 0 \
        -height 24 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but72 \
        -in $site_3_0 -x 0 -relx 0.603 -y 0 -rely 0.882 -width 47 -relwidth 0 \
        -height 24 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.ent73 \
        -in $site_3_0 -x 0 -relx 0.795 -y 0 -rely 0.695 -width 34 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.lab74 \
        -in $site_3_0 -x 0 -relx 0.795 -y 0 -rely 0.634 -width 0 \
        -relwidth 0.093 -height 0 -relheight 0.056 -anchor nw \
        -bordermode ignore 
    place $site_3_0.ent75 \
        -in $site_3_0 -x 0 -relx 0.466 -y 0 -rely 0.214 -width 34 -relwidth 0 \
        -height 20 -relheight 0 -anchor nw -bordermode ignore 
    place $site_3_0.but77 \
        -in $site_3_0 -x 0 -relx 0.63 -y 0 -rely 0.481 -width 77 -relwidth 0 \
        -height 24 -relheight 0 -anchor nw -bordermode ignore 
    button $top.but64 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Reset 
    vTcl:DefineAlias "$top.but64" "Button4" vTcl:WidgetProc "Toplevel1" 1
    vTcl::widgets::ttk::scrolledtext::CreateCmd $top.scr78 \
        -borderwidth 2 -relief groove -background $vTcl(actual_gui_bg) \
        -height 75 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -width 125 
    vTcl:DefineAlias "$top.scr78" "results_TB" vTcl:WidgetProc "Toplevel1" 1

    $top.scr78.01 configure -background white \
        -font TkTextFont \
        -foreground black \
        -height 3 \
        -highlightbackground #d9d9d9 \
        -highlightcolor black \
        -insertbackground black \
        -insertborderwidth 3 \
        -selectbackground blue \
        -selectforeground white \
        -width 10 \
        -wrap none
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.fra45 \
        -in $top -x 0 -relx 0.013 -y 0 -rely 0.026 -width 0 -relwidth 0.47 \
        -height 0 -relheight 0.49 -anchor nw -bordermode ignore 
    place $top.fra62 \
        -in $top -x 0 -relx 0.502 -y 0 -rely 0.026 -width 0 -relwidth 0.47 \
        -height 0 -relheight 0.487 -anchor nw -bordermode ignore 
    place $top.but64 \
        -in $top -x 0 -relx 0.476 -y 0 -rely 0.938 -width 47 -relwidth 0 \
        -height 24 -relheight 0 -anchor nw -bordermode ignore 
    place $top.scr78 \
        -in $top -x 0 -relx 0.013 -y 0 -rely 0.534 -width 0 -relwidth 0.97 \
        -height 0 -relheight 0.391 -anchor nw -bordermode ignore 
    } ;# end vTcl:withBusyCursor 

    vTcl:FireEvent $base <<Ready>>
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top44 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}

