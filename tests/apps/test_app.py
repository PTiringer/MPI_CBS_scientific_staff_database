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
    from mpi_cbs_scientific_staff_database.apps import (
        DEFAULT_WIDGET_HEIGHT,
        app_entry_point,
        schema,
    )

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
    assert all(widget.layout['lg'].h == DEFAULT_WIDGET_HEIGHT for widget in widgets)
    assert all(widget.layout['lg'].minH == DEFAULT_WIDGET_HEIGHT for widget in widgets)

    # Small screens use a 2-by-2 layout that fills all 12 grid columns.
    small_layout = [
        (widget.layout['sm'].x, widget.layout['sm'].y, widget.layout['sm'].w)
        for widget in widgets
    ]
    assert small_layout == [
        (0, 0, 6),
        (6, 0, 6),
        (0, DEFAULT_WIDGET_HEIGHT, 6),
        (6, DEFAULT_WIDGET_HEIGHT, 6),
    ]

    # Medium and larger screens keep all widgets in one full-width row.
    expected_layouts = {
        'md': [(0, 5), (5, 4), (9, 4), (13, 5)],
        'lg': [(0, 6), (6, 6), (12, 6), (18, 6)],
        'xl': [(0, 8), (8, 7), (15, 7), (22, 8)],
        'xxl': [(0, 9), (9, 9), (18, 9), (27, 9)],
    }
    for breakpoint, expected in expected_layouts.items():
        assert [
            (widget.layout[breakpoint].x, widget.layout[breakpoint].w)
            for widget in widgets
        ] == expected
        assert all(widget.layout[breakpoint].y == 0 for widget in widgets)
