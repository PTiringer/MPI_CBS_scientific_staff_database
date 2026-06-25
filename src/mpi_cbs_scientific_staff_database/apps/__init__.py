from nomad.config.models.plugins import AppEntryPoint
from nomad.config.models.ui import (
    App,
    Axis,
    Column,
    Columns,
    Filters,
    Menu,
    MenuItemCustomQuantities,
    MenuItemDefinitions,
    MenuItemHistogram,
    MenuItemTerms,
    MenuItemVisibility,
    SearchQuantities,
)

schema = (
    'mpi_cbs_scientific_staff_database.schema_packages.schema_package.'
    'ScientificStaffProfile'
)

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
