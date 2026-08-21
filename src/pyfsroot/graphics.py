import ROOT

from typing import Literal, Union

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
    ROOT.TColor.GetColor("#7a21dd"),
]
PPP8 = [
    ROOT.TColor.GetColor("#1845fb"),
    ROOT.TColor.GetColor("#ff5e02"),
    ROOT.TColor.GetColor("#c91f16"),
    ROOT.TColor.GetColor("#c849a9"),
    ROOT.TColor.GetColor("#adad7d"),
    ROOT.TColor.GetColor("#86c8dd"),
    ROOT.TColor.GetColor("#578dff"),
    ROOT.TColor.GetColor("#656364"),
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
    ROOT.TColor.GetColor("#92dadd"),
]


# Define some functions for drawing vertical and horizontal lines,
# as well as boxes bounded by vertical and horizontal lines.


def get_vertical_line(
    x: float,
    style: int = 2,
    width: int = 3,
    color: int = ROOT.TColor.GetColor("#e42536"),
    relative_margin: float = 0.01,
) -> ROOT.TLine:
    """
    Create a vertical ROOT.TLine object at position x.

    :param x: The horizontal position of the vertical line in user coordinates.
    :type x: float

    :param style: The ROOT.TAttLine line style.
    :type style: int

    :param width: The line width in pixels.
    :type width: int

    :param color: The ROOT.TColor expressed as an integer.
    :type color: int

    :param relative_margin: The fraction of the axis to use as the margin on either end of the line.
    :type relative_margin: float

    :returns: a ROOT.TLine object with the specified properties.
    :rtype: ROOT.TLine
    """
    ROOT.gPad.Update()
    ul = ROOT.gPad.GetUymax()
    ll = ROOT.gPad.GetUymin()
    margin = (ul - ll) * relative_margin
    line = ROOT.TLine(x, ll + margin, x, ul - margin)
    line.SetLineStyle(style)
    line.SetLineWidth(width)
    line.SetLineColor(color)
    return line


def get_horizontal_line(
    y: float,
    style: int = 2,
    width: int = 3,
    color: int = ROOT.TColor.GetColor("#e42536"),
    relative_margin: float = 0.01,
) -> ROOT.TLine:
    """
    Create a horizontal ROOT.TLine object at position y.

    :param x: The vertical position of the horizontal line in user coordinates.
    :type x: float

    :param style: The ROOT.TAttLine line style.
    :type style: int

    :param width: The line width in pixels.
    :type width: int

    :param color: The ROOT.TColor expressed as an integer.
    :type color: int

    :param relative_margin: The fraction of the axis to use as the margin on either end of the line.
    :type relative_margin: float

    :returns: a ROOT.TLine object with the specified properties.
    :rtype: ROOT.TLine
    """
    ROOT.gPad.Update()
    ul = ROOT.gPad.GetUxmax()
    ll = ROOT.gPad.GetUxmin()
    margin = (ul - ll) * relative_margin
    line = ROOT.TLine(ll + margin, y, ul - margin, y)
    line.SetLineStyle(style)
    line.SetLineWidth(width)
    line.SetLineColor(color)
    return line


def draw_vertical_line(
    x: float,
    style: int = 2,
    width: int = 3,
    color: int = ROOT.TColor.GetColor("#e42536"),
    relative_margin: float = 0.01,
) -> ROOT.TLine:
    """
    Create a vertical ROOT.TLine object at position x and draw it on the current pad.

    :param x: The horizontal position of the vertical line in user coordinates.
    :type x: float

    :param style: The ROOT.TAttLine line style.
    :type style: int

    :param width: The line width in pixels.
    :type width: int

    :param color: The ROOT.TColor expressed as an integer.
    :type color: int

    :param relative_margin: The fraction of the axis to use as the margin on either end of the line.
    :type relative_margin: float

    :returns: a ROOT.TLine object with the specified properties.
    :rtype: ROOT.TLine
    """
    line = get_vertical_line(x, style, width, color, relative_margin)
    line.Draw()
    return line


def draw_horizontal_line(
    y: float,
    style: int = 2,
    width: int = 3,
    color: int = ROOT.TColor.GetColor("#e42536"),
    relative_margin: float = 0.01,
) -> ROOT.TLine:
    """
    Create a horizontal ROOT.TLine object at position y and draw it on the current pad.

    :param x: The vertical position of the horizontal line in user coordinates.
    :type x: float

    :param style: The ROOT.TAttLine line style.
    :type style: int

    :param width: The line width in pixels.
    :type width: int

    :param color: The ROOT.TColor expressed as an integer.
    :type color: int

    :param relative_margin: The fraction of the axis to use as the margin on either end of the line.
    :type relative_margin: float

    :returns: a ROOT.TLine object with the specified properties.
    :rtype: ROOT.TLine
    """
    line = get_horizontal_line(y, style, width, color, relative_margin)
    line.Draw()
    return line


def get_vertical_box(
    x1: float,
    x2: float,
    color: int = ROOT.TColor.GetColor("#e42536"),
    alpha: float = 0.1,
    relative_margin: float = 0.0,
) -> ROOT.TBox:
    """
    Create a box bounded by vertical lines at positions x1 and x2.

    :param x1: The horizontal position of the first vertical line in user coordinates.
    :type x1: float

    :param x2: The horizontal position of the second vertical line in user coordinates.
    :type x2: float

    :param color: The ROOT.TColor expressed as an integer.
    :type color: int

    :param alpha: The transparency level of the box. The box is fully transparent at 0 and fully opaque at 1.0.
    :type alpha: int

    :param relative_margin: The fraction of the axis to use as the margin on either end of each vertical line.
    :type relative_margin: float

    :returns: a ROOT.TBox object with the specified properties.
    :rtype: ROOT.TBox
    """
    ROOT.gPad.Update()
    ul = ROOT.gPad.GetUymax()
    ll = ROOT.gPad.GetUymin()
    margin = (ul - ll) * relative_margin
    box = ROOT.TBox(x1, ll + margin, x2, ul - margin)
    box.SetFillColorAlpha(color, alpha)
    return box


def get_horizontal_box(
    y1: float,
    y2: float,
    color: int = ROOT.TColor.GetColor("#e42536"),
    alpha: float = 0.1,
    relative_margin: float = 0.0,
) -> ROOT.TBox:
    """
    Create a box bounded by horizontal lines at positions y1 and y2.

    :param y1: The vertical position of the first horizontal line in user coordinates.
    :type y1: float

    :param y2: The vertical position of the second horizontal line in user coordinates.
    :type y2: float

    :param color: The ROOT.TColor expressed as an integer.
    :type color: int

    :param alpha: The transparency level of the box. The box is fully transparent at 0 and fully opaque at 1.0.
    :type alpha: int

    :param relative_margin: The fraction of the axis to use as the margin on either end of each horizontal line.
    :type relative_margin: float

    :returns: a ROOT.TBox object with the specified properties.
    :rtype: ROOT.TBox
    """
    ROOT.gPad.Update()
    ul = ROOT.gPad.GetUxmax()
    ll = ROOT.gPad.GetUxmin()
    margin = (ul - ll) * relative_margin
    box = ROOT.TBox(ll + margin, y1, ul - margin, y2)
    box.SetFillColorAlpha(color, alpha)
    return box


def draw_vertical_box(
    x1: float,
    x2: float,
    color: int = ROOT.TColor.GetColor("#e42536"),
    alpha: float = 0.1,
    relative_margin: float = 0.0,
) -> ROOT.TBox:
    """
    Create a box bounded by vertical lines at positions x1 and x2 and draw it on the current pad.

    :param x1: The horizontal position of the first vertical line in user coordinates.
    :type x1: float

    :param x2: The horizontal position of the second vertical line in user coordinates.
    :type x2: float

    :param color: The ROOT.TColor expressed as an integer.
    :type color: int

    :param alpha: The transparency level of the box. The box is fully transparent at 0 and fully opaque at 1.0.
    :type alpha: int

    :param relative_margin: The fraction of the axis to use as the margin on either end of each vertical line.
    :type relative_margin: float

    :returns: the drawn ROOT.TBox object with the specified properties.
    :rtype: ROOT.TBox
    """
    box = get_vertical_box(x1, x2, color, alpha, relative_margin)
    box.Draw()
    return box


def draw_horizontal_box(
    y1: float,
    y2: float,
    color: int = ROOT.TColor.GetColor("#e42536"),
    alpha: float = 0.1,
    relative_margin: float = 0.0,
) -> ROOT.TBox:
    """
    Create a box bounded by horizontal lines at positions y1 and y2 and draw it on the current pad.

    :param y1: The vertical position of the first horizontal line in user coordinates.
    :type y1: float

    :param y2: The vertical position of the second horizontal line in user coordinates.
    :type y2: float

    :param color: The ROOT.TColor expressed as an integer.
    :type color: int

    :param alpha: The transparency level of the box. The box is fully transparent at 0 and fully opaque at 1.0.
    :type alpha: int

    :param relative_margin: The fraction of the axis to use as the margin on either end of each horizontal line.
    :type relative_margin: float

    :returns: the drawn ROOT.TBox object with the specified properties.
    :rtype: ROOT.TBox
    """
    box = get_horizontal_box(y1, y2, color, alpha, relative_margin)
    box.Draw()
    return box


def redraw_border():
    """
    Redraw the border in the current pad.
    """
    # Adapted for Python from C++ written by couet:
    # https://root-forum.cern.ch/t/how-to-redraw-axis-and-plot-borders/28252
    ROOT.gPad.Update()
    ROOT.gPad.RedrawAxis()
    l = ROOT.TLine()
    l.DrawLine(
        ROOT.gPad.GetUxmin(),
        ROOT.gPad.GetUymax(),
        ROOT.gPad.GetUxmax(),
        ROOT.gPad.GetUymax(),
    )
    l.DrawLine(
        ROOT.gPad.GetUxmax(),
        ROOT.gPad.GetUymin(),
        ROOT.gPad.GetUxmax(),
        ROOT.gPad.GetUymax(),
    )


def get_pad_xmin():
    return ROOT.gPad.GetUxmin()


def get_pad_xmax():
    return ROOT.gPad.GetUxmax()


def get_pad_ymin():
    return ROOT.gPad.GetUymin()


def get_pad_ymax():
    return ROOT.gPad.GetUymax()


def get_pad_xrange():
    return ROOT.gPad.GetUxmax() - ROOT.gPad.GetUxmin()


def get_pad_yrange():
    return ROOT.gPad.GetUymax() - ROOT.gPad.GetUymin()


def get_pad_xyratio():
    return (ROOT.gPad.GetUxmax() - ROOT.gPad.GetUxmin()) / (
        ROOT.gPad.GetUymax() - ROOT.gPad.GetUymin()
    )


def get_label_anchor_left(x=0.03):
    return x * get_pad_xrange() + get_pad_xmin()


def get_label_anchor_right(x=0.03):
    return (1.0 - x) * get_pad_xrange() + get_pad_xmin()


def get_label_anchor_top(y=0.03):
    return (1.0 - y) * get_pad_yrange() + get_pad_ymin()


def get_label_anchor_bottom(y=0.03):
    return y * get_pad_yrange() + get_pad_ymin()


def draw_label_top_left(
    label: str,
    scaling: Literal["ndc", "pixels"] = "ndc",
    size: Union[int, float] = None,
    text_align: int = ROOT.kVAlignTop + ROOT.kHAlignLeft,
    color: int = ROOT.kBlack,
    margin_NDC: float = 0.03,
) -> ROOT.TLatex:
    """
    Draw a text label in the top-left corner of the current ROOT pad.

    :param label: The label to draw.
    :type label: str

    :param scaling: The type of scaling to use. By default, use NDC scaling. Otherwise, use traditional pixel scaling.
    :type scaling: Literal["ndc", "user"]

    :param size: The size in pixels if using 'pixels' scaling or as a fraction of the pad height if using 'ndc' scaling. If empty, use the default values.
    :type size: int or float, optional

    :param text_align: The ROOT.TAttText text alignment specifier.
    :type text_align: int

    :param color: The ROOT.TColor expressed as an integer.
    :type color: int

    :param margin_NDC: The fraction of the plot window to use as a margin.
    :type margin_NDC: float

    :returns: the ROOT.TLatex object generating the label.
    :rtype: ROOT.TLatex
    :raises ValueError: if the scaling is not 'ndc' or 'pixels'
    """
    ltx = ROOT.TLatex()
    if scaling == "ndc":
        if size is not None:
            ltx.SetTextSize(size)
    elif scaling == "pixels":
        ltx.SetTextFont(63)
        if size is not None:
            ltx.SetTextSizePixels(size)
    else:
        raise ValueError("Scaling must be 'ndc' or 'pixels' only.")
    ltx.SetTextAlign(text_align)
    ltx.SetTextColor(color)
    ltx.DrawLatex(
        get_label_anchor_left(margin_NDC), get_label_anchor_top(margin_NDC), label
    )
    return ltx


def draw_label_top_right(
    label: str,
    scaling: Literal["ndc", "pixels"] = "ndc",
    size: Union[int, float] = None,
    text_align: int = ROOT.kVAlignTop + ROOT.kHAlignRight,
    color: int = ROOT.kBlack,
    margin_NDC: float = 0.03,
) -> ROOT.TLatex:
    """
    Draw a text label in the top-right corner of the current ROOT pad.

    :param label: The label to draw.
    :type label: str

    :param scaling: The type of scaling to use. By default, use NDC scaling. Otherwise, use traditional pixel scaling.
    :type scaling: Literal["ndc", "user"]

    :param size: The size in pixels if using 'pixels' scaling or as a fraction of the pad height if using 'ndc' scaling. If empty, use the default values.
    :type size: int or float, optional

    :param text_align: The ROOT.TAttText text alignment specifier.
    :type text_align: int

    :param color: The ROOT.TColor expressed as an integer.
    :type color: int

    :param margin_NDC: The fraction of the plot window to use as a margin.
    :type margin_NDC: float

    :returns: the ROOT.TLatex object generating the label.
    :rtype: ROOT.TLatex
    :raises ValueError: if the scaling is not 'ndc' or 'pixels'
    """
    ltx = ROOT.TLatex()
    if scaling == "ndc":
        if size is not None:
            ltx.SetTextSize(size)
    elif scaling == "pixels":
        ltx.SetTextFont(63)
        if size is not None:
            ltx.SetTextSizePixels(size)
    else:
        raise ValueError("Scaling must be 'ndc' or 'pixels' only.")
    ltx.SetTextAlign(text_align)
    ltx.SetTextColor(color)
    ltx.DrawLatex(
        get_label_anchor_right(margin_NDC), get_label_anchor_top(margin_NDC), label
    )
    return ltx


def draw_label_bottom_left(
    label: str,
    scaling: Literal["ndc", "pixels"] = "ndc",
    size: Union[int, float] = None,
    text_align: int = ROOT.kVAlignBottom + ROOT.kHAlignLeft,
    color: int = ROOT.kBlack,
    margin_NDC: float = 0.03,
) -> ROOT.TLatex:
    """
    Draw a text label in the bottom-left corner of the current ROOT pad.

    :param label: The label to draw.
    :type label: str

    :param scaling: The type of scaling to use. By default, use NDC scaling. Otherwise, use traditional pixel scaling.
    :type scaling: Literal["ndc", "user"]

    :param size: The size in pixels if using 'pixels' scaling or as a fraction of the pad height if using 'ndc' scaling. If empty, use the default values.
    :type size: int or float, optional

    :param text_align: The ROOT.TAttText text alignment specifier.
    :type text_align: int

    :param color: The ROOT.TColor expressed as an integer.
    :type color: int

    :param margin_NDC: The fraction of the plot window to use as a margin.
    :type margin_NDC: float

    :returns: the ROOT.TLatex object generating the label.
    :rtype: ROOT.TLatex
    :raises ValueError: if the scaling is not 'ndc' or 'pixels'
    """
    ltx = ROOT.TLatex()
    if scaling == "ndc":
        if size is not None:
            ltx.SetTextSize(size)
    elif scaling == "pixels":
        ltx.SetTextFont(63)
        if size is not None:
            ltx.SetTextSizePixels(size)
    else:
        raise ValueError("Scaling must be 'ndc' or 'pixels' only.")
    ltx.SetTextAlign(text_align)
    ltx.SetTextColor(color)
    ltx.DrawLatex(
        get_label_anchor_left(margin_NDC), get_label_anchor_bottom(margin_NDC), label
    )
    return ltx


def draw_label_bottom_right(
    label: str,
    scaling: Literal["ndc", "pixels"] = "ndc",
    size: Union[int, float] = None,
    text_align: int = ROOT.kVAlignBottom + ROOT.kHAlignRight,
    color: int = ROOT.kBlack,
    margin_NDC: float = 0.03,
) -> ROOT.TLatex:
    """
    Draw a text label in the bottom-right corner of the current ROOT pad.

    :param label: The label to draw.
    :type label: str

    :param scaling: The type of scaling to use. By default, use NDC scaling. Otherwise, use traditional pixel scaling.
    :type scaling: Literal["ndc", "user"]

    :param size: The size in pixels if using 'pixels' scaling or as a fraction of the pad height if using 'ndc' scaling. If empty, use the default values.
    :type size: int or float, optional

    :param text_align: The ROOT.TAttText text alignment specifier.
    :type text_align: int

    :param color: The ROOT.TColor expressed as an integer.
    :type color: int

    :param margin_NDC: The fraction of the plot window to use as a margin.
    :type margin_NDC: float

    :returns: the ROOT.TLatex object generating the label.
    :rtype: ROOT.TLatex
    :raises ValueError: if the scaling is not 'ndc' or 'pixels'
    """
    ltx = ROOT.TLatex()
    if scaling == "ndc":
        if size is not None:
            ltx.SetTextSize(size)
    elif scaling == "pixels":
        ltx.SetTextFont(63)
        if size is not None:
            ltx.SetTextSizePixels(size)
    else:
        raise ValueError("Scaling must be 'ndc' or 'pixels' only.")
    ltx.SetTextAlign(text_align)
    ltx.SetTextColor(color)
    ltx.DrawLatex(
        get_label_anchor_right(margin_NDC), get_label_anchor_bottom(margin_NDC), label
    )
    return ltx


def draw_label_at_fraction(
    label: str,
    font: int = 6,
    scaling: Literal["ndc", "pixels"] = "ndc",
    size: Union[int, float] = None,
    text_align: int = "top right",
    color: int = ROOT.kBlack,
    x: float = 0.95,
    y: float = 0.95,
) -> ROOT.TLatex:
    """
    Draw a text label at the given position relative to the size of the plot content. Accounts for log scaling.

    :param label: The label to draw.
    :type label: str

    :param font: The font to use. ROOT enables fonts [1, 14].
    :type label: int

    :param scaling: The type of scaling to use. By default, use NDC scaling. Otherwise, use traditional pixel scaling.
    :type scaling: Literal["ndc", "pixels"]

    :param size: The size in pixels if using 'pixels' scaling or as a fraction of the pad height if using 'ndc' scaling. If empty, use the default values.
    :type size: int or float, optional

    :param text_align: The ROOT.TAttText text alignment specifier.
    :type text_align: int

    :param color: The ROOT.TColor expressed as an integer.
    :type color: int

    :param x: Where to plot the label anchor horizontally, as a fraction of the plot content.
    :type x: float

    :param y: Where to plot the label anchor vertically, as a fraction of the plot content.
    :type y: float

    :returns: the ROOT.TLatex object generating the label.
    :rtype: ROOT.TLatex
    :raises ValueError: if the scaling is not 'ndc' or 'pixels'
    """
    # Set up a TLatex
    ltx = ROOT.TLatex()
    # Set the font, precision, and size
    if font < 1 or font > 14:
        raise ValueError("Font must be an integer between 1 and 14, inclusive.")
    if scaling == "ndc":
        ltx.SetTextFont(font*10 + 2)
        if size is not None:
            ltx.SetTextSize(size)
    elif scaling == "pixels":
        ltx.SetTextFont(font*10 + 3)
        if size is not None:
            ltx.SetTextSizePixels(size)
    else:
        raise ValueError("Scaling must be 'ndc' or 'pixels' only.")
    # Set the alignment using strings or integers
    if type(text_align) == int:
        ltx.SetTextAlign(text_align)
    elif type(text_align) == str:
        lc_text_align = text_align.lower()
        if   lc_text_align == "top right" or lc_text_align == "right top":
            ltx.SetTextAlign(ROOT.kVAlignTop + ROOT.kHAlignRight)
        elif lc_text_align == "top left" or lc_text_align == "left top":
            ltx.SetTextAlign(ROOT.kVAlignTop + ROOT.kHAlignLeft)
        elif lc_text_align == "bottom right" or lc_text_align == "right bottom":
            ltx.SetTextAlign(ROOT.kVAlignBottom + ROOT.kHAlignRight)
        elif lc_text_align == "bottom left" or lc_text_align == "left bottom":
            ltx.SetTextAlign(ROOT.kVAlignBottom + ROOT.kHAlignLeft)
        else:
            raise ValueError("When passing strings as text alignment, must use 'top/bottom left/right'.")
    else:
        raise ValueError("Text alignment must be an integer or a string!")
    # Set the color
    ltx.SetTextColor(color)
    # Figure out where to draw it, assuming the current pad
    left_margin   = ROOT.gPad.GetLeftMargin()
    right_margin  = ROOT.gPad.GetRightMargin()
    top_margin    = ROOT.gPad.GetTopMargin()
    bottom_margin = ROOT.gPad.GetBottomMargin()
    x_NDC = left_margin   + x * (1.0 - left_margin - right_margin)
    y_NDC = bottom_margin + y * (1.0 - bottom_margin - top_margin)
    ltx.DrawLatexNDC(x_NDC, y_NDC, label)
    return ltx


def make_multi_pad_canvas(
    rows=1,
    columns=1,
    normal_height=None,
    normal_width=None,
    info_height=100,
    name="",
    title="Canvas",
    extras=0,
):
    """
    Make a grid of identical canvases with room on the bottom for an info
    panel, such as a legend or other notes. This is a non-trivial problem
    because ideally you want all the plots--not pads--to be the same size,
    accounting for margins.
    """

    if extras >= columns:
        raise ValueError("Extras must be less than the number of columns!")
    enable_extras_panel = True
    if extras < 0:
        extras = -extras
        enable_extras_panel = False

    f_normal_height = (
        int(ROOT.gStyle.GetCanvasDefH()) if normal_height is None else normal_height
    )
    f_normal_width = (
        int(ROOT.gStyle.GetCanvasDefW()) if normal_width is None else normal_width
    )
    f_info_height = int(info_height)

    pad_top_margin_NDC    = ROOT.gStyle.GetPadTopMargin()
    pad_bottom_margin_NDC = ROOT.gStyle.GetPadBottomMargin()
    pad_left_margin_NDC   = ROOT.gStyle.GetPadLeftMargin()
    pad_right_margin_NDC  = ROOT.gStyle.GetPadRightMargin()

    pad_top_margin    = int(pad_top_margin_NDC    * f_normal_height)
    pad_bottom_margin = int(pad_bottom_margin_NDC * f_normal_height)
    pad_left_margin   = int(pad_left_margin_NDC   * f_normal_width)
    pad_right_margin  = int(pad_right_margin_NDC  * f_normal_width)

    plot_height = f_normal_height - pad_top_margin - pad_bottom_margin
    plot_width = f_normal_width - pad_left_margin - pad_right_margin

    canvas_height = (
        pad_top_margin + pad_bottom_margin + (rows * plot_height) + info_height
    )
    canvas_width = pad_left_margin + pad_right_margin + (columns * plot_width)

    canvas = ROOT.TCanvas(name, title, canvas_width, canvas_height)

    grid_pads = []

    info_pad_bottom_left_x = 0
    info_pad_bottom_left_y = 0
    info_pad_top_right_x = 1.0
    info_pad_top_right_y = info_height / canvas_height

    current_top_left_x = 0
    current_top_left_y = 1.0

    clamp = lambda x: max(0.0, min(x, 1.0))

    escape_loop = False

    for ri in range(rows):

        for ci in range(columns):

            pad_number = ri * columns + ci + 1
            pad_name = f"canvas_{name}_pad_{pad_number}"

            current_top_margin = int(ri == 0) * pad_top_margin
            current_bottom_margin = int(ri == rows - 1) * pad_bottom_margin
            current_left_margin = int(ci == 0) * pad_left_margin
            current_right_margin = int(ci == columns - 1) * pad_right_margin

            current_pad_height = (
                current_top_margin + current_bottom_margin + plot_height
            )
            current_pad_width = current_left_margin + current_right_margin + plot_width

            current_pad_height_ndc = current_pad_height / canvas_height
            current_pad_width_ndc = current_pad_width / canvas_width

            extra_top_buffer = 0
            extra_bottom_buffer = 0
            if extras and ri == rows - 2 and ci >= columns - extras: 
                extra_bottom_buffer = pad_bottom_margin
            if extras and ri == rows - 1 and ci >= columns - extras: 
                extra_top_buffer = pad_bottom_margin
                # Break here because no more plots need to be drawn
                # We'll draw one more special panel, the "extras" panel
                # that contains the remaining space after the loop
                escape_loop = True
                continue

            ipad = ROOT.TPad(
                pad_name,
                pad_name,
                clamp(current_top_left_x),
                clamp(current_top_left_y - current_pad_height_ndc - extra_bottom_buffer / canvas_height),
                clamp(current_top_left_x + current_pad_width_ndc),
                clamp(current_top_left_y),
            )

            ipad.SetNumber(pad_number)

            ipad.SetTopMargin(current_top_margin / current_pad_height)
            ipad.SetBottomMargin((current_bottom_margin + extra_bottom_buffer) / (current_pad_height + extra_bottom_buffer))
            ipad.SetLeftMargin(current_left_margin / current_pad_width)
            ipad.SetRightMargin(current_right_margin / current_pad_width)

            ipad.Draw()

            grid_pads.append(ipad)

            current_top_left_x += current_pad_width_ndc

        if escape_loop: break

        current_top_left_x = 0.0
        current_top_left_y -= current_pad_height_ndc

    canvas._grid_pads = grid_pads

    # If there is extra space, make an "extras panel"
    # This panel is just meant for things like text and legends
    # It will have zero margins and a weird shape so it is
    # not suitable for plotting
    extras_pad = None
    if extras and enable_extras_panel:
        extras_pad_name = f"canvas_{name}_extras_pad"
        extras_pad = ROOT.TPad(
            extras_pad_name,
            extras_pad_name,
            # Use the left/bottom margins for both sides
            # # It just looks better generally 
            clamp(current_top_left_x + pad_left_margin / canvas_width),    # LEFT
            #clamp(pad_bottom_margin / canvas_height),                      # BOTTOM
            #clamp(((info_pad_top_right_y * canvas_height) + pad_bottom_margin )/ canvas_height),                                   # BOTTOM
            clamp(info_pad_top_right_y + pad_bottom_margin / canvas_height),                                   # BOTTOM
            clamp((canvas_width - pad_left_margin) / canvas_width),        # RIGHT
            clamp(current_top_left_y - pad_bottom_margin / canvas_height), # TOP
        )
        extras_pad.SetTopMargin(0.0)
        extras_pad.SetBottomMargin(0.0)
        extras_pad.SetLeftMargin(0.0)
        extras_pad.SetRightMargin(0.0)
        extras_pad.Draw()
    canvas._extras_pad = extras_pad


    # And lastly make the info panel
    info_pad = None
    if info_height:
        info_pad_name = f"canvas_{name}_info_pad"
        info_pad = ROOT.TPad(
            info_pad_name,
            info_pad_name,
            info_pad_bottom_left_x,
            info_pad_bottom_left_y,
            info_pad_top_right_x,
            info_pad_top_right_y,
        )
        info_pad.SetNumber(rows * columns + 1)
        info_pad.Draw()
    canvas._info_pad = info_pad
    
    return canvas
