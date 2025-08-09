import ROOT

def get_vertical_line(x, style = 2, width = 3, color = ROOT.TColor.GetColor("#e42536"), relative_margin = 0.01):
    ROOT.gPad.Update()
    ul = ROOT.gPad.GetUymax()
    ll = ROOT.gPad.GetUymin()
    margin = (ul - ll) * relative_margin
    line = ROOT.TLine(x, ll+margin, x, ul-margin)
    line.SetLineStyle(style)
    line.SetLineWidth(width)
    line.SetLineColor(color)
    return line

def get_horizontal_line(y, style = 2, width = 3, color = ROOT.TColor.GetColor("#e42536"), relative_margin = 0.01):
    ROOT.gPad.Update()
    ul = ROOT.gPad.GetUxmax()
    ll = ROOT.gPad.GetUxmin()
    margin = (ul - ll) * relative_margin
    line = ROOT.TLine(ll+margin, y, ul-margin, y)
    line.SetLineStyle(style)
    line.SetLineWidth(width)
    line.SetLineColor(color)
    return line

def draw_vertical_line(x, style = 2, width = 3, color = ROOT.TColor.GetColor("#e42536"), relative_margin = 0.01):
    line = get_vertical_line(x, style, width, color, relative_margin)
    line.Draw()
    return line

def draw_horizontal_line(y, style = 2, width = 3, color = ROOT.TColor.GetColor("#e42536"), relative_margin = 0.01):
    line = get_horizontal_line(y, style, width, color, relative_margin)
    line.Draw()
    return line


def get_vertical_box(x1, x2, color = ROOT.TColor.GetColor("#e42536"), alpha = 0.1, relative_margin = 0.0):
    ROOT.gPad.Update()
    ul = ROOT.gPad.GetUymax()
    ll = ROOT.gPad.GetUymin()
    margin = (ul - ll) * relative_margin
    box = ROOT.TBox(x1, ll+margin, x2, ul-margin)
    box.SetFillColorAlpha(color, alpha)
    return box

def get_horizontal_box(y1, y2, color = ROOT.TColor.GetColor("#e42536"), alpha = 0.1, relative_margin = 0.0):
    ROOT.gPad.Update()
    ul = ROOT.gPad.GetUxmax()
    ll = ROOT.gPad.GetUxmin()
    margin = (ul - ll) * relative_margin
    box = ROOT.TBox(ll+margin, y1, ul-margin, y2)
    box.SetFillColorAlpha(color, alpha)
    return box

def draw_vertical_box(x1, x2, color = ROOT.TColor.GetColor("#e42536"), alpha = 0.1, relative_margin = 0.0):
    box = get_vertical_box(x1, x2, color, alpha, relative_margin)
    box.Draw()
    return box

def draw_horizontal_box(y1, y2, color = ROOT.TColor.GetColor("#e42536"), alpha = 0.1, relative_margin = 0.0):
    box = get_horizontal_box(y1, y2, color, alpha, relative_margin)
    box.Draw()
    return box


def redraw_border():
   # Adapted for Python from C++ written by couet:
   # https://root-forum.cern.ch/t/how-to-redraw-axis-and-plot-borders/28252
   ROOT.gPad.Update();
   ROOT.gPad.RedrawAxis();
   l = ROOT.TLine()
   l.DrawLine(ROOT.gPad.GetUxmin(), ROOT.gPad.GetUymax(), ROOT.gPad.GetUxmax(), ROOT.gPad.GetUymax());
   l.DrawLine(ROOT.gPad.GetUxmax(), ROOT.gPad.GetUymin(), ROOT.gPad.GetUxmax(), ROOT.gPad.GetUymax());