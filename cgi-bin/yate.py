from string import Template


def start_response(response='text/html'):
    return f'Content-type: {response}'

def include_header(title):
    with open('../templates/header.html') as headf:
        text = headf.read()
    header = Template(text)
    return header.substitute(title=title)

def include_footer(links):
    with open('../templates/footer.html') as footf:
        text = footf.read()
    link_string = ''
    for link in links:
        link_string += f'<a href="{links[link]}">{link}</a>&nbsp;&nbsp;&nbsp;'
    footer = Template(text)
    return footer.substitute(links=link_string)

def start_form(url_action, method="POST"):
    return f'<form action="{url_action}" method="{method}">'

def end_form(value="Submit"):
    return f'<p></p><input type=submit value="{value}">'

def radio_button(name, value):
    return f'<input type="radio" name="{name}" value="{value}">{value}<br />'

def u_list(items):
    u_string = '<ul>'
    for item in items:
        u_string += f'<li>{item}</li>'
    u_string += '</ul>'
    return u_string

def head(text, level=2):
    return f'<h{level}>{text}</h{level}>'

def para(text):
    return f'<p>{text}</p>'


print(start_response())
print(include_header('I and Mucura in the canoe.'))
print(head('I and Mucura in the canoe.'))
print(include_footer({'Home': '/index.html', 'Select': '/cgi-bin/select.py'}))
print(start_form('cgi-bin/process_athlete.py'))
print(end_form())
for fab in ['John', 'Paul', 'George', 'Ringo']:
    print(radio_button(fab, fab))
print(u_list(['Life of Brian', 'Hole Grail']))
