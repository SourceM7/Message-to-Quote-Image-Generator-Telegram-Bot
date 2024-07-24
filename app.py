# -*- coding: utf-8 -*-
from html2image import Html2Image
from PIL import Image
from jinja2 import Environment, FileSystemLoader

def render_quote(mentioned_message, mentioned_user):
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('index.html')

    data = {
        'user': mentioned_user,
        'message': mentioned_message
    }

    rendered_html = template.render(data)

    with open('rendered_index.html', 'w',encoding='utf-8') as file:
        file.write(rendered_html)

    hti = Html2Image()
    hti.size = (413, 250)
    hti.screenshot(
        html_file='rendered_index.html', css_file='styles.css',
        save_as='temp_blue_page.png'
    )

    return 'temp_blue_page.png'