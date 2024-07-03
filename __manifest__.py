{
    'name': 'Department status button',
    'version': '0.0.1',
    'category': '',
    'description': 'Adding the number of statuses in a department',
    'website': 'https://nvt.miem.hse.ru',
    'author': 'Tselovalnikova A.T.',
    'depends': [
        'base',
        'hr',
        'hr_employee_status'
    ],
    'installable': True,
    'application': False,
    'data': [
        'views/hr_department_views.xml',
    ],
}
