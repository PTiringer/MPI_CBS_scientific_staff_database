import os.path

from nomad.client import normalize_all, parse


def test_schema_package():
    test_file = os.path.join('tests', 'data', 'test.archive.yaml')
    entry_archive = parse(test_file)[0]
    normalize_all(entry_archive)

    assert entry_archive.data.display_name == 'Ada Lovelace'
    assert entry_archive.data.email == 'ada.lovelace@example.org'
    assert entry_archive.data.position_role == 'Research Scientist'
    assert entry_archive.data.main_expertise_type == 'Data Analysis'
    assert 'Cognitive neuroscience' in entry_archive.data.research_domains
    assert 'MNE-Python' in entry_archive.data.tools_software
    assert entry_archive.metadata.entry_name == 'Ada Lovelace'
