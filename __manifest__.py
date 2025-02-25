# noinspection PyStatementEffect
{
    'name': 'To-DO List',
    'author': 'Hassan Haridy',
    'version': '17.0.0.1.0',
    'category': '',
    'depends': [
        'base', 'mail'
    ],
    'data':[
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/base_menu.xml',
        'views/todo_task_view.xml',
    ],
    'assets':{

    },
    'application': True,
}