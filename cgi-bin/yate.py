from pathlib import Path
from string import Template


def start_response(response='text/html; charset=utf-8\n\n'):
    return f'Content-Type: {response}'

def start_page(title):
    file = Path.cwd() / 'templates' / 'start_page.html'
    with open (file) as stf:
        text = stf.read()
    start = Template(text)
    return start.substitute(title=title)

def include_header(title):
    file = Path.cwd() / 'templates' / 'header.html'
    with open(file) as headf:
        text = headf.read()
    header = Template(text)
    return header.substitute(title=title)

def include_footer(links):
    file = Path.cwd() / 'templates' / 'footer.html'
    with open(file) as footf:
        text = footf.read()
    link_string = ''
    for link in links:
        link_string += f'<a href="{links[link]}">{link}</a>&nbsp;&nbsp;&nbsp;'
    footer = Template(text)
    return footer.substitute(links=link_string)

def start_form(url_action, method="POST"):
    return f'<form action="{url_action}" method="{method}">'

def end_form(value="Submit"):
    return f'<p></p><input type=submit value="{value}"></form>'

def radio_button(name, value):
    return f'<input type="radio" name="{name}" value="{value}">{value}<br />'

def u_list(items):
    u_string = '<ul>'
    for item in items:
        u_string += f'<li>{item}</li>'
    u_string += '</ul>'
    return u_string

def header(text, level=2):
    return f'<h{level}>{text}</h{level}>'

def para(text):
    return f'<p>{text}</p>'

def do_form(action, time_value, text):
    file = Path.cwd() / 'templates' / 'form.html'
    with open(file) as formf:
        text_form = formf.read()
    form = Template(text_form)
    return form.substitute(action=action, time_value=time_value, text=text)

