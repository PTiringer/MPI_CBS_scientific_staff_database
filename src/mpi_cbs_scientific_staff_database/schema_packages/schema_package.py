from typing import TYPE_CHECKING

from nomad.datamodel.data import BasicElnCategory, EntryData
from nomad.datamodel.metainfo.eln import ElnBaseSection
from nomad.metainfo import Datetime, Quantity, SchemaPackage, Section

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import EntryArchive
    from structlog.stdlib import BoundLogger

m_package = SchemaPackage(name='mpi_cbs_scientific_staff_database')


class ScientificStaffProfile(ElnBaseSection, EntryData):
    m_def = Section(
        categories=[BasicElnCategory],
        label='Scientific Staff Profile',
        a_eln=dict(
            lane_width='1200px',
            hide=['lab_id', 'datetime'],
            properties=dict(
                order=[
                    'display_name',
                    'email',
                    'position_role',
                    'department_or_independent_group',
                    'subgroup_lab_team',
                    'main_expertise_type',
                    'expertise_summary',
                    'research_domains',
                    'methods_modalities',
                    'skills_keywords',
                    'tools_software',
                    'subject_populations',
                    'socials',
                    'equipment',
                    'last_updated',
                ]
            ),
        ),
        a_template=dict(name='Scientific Staff Profile'),
    )

    display_name = Quantity(
        type=str,
        description='Preferred display name for the staff member.',
        a_eln=dict(component='StringEditQuantity'),
    )
    email = Quantity(
        type=str,
        description='Institutional or preferred contact email address.',
        a_eln=dict(component='StringEditQuantity'),
    )
    position_role = Quantity(
        type=str,
        description='Position or role of the staff member.',
        a_eln=dict(component='StringEditQuantity'),
    )
    department_or_independent_group = Quantity(
        type=str,
        description='Department or Independent Group affiliation.',
        a_eln=dict(component='StringEditQuantity'),
    )
    subgroup_lab_team = Quantity(
        type=str,
        description='Subgroup, lab, or team affiliation.',
        a_eln=dict(component='StringEditQuantity'),
    )
    main_expertise_type = Quantity(
        type=str,
        description='Primary expertise category.',
        a_eln=dict(component='StringEditQuantity'),
    )
    expertise_summary = Quantity(
        type=str,
        description='Free-text summary of the staff member expertise.',
        a_eln=dict(component='RichTextEditQuantity', props=dict(height=180)),
    )
    research_domains = Quantity(
        type=str,
        shape=['*'],
        description='Research domains associated with this staff member.',
        a_eln=dict(component='StringEditQuantity'),
    )
    methods_modalities = Quantity(
        type=str,
        shape=['*'],
        description='Methods and modalities used by this staff member.',
        a_eln=dict(component='StringEditQuantity'),
    )
    skills_keywords = Quantity(
        type=str,
        shape=['*'],
        description='Search keywords for skills and expertise.',
        a_eln=dict(component='StringEditQuantity'),
    )
    tools_software = Quantity(
        type=str,
        shape=['*'],
        description='Tools and software used by this staff member.',
        a_eln=dict(component='StringEditQuantity'),
    )
    subject_populations = Quantity(
        type=str,
        shape=['*'],
        description='Subject populations this staff member works with.',
        a_eln=dict(component='StringEditQuantity'),
    )
    socials = Quantity(
        type=str,
        shape=['*'],
        description='Social, web, or profile links.',
        a_eln=dict(component='StringEditQuantity'),
    )
    equipment = Quantity(
        type=str,
        shape=['*'],
        description='Equipment expertise or equipment responsibilities.',
        a_eln=dict(component='StringEditQuantity'),
    )
    last_updated = Quantity(
        type=Datetime,
        description='Date and time when this profile was last updated.',
        a_eln=dict(component='DateTimeEditQuantity'),
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)

        if archive.metadata and self.display_name:
            archive.metadata.entry_name = self.display_name


m_package.__init_metainfo__()
