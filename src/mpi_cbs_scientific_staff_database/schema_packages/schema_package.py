from typing import TYPE_CHECKING

from nomad.datamodel.data import BasicElnCategory, EntryData
from nomad.datamodel.metainfo.eln import ElnBaseSection
from nomad.metainfo import Datetime, MEnum, Quantity, SchemaPackage, Section

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import EntryArchive
    from structlog.stdlib import BoundLogger

m_package = SchemaPackage(name='mpi_cbs_scientific_staff_database')

MAIN_EXPERTISE_TYPES = [
    'Theoretical/Computational',
    'Experimental',
    'Both',
    'Methodological/Technical Support',
    'Clinical/Applied',
    'Other',
]

POSITIONS_ROLES = [
    'PhD student',
    'Postdoc',
    'Research Scientist',
    'PI / Group Leader',
    'Technician',
    'Scientific Coordinator',
    'Guest Scientist',
    'Student Assistant',
    'Alumni',
    'Other',
]

METHODS_MODALITIES = [
    'fMRI',
    'structural MRI',
    'diffusion MRI',
    'EEG',
    'MEG',
    'TMS',
    'tDCS/tACS',
    'eye-tracking',
    'behavioral experiments',
    'psychophysics',
    'computational modeling',
    'machine learning/deep learning',
    'statistics',
    'neuropsychology',
    'clinical assessment',
    'data management',
    'open science/reproducibility',
]

SUBJECT_POPULATIONS = [
    'adults',
    'children',
    'infants',
    'patients',
    'multilingual participants',
    'non-human animals',
]

REQUIRED_FIELDS = {
    'display_name': 'Display Name',
    'email': 'Email',
    'position_role': 'Position/Role',
    'department_or_independent_group': 'Department or Independent Group',
    'main_expertise_type': 'Main Expertise Type',
    'expertise_summary': 'Expertise Summary',
    'research_domains': 'Research Domains',
    'methods_modalities': 'Methods/Modalities',
    'skills_keywords': 'Skills Keywords',
    'last_updated': 'Last Updated',
}


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
        description='Required. Public-facing name as it should appear in the database.',
        a_eln=dict(component='StringEditQuantity'),
    )
    email = Quantity(
        type=str,
        description='Required. Primary contact email.',
        a_eln=dict(component='StringEditQuantity'),
    )
    position_role = Quantity(
        type=MEnum(POSITIONS_ROLES),
        description='Required. Controlled position or role of the staff member.',
        a_eln=dict(
            component='EnumEditQuantity',
            props=dict(suggestions=POSITIONS_ROLES),
        ),
    )
    department_or_independent_group = Quantity(
        type=str,
        description=(
            'Required. Department or Independent Group affiliation. Use this one '
            'field for both departments and independent research groups.'
        ),
        a_eln=dict(component='EnumEditQuantity', props=dict(suggestions=[])),
    )
    subgroup_lab_team = Quantity(
        type=str,
        description='Optional. Subgroup, lab, or team affiliation, if applicable.',
        a_eln=dict(component='StringEditQuantity'),
    )
    main_expertise_type = Quantity(
        type=MEnum(MAIN_EXPERTISE_TYPES),
        description='Required. Primary expertise category.',
        a_eln=dict(
            component='EnumEditQuantity',
            props=dict(suggestions=MAIN_EXPERTISE_TYPES),
        ),
    )
    expertise_summary = Quantity(
        type=str,
        description=(
            'Required. One or two sentences describing what this person can be '
            'contacted about.'
        ),
        a_eln=dict(component='StringEditQuantity'),
    )
    research_domains = Quantity(
        type=str,
        shape=['1..*'],
        description=(
            'Required. Broad topics such as language, memory, perception, '
            'attention, BCI, or development.'
        ),
        a_eln=dict(component='StringEditQuantity'),
    )
    methods_modalities = Quantity(
        type=MEnum(METHODS_MODALITIES),
        shape=['1..*'],
        description='Required. Controlled methods and modalities.',
        a_eln=dict(
            component='EnumEditQuantity',
            props=dict(suggestions=METHODS_MODALITIES),
        ),
    )
    skills_keywords = Quantity(
        type=str,
        shape=['1..*'],
        description='Required. Flexible search field for methods, concepts, and techniques.',
        a_eln=dict(component='StringEditQuantity'),
    )
    tools_software = Quantity(
        type=str,
        shape=['*'],
        description=(
            'Recommended. Tools and software, for example Python, PyTorch, MNE, '
            'SPM, FSL, FreeSurfer, MATLAB, R, or PsychoPy.'
        ),
        a_eln=dict(component='StringEditQuantity'),
    )
    subject_populations = Quantity(
        type=MEnum(SUBJECT_POPULATIONS),
        shape=['*'],
        description='Optional. Broad subject population categories only.',
        a_eln=dict(
            component='EnumEditQuantity',
            props=dict(suggestions=SUBJECT_POPULATIONS),
        ),
    )
    socials = Quantity(
        type=str,
        description='Optional. Google Scholar, Bluesky, or other profile links.',
        a_eln=dict(component='StringEditQuantity'),
    )
    equipment = Quantity(
        type=str,
        shape=['*'],
        description=(
            'Optional. Equipment or facility experience, for example 7T MRI, '
            '3T MRI, EEG setup, MEG, TMS, eye tracker, or response boxes.'
        ),
        a_eln=dict(component='StringEditQuantity'),
    )
    last_updated = Quantity(
        type=Datetime,
        description='Required. Date when this profile was last updated.',
        a_eln=dict(component='DateTimeEditQuantity'),
    )

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)

        if archive.metadata and self.display_name:
            archive.metadata.entry_name = self.display_name

        missing = []
        for field, label in REQUIRED_FIELDS.items():
            value = getattr(self, field)
            if value is None or value == '' or value == []:
                missing.append(label)

        if missing:
            raise ValueError(
                'Missing required scientific staff profile fields: '
                + ', '.join(missing)
            )


m_package.__init_metainfo__()
