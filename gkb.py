#! /usr/bin/env python3
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 8.0
#  in conjunction with Tcl version 8.6
#    Jan 12, 2024 03:53:13 AM CST  platform: Linux

import tkinter as tk
import tkinter.ttk as ttk
from tkinter.constants import *
import os.path

_location = os.path.dirname(__file__)

import gkb_support

_bgcolor = "cornsilk4"
_fgcolor = "black"
_tabfg1 = "black"
_tabfg2 = "white"
_bgmode = "light"
_tabbg1 = "#d9d9d9"
_tabbg2 = "gray40"

_style_code_ran = 0


def _style_code():
    global _style_code_ran
    if _style_code_ran:
        return
    try:
        gkb_support.root.tk.call(
            "source", os.path.join(_location, "themes", "cornsilk-dark.tcl")
        )
    except:
        pass
    style = ttk.Style()
    style.theme_use("cornsilk-dark")
    style.configure(".", font="-family {DejaVu Sans} -size 11 -weight bold")
    _style_code_ran = 1


class Main:
    def __init__(self, top=None):
        """This class configures and populates the toplevel window.
        top is the toplevel containing window."""

        top.geometry("1010x827+809+248")
        top.minsize(1, 1)
        top.maxsize(4225, 1410)
        top.resizable(0, 0)
        top.title("Greg's Knowledge Base")
        top.configure(background="cornsilk4")
        top.configure(highlightbackground="cornsilk4")
        top.configure(highlightcolor="black")

        self.top = top
        self.StatusTime = tk.StringVar()
        self.msg2kwds = tk.StringVar()
        self.EntTopic = tk.StringVar()
        self.EntryKeywords1 = tk.StringVar()
        self.EditorMode = tk.StringVar()
        self.EntryKeyword = tk.StringVar()
        self.KwdTopic = tk.StringVar()
        self.ParamSQL = tk.StringVar()
        self.SearchResultsTitle = tk.StringVar()

        self.menubar = tk.Menu(
            top,
            font="-family {DejaVu Sans} -size 11 -weight bold",
            bg="cornsilk4",
            fg=_fgcolor,
        )
        top.configure(menu=self.menubar)

        _style_code()
        self.TFrame1 = ttk.Frame(self.top)
        self.TFrame1.place(x=0, y=0, height=750, width=1010)
        self.TFrame1.configure(relief="sunken")
        self.TFrame1.configure(borderwidth="2")
        self.TFrame1.configure(relief="sunken")

        self.FrameStatusBar = ttk.Frame(self.TFrame1)
        self.FrameStatusBar.place(x=3, y=696, height=50, width=1004)
        self.FrameStatusBar.configure(relief="sunken")
        self.FrameStatusBar.configure(borderwidth="2")
        self.FrameStatusBar.configure(relief="sunken")

        self.LabelStatusTime = ttk.Label(self.FrameStatusBar)
        self.LabelStatusTime.place(x=845, y=1, height=44, width=151)
        self.LabelStatusTime.configure(
            font="-family {DejaVu Sans} -size 11 -weight bold"
        )
        self.LabelStatusTime.configure(relief="sunken")
        self.LabelStatusTime.configure(anchor="center")
        self.LabelStatusTime.configure(justify="left")
        self.LabelStatusTime.configure(textvariable=self.StatusTime)
        self.StatusTime.set("""""")
        self.LabelStatusTime.configure(compound="left")

        self.FrameButtonBar = ttk.Frame(self.TFrame1)
        self.FrameButtonBar.place(x=3, y=2, height=50, width=1004)
        self.FrameButtonBar.configure(relief="sunken")
        self.FrameButtonBar.configure(borderwidth="2")
        self.FrameButtonBar.configure(relief="sunken")

        self.btnAbout = ttk.Button(self.FrameButtonBar)
        self.btnAbout.place(x=840, y=4, height=40, width=40)
        self.btnAbout.configure(command=gkb_support.on_btnAbout)
        photo_location = os.path.join(_location, "./graphics/information.png")
        global _img0
        _img0 = tk.PhotoImage(file=photo_location)
        self.btnAbout.configure(image=_img0)
        self.btnAbout.configure(compound="none")
        self.btnAbout.configure(style="Toolbutton")
        self.btnAbout_tooltip = ToolTip(self.btnAbout, """About""")

        self.btnExit = ttk.Button(self.FrameButtonBar)
        self.btnExit.place(x=951, y=4, height=42, width=42)
        self.btnExit.configure(command=gkb_support.on_btnExit)
        photo_location = os.path.join(_location, "./graphics/system-shutdown.png")
        global _img1
        _img1 = tk.PhotoImage(file=photo_location)
        self.btnExit.configure(image=_img1)
        self.btnExit.configure(compound="none")
        self.btnExit.configure(style="Toolbutton")
        self.btnExit_tooltip = ToolTip(self.btnExit, """Exit""")

        self.btnAdd = ttk.Button(self.FrameButtonBar)
        self.btnAdd.place(x=490, y=4, height=40, width=40)
        self.btnAdd.configure(command=gkb_support.on_btnAdd)
        photo_location = os.path.join(_location, "./graphics/list-add.png")
        global _img2
        _img2 = tk.PhotoImage(file=photo_location)
        self.btnAdd.configure(image=_img2)
        self.btnAdd.configure(compound="none")
        self.btnAdd.configure(style="Toolbutton")
        self.btnAdd_tooltip = ToolTip(self.btnAdd, """Add to database""")

        self.btnSQLShow = ttk.Button(self.FrameButtonBar)
        self.btnSQLShow.place(x=220, y=4, height=40, width=40)
        self.btnSQLShow.configure(command=gkb_support.on_btnSQLShow)
        photo_location = os.path.join(_location, "./graphics/database.png")
        global _img3
        _img3 = tk.PhotoImage(file=photo_location)
        self.btnSQLShow.configure(image=_img3)
        self.btnSQLShow.configure(compound="none")
        self.btnSQLShow.configure(style="Toolbutton")

        self.btnHelp = ttk.Button(self.FrameButtonBar)
        self.btnHelp.place(x=890, y=4, height=40, width=40)
        self.btnHelp.configure(command=gkb_support.on_btnHelp)
        photo_location = os.path.join(_location, "./graphics/question.png")
        global _img4
        _img4 = tk.PhotoImage(file=photo_location)
        self.btnHelp.configure(image=_img4)
        self.btnHelp.configure(compound="none")
        self.btnHelp.configure(style="Toolbutton")
        self.btnHelp_tooltip = ToolTip(self.btnHelp, """Help""")

        self.btnRemove = ttk.Button(self.FrameButtonBar)
        self.btnRemove.place(x=550, y=4, height=40, width=40)
        self.btnRemove.configure(command=gkb_support.on_btnRemove)
        photo_location = os.path.join(_location, "./graphics/list-remove.png")
        global _img5
        _img5 = tk.PhotoImage(file=photo_location)
        self.btnRemove.configure(image=_img5)
        self.btnRemove.configure(compound="none")
        self.btnRemove.configure(state="disabled")
        self.btnRemove.configure(style="Toolbutton")
        self.btnRemove_tooltip = ToolTip(self.btnRemove, """Remove Current record""")

        self.btnTopicEdit = ttk.Button(self.FrameButtonBar)
        self.btnTopicEdit.place(x=640, y=4, height=40, width=40)
        self.btnTopicEdit.configure(command=gkb_support.on_btnTopicEdit)
        photo_location = os.path.join(
            _location, "./graphics/accessories-text-editor.png"
        )
        global _img6
        _img6 = tk.PhotoImage(file=photo_location)
        self.btnTopicEdit.configure(image=_img6)
        self.btnTopicEdit.configure(compound="none")
        self.btnTopicEdit.configure(state="disabled")
        self.btnTopicEdit.configure(style="Toolbutton")
        self.btnTopicEdit_tooltip = ToolTip(self.btnTopicEdit, """Edit Topic""")

        self.TLabel9 = ttk.Label(self.FrameButtonBar)
        self.TLabel9.place(x=10, y=4, height=40, width=40)
        self.TLabel9.configure(font="-family {DejaVu Sans} -size 11 -weight bold")
        self.TLabel9.configure(relief="flat")
        self.TLabel9.configure(anchor="w")
        self.TLabel9.configure(justify="left")
        photo_location = os.path.join(_location, "./graphics/ChubbyOwl.png")
        global _img7
        _img7 = tk.PhotoImage(file=photo_location)
        self.TLabel9.configure(image=_img7)
        self.TLabel9.configure(compound="left")

        self.FrameMain = ttk.Frame(self.TFrame1)
        self.FrameMain.place(x=3, y=51, height=644, width=1004)
        self.FrameMain.configure(relief="sunken")
        self.FrameMain.configure(borderwidth="2")
        self.FrameMain.configure(relief="sunken")

        self.FrameKeywords = ttk.Frame(self.FrameMain)
        self.FrameKeywords.place(x=10, y=83, height=75, width=985)
        self.FrameKeywords.configure(relief="sunken")
        self.FrameKeywords.configure(borderwidth="2")
        self.FrameKeywords.configure(relief="sunken")

        self.TLabel2 = ttk.Label(self.FrameKeywords)
        self.TLabel2.place(x=6, y=2, height=24, width=115)
        self.TLabel2.configure(font="-family {DejaVu Sans} -size 11 -weight bold")
        self.TLabel2.configure(relief="flat")
        self.TLabel2.configure(anchor="center")
        self.TLabel2.configure(justify="left")
        self.TLabel2.configure(text="""Keywords:""")
        self.TLabel2.configure(compound="left")

        self.Message2 = tk.Message(self.FrameKeywords)
        self.Message2.place(x=10, y=25, height=44, width=965)
        self.Message2.configure(anchor="nw")
        self.Message2.configure(background="cornsilk4")
        self.Message2.configure(font="-family {DejaVu Sans} -size 11 -weight bold")
        self.Message2.configure(highlightbackground="cornsilk4")
        self.Message2.configure(padx="1")
        self.Message2.configure(pady="1")
        self.Message2.configure(text="""Message""")
        self.Message2.configure(textvariable=self.msg2kwds)
        self.msg2kwds.set("""Message""")
        self.Message2.configure(width=965)

        self.FrameHider = ttk.Frame(self.FrameMain)
        self.FrameHider.place(x=10, y=83, height=75, width=985)
        self.FrameHider.configure(relief="flat")
        self.FrameHider.configure(borderwidth="2")
        self.FrameHider.configure(relief="flat")

        self.FrameAbout = ttk.Frame(self.FrameMain)
        self.FrameAbout.place(x=10, y=160, height=475, width=985)
        self.FrameAbout.configure(relief="groove")
        self.FrameAbout.configure(borderwidth="2")
        self.FrameAbout.configure(relief="groove")

        self.TLableLogo = ttk.Label(self.FrameAbout)
        self.TLableLogo.place(x=10, y=2, height=60, width=60)
        self.TLableLogo.configure(font="-family {DejaVu Sans} -size 11 -weight bold")
        self.TLableLogo.configure(relief="flat")
        self.TLableLogo.configure(anchor="w")
        self.TLableLogo.configure(justify="left")
        self.TLableLogo.configure(text="""Tlabel""")
        photo_location = os.path.join(_location, "./graphics/logo.png")
        global _img8
        _img8 = tk.PhotoImage(file=photo_location)
        self.TLableLogo.configure(image=_img8)
        self.TLableLogo.configure(compound="left")

        self.TFrame4 = ttk.Frame(self.FrameAbout)
        self.TFrame4.place(x=10, y=70, height=395, width=965)
        self.TFrame4.configure(relief="sunken")
        self.TFrame4.configure(borderwidth="2")
        self.TFrame4.configure(relief="sunken")

        self.Message1 = tk.Message(self.TFrame4)
        self.Message1.place(x=4, y=4, height=334, width=955)
        self.Message1.configure(anchor="n")
        self.Message1.configure(background="cornsilk4")
        self.Message1.configure(borderwidth="2")
        self.Message1.configure(font="-family {DejaVu Sans} -size 11 -weight bold")
        self.Message1.configure(highlightbackground="cornsilk4")
        self.Message1.configure(justify="center")
        self.Message1.configure(padx="1")
        self.Message1.configure(pady="1")
        self.Message1.configure(relief="sunken")
        self.Message1.configure(
            text="""Greg's Knowledge Base

A database repository of some of my most helpful code snippets for PAGE and Python projects.

Project started 21 December, 2023

Written by Gregory Walters.

Copyright © 2023,2024 by Gregory Walters"""
        )
        self.Message1.configure(width=955)

        self.btnAboutDismiss = ttk.Button(self.TFrame4)
        self.btnAboutDismiss.place(x=433, y=350, height=30, width=98)
        self.btnAboutDismiss.configure(command=gkb_support.on_btnAboutDismiss)
        self.btnAboutDismiss.configure(text="""Dismiss""")
        self.btnAboutDismiss.configure(compound="left")

        self.TSeparator1 = ttk.Separator(self.FrameAbout)
        self.TSeparator1.place(x=102, y=52, width=870)

        self.TLabel3 = ttk.Label(self.FrameAbout)
        self.TLabel3.place(x=110, y=15, height=29, width=774)
        self.TLabel3.configure(font="-family {DejaVu Sans} -size 14 -weight bold")
        self.TLabel3.configure(relief="flat")
        self.TLabel3.configure(anchor="center")
        self.TLabel3.configure(justify="left")
        self.TLabel3.configure(text="""About""")
        self.TLabel3.configure(compound="left")

        self.FrameMainText = ttk.Frame(self.FrameMain)
        self.FrameMainText.place(x=10, y=160, height=475, width=985)
        self.FrameMainText.configure(relief="groove")
        self.FrameMainText.configure(borderwidth="2")
        self.FrameMainText.configure(relief="groove")

        self.btnMainDismiss = ttk.Button(self.FrameMainText)
        self.btnMainDismiss.place(x=820, y=10, height=30, width=118)
        self.btnMainDismiss.configure(command=gkb_support.on_btnMainDismiss)
        self.btnMainDismiss.configure(text="""Dismiss""")
        self.btnMainDismiss.configure(compound="left")

        self.TLabel8 = ttk.Label(self.FrameMainText)
        self.TLabel8.place(x=400, y=10, height=36, width=184)
        self.TLabel8.configure(font="-family {DejaVu Sans} -size 12 -weight bold")
        self.TLabel8.configure(relief="flat")
        self.TLabel8.configure(anchor="center")
        self.TLabel8.configure(justify="left")
        self.TLabel8.configure(text="""Search Results""")
        self.TLabel8.configure(compound="left")

        self.Scrolledtext1 = ScrolledText(self.FrameMainText)
        self.Scrolledtext1.place(x=4, y=60, height=415, width=976)
        self.Scrolledtext1.configure(background="white")
        self.Scrolledtext1.configure(exportselection="0")
        self.Scrolledtext1.configure(font="-family {DejaVu Sans} -size 11 -weight bold")
        self.Scrolledtext1.configure(highlightbackground="cornsilk4")
        self.Scrolledtext1.configure(insertborderwidth="3")
        self.Scrolledtext1.configure(selectbackground="#d9d9d9")
        self.Scrolledtext1.configure(wrap="none")

        self.FrameEditor = ttk.Frame(self.FrameMain)
        self.FrameEditor.place(x=10, y=160, height=475, width=985)
        self.FrameEditor.configure(relief="groove")
        self.FrameEditor.configure(borderwidth="2")
        self.FrameEditor.configure(relief="groove")

        self.TLabel6 = ttk.Label(self.FrameEditor)
        self.TLabel6.place(x=20, y=40, height=24, width=141)
        self.TLabel6.configure(font="-family {DejaVu Sans} -size 11 -weight bold")
        self.TLabel6.configure(relief="flat")
        self.TLabel6.configure(anchor="e")
        self.TLabel6.configure(justify="left")
        self.TLabel6.configure(text="""Topic:""")
        self.TLabel6.configure(compound="left")

        self.TLabel5 = ttk.Label(self.FrameEditor)
        self.TLabel5.place(x=20, y=73, height=24, width=141)
        self.TLabel5.configure(font="-family {DejaVu Sans} -size 11 -weight bold")
        self.TLabel5.configure(relief="flat")
        self.TLabel5.configure(anchor="e")
        self.TLabel5.configure(justify="left")
        self.TLabel5.configure(text="""Keywords:""")
        self.TLabel5.configure(compound="left")

        self.TFrame2 = ttk.Frame(self.FrameEditor)
        self.TFrame2.place(x=5, y=116, height=355, width=975)
        self.TFrame2.configure(relief="groove")
        self.TFrame2.configure(borderwidth="2")
        self.TFrame2.configure(relief="groove")

        self.Scrolledtext3 = ScrolledText(self.TFrame2)
        self.Scrolledtext3.place(x=0, y=0, height=355, width=969)
        self.Scrolledtext3.configure(background="white")
        self.Scrolledtext3.configure(exportselection="0")
        self.Scrolledtext3.configure(font="-family {DejaVu Sans} -size 11 -weight bold")
        self.Scrolledtext3.configure(highlightbackground="cornsilk4")
        self.Scrolledtext3.configure(insertborderwidth="3")
        self.Scrolledtext3.configure(selectbackground="#d9d9d9")
        self.Scrolledtext3.configure(wrap="none")

        self.btnFrameEditDismiss = ttk.Button(self.FrameEditor)
        self.btnFrameEditDismiss.place(x=860, y=20, height=30, width=98)
        self.btnFrameEditDismiss.configure(command=gkb_support.on_frameEditDismiss)
        self.btnFrameEditDismiss.configure(text="""Dismiss""")
        self.btnFrameEditDismiss.configure(compound="left")

        self.btnEditSave = ttk.Button(self.FrameEditor)
        self.btnEditSave.place(x=730, y=20, height=30, width=98)
        self.btnEditSave.configure(command=gkb_support.on_btnEditSave)
        self.btnEditSave.configure(text="""Save""")
        self.btnEditSave.configure(compound="left")

        self.TEntry3 = ttk.Entry(self.FrameEditor)
        self.TEntry3.place(x=170, y=40, height=24, width=396)
        self.TEntry3.configure(font="-family {DejaVu Sans} -size 10")
        self.TEntry3.configure(textvariable=self.EntTopic)
        self.TEntry3.configure(cursor="xterm")

        self.TEntry2 = ttk.Entry(self.FrameEditor)
        self.TEntry2.place(x=170, y=74, height=24, width=716)
        self.TEntry2.configure(exportselection="0")
        self.TEntry2.configure(font="-family {DejaVu Sans} -size 10")
        self.TEntry2.configure(textvariable=self.EntryKeywords1)
        self.TEntry2.configure(cursor="xterm")

        self.TLabel4 = ttk.Label(self.FrameEditor)
        self.TLabel4.place(x=10, y=10, height=24, width=281)
        self.TLabel4.configure(font="-family {DejaVu Sans} -size 11 -weight bold")
        self.TLabel4.configure(relief="flat")
        self.TLabel4.configure(anchor="center")
        self.TLabel4.configure(justify="left")
        self.TLabel4.configure(textvariable=self.EditorMode)
        self.EditorMode.set("""""")
        self.TLabel4.configure(compound="left")

        self.FrameSearchBar = ttk.Frame(self.FrameMain)
        self.FrameSearchBar.place(x=10, y=10, height=55, width=975)
        self.FrameSearchBar.configure(relief="groove")
        self.FrameSearchBar.configure(borderwidth="2")
        self.FrameSearchBar.configure(relief="groove")

        self.TEntry1 = ttk.Entry(self.FrameSearchBar)
        self.TEntry1.place(x=220, y=16, height=24, width=386)
        self.TEntry1.configure(exportselection="0")
        self.TEntry1.configure(font="-family {DejaVu Sans} -size 10")
        self.TEntry1.configure(textvariable=self.EntryKeyword)
        self.TEntry1.configure(cursor="xterm")

        self.btnKeywordSearch = ttk.Button(self.FrameSearchBar)
        self.btnKeywordSearch.place(x=611, y=7, height=42, width=42)
        self.btnKeywordSearch.configure(command=gkb_support.on_keywordSearch)
        photo_location = os.path.join(_location, "./graphics/edit-find.png")
        global _img9
        _img9 = tk.PhotoImage(file=photo_location)
        self.btnKeywordSearch.configure(image=_img9)
        self.btnKeywordSearch.configure(compound="none")
        self.btnKeywordSearch_tooltip = ToolTip(self.btnKeywordSearch, """Search""")

        self.TLabel1 = ttk.Label(self.FrameSearchBar)
        self.TLabel1.place(x=20, y=14, height=24, width=201)
        self.TLabel1.configure(font="-family {DejaVu Sans} -size 11 -weight bold")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(anchor="e")
        self.TLabel1.configure(justify="left")
        self.TLabel1.configure(text="""Keywords:""")
        self.TLabel1.configure(textvariable=self.KwdTopic)
        self.KwdTopic.set("""Keywords: """)
        self.TLabel1.configure(compound="left")

        self.btnKwdClear = ttk.Button(self.FrameSearchBar)
        self.btnKwdClear.place(x=660, y=7, height=42, width=42)
        self.btnKwdClear.configure(command=gkb_support.on_btnKwdClear)
        self.btnKwdClear.configure(takefocus="")
        photo_location = os.path.join(_location, "./graphics/edit-clear.png")
        global _img10
        _img10 = tk.PhotoImage(file=photo_location)
        self.btnKwdClear.configure(image=_img10)
        self.btnKwdClear.configure(compound="center")
        self.btnKwdClear_tooltip = ToolTip(self.btnKwdClear, """Clear Search Box""")

        self.btnSwap = ttk.Button(self.FrameSearchBar)
        self.btnSwap.place(x=710, y=7, height=42, width=42)
        self.btnSwap.configure(command=gkb_support.on_btnSwap)
        self.btnSwap.configure(takefocus="")
        photo_location = os.path.join(_location, "./graphics/view-refresh.png")
        global _img11
        _img11 = tk.PhotoImage(file=photo_location)
        self.btnSwap.configure(image=_img11)
        self.btnSwap.configure(compound="center")
        self.btnSwap_tooltip = ToolTip(self.btnSwap, """Swap Keyword/Topic""")

        self.FrameSQL = ttk.Frame(self.FrameMain)
        self.FrameSQL.place(x=10, y=160, height=475, width=985)
        self.FrameSQL.configure(relief="groove")
        self.FrameSQL.configure(borderwidth="2")
        self.FrameSQL.configure(relief="groove")

        self.TLabel7 = ttk.Label(self.FrameSQL)
        self.TLabel7.place(x=20, y=20, height=34, width=131)
        self.TLabel7.configure(font="-family {DejaVu Sans} -size 14 -weight bold")
        self.TLabel7.configure(relief="flat")
        self.TLabel7.configure(anchor="w")
        self.TLabel7.configure(justify="left")
        self.TLabel7.configure(text="""All Topics""")
        self.TLabel7.configure(compound="left")

        self.TFrame3 = ttk.Frame(self.FrameSQL)
        self.TFrame3.place(x=10, y=70, height=395, width=295)
        self.TFrame3.configure(relief="groove")
        self.TFrame3.configure(borderwidth="2")
        self.TFrame3.configure(relief="groove")

        self.Scrolledlistbox2 = ScrolledListBox(self.TFrame3)
        self.Scrolledlistbox2.place(x=3, y=10, height=380, width=286)
        self.Scrolledlistbox2.configure(background="white")
        self.Scrolledlistbox2.configure(cursor="xterm")
        self.Scrolledlistbox2.configure(disabledforeground="#68665a")
        self.Scrolledlistbox2.configure(exportselection="0")
        self.Scrolledlistbox2.configure(font="TkFixedFont")
        self.Scrolledlistbox2.configure(highlightbackground="cornsilk4")
        self.Scrolledlistbox2.configure(highlightcolor="#d9d9d9")
        self.Scrolledlistbox2.configure(selectbackground="#d9d9d9")

        self.TFrame7 = ttk.Frame(self.FrameSQL)
        self.TFrame7.place(x=310, y=70, height=395, width=665)
        self.TFrame7.configure(relief="groove")
        self.TFrame7.configure(borderwidth="2")
        self.TFrame7.configure(relief="groove")

        self.Scrolledtext4 = ScrolledText(self.TFrame7)
        self.Scrolledtext4.place(x=3, y=10, height=380, width=660)
        self.Scrolledtext4.configure(background="white")
        self.Scrolledtext4.configure(font="-family {DejaVu Sans} -size 11 -weight bold")
        self.Scrolledtext4.configure(highlightbackground="cornsilk4")
        self.Scrolledtext4.configure(insertborderwidth="3")
        self.Scrolledtext4.configure(selectbackground="#d9d9d9")
        self.Scrolledtext4.configure(wrap="none")

        self.btnSQLDismiss = ttk.Button(self.FrameSQL)
        self.btnSQLDismiss.place(x=870, y=20, height=30, width=98)
        self.btnSQLDismiss.configure(command=gkb_support.on_btnSQLDismiss)
        self.btnSQLDismiss.configure(text="""Dismiss""")
        self.btnSQLDismiss.configure(compound="left")

        self.TEntry4 = ttk.Entry(self.FrameSQL)
        self.TEntry4.place(x=180, y=24, height=24, width=326)
        self.TEntry4.configure(font="-family {DejaVu Sans} -size 10")
        self.TEntry4.configure(textvariable=self.ParamSQL)
        self.TEntry4.configure(cursor="xterm")

        self.btnSQLGo = ttk.Button(self.FrameSQL)
        self.btnSQLGo.place(x=508, y=17, height=42, width=42)
        self.btnSQLGo.configure(command=gkb_support.on_btnSQLGo)
        photo_location = os.path.join(_location, "./graphics/go-next.png")
        global _img12
        _img12 = tk.PhotoImage(file=photo_location)
        self.btnSQLGo.configure(image=_img12)
        self.btnSQLGo.configure(compound="none")

        self.FrameSearchResults = ttk.Frame(self.FrameMain)
        self.FrameSearchResults.place(x=10, y=160, height=475, width=985)
        self.FrameSearchResults.configure(relief="groove")
        self.FrameSearchResults.configure(borderwidth="2")
        self.FrameSearchResults.configure(relief="groove")

        self.TLabel2 = ttk.Label(self.FrameSearchResults)
        self.TLabel2.place(x=20, y=20, height=29, width=507)
        self.TLabel2.configure(font="-family {DejaVu Sans} -size 14 -weight bold")
        self.TLabel2.configure(relief="flat")
        self.TLabel2.configure(anchor="center")
        self.TLabel2.configure(justify="left")
        self.TLabel2.configure(textvariable=self.SearchResultsTitle)
        self.SearchResultsTitle.set("""""")
        self.TLabel2.configure(compound="left")

        self.btnSearchDone = ttk.Button(self.FrameSearchResults)
        self.btnSearchDone.place(x=830, y=10, height=40, width=131)
        self.btnSearchDone.configure(command=gkb_support.on_btnSearchDone)
        self.btnSearchDone.configure(text="""Done""")
        self.btnSearchDone.configure(compound="left")

        self.TFrame6 = ttk.Frame(self.FrameSearchResults)
        self.TFrame6.place(x=320, y=80, height=385, width=655)
        self.TFrame6.configure(relief="groove")
        self.TFrame6.configure(borderwidth="2")
        self.TFrame6.configure(relief="groove")

        self.Scrolledtext2 = ScrolledText(self.TFrame6)
        self.Scrolledtext2.place(x=4, y=4, height=374, width=644)
        self.Scrolledtext2.configure(background="white")
        self.Scrolledtext2.configure(exportselection="0")
        self.Scrolledtext2.configure(font="-family {DejaVu Sans} -size 11 -weight bold")
        self.Scrolledtext2.configure(highlightbackground="cornsilk4")
        self.Scrolledtext2.configure(insertborderwidth="3")
        self.Scrolledtext2.configure(selectbackground="#d9d9d9")
        self.Scrolledtext2.configure(wrap="none")

        self.TFrame5 = ttk.Frame(self.FrameSearchResults)
        self.TFrame5.place(x=10, y=80, height=385, width=305)
        self.TFrame5.configure(relief="groove")
        self.TFrame5.configure(borderwidth="2")
        self.TFrame5.configure(relief="groove")

        self.Scrolledlistbox1 = ScrolledListBox(self.TFrame5)
        self.Scrolledlistbox1.place(x=3, y=3, height=377, width=294)
        self.Scrolledlistbox1.configure(background="white")
        self.Scrolledlistbox1.configure(cursor="xterm")
        self.Scrolledlistbox1.configure(disabledforeground="#68665a")
        self.Scrolledlistbox1.configure(exportselection="0")
        self.Scrolledlistbox1.configure(font="TkFixedFont")
        self.Scrolledlistbox1.configure(highlightbackground="cornsilk4")
        self.Scrolledlistbox1.configure(highlightcolor="#d9d9d9")
        self.Scrolledlistbox1.configure(selectbackground="#d9d9d9")

    def popup1(self, event, *args, **kwargs):
        self.Popupmenu1 = tk.Menu(self.top, tearoff=0)
        self.Popupmenu1.configure(background=_bgcolor)
        self.Popupmenu1.configure(foreground=_fgcolor)
        self.Popupmenu1.configure(font="-family {DejaVu Sans} -size 11 -weight bold")
        self.Popupmenu1.add_command(
            command=lambda: gkb_support.on_popCopy(args[0]),
            compound="left",
            font="-family {DejaVu Sans} -size 11 -weight bold",
            label="Copy",
        )

        self.Popupmenu1.add_command(
            command=lambda: gkb_support.on_popClear(args[0]),
            compound="left",
            font="-family {DejaVu Sans} -size 11 -weight bold",
            label="Clear",
        )
        self.Popupmenu1.add_command(
            command=lambda: gkb_support.on_popPaste(args[0]),
            compound="left",
            font="-family {DejaVu Sans} -size 11 -weight bold",
            label="Paste",
        )
        self.Popupmenu1.post(event.x_root, event.y_root)

    def popup2(self, event, *args, **kwargs):
        self.Popupmenu2 = tk.Menu(self.top, tearoff=0)
        self.Popupmenu2.configure(background=_bgcolor)
        self.Popupmenu2.configure(foreground=_fgcolor)
        self.Popupmenu2.configure(font="-family {DejaVu Sans} -size 11 -weight bold")
        self.Popupmenu2.add_command(
            command=gkb_support.on_pop2EditTopic,
            compound="left",
            font="-family {DejaVu Sans} -size 11 -weight bold",
            label="Edit Topic",
        )
        self.Popupmenu2.add_separator()
        self.Popupmenu2.add_command(
            command=gkb_support.on_pop2DeleteTopic,
            compound="left",
            font="-family {DejaVu Sans} -size 11 -weight bold",
            label="Delete Topic",
        )
        self.Popupmenu2.add_separator()
        self.Popupmenu2.add_command(
            command=gkb_support.on_pop2CloseMenu,
            compound="left",
            font="-family {DejaVu Sans} -size 11 -weight bold",
            label="Close Menu",
        )
        self.Popupmenu2.post(event.x_root, event.y_root)


from time import time


class ToolTip(tk.Toplevel):
    """Provides a ToolTip widget for Tkinter."""

    def __init__(self, wdgt, msg=None, msgFunc=None, delay=0.5, follow=True):
        self.wdgt = wdgt
        self.parent = self.wdgt.master
        tk.Toplevel.__init__(self, self.parent, bg="black", padx=1, pady=1)
        self.withdraw()
        self.overrideredirect(True)
        self.msgVar = tk.StringVar()
        if msg is None:
            self.msgVar.set("No message provided")
        else:
            self.msgVar.set(msg)
        self.msgFunc = msgFunc
        self.delay = delay
        self.follow = follow
        self.visible = 0
        self.lastMotion = 0
        self.msg = tk.Message(
            self,
            textvariable=self.msgVar,
            bg=_bgcolor,
            fg=_fgcolor,
            font="TkDefaultFont",
            aspect=1000,
        )
        self.msg.grid()
        self.wdgt.bind("<Enter>", self.spawn, "+")
        self.wdgt.bind("<Leave>", self.hide, "+")
        self.wdgt.bind("<Motion>", self.move, "+")

    def spawn(self, event=None):
        self.visible = 1
        self.after(int(self.delay * 1000), self.show)

    def show(self):
        if self.visible == 1 and time() - self.lastMotion > self.delay:
            self.visible = 2
        if self.visible == 2:
            self.deiconify()

    def move(self, event):
        self.lastMotion = time()
        if self.follow is False:
            self.withdraw()
            self.visible = 1
        self.geometry("+%i+%i" % (event.x_root + 20, event.y_root - 10))
        try:
            self.msgVar.set(self.msgFunc())
        except:
            pass
        self.after(int(self.delay * 1000), self.show)

    def hide(self, event=None):
        self.visible = 0
        self.withdraw()

    def update(self, msg):
        self.msgVar.set(msg)

    def configure(self, **kwargs):
        backgroundset = False
        foregroundset = False
        # Get the current tooltip text just in case the user doesn't provide any.
        current_text = self.msgVar.get()
        # to clear the tooltip text, use the .update method
        if "debug" in kwargs.keys():
            debug = kwargs.pop("debug", False)
            if debug:
                for key, value in kwargs.items():
                    print(f"key: {key} - value: {value}")
        if "background" in kwargs.keys():
            background = kwargs.pop("background")
            backgroundset = True
        if "bg" in kwargs.keys():
            background = kwargs.pop("bg")
            backgroundset = True
        if "foreground" in kwargs.keys():
            foreground = kwargs.pop("foreground")
            foregroundset = True
        if "fg" in kwargs.keys():
            foreground = kwargs.pop("fg")
            foregroundset = True

        fontd = kwargs.pop("font", None)
        if "text" in kwargs.keys():
            text = kwargs.pop("text")
            if (text == "") or (text == "\n"):
                text = current_text
            else:
                self.msgVar.set(text)
        reliefd = kwargs.pop("relief", "flat")
        justifyd = kwargs.pop("justify", "left")
        padxd = kwargs.pop("padx", 1)
        padyd = kwargs.pop("pady", 1)
        borderwidthd = kwargs.pop("borderwidth", 2)
        wid = self.msg  # The message widget which is the actual tooltip
        if backgroundset:
            wid.config(bg=background)
        if foregroundset:
            wid.config(fg=foreground)
        wid.config(font=fontd)
        wid.config(borderwidth=borderwidthd)
        wid.config(relief=reliefd)
        wid.config(justify=justifyd)
        wid.config(padx=padxd)
        wid.config(pady=padyd)


#                   End of Class ToolTip


# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    """Configure the scrollbars for a widget."""

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient="vertical", command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient="horizontal", command=self.xview)
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky="nsew")
        try:
            vsb.grid(column=1, row=0, sticky="ns")
        except:
            pass
        hsb.grid(column=0, row=1, sticky="ew")
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        # Copy geometry methods of master  (taken from ScrolledText.py)
        methods = (
            tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() | tk.Place.__dict__.keys()
        )
        for meth in methods:
            if meth[0] != "_" and meth not in ("config", "configure"):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        """Hide and show scrollbar as needed."""

        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)

        return wrapped

    def __str__(self):
        return str(self.master)


def _create_container(func):
    """Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget."""

    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind("<Enter>", lambda e: _bound_to_mousewheel(e, container))
        container.bind("<Leave>", lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)

    return wrapped


class ScrolledText(AutoScroll, tk.Text):
    """A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed."""

    @_create_container
    def __init__(self, master, **kw):
        tk.Text.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)


class ScrolledListBox(AutoScroll, tk.Listbox):
    """A standard Tkinter Listbox widget with scrollbars that will
    automatically show/hide as needed."""

    @_create_container
    def __init__(self, master, **kw):
        tk.Listbox.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

    def size_(self):
        sz = tk.Listbox.size(self)
        return sz


import platform


def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == "Windows" or platform.system() == "Darwin":
        child.bind_all("<MouseWheel>", lambda e: _on_mousewheel(e, child))
        child.bind_all("<Shift-MouseWheel>", lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all("<Button-4>", lambda e: _on_mousewheel(e, child))
        child.bind_all("<Button-5>", lambda e: _on_mousewheel(e, child))
        child.bind_all("<Shift-Button-4>", lambda e: _on_shiftmouse(e, child))
        child.bind_all("<Shift-Button-5>", lambda e: _on_shiftmouse(e, child))


def _unbound_to_mousewheel(event, widget):
    if platform.system() == "Windows" or platform.system() == "Darwin":
        widget.unbind_all("<MouseWheel>")
        widget.unbind_all("<Shift-MouseWheel>")
    else:
        widget.unbind_all("<Button-4>")
        widget.unbind_all("<Button-5>")
        widget.unbind_all("<Shift-Button-4>")
        widget.unbind_all("<Shift-Button-5>")


def _on_mousewheel(event, widget):
    if platform.system() == "Windows":
        widget.yview_scroll(-1 * int(event.delta / 120), "units")
    elif platform.system() == "Darwin":
        widget.yview_scroll(-1 * int(event.delta), "units")
    else:
        if event.num == 4:
            widget.yview_scroll(-1, "units")
        elif event.num == 5:
            widget.yview_scroll(1, "units")


def _on_shiftmouse(event, widget):
    if platform.system() == "Windows":
        widget.xview_scroll(-1 * int(event.delta / 120), "units")
    elif platform.system() == "Darwin":
        widget.xview_scroll(-1 * int(event.delta), "units")
    else:
        if event.num == 4:
            widget.xview_scroll(-1, "units")
        elif event.num == 5:
            widget.xview_scroll(1, "units")


def start_up():
    gkb_support.main()


if __name__ == "__main__":
    gkb_support.main()
