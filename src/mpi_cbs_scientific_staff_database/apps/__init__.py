from nomad.config.models.plugins import AppEntryPoint
from nomad.config.models.ui import (
    App,
    Axis,
    Column,
    Columns,
    Dashboard,
    Filters,
    Layout,
    Menu,
    MenuItemCustomQuantities,
    MenuItemDefinitions,
    MenuItemHistogram,
    MenuItemTerms,
    MenuItemVisibility,
    SearchQuantities,
    WidgetTerms,
)

schema = (
    'mpi_cbs_scientific_staff_database.schema_packages.schema_package.'
    'ScientificStaffProfile'
)


def widget_layout(index: int) -> dict[str, Layout]:
    md_x = 4 * (index % 4)
    md_y = 3 * (index // 4)
    xl_x = 8 * (index % 3)
    xl_y = 3 * (index // 3)
    xxl_x = 10 * (index % 3)
    xxl_y = 3 * (index // 3)

    return {
        'sm': Layout(h=3, w=12, x=0, y=3 * index, minH=3, minW=4),
        'md': Layout(h=3, w=4, x=md_x, y=md_y, minH=3, minW=4),
        'lg': Layout(h=3, w=4, x=md_x, y=md_y, minH=3, minW=4),
        'xl': Layout(h=3, w=8, x=xl_x, y=xl_y, minH=3, minW=4),
        'xxl': Layout(h=3, w=10, x=xxl_x, y=xxl_y, minH=3, minW=4),
    }


app_entry_point = AppEntryPoint(
    name='Scientific Staff Database',
    description='Search app for MPI CBS scientific staff expertise profiles.',
    app=App(
        label='Scientific Staff',
        path='scientific-staff',
        category='CBS',
        description='Search scientific staff expertise profiles.',
        readme=(
            'This page allows you to search **MPI CBS scientific staff profiles** '
            'by role, affiliation, expertise, methods, skills, tools, subject '
            'populations, socials, equipment, and update date.'
        ),
        search_quantities=SearchQuantities(include=[f'*#{schema}']),
        filters_locked={'section_defs.definition_qualified_name': schema},
        filters=Filters(exclude=['mainfile', 'entry_name', 'combine']),
        columns=Columns(
            selected=[
                f'data.display_name#{schema}',
                f'data.email#{schema}',
                f'data.position_role#{schema}',
                f'data.department_or_independent_group#{schema}',
                f'data.main_expertise_type#{schema}',
                f'data.last_updated#{schema}',
            ],
            options={
                f'data.display_name#{schema}': Column(label='Display Name'),
                f'data.email#{schema}': Column(label='Email'),
                f'data.position_role#{schema}': Column(label='Position / Role'),
                f'data.department_or_independent_group#{schema}': Column(
                    label='Department / Independent Group'
                ),
                f'data.main_expertise_type#{schema}': Column(
                    label='Main Expertise Type'
                ),
                f'data.last_updated#{schema}': Column(label='Last Updated'),
            },
        ),
        dashboard=Dashboard(
            widgets=[
                WidgetTerms(
                    title='Display Name',
                    search_quantity=f'data.display_name#{schema}',
                    layout=widget_layout(0),
                    show_input=True,
                ),
                WidgetTerms(
                    title='Position / Role',
                    search_quantity=f'data.position_role#{schema}',
                    layout=widget_layout(1),
                    show_input=True,
                ),
                WidgetTerms(
                    title='Department / Independent Group',
                    search_quantity=(
                        f'data.department_or_independent_group#{schema}'
                    ),
                    layout=widget_layout(2),
                    show_input=True,
                ),
                WidgetTerms(
                    title='Main Expertise Type',
                    search_quantity=f'data.main_expertise_type#{schema}',
                    layout=widget_layout(3),
                    show_input=True,
                ),
            ],
        ),
        menu=Menu(
            title='Filters',
            size='sm',
            items=[
                Menu(
                    title='Staff',
                    items=[
                        MenuItemTerms(
                            title='Display Name / Email',
                            search_quantity='results.eln.names',
                            options=0,
                        ),
                        MenuItemTerms(
                            search_quantity=f'data.position_role#{schema}',
                            options=10,
                        ),
                        MenuItemTerms(
                            search_quantity=(
                                f'data.department_or_independent_group#{schema}'
                            ),
                            options=10,
                        ),
                        MenuItemTerms(
                            search_quantity=f'data.subgroup_lab_team#{schema}',
                            options=10,
                        ),
                    ],
                ),
                Menu(
                    title='Expertise',
                    size='lg',
                    items=[
                        MenuItemTerms(
                            search_quantity=f'data.main_expertise_type#{schema}',
                            options=10,
                        ),
                        MenuItemTerms(
                            title='Expertise Summary',
                            search_quantity='results.eln.descriptions',
                            options=0,
                        ),
                    ],
                ),
                Menu(
                    title='Resources',
                    size='lg',
                    items=[
                        MenuItemTerms(
                            search_quantity=f'data.socials#{schema}',
                            options=0,
                        ),
                        MenuItemHistogram(
                            title='Last Updated',
                            x=Axis(search_quantity=f'data.last_updated#{schema}'),
                        ),
                    ],
                ),
                Menu(
                    title='User Defined Quantities',
                    size='xl',
                    items=[MenuItemCustomQuantities()],
                ),
                Menu(
                    title='Author / Origin / Dataset',
                    size='lg',
                    items=[
                        MenuItemTerms(search_quantity='authors.name', options=0),
                        MenuItemHistogram(x=Axis(search_quantity='upload_create_time')),
                        MenuItemTerms(
                            search_quantity='external_db',
                            options=5,
                            show_input=False,
                        ),
                        MenuItemTerms(search_quantity='datasets.dataset_name'),
                        MenuItemTerms(search_quantity='datasets.doi', options=0),
                    ],
                ),
                Menu(
                    title='Visibility / IDs / Schema',
                    items=[
                        MenuItemVisibility(),
                        MenuItemTerms(search_quantity='entry_id', options=0),
                        MenuItemTerms(search_quantity='upload_id', options=0),
                        MenuItemTerms(search_quantity='upload_name', options=0),
                        MenuItemTerms(search_quantity='results.material.material_id', options=0),
                        MenuItemTerms(search_quantity='datasets.dataset_id', options=0),
                        MenuItemDefinitions(),
                    ],
                ),
            ],
        ),
    ),
)
