from django.test import TestCase
from django.contrib.auth.models import User

from .models import Servicio


class ServicioOwnerAccessTests(TestCase):
    def setUp(self):
        self.usuario_a = User.objects.create_user(username='usuario_a', password='clave-segura')
        self.usuario_b = User.objects.create_user(username='usuario_b', password='clave-segura')
        self.servicio_a = Servicio.objects.create(
            propietario=self.usuario_a,
            titulo='Servicio A',
            descripcion='Servicio privado del usuario A',
            precio='10.00',
            categoria='Prueba',
        )
        self.servicio_b = Servicio.objects.create(
            propietario=self.usuario_b,
            titulo='Servicio B',
            descripcion='Servicio privado del usuario B',
            precio='20.00',
            categoria='Prueba',
        )

    def test_only_owner_can_edit_service(self):
        casos = (
            (self.usuario_a, self.servicio_b),
            (self.usuario_b, self.servicio_a),
        )

        for usuario, servicio_ajeno in casos:
            with self.subTest(usuario=usuario.username):
                self.client.force_login(usuario)
                url = f'/servicios/{servicio_ajeno.pk}/editar/'

                self.assertEqual(self.client.get(url).status_code, 404)
                self.assertEqual(
                    self.client.post(url, {
                        'titulo': 'Título modificado',
                        'descripcion': 'Intento de modificación',
                        'precio': '99.00',
                        'categoria': 'Prueba',
                    }).status_code,
                    404,
                )

        self.servicio_a.refresh_from_db()
        self.servicio_b.refresh_from_db()
        self.assertEqual(self.servicio_a.titulo, 'Servicio A')
        self.assertEqual(self.servicio_b.titulo, 'Servicio B')

    def test_only_owner_can_delete_service(self):
        casos = (
            (self.usuario_a, self.servicio_b),
            (self.usuario_b, self.servicio_a),
        )

        for usuario, servicio_ajeno in casos:
            with self.subTest(usuario=usuario.username):
                self.client.force_login(usuario)
                url = f'/servicios/{servicio_ajeno.pk}/eliminar/'

                self.assertEqual(self.client.get(url).status_code, 404)
                self.assertEqual(self.client.post(url).status_code, 404)

        self.assertTrue(Servicio.objects.filter(pk=self.servicio_a.pk).exists())
        self.assertTrue(Servicio.objects.filter(pk=self.servicio_b.pk).exists())
