# -*- coding: utf-8 -*-

"""
This file is part of the Mouseover Dictionary add-on for Anki.

Note type and card templates.

Copyright: (c) 2018 Glutanimate <https://glutanimate.com/>
License: GNU AGPLv3 <https://www.gnu.org/licenses/agpl.html>
"""

from __future__ import unicode_literals

from .config import NOTETYPE, TERM_FIELD, DEFINITION_FIELD

fields = (
    TERM_FIELD,
    DEFINITION_FIELD
)

# Default card template
card_front = """\
<b>Define</b>: {{%s}}
""" % TERM_FIELD

card_back = """\
{{FrontSide}}

<hr id=answer>

{{%s}}
""" % DEFINITION_FIELD

css = """\
.card {
 font-family: arial;
 font-size: 20px;
 text-align: center;
 color: black;
 background-color: white;
}
"""


def addModel(col):
  models = col.models
  def_model = models.new(NOTETYPE)
  # Add fields:
  for fname in fields:
    fld = models.newField(fname)
    models.addField(def_model, fld)
  # Add template
  template = models.newTemplate("Definition")
  template['qfmt'] = card_front
  template['afmt'] = card_back
  def_model['css'] = css
  models.addTemplate(def_model, template)
  models.add(def_model)
  return def_model