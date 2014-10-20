# encoding: utf-8

"""
Desc: A filter to highlight code blocks in html with Pygments and BeautifulSoup.
Usage:  {% load highlight_code %}
        {{ text|formatCode|safe }}
"""

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

from pygments import highlight
from pygments.lexers import get_lexer_for_filename, guess_lexer
from pygments.formatters.html import HtmlFormatter

import re

register = template.Library()
regexp = re.compile("{{{(?P<comment>.*)}{(?P<code>.*)}}}")

@register.filter
@stringfilter
def formatCode(code, name):
    ''' Removes specials comments and then formats the code using pygments'''

    formatter = HtmlFormatter(linenum="table")
    raw_cleaned_code = matcher(code)
    
    # guess lexer from code
    try:
        lexer = get_lexer_for_filename(name)
    except:
        lexer = guess_lexer(code)

    cleaned_code = "<p>Parsed by the "+lexer.name+" lexer.</p>"
    # get the code, parse it and add <span id="comment_#">
    for block in raw_cleaned_code:
        cleaned_code += '<div class="commented_block">'
        cleaned_code += '<div class="cm floating_comment">'
        cleaned_code += get_key(block, "comment")
        cleaned_code += '</div>'
        cleaned_code += '<div class="code">'
        cleaned_code += highlight(get_key(block,"code"), lexer, formatter)
        cleaned_code += '</div>'
        cleaned_code += '</div>'

    return cleaned_code

def get_key (d, key):
    r = d.get(key)
    if r == None:
        return ""
    else:
        return r

def next3(code):
    ''' Finds the first occurence of '{{{', '}-{' or '}}}' '''
    
    for k in range(len(code)-2):
        yield (k, code[k:k+3])

def matcher(code):
    '''
    Matches the form {{{ Comment }{ Code }}}
    and returns a list of dictionnaries {code: "",comment:""}.
    The two preceding and following characters are removed.
    '''
    opened_braces = 0
    counter = 0

    brace_beg = 0
    brace_end = 0
    brace_middle = -1

    listed_code = []

    for pos,s in next3(code):
        if s == "{{{": # starting comment

            opened_braces += 1
            if opened_braces == 1:
                brace_beg = pos
                counter += 1
                listed_code.append({
                    'code': code[brace_end:brace_beg-2],
                    'n'   : counter
                })
            print "\t{{{ matched\t", opened_braces

        elif s == "}-{" and opened_braces == 1: # switching (count only if in lvl 1 comment)
            brace_middle = pos
            print "\t}-{ matched\t", opened_braces

        elif s == "}}}": # brace_ending comment
            opened_braces -= 1

            # if switched back to lvl 0
            if opened_braces == 0:
                brace_end = pos + 3
                if brace_middle < brace_beg + 3:
                    counter += 1
                    listed_code.append({
                        'comment': code[brace_beg+3:brace_end-3],
                        'n'      : counter
                    })
                    print brace_beg+3, brace_end
                else:
                    counter += 1
                    listed_code.append({
                        'comment': code[brace_beg+3:brace_middle],
                        'code'   : code[brace_middle+3:brace_end-3-2],
                        'n'      : counter
                    })
            print "\t}}} matched\t", opened_braces

        if opened_braces < 0:
            raise Exception("Unbalanced parentheses!")

    if opened_braces != 0:
            raise Exception("Unbalanced parentheses!")

    # add the end of the code
    counter += 1
    listed_code.append({
        "code": code[brace_end-2:],
        'n'   : counter})
    return listed_code

