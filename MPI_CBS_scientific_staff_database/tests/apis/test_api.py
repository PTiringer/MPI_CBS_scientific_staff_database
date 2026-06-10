def test_importing_api():
    from mpi_cbs_scientific_staff_database.apis import api_entry_point

    assert api_entry_point.prefix == 'newapi'
    assert api_entry_point.name == 'NewAPI'
