from nomad.config.models.plugins import SchemaPackageEntryPoint


class ScientificStaffSchemaPackageEntryPoint(SchemaPackageEntryPoint):
    def load(self):
        from mpi_cbs_scientific_staff_database.schema_packages.schema_package import m_package

        return m_package


schema_package_entry_point = ScientificStaffSchemaPackageEntryPoint(
    name='ScientificStaffSchemaPackage',
    description='Schema package for MPI CBS scientific staff profiles.',
)
