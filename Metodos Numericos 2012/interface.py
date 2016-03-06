#!/usr/bin/env python
# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.4 on Wed Apr  2 15:07:52 2014
import wx
import ui_biseccion as ui_b
import ui_newtonraphson as ui_n
import ui_puntofijo as ui_p
import ui_simpson13 as ui_s13
import ui_simpson13comp as ui_s13c
import ui_simpson38 as ui_s38
import ui_simpson38comp as ui_s38c
import ui_trapecio as ui_t
import ui_trapeciocompuesto as ui_tc

# begin wxGlade: extracode
# end wxGlade


class main(wx.Frame):
	def __init__(self, *args, **kwds):
		# begin wxGlade: main.__init__
		kwds["style"] = wx.DEFAULT_FRAME_STYLE
		wx.Frame.__init__(self, *args, **kwds)
		self.label_1 = wx.StaticText(self, -1, "METODOS NUMERICOS", style=wx.ALIGN_CENTRE)
		self.button_14 = wx.Button(self, -1, "Biseccion")
		self.button_15 = wx.Button(self, -1, "Newton - Raphson")
		self.button_16 = wx.Button(self, -1, "Punto Fijo")
		self.button_18 = wx.Button(self, -1, "Trapecio")
		self.button_17 = wx.Button(self, -1, "Trapecio Compuesto")
		self.button_19 = wx.Button(self, -1, "Simpson 1/3")
		self.button_20 = wx.Button(self, -1, "Simpson 1/3 Compuesto")
		self.button_21 = wx.Button(self, -1, "Simpson 3/8")
		self.button_22 = wx.Button(self, -1, "Simpson 3/8 Compuesto")
		self.static_line_1 = wx.StaticLine(self, -1)
		self.button_23 = wx.Button(self, -1, "EXIT")
		self.sizer_2_staticbox = wx.StaticBox(self, -1, "")

		self.__set_properties()
		self.__do_layout()

		self.Bind(wx.EVT_BUTTON, self.biseccion, self.button_14)
		self.Bind(wx.EVT_BUTTON, self.NewtonRapson, self.button_15)
		self.Bind(wx.EVT_BUTTON, self.PuntoFijo, self.button_16)
		self.Bind(wx.EVT_BUTTON, self.Trapecio, self.button_18)
		self.Bind(wx.EVT_BUTTON, self.TrapecioCompuesto, self.button_17)
		self.Bind(wx.EVT_BUTTON, self.Simpson13, self.button_19)
		self.Bind(wx.EVT_BUTTON, self.Simpson13Comp, self.button_20)
		self.Bind(wx.EVT_BUTTON, self.Simpson38, self.button_21)
		self.Bind(wx.EVT_BUTTON, self.Simpson38Comp, self.button_22)
		self.Bind(wx.EVT_BUTTON, self.Salir, self.button_23)
		# end wxGlade

	def __set_properties(self):
		# begin wxGlade: main.__set_properties
		self.SetTitle("Metodos Numericos")
		self.label_1.SetFont(wx.Font(18, wx.MODERN, wx.NORMAL, wx.NORMAL, 0, ""))
		# end wxGlade

	def __do_layout(self):
		# begin wxGlade: main.__do_layout
		sizer_1 = wx.BoxSizer(wx.VERTICAL)
		self.sizer_2_staticbox.Lower()
		sizer_2 = wx.StaticBoxSizer(self.sizer_2_staticbox, wx.VERTICAL)
		sizer_2.Add(self.label_1, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
		sizer_2.Add(self.button_14, 0, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
		sizer_2.Add(self.button_15, 0, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
		sizer_2.Add(self.button_16, 0, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
		sizer_2.Add(self.button_18, 0, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
		sizer_2.Add(self.button_17, 0, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
		sizer_2.Add(self.button_19, 0, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
		sizer_2.Add(self.button_20, 0, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
		sizer_2.Add(self.button_21, 0, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
		sizer_2.Add(self.button_22, 0, wx.EXPAND | wx.ALIGN_CENTER_HORIZONTAL | wx.ALIGN_CENTER_VERTICAL, 0)
		sizer_2.Add(self.static_line_1, 0, wx.EXPAND, 0)
		sizer_2.Add(self.button_23, 0, wx.ALIGN_RIGHT, 0)
		sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)
		self.SetSizer(sizer_1)
		sizer_1.Fit(self)
		self.Layout()
		# end wxGlade

	def biseccion(self, event):  # wxGlade: main.<event_handler>
		frame_biseccion = ui_b.biseccion(None, -1, "")
		frame_biseccion.Show()
		event.Skip()

	def NewtonRapson(self, event):  # wxGlade: main.<event_handler>
		frame_newton = ui_n.newtonraphson(None, -1, "")
		frame_newton.Show()
		event.Skip()

	def PuntoFijo(self, event):  # wxGlade: main.<event_handler>
		frame_puntoFijo = ui_p.puntofijo(None, -1, "")
		frame_puntoFijo.Show()
		event.Skip()

	def Trapecio(self, event):  # wxGlade: main.<event_handler>
		frame_trapecio = ui_t.trapecio(None, -1, "")
		frame_trapecio.Show()
		event.Skip()

	def TrapecioCompuesto(self, event):  # wxGlade: main.<event_handler>
		frame_trapecioCompuesto = ui_tc.trapeciocompuesto(None, -1, "")
		frame_trapecioCompuesto.Show()
		event.Skip()

	def Simpson13(self, event):  # wxGlade: main.<event_handler>
		frame = ui_s13.simpson13(None, -1, "")
		frame.Show()
		event.Skip()

	def Simpson13Comp(self, event):  # wxGlade: main.<event_handler>
		frame = ui_s13c.simpson13comp(None, -1, "")
		frame.Show()
		event.Skip()

	def Simpson38(self, event):  # wxGlade: main.<event_handler>
		frame = ui_s38.simpson38(None, -1, "")
		frame.Show()
		event.Skip()

	def Simpson38Comp(self, event):  # wxGlade: main.<event_handler>
		frame = ui_s38c.simpson38comp(None, -1, "")
		frame.Show()
		event.Skip()

	def Salir(self, event):  # wxGlade: main.<event_handler>
		print "Event handler `Salir' not implemented!"
		event.Skip()

# end of class main
if __name__ == "__main__":
	app = wx.PySimpleApp(0)
	wx.InitAllImageHandlers()
	MetodosNumericos = main(None, -1, "")
	app.SetTopWindow(MetodosNumericos)
	MetodosNumericos.Show()
	app.MainLoop()