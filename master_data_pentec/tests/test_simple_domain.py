from odoo.tests.common import TransactionCase


class TestSimpleDomain(TransactionCase):

	def test_crud_simple_domain(self):
		test_simple_domain = self.env['simple.domain'].create({
			'name': 'Por redes sociales',
			'code': 'PRS',
			'type': 'conocidopor'
		})

		# Checks object is created.
		self.assertTrue(test_simple_domain.exists())

		# Checks editing object.
		test_simple_domain.write(
			{'description': 'Opcion de Por redes sociales'}
		)
		self.assertEqual(
			test_simple_domain.description, 'Opcion de Por redes sociales'
		)

		test_simple_domain.write({'active': False})
		self.assertEqual(test_simple_domain.active, False)

		# Checks deleting object.
		test_simple_domain_id = test_simple_domain.id
		test_simple_domain.unlink()
		test_simple_domain = self.env['simple.domain'].search(
			[('id', '=', test_simple_domain_id)]
		)
		self.assertFalse(test_simple_domain.exists())
