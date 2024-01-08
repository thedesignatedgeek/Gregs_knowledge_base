#
# "mine" learning theme.
# -------------------------------
# Inspired by the Clam, Alt and other themes.
# Written by G.D. Walters
# Copyright © 2023,2024 by G.D. Walters  <thedesignatedgeek@gmail.com>
#
#====================================================
# Version 0.1.1
# December 4, 2023
#====================================================
# Still to do: 02/01/2023
# ---------------------------------------------------
#
#====================================================
# Change log
#----------------------------------------------------
# 12/04/2023 - Initial creation
#----------------------------------------------------

package require Tk 8.6



namespace eval ttk::theme::mine {
    variable version 0.1.1
    package provide ttk::theme::mine $version
    variable colors
    array set colors {
        -disabledfg     gray54
        -frame          black
        -window         "#ffffff"
        -dark           black
        -darker         "#c3c3c3"
        -lighter        "#eeebe7"
        -lightcolor     snow
        -selectbackground   darkslategray1
        -selectforeground   "#000000"
        -alternate          "#aaaaaa"
        -disabledcolor  gray54
        -bgcolor        #B3B092
        -fgcolor        black
        -activebgcolor  gray66
        -troughcolor    gray45
        -barcolor       royalblue3
        -fieldbgcolor   black
        -bordercolor    dimgray
        -tvwindow       #cdbd70
        -tvwindowdisabled  #cdaf95
        -texthighlight   darkslategray1
    }



    # Settings
    ttk::style theme create mine -parent clam -settings {

        ttk::style configure "." \
            -background $colors(-bgcolor) \
            -foreground $colors(-fgcolor) \
            -bordercolor $colors(-frame) \
            -darkcolor $colors(-dark) \
            -lightcolor $colors(-lightcolor) \
            -troughcolor $colors(-troughcolor) \
            -focuscolor $colors(-selectbackground) \
            -selectbackground $colors(-selectbackground) \
            -selectforeground $colors(-selectforeground) \
            -activebgcolor  gray66 \
            -fieldbgcolor   gray39 \
            -barcolor $colors(-barcolor) \
            -selectborderwidth 0 \
            -borderwidth 2 \
            -font TkDefaultFont \
        ;

        ttk::style map "." \
            -background [list active $colors(-activebgcolor)] \
            -foreground [list disabled $colors(-disabledfg)] \
            -selectbackground [list  !focus $colors(-selectbackground)] \
            -selectforeground [list  !focus white] \
            -embossed [list disabled 1]
        ;



        #proc load_images {imgdir} {
        #    variable I
        #    foreach file [glob -directory $imgdir *.png] {
        #        set img [file tail [file rootname $file]]
        #        set I($img) [image create photo -file $file -format png]
        #    }
        #}

        # Load the images for TCheckbutton and TRadiobutton
        #load_images [file join [file dirname [info script]] cornsilk]

        # Force a black foreground to the filedialogs
        option add *TkFDialog*foreground black
        option add *TkChooseDir*foreground black
        
        # ====================================
        # TButton
        # ====================================
        ttk::style configure TButton \
            -anchor center -width -11 -padding {1 1 1 1} -relief raised \
            -shiftrelief 2 -highlightthickness 1 -highlightcolor $colors(-frame) \
            -background $colors(-bgcolor) -foreground $colors(-fgcolor) \
            -bordercolor $colors(-bgcolor)
            
        ttk::style map TButton -relief {
            {pressed !disabled} sunken
            {active !disabled}  raised
            } -highlightcolor {alternate black}
                        
        ttk::style map TButton \
            -background [list \
                 disabled $colors(-frame) \
                 pressed $colors(-darker) \
                 active $colors(-lighter)] \
            -lightcolor [list pressed $colors(-darker)] \
            -darkcolor [list pressed $colors(-darker)] \
            -bordercolor [list alternate "#000000"] \
        ;

        # ====================================
        # Toolbutton
        # ====================================
        ttk::style configure Toolbutton \
            -anchor center -padding 1 -relief flat \
            -shiftrelief 2
            
        ttk::style map Toolbutton \
            -relief [list \
                disabled flat \
                selected sunken \
                pressed sunken \
                active raised] \
            -background [list \
                disabled $colors(-frame) \
                pressed $colors(-darker) \
                active $colors(-lighter)] \
            -lightcolor [list pressed $colors(-darker)] \
            -darkcolor [list pressed $colors(-darker)] \
        ;
        
        # --------------------------------------------------
        # TLabel
        # --------------------------------------------------
        ttk::style configure TLabel \
            -background $colors(-bgcolor) -bordercolor $colors(-frame) \
            -borderwidth 1 -relief groove -anchor center
        # --------------------------------------------------
        # TFrame
        # --------------------------------------------------
        ttk::style configure TFrame \
            -background $colors(-bgcolor) -borderwidth 2 -relief groove
        ttk::style configure Flat.TFrame -relief flat -borderwidth 5
        ttk::style configure Sunken.TFrame -relief sunken -borderwidth 5

        # --------------------------------------------------
        # TLabelframe
        # --------------------------------------------------
        ttk::style configure TLabelframe \
            -background $colors(-bgcolor) -bordercolor $colors(-fgcolor) \
            -labeloutside false -labelmargins {0 0 0 4} \
            -borderwidth 1 -relief groove 
        ttk::style configure TLabelframe.Label \
            -background $colors(-bgcolor)\
            -foreground $colors(-fgcolor) -padding {12 6} \
			-font TkDefaultFont -size 12 -weight bold
        # --------------------------------------------------
        # TProgressbar
        # --------------------------------------------------
        ttk::style configure TProgressbar -background skyblue2        
    }
}
