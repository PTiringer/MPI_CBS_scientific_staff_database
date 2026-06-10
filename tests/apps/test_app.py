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

    last_updated_filter = app_entry_point.app.menu.items[2].items[4]

    assert last_updated_filter.type == 'histogram'
    assert last_updated_filter.title == 'Last Updated'
    assert last_updated_filter.x.search_quantity == f'data.last_updated#{schema}'
    assert last_updated_filter.show_statistics is False
