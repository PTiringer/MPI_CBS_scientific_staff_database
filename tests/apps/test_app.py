def test_importing_app():
    from mpi_cbs_scientific_staff_database.apps import app_entry_point

    assert app_entry_point.app.label == 'Scientific Staff'
    assert app_entry_point.app.path == 'scientific-staff'


def test_staff_app_searches_schema_quantities():
    from mpi_cbs_scientific_staff_database.apps import app_entry_point, schema

    assert app_entry_point.app.search_quantities.include == [f'*#{schema}']
    assert app_entry_point.app.filters_locked == {
        'section_defs.definition_qualified_name': schema
    }


def test_last_updated_filter_uses_datetime_widget():
    from mpi_cbs_scientific_staff_database.apps import app_entry_point, schema

    last_updated_filter = app_entry_point.app.menu.items[2].items[1]

    assert last_updated_filter.type == 'histogram'
    assert last_updated_filter.title == 'Last Updated'
    assert last_updated_filter.x.search_quantity == f'data.last_updated#{schema}'
    assert last_updated_filter.show_statistics is True


def test_staff_app_has_default_dashboard_widgets():
    from mpi_cbs_scientific_staff_database.apps import app_entry_point, schema

    widgets = app_entry_point.app.dashboard.widgets

    assert [widget.title for widget in widgets] == [
        'Display Name',
        'Position / Role',
        'Department / Independent Group',
        'Main Expertise Type',
    ]
    assert [widget.search_quantity for widget in widgets] == [
        f'data.display_name#{schema}',
        f'data.position_role#{schema}',
        f'data.department_or_independent_group#{schema}',
        f'data.main_expertise_type#{schema}',
    ]
    assert all(widget.type == 'terms' for widget in widgets)
    assert all(widget.input_mode == 'contains' for widget in widgets)
