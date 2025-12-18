from odoo.tests.common import TransactionCase
from odoo.tests import tagged


@tagged('standard', 'at_install')
class TestHrMilitary(TransactionCase):
    """Basic unit/integration tests for the military records addon."""

    def test_create_tck_sp(self):
        tck = self.env['tck.sp'].create({
            'name': 'Kyiv TCK & SP',
            'code': 'UA-001',
            'phone': '+380000000000',
        })
        self.assertTrue(tck.id, 'TCK&SP record should be created')
        self.assertEqual(tck.name, 'Kyiv TCK & SP')
        self.assertEqual(tck.code, 'UA-001')

    def test_employee_military_fields(self):
        tck = self.env['tck.sp'].create({'name': 'Kyiv TCK & SP'})
        employee = self.env['hr.employee'].create({
            'name': 'Test Employee',
            'is_reserved': True,
            'is_mobilized': False,
            'tck_sp_id': tck.id,
            'edrpvr_number': '123456',
        })
        self.assertEqual(employee.tck_sp_id, tck)
        self.assertTrue(employee.is_reserved)
        self.assertFalse(employee.is_mobilized)
        self.assertEqual(employee.edrpvr_number, '123456')
