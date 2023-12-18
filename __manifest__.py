{
    # App information
    'name': 'Personalización para Tu Boda Hoy',
    'version': '15.0.1',
    'category': 'Other',
    'license': 'AGPL-3',
    # Author
    'author': 'Javier L. de los Mozos',
    'website': 'http://www.jdelosmozos.com',
    'maintainer': 'jdelosmozos@coit.es',
    # Dependencies
    'depends': ['crm', 'project', 'projectProduct'],
    'data':[
            'security/ir.model.access.csv',
            'views/view_event.xml',
            'views/view_proceedings.xml',
            'views/crm_lead_view.xml',
            'views/project_task_views.xml',
            ],
    'installable': True,
}
