import ROOT

# Define the Petroff color palettes from arXiv:2107.02270v2
# These are defined in later versions of ROOT, but if your 
# institution uses an older version of ROOT, it is useful to
# have access to them here.

PPP6 = [
    ROOT.TColor.GetColor("#5790fc"),
    ROOT.TColor.GetColor("#f89c20"),
    ROOT.TColor.GetColor("#e42536"),
    ROOT.TColor.GetColor("#964a8b"),
    ROOT.TColor.GetColor("#9c9ca1"),
    ROOT.TColor.GetColor("#7a21dd")
]
PPP8 = [
    ROOT.TColor.GetColor("#1845fb"),
    ROOT.TColor.GetColor("#ff5e02"),
    ROOT.TColor.GetColor("#c91f16"),
    ROOT.TColor.GetColor("#c849a9"),
    ROOT.TColor.GetColor("#adad7d"),
    ROOT.TColor.GetColor("#86c8dd"),
    ROOT.TColor.GetColor("#578dff"),
    ROOT.TColor.GetColor("#656364")
]
PPP10 = [
    ROOT.TColor.GetColor("#3f90da"),
    ROOT.TColor.GetColor("#ffa90e"),
    ROOT.TColor.GetColor("#bd1f01"),
    ROOT.TColor.GetColor("#94a4a2"),
    ROOT.TColor.GetColor("#832db6"),
    ROOT.TColor.GetColor("#a96b59"),
    ROOT.TColor.GetColor("#e76300"),
    ROOT.TColor.GetColor("#b9ac70"),
    ROOT.TColor.GetColor("#717581"),
    ROOT.TColor.GetColor("#92dadd")
]


# Define some functions for drawing vertical and horizontal lines,
# as well as boxes bounded by vertical and horizontal lines.

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
   ROOT.gPad.Update()
   ROOT.gPad.RedrawAxis()
   l = ROOT.TLine()
   l.DrawLine(ROOT.gPad.GetUxmin(), ROOT.gPad.GetUymax(), ROOT.gPad.GetUxmax(), ROOT.gPad.GetUymax())
   l.DrawLine(ROOT.gPad.GetUxmax(), ROOT.gPad.GetUymin(), ROOT.gPad.GetUxmax(), ROOT.gPad.GetUymax())


def get_pad_xmin():
    return ROOT.gPad.GetUxmin()

def get_pad_xmax():
    return ROOT.gPad.GetUxmax()

def get_pad_ymin():
    return ROOT.gPad.GetUymin()

def get_pad_ymax():
    return ROOT.gPad.GetUymax()

def get_pad_xrange():
    return (ROOT.gPad.GetUxmax() - ROOT.gPad.GetUxmin())

def get_pad_yrange():
    return (ROOT.gPad.GetUymax() - ROOT.gPad.GetUymin())

def get_pad_xyratio():
    return (ROOT.gPad.GetUxmax() - ROOT.gPad.GetUxmin()) / (ROOT.gPad.GetUymax() - ROOT.gPad.GetUymin())

def get_label_anchor_left(x = 0.03):
    return x * get_pad_xrange() + get_pad_xmin()

def get_label_anchor_right(x = 0.03):
    return (1.0 - x) * get_pad_xrange() + get_pad_xmin()

def get_label_anchor_top(y = 0.03):
    return (1.0 - y) * get_pad_yrange() + get_pad_ymin()

def get_label_anchor_bottom(y = 0.03):
    return y * get_pad_yrange() + get_pad_ymin()

def draw_label_top_left(label, size_pixels = 3, text_align = ROOT.kVAlignTop + ROOT.kHAlignLeft, color=ROOT.kBlack, margin_NDC = 0.03):
    ltx = ROOT.TLatex()
    ltx.SetTextSizePixels(size_pixels)
    ltx.SetTextAlign(text_align)
    ltx.SetTextColor(color)
    ltx.DrawLatex(get_label_anchor_left(margin_NDC), get_label_anchor_top(margin_NDC), label)
    return ltx

def draw_label_top_right(label, size_pixels = 3, text_align = ROOT.kVAlignTop + ROOT.kHAlignRight, color=ROOT.kBlack, margin_NDC = 0.03):
    ltx = ROOT.TLatex()
    ltx.SetTextSizePixels(size_pixels)
    ltx.SetTextAlign(text_align)
    ltx.SetTextColor(color)
    ltx.DrawLatex(get_label_anchor_right(margin_NDC), get_label_anchor_top(margin_NDC), label)
    return ltx

def draw_label_bottom_left(label, size_pixels = 3, text_align = ROOT.kVAlignBottom + ROOT.kHAlignLeft, color=ROOT.kBlack, margin_NDC = 0.03):
    ltx = ROOT.TLatex()
    ltx.SetTextSizePixels(size_pixels)
    ltx.SetTextAlign(text_align)
    ltx.SetTextColor(color)
    ltx.DrawLatex(get_label_anchor_left(margin_NDC), get_label_anchor_bottom(margin_NDC), label)
    return ltx

def draw_label_bottom_right(label, size_pixels = 3, text_align = ROOT.kVAlignBottom + ROOT.kHAlignRight, color=ROOT.kBlack, margin_NDC = 0.03):
    ltx = ROOT.TLatex()
    ltx.SetTextSizePixels(size_pixels)
    ltx.SetTextAlign(text_align)
    ltx.SetTextColor(color)
    ltx.DrawLatex(get_label_anchor_right(margin_NDC), get_label_anchor_bottom(margin_NDC), label)
    return ltx