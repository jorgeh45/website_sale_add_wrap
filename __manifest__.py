{
    'name': 'Website Sale-Gift Wrap',
    'category': 'Website',
    'summary': 'Add gift wrap option in the cart',
    'version': '1.0',
    'description': """
        Add the option to indicate if the product has a wrap
        """,
    'author': 'Jorge Miguel Hernandez Santos (dev.jhernandez@gmail.com)',
    'depends': ['sale',
                'website',
                'website_sale'],
    'data': [
        'views/template.xml',
        'views/sale_order_line.xml'
    ],
    'qweb': ['static/src/xml/*.xml'],

    'installable': True,
    'application': True,
}
