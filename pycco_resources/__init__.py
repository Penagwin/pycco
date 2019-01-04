import pystache

css = """\
.pydoc {
  padding-top: 0px!important;
  padding-bottom: 0px!important;
  margin-top: 0px!important;
  padding-left: 15px;
  margin-bottom: 0px!important;
  font-size: .75em!important;
  background-color: #fafafa;

}

.def.nf{
  font-wieght: lighter;
  font-size: .9em; 
}

.class.nf code::before {
  content: "Class - ";
  color: #a0a0a0;

}


.indent-docs p:first-of-type {
  margin-top: 15px;
}

.declaration {
  font-weight: bold;
      padding-top: 5px!important;
    padding-bottom: 5px!important;
    margin-top: 0px!important;
    padding-left: 2.8em!important;
    font-size: .9em;
    margin-bottom: 0px!important;
    background-color: #fafafa;
}

.pydoc:first-of-type {
    padding-top: 5px!important;
}
.pydoc:last-of-type {
    padding-bottom: 5px!important;
}

.pydoc + p{
  margin-top: 5px;

}

.pydoc.indent {
  padding-left: 2em;
  text-indent: 0em;
}

.indent-docs {
    padding-left: 3em;
}
.single_comment {
    color: #99A4AE;
}
.codehilite {
  font-size: .8em;
}
/*--------------------- Layout and Typography ----------------------------*/
body {
  font-family: 'Palatino Linotype', 'Book Antiqua', Palatino, FreeSerif, serif;
  font-size: 16px;
  line-height: 24px;
  color: #252519;
  margin: 0; padding: 0;
  background: #f5f5ff;
}
a {
  color: #261a3b;
}
  a:visited {
    color: #261a3b;
  }
p {
  margin: 0 0 0px 0;
}
h1, h2, h3, h4, h5, h6 {
  margin: 40px 0 15px 0;
}
h2, h3, h4, h5, h6 {
    margin-top: 0;
  }
#container {
  background: white;
 }
#container, div.section {
  position: relative;
}

#container, div.section:first-of-type {
  position: relative;
  padding-bottom: 0;
}
#background {
  position: absolute;
  top: 0; left: 780px; right: 0; bottom: 0;
  background: #f5f5ff;
  border-left: 1px solid #e5e5ee;
  z-index: 0;
}
#jump_to, #jump_page {
  background: white;
  -webkit-box-shadow: 0 0 25px #777; -moz-box-shadow: 0 0 25px #777;
  -webkit-border-bottom-left-radius: 5px; -moz-border-radius-bottomleft: 5px;
  font: 10px Arial;
  text-transform: uppercase;
  cursor: pointer;
  text-align: right;
}
#jump_to, #jump_wrapper {
  position: fixed;
  right: 0; top: 0;
  padding: 5px 10px;
}
  #jump_wrapper {
    padding: 0;
    display: none;
  }
    #jump_to:hover #jump_wrapper {
      display: block;
    }
    #jump_page {
      padding: 5px 0 3px;
      margin: 0 0 25px 25px;
    }
      #jump_page .source {
        display: block;
        padding: 5px 10px;
        text-decoration: none;
        border-top: 1px solid #eee;
      }
        #jump_page .source:hover {
          background: #f5f5ff;
        }
        #jump_page .source:first-child {
        }
div.docs {
  float: left;
  max-width: 700px;
  min-width: 700px;
  min-height: 5px;
  padding: 10px 25px 1px 50px;
  vertical-align: top;
  text-align: left;
    padding-bottom: 2em!important;
}

div.docs:first-child {
      padding-bottom: 0em;

}
  .docs pre {
    margin: 15px 0 15px;
    white-space: pre-wrap;
    padding-left: 4em;
    text-indent: -2em;
  }
  .docs p tt, .docs p code {
    background: #f8f8ff;
    border: 1px solid #dedede;
    font-size: 12px;
    padding: 0 0.2em;
  }
  .octowrap {
    position: relative;
  }
    .octothorpe {
      font: 12px Arial;
      text-decoration: none;
      color: #454545;
      position: absolute;
      top: 3px; left: -20px;
      padding: 1px 2px;
      opacity: 0;
      -webkit-transition: opacity 0.2s linear;
    }
      div.docs:hover .octothorpe {
        opacity: 1;
      }
div.code {
  border-top: 1px #c5c5cc dotted;
  margin-left: 780px;
  padding: 14px 15px 16px 50px;
  vertical-align: top;
}
  .code pre, .docs p code {
    font-size: 12px;
  }
    pre, tt, code {
      line-height: 18px;
      font-family: Monaco, Consolas, "Lucida Console", monospace;
      margin: 0; padding: 0;
    }
div.clearall {
    clear: both;
}


/*---------------------- Syntax Highlighting -----------------------------*/
td.linenos { background-color: #f0f0f0; padding-right: 10px; }
span.lineno { background-color: #f0f0f0; padding: 0 5px 0 5px; }
body .hll { background-color: #ffffcc }
body .c { color: #408080; font-style: italic }  /* Comment */
body .err { border: 1px solid #FF0000 }         /* Error */
body .k { color: #954121 }                      /* Keyword */
body .o { color: #666666 }                      /* Operator */
body .cm { color: #408080; font-style: italic } /* Comment.Multiline */
body .cp { color: #BC7A00 }                     /* Comment.Preproc */
body .c1 { color: #408080; font-style: italic } /* Comment.Single */
body .cs { color: #408080; font-style: italic } /* Comment.Special */
body .gd { color: #A00000 }                     /* Generic.Deleted */
body .ge { font-style: italic }                 /* Generic.Emph */
body .gr { color: #FF0000 }                     /* Generic.Error */
body .gh { color: #000080; font-weight: bold }  /* Generic.Heading */
body .gi { color: #00A000 }                     /* Generic.Inserted */
body .go { color: #808080 }                     /* Generic.Output */
body .gp { color: #000080; font-weight: bold }  /* Generic.Prompt */
body .gs { font-weight: bold }                  /* Generic.Strong */
body .gu { color: #800080; font-weight: bold }  /* Generic.Subheading */
body .gt { color: #0040D0 }                     /* Generic.Traceback */
body .kc { color: #954121 }                     /* Keyword.Constant */
body .kd { color: #954121; font-weight: bold }  /* Keyword.Declaration */
body .kn { color: #954121; font-weight: bold }  /* Keyword.Namespace */
body .kp { color: #954121 }                     /* Keyword.Pseudo */
body .kr { color: #954121; font-weight: bold }  /* Keyword.Reserved */
body .kt { color: #B00040 }                     /* Keyword.Type */
body .m { color: #666666 }                      /* Literal.Number */
body .s { color: #219161 }                      /* Literal.String */
body .na { color: #7D9029 }                     /* Name.Attribute */
body .nb { color: #954121 }                     /* Name.Builtin */
body .nc { color: #0000FF; font-weight: bold }  /* Name.Class */
body .no { color: #880000 }                     /* Name.Constant */
body .nd { color: #AA22FF }                     /* Name.Decorator */
body .ni { color: #999999; font-weight: bold }  /* Name.Entity */
body .ne { color: #D2413A; font-weight: bold }  /* Name.Exception */
body .nf { color: #0000FF }                     /* Name.Function */
body .nl { color: #A0A000 }                     /* Name.Label */
body .nn { color: #0000FF; font-weight: bold }  /* Name.Namespace */
body .nt { color: #954121; font-weight: bold }  /* Name.Tag */
body .nv { color: #19469D }                     /* Name.Variable */
body .ow { color: #AA22FF; font-weight: bold }  /* Operator.Word */
body .w { color: #bbbbbb }                      /* Text.Whitespace */
body .mf { color: #666666 }                     /* Literal.Number.Float */
body .mh { color: #666666 }                     /* Literal.Number.Hex */
body .mi { color: #666666 }                     /* Literal.Number.Integer */
body .mo { color: #666666 }                     /* Literal.Number.Oct */
body .sb { color: #219161 }                     /* Literal.String.Backtick */
body .sc { color: #219161 }                     /* Literal.String.Char */
body .sd { color: #219161; font-style: italic } /* Literal.String.Doc */
body .s2 { color: #219161 }                     /* Literal.String.Double */
body .se { color: #BB6622; font-weight: bold }  /* Literal.String.Escape */
body .sh { color: #219161 }                     /* Literal.String.Heredoc */
body .si { color: #BB6688; font-weight: bold }  /* Literal.String.Interpol */
body .sx { color: #954121 }                     /* Literal.String.Other */
body .sr { color: #BB6688 }                     /* Literal.String.Regex */
body .s1 { color: #219161 }                     /* Literal.String.Single */
body .ss { color: #19469D }                     /* Literal.String.Symbol */
body .bp { color: #954121 }                     /* Name.Builtin.Pseudo */
body .vc { color: #19469D }                     /* Name.Variable.Class */
body .vg { color: #19469D }                     /* Name.Variable.Global */
body .vi { color: #19469D }                     /* Name.Variable.Instance */
body .il { color: #666666 }                     /* Literal.Number.Integer.Long */
"""

html = """\
<!DOCTYPE html>
<html>
<head>
  <meta http-equiv="content-type" content="text/html;charset=utf-8">
  <title>{{ title }}</title>
  <link rel="stylesheet" href="{{ stylesheet }}">
  <style>.markdown-section#main{
    max-width: initial!important;
}</style>
</head>
<body>
<div id='container'>
  <div id="background"></div>
  {{#sources?}}
  <div id="jump_to">
    Jump To &hellip;
    <div id="jump_wrapper">
      <div id="jump_page">
        {{#sources}}
          <a class="source" href="{{ url }}">{{ basename }}</a>
        {{/sources}}
      </div>
    </div>
  </div>
  {{/sources?}}
  <div class='section'>
    <div class='docs'><h1>{{ title }}</h1></div>
  </div>
  <div class='clearall'>
  {{#sections}}
  <div class='section' id='section-{{ num }}'>
    <div class='docs'>
      <div class='octowrap'>
        <a class='octothorpe' href='#section-{{ num }}'>#</a>
      </div>
      {{{ docs_html }}}
    </div>
    <div class='code'>
      {{{ code_html }}}
    </div>
  </div>
  <div class='clearall'></div>
  {{/sections}}
</div>
</body>
"""


def template(source):
    return lambda context: pystache.render(source, context)
# Create the template that we will use to generate the Pycco HTML page.
pycco_template = template(html)
